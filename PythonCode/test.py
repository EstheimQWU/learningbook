# -*- coding: UTF-8 -*-
import random
import math

def num():
    return [lambda x: i*x for i in range(4)]
    

def test014():
    a = input("input a string or a integer.")
    print(type(a))
    print(a)
    print('"input"会将所有的标准输入转换为一个字符串。')


def test_return():
    print('hello')
    return 1, 2


def test_():
    f = open("C:/github/learningbook/pythoncode/test.py", "r", encoding='UTF-8')
    lines = f.readlines()
    print(lines)
    f.close()


def test_three_one():
    fruit = "apple"
    for idx in range(len(fruit)-1, -1, -1):
        print(fruit[idx])


def return_list():
    list = [1, 2, 3]
    return list


def sieve(size):
    sieve= [True] * size
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        k= i * 2
        while k < size:
           sieve[k] = False
           k += i
    return sum(1 for x in sieve if x)

# def countAndSay(n):
#         # 递归
#         if n == 1:
#             return 11
#         else:
#             source = str(countAndSay(n-1))
#             res = ""
#             count = 1
#             # 1个1
#             for i in range(len(source) - 1):
#                 # 累计
#                 if source[i] == source[i+1]:
#                     count = count + 1
#                 else:
#                     # 加
#                     res = res + str(count) + source[i]
#                     count = 1
#             print(res + '?')
#             return int(res)


def lengthOfLastWord(s):
        l = s.split(' ')
        if len(l) == 0:
            return 0
        else:
            l[-1]

import copy

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # 新建一个列表存储第一个数组
    # 准备两个指针，一个慢指向nums1，一个快指向nums2
    # p1指向nums[p1]，移动p2，比较nums[p2]与nums[p1]的大小
    # 如果nums[p2]大于nums[p1]，移动p1，再做比较，
    # 如果nums[p2]小于等于nums[p1]，把nums[p2]放进去
    res = copy.deepcopy(nums1)
    p1 = 0
    p2 = 0
    p = 0
    for p1 in range(len(nums1)):
        print('time', p1)
        print(res)
        if nums1[p1] > nums2[p2]:
            res[p] = nums2[p2]
            p = p + 1
            p2 = p2 + 1
        elif nums1[p1] < nums2[p2]:
            res[p] = nums1[p1]
            p = p + 1
            continue
        elif nums1[p1] == nums2[p2]:
            res[p] = nums1[p1]
            p = p + 1
    # for p2 in range(len(nums2)):
    #     print('time', p2)
    #     print(p1, p2)
    #     print(res)
    #     print(nums2[p2], nums1[p1])
    #     if nums2[p2] >= nums1[p1]:
    #         print('if')
    #         res[p] = nums1[p1]
    #         p = p + 1
    #         p1 = p1 + 1
    #     elif nums2[p2] < nums1[p1]:
    #         print('el')
    #         res[p] = nums2[p2]
    #         continue
    return res
                
                


if __name__ == "__main__":
    print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    pass
