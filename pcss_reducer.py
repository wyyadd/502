#!/usr/bin/python3
import sys

current_edge = None
current_adj_list = None


def structural_similarity(adj_set1, adj_set2):
    size_of_intersection = len(adj_set1 & adj_set2)
    denominator = (len(adj_set1) * len(adj_set2)) ** 0.5
    similarity = size_of_intersection / denominator
    return similarity


for line in sys.stdin:
    arr = line.strip().split('\t')

    edge = eval(arr[0])
    adj_list = eval(arr[1])

    if current_edge == edge:
        value = structural_similarity(set(current_adj_list), set(adj_list))
        if value > 0.2:
            print(edge, "\t", value)
    else:
        current_edge = edge
        current_adj_list = adj_list
