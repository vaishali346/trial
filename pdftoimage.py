# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:37:09 2019

@author: Administrator
"""
from wand.image import Image as Img

with Img(filename=r'data.pdf', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename=r'data.jpg')
