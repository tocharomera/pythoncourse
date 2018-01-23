#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:09:36 2018

@author: mariachi
"""
import math

def polysum(n, s):
    """
    sums the area of a regular polygon and its perimeter**2
    """
    area = (0.25 * n * s**2)/math.tan(math.pi/n)
    perimeter = n * s
    return float("{0:.4f}".format(area+perimeter**2))   

print(polysum(62, 40))