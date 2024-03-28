#!/usr/bin/python3
import sys

for line in sys.stdin:
    arr = line.strip().split('\t')
    v = int(arr[0])
    neighbors = eval(arr[1])
    for vi in neighbors:
        if v < vi:
            print((v, vi), "\t", neighbors)
        else:
            print((vi, v), "\t", neighbors)
