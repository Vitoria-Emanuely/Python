#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" Série de Fibonacci
    até 1.000.000
"""
a = b = 1
while a < 10**6:
    print(a, end=' ')
    a, b = b, a + b

