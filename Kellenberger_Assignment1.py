# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:23:58 2023

@author: drewt
"""

def intersect2d(LLX1, LLY1, URX1, URY1, LLX2, LLY2, URX2, URY2):
    
    if URY1 < LLY2:
        return False
    if URX1 < LLX2:
        return False
    if URY2 < LLY1:
        return False
    if URX2 < LLX1:
        return False
    else:
        return True
            

def intersect3d(LLX1, LLY1, URX1, URY1, ZBOT1, ZTOP1, LLX2, LLY2, URX2, URY2, ZBOT2, ZTOP2):
    
    if URY1 < LLY2:
        return False
    if URX1 < LLX2:
        return False
    if URY2 < LLY1:
        return False
    if URX2 < LLX1:
        return False
    if ZBOT2 < ZTOP1:
        return False
    if ZBOT1 < ZTOP2:
        return False
    else:
        return True

