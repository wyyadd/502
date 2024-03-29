#!/usr/bin/python3
import sys

for line in sys.stdin:
    arr = line.strip().split('\t', 1)
    v = int(arr[0])
    # status, label, adjacency list
    struct_info = eval(arr[1])
    status = struct_info[0]
    label = struct_info[1]
    adj_list = struct_info[2]

    if status == 1:
        for vi in adj_list:
            print(vi, "\t", label)
    print(v, "\t", struct_info)
