from typing import Dict, List, Union, Any

def build_query_string(params: Dict[str, Any]) -> str:
    """
    Build a query string from a dictionary of parameters.

    Args:
        params (Dict[str, Any]): The parameters to include in the query string.

    Returns:
        str: The constructed query string.
    """
    from urllib.parse import urlencode
    return urlencode(params)

def str_to_dict(json_str: str) -> dict:
    """
    Convert a JSON string to a dictionary.

    Args:
        json_str (str): The JSON string to convert.

    Returns:
        dict: The converted dictionary.
    """
    import json
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}") from e


def extract_fields(data: Dict, fields: List[str], default: Any = None) -> Dict:
    """
    从字典中提取指定字段。

    :param data: 原始数据
    :param fields: 需要提取的字段列表
    :param default: 字段不存在时的默认值
    :return: 提取后的字典
    """
    result = {}
    for field in fields:
        value = data.get(field, default)
        result[field] = value
    return result


def extract_fields_nested(data: Dict, fields: List[str], default: Any = None, sep: str = ".") -> Dict:
    """
    从嵌套字典中提取字段，并以原始层级结构返回。

    :param data: 原始数据
    :param fields: 需要提取的字段路径，如 ["user.name", "user.profile.email"]
    :param default: 字段不存在时的默认值
    :param sep: 路径分隔符
    :return: 提取后的嵌套字典
    """

    def get_nested(d: Union[Dict, List], keys: List[str]) -> Any:
        current = d
        try:
            for key in keys:
                if isinstance(current, list):
                    key = int(key)
                current = current[key]
            return current
        except (KeyError, IndexError, ValueError, TypeError):
            return default

    def set_nested(d: Dict, keys: List[str], value: Any):
        current = d
        for key in keys[:-1]:
            key = int(key) if key.isdigit() else key
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        final_key = int(keys[-1]) if keys[-1].isdigit() else keys[-1]
        current[final_key] = value

    result = {}
    for field in fields:
        path = field.split(sep)
        value = get_nested(data, path)
        set_nested(result, path, value)
    return result