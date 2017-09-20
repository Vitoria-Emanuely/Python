#!/usr/bin/env python
#-*- coding:utf-8 -*-

total=0
while True:
    p = input('+')
    if not p.strip(): break
    total += float(p)
print('---------')
print(total)
