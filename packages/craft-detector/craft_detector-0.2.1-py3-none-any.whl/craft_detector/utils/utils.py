import torch

from shapely.geometry import Polygon


# from A1111 stable diffusion code with some modification.
class ReplaceHelper:
    def __init__(self):
        self.replaced = []

    def replace(self, obj, field, func):
        original = getattr(obj, field, None)
        if original is None:
            return None

        self.replaced.append((obj, field, original))
        setattr(obj, field, func)

        return original

    def restore(self):
        for obj, field, original in self.replaced:
            setattr(obj, field, original)

        self.replaced.clear()


class InitializeOnMeta(ReplaceHelper):
    """
    Context manager that causes all parameters for linear/conv2d layers to be allocated on meta device,
    which results in those parameters having no values and taking no memory. model.to() will be broken and
    will need to be repaired by using LoadStateDictOnMeta below when loading params from state dict.

    Usage:
    ```
    with InitializeOnMeta():
        ...
    ```
    """

    def __enter__(self):

        def set_device(x):
            x["device"] = "meta"
            return x

        linear_init = self.replace(torch.nn.Linear, '__init__', lambda *args, **kwargs: linear_init(*args, **set_device(kwargs)))
        conv2d_init = self.replace(torch.nn.Conv2d, '__init__', lambda *args, **kwargs: conv2d_init(*args, **set_device(kwargs)))
        self.replace(torch.nn.Module, 'to', lambda *args, **kwargs: None)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.restore()


class LoadStateDictOnMeta(ReplaceHelper):
    """
    Context manager that allows to read parameters from state_dict into a model that has some of its parameters in the meta device.
    As those parameters are read from state_dict, they will be deleted from it, so by the end state_dict will be mostly empty, to save memory.
    Meant to be used together with InitializeOnMeta above.

    Usage:
    ```
    with LoadStateDictOnMeta(state_dict):
        model.load_state_dict(state_dict, strict=False)
    ```
    """

    def __init__(self, state_dict, device, weight_dtype_conversion=None):
        super().__init__()
        self.state_dict = state_dict
        self.device = device
        self.weight_dtype_conversion = weight_dtype_conversion or {}
        self.default_dtype = self.weight_dtype_conversion.get('', None)

    def get_weight_dtype(self, key):
        key_first_term, _ = key.split('.', 1)
        return self.weight_dtype_conversion.get(key_first_term, self.default_dtype)

    def __enter__(self):

        sd = self.state_dict
        device = self.device

        def load_from_state_dict(original, module, state_dict, prefix, *args, **kwargs):
            used_param_keys = []

            if isinstance(module, (torch.nn.Linear, torch.nn.Conv2d, torch.nn.GroupNorm,)):
                # HACK add assign=True to local_metadata for some cases
                args[0]['assign_to_params_buffers'] = True


            for name, param in module._parameters.items():
                if param is None:
                    continue

                key = prefix + name
                sd_param = sd.pop(key, None)
                if sd_param is not None:
                    dtype = self.get_weight_dtype(key)
                    if dtype is None:
                        state_dict[key] = sd_param
                    else:
                        state_dict[key] = sd_param.to(dtype=dtype)
                    used_param_keys.append(key)

                if param.is_meta:
                    dtype = sd_param.dtype if sd_param is not None else param.dtype
                    module._parameters[name] = torch.nn.parameter.Parameter(torch.empty_like(param, device=device, dtype=dtype), requires_grad=param.requires_grad)

            for name in module._buffers:
                key = prefix + name

                sd_param = sd.pop(key, None)
                if sd_param is not None:
                    state_dict[key] = sd_param
                    used_param_keys.append(key)

            original(module, state_dict, prefix, *args, **kwargs)

            for key in used_param_keys:
                state_dict.pop(key, None)

        def load_state_dict(original, module, state_dict, strict=True):
            """torch makes a lot of copies of the dictionary with weights, so just deleting entries from state_dict does not help
            because the same values are stored in multiple copies of the dict. The trick used here is to give torch a dict with
            all weights on meta device, i.e. deleted, and then it doesn't matter how many copies torch makes.

            In _load_from_state_dict, the correct weight will be obtained from a single dict with the right weights (sd).

            The dangerous thing about this is if _load_from_state_dict is not called, (if some exotic module overloads
            the function and does not call the original) the state dict will just fail to load because weights
            would be on the meta device.
            """

            if state_dict is sd:
                state_dict = {k: v.to(device="meta", dtype=v.dtype) for k, v in state_dict.items()}

            original(module, state_dict, strict=strict)

        module_load_state_dict = self.replace(torch.nn.Module, 'load_state_dict', lambda *args, **kwargs: load_state_dict(module_load_state_dict, *args, **kwargs))
        module_load_from_state_dict = self.replace(torch.nn.Module, '_load_from_state_dict', lambda *args, **kwargs: load_from_state_dict(module_load_from_state_dict, *args, **kwargs))
        linear_load_from_state_dict = self.replace(torch.nn.Linear, '_load_from_state_dict', lambda *args, **kwargs: load_from_state_dict(linear_load_from_state_dict, *args, **kwargs))
        conv2d_load_from_state_dict = self.replace(torch.nn.Conv2d, '_load_from_state_dict', lambda *args, **kwargs: load_from_state_dict(conv2d_load_from_state_dict, *args, **kwargs))
        layer_norm_load_from_state_dict = self.replace(torch.nn.LayerNorm, '_load_from_state_dict', lambda *args, **kwargs: load_from_state_dict(layer_norm_load_from_state_dict, *args, **kwargs))
        group_norm_load_from_state_dict = self.replace(torch.nn.GroupNorm, '_load_from_state_dict', lambda *args, **kwargs: load_from_state_dict(group_norm_load_from_state_dict, *args, **kwargs))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.restore()


def get_center(box):
    """사각형 박스(box)의 중심 좌표 (cx, cy) 반환"""
    x_coords = [point[0] for point in box]
    y_coords = [point[1] for point in box]
    return (sum(x_coords) / 4, sum(y_coords) / 4)


def get_box_center_y(box):
    """각 박스의 중심 y 좌표 반환"""
    return box[:, 1].mean()


def merge_boxes(boxA, boxB):
    # 두 박스의 모든 점을 하나의 배열로 합치기
    points = np.vstack([boxA, boxB])

    print("<< from box ", boxA, boxB)

    # Convex Hull 적용
    hull = cv2.convexHull(points.astype(np.float32))

    # 최소 면적 회전된 사각형 찾기
    rect = cv2.minAreaRect(hull)  # (center (x, y), (w, h), angle)

    # 회전된 사각형을 4개의 꼭짓점으로 변환
    box = cv2.boxPoints(rect)
    box = np.int32(box)  # 정수 좌표 변환

    # make clock-wise order
    startidx = box.sum(axis=1).argmin()
    box = np.roll(box, 4-startidx, 0)
    box = np.array(box)
    print(">> to box -> ", box)

    return box


def sort_text_boxes(boxes, y_threshold=5, merge=False):
    """
    CRAFT 결과로 얻은 텍스트 박스를 줄 단위로 정렬
    :param boxes: 네 개의 좌표 (x, y)로 구성된 텍스트 박스 리스트
    :param y_threshold: 같은 줄로 묶을 y 축 거리 기준
    :return: 정렬된 텍스트 박스 리스트 (줄 단위)
    """
    # y 값을 기준으로 정렬
    sorted_boxes = sorted(boxes, key=get_box_center_y)

    min_area = y_threshold * y_threshold * 1.2 # minimal area

    # 줄 단위로 그룹화
    lines = []
    current_line = [sorted_boxes[0]]

    for i in range(1, len(sorted_boxes)):
        box = sorted_boxes[i]
        curr_y = np.mean([get_box_center_y(b) for b in current_line])
        box_y = get_box_center_y(box)

        if len(current_line) > 0 and abs(box_y - curr_y) < y_threshold:
            current_line.append(box)
        else:
            lines.append(current_line)
            current_line = [box]

    if current_line:
        lines.append(current_line)

    # 각 줄을 x 좌표 기준으로 정렬
    sorted_lines = [sorted(line, key=lambda b: b[0][0]) for line in lines]

    # 겹치거나 가까운 박스 검사
    if not merge:
        return sorted_lines

    for j, lines in enumerate(sorted_lines):
        current_line = [lines[0]]
        for i in range(1, len(lines)):
            last_box = current_line[-1]
            box = lines[i]

            last_poly = Polygon(last_box)
            poly = Polygon(box)

            intersect = poly.intersection(last_poly)
            if not intersect.is_empty or poly.area < min_area or last_poly.area < min_area:
                box = merge_boxes(last_box, box)
                current_line[-1] = box
                continue

            if box[0][0] > last_box[1][0] and box[0][0] - last_box[1][0] < y_threshold * 0.3:
                box = merge_boxes(last_box, box)
                current_line[-1] = box
                print("XXX mergable", i - 1, i)
                continue

            current_line.append(box)

        sorted_lines[j] = current_line

    return sorted_lines


def _get_box_height(box):
    """주어진 4개 좌표의 텍스트 박스에서 높이를 계산"""
    y_coords = [point[1] for point in box]
    height = (max(y_coords) - min(y_coords))  # 높이 = 최대 y값 - 최소 y값
    return height


def get_average_height(boxes):
    """Calculate the average height of all text boxes"""
    heights = [_get_box_height(box) for box in boxes]
    avg_height = np.mean(heights) if heights else 0
    return avg_height
