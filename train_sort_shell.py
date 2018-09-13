#!/usr/bin/env python
# coding:utf-8


def shell_sort(nums):
    step = len(nums)/2  # 设定步长
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and nums[i-step] > nums[i]:
                nums[i], nums[i-step] = nums[i-step], nums[i]
                i -= step
        step /= 2
    return nums


if __name__ == "__main__":
    array = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
    shell_sort(array)
    print(">:", array)
