#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Author   : Skypekey
# @FileName : uobj
# @Time     : 2025-08-30 19:19:09

from __future__ import annotations


def compare_dict_structure(dict1: dict, dict2: dict) -> bool:
    """递归比较两个字典的键结构是否完全一致

    参数:
        dict1 (dict): 第一个要比较的字典
        dict2 (dict): 第二个要比较的字典

    返回:
        bool:
            - True: 两个字典的键结构完全一致
            - False: 键结构不一致或类型不同

    示例:
        >>> d1 = {"a": 1, "b": {"x": 2}}
        >>> d2 = {"a": 3, "b": {"x": 4}}
        >>> compare_dict_structure(d1, d2)  # True

        >>> d3 = {"a": 1, "b": {"y": 2}}
        >>> compare_dict_structure(d1, d3)  # False

    比较逻辑:
        1. 首先比较两个对象的类型是否相同
        2. 如果不是字典类型, 直接返回True
        3. 如果是字典, 比较所有键是否相同
        4. 对每个键对应的值递归调用本方法
    """

    if not isinstance(dict1, type(dict2)):
        return False

    if not isinstance(dict1, dict):
        return True

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    return all(compare_dict_structure(dict1[key], dict2[key]) for key in dict1)


if __name__ == "__main__":
    pass
