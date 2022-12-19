#!/usr/bin/python3
"""
This module defines find_peak function
"""


def find_peak(list_of_integers):
    '''
        Finds the pick in a list of numbers
    '''
    nums = list_of_integers
    length = len(nums)
    if length == 0:
        return None
    if length == 1:
        return (nums[0])
    if length == 2:
        return nums[0] if nums[0] >= nums[1] else nums[1]

    for idx in range(0, length):
        lidx = length - 1
        nidx = idx + 1
        pidx = idx - 1
        val = nums[idx]
        if idx > 0 and idx < lidx and nums[nidx] <= val and nums[pidx] <= val:
            return val
        elif idx == 0 and nums[nidx] <= val:
            return val
        elif idx == lidx and nums[pidx] <= val:
            return val
    return
