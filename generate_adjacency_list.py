#!/usr/bin/python3
import os

data_size = int(os.environ.get('DATA_SIZE', '5'))

adjacency_list = [[] for _ in range(data_size * 1000 + 1)]
with open(f"dataset/{data_size}k/network.dat", "r") as f:
    for line in f.readlines()[1:]:
        arr = line.strip().split('\t')
        v1 = int(arr[0])
        v2 = int(arr[1])
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)
with open("output/adjacency_list.txt", "w") as f:
    for i, l in enumerate(adjacency_list[1:], start=1):
        f.write(f"{i}\t{l}\n")
