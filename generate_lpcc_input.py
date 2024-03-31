#!/usr/bin/python3
import os

data_size = int(os.environ.get('DATA_SIZE', '5'))

adjacency_list = [[] for _ in range(data_size * 1000 + 1)]
with open("output/pcss_output.txt", "r") as f:
    for line in f.readlines():
        arr = line.strip().split('\t')
        edge = eval(arr[0])
        v1 = edge[0]
        v2 = edge[1]
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)
for i, l in enumerate(adjacency_list[1:], start=1):
    # status, label, adjacency list
    adjacency_list[i] = [1, i, l]
    pass
with open("output/lpcc_input.txt", "w") as f:
    for i, l in enumerate(adjacency_list[1:], start=1):
        f.write(f"{i}\t{l}\n")