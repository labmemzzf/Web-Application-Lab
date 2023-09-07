#!/usr/bin/env python
# -*- coding: utf-8 -*-

import example
import os

print("Content-Type: text/plain;charset=utf-8")
print()
print(example.words)
print("hello, I am {} from {}".format("daming", os.environ['SERVER_SOFTWARE']))

# 无效，因为服务器不支持
# print("{}, {}, {}".format(os.environ["type"], os.environ["name"], os.environ["value"]))