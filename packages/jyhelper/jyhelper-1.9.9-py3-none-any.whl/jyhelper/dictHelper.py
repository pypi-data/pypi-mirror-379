#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2025/09/26 10:36 
# @Author : JY
"""
"""


class dictHelper:
    def __init__(self):
        pass

    @staticmethod
    def sort_by_key(data, sort_func=None, reverse=False):
        """
        按key对字典排序\n
        :param data: 待排序字典
        :param sort_func: 排序方法,不传默认按key的值比较 例传: lambda x:int(x) 整数排序
        :param reverse: 是否倒序
        :return: 排序后的字典
        """
        if sort_func is not None:
            return dict(sorted(data.items(), key=lambda x: sort_func(x[0]), reverse=reverse))
        else:
            return dict(sorted(data.items(), key=lambda x: x[0], reverse=reverse))

    @staticmethod
    def sort_by_value(data, sort_func=None, reverse=False):
        """
        按value对字典排序\n
        :param data: 待排序字典
        :param sort_func: 排序方法,不传默认按value的值比较 例传: lambda x:int(x) 整数排序
        :param reverse: 是否倒序
        :return: 排序后的字典
        """
        if sort_func is not None:
            return dict(sorted(data.items(), key=lambda x: sort_func(x[1]), reverse=reverse))
        else:
            return dict(sorted(data.items(), key=lambda x: x[1], reverse=reverse))

    @staticmethod
    def del_by_key(data, key):
        """
        根据条件，删除字典中的数据\n
        :param data: 字典
        :param key: key的值 str/list
        :return: 新字典
        """
        if not isinstance(key,list):
            key = [key]
        new_data = data.copy()
        for row in key:
            new_data.pop(row, None)
        return new_data

    @staticmethod
    def del_by_value(data, value):
        """
        根据条件，删除字典中的数据\n
        :param data: 字典
        :param value: value的值 str/list
        :return: 新字典
        """
        if not isinstance(value, list):
            value = [value]
        # 使用字典推导式创建新字典，排除要删除的数据
        return {k: v for k, v in data.items() if v not in value}


if __name__ == '__main__':
    dataa = {'b1': 1, 'c1': 1, 'a12': 12, 'a9': 9, 'a88': 88, '98': None}
    print('原始数据', dataa)
    res = dictHelper.del_by_value(dataa,[1,12,None])
    print('原始数据', dataa)
    print('------------------')
    print('修后数据', res)
