#!/usr/bin/env python
#-*- coding:utf-8 -*-

total=0
while True:
    p = input('+')
    if not p.strip(): break
    try:
        total += float(p)
        print("\t ", total)
    except ValueError:
        print(".")
print('---------')
print(total)
