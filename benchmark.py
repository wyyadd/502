#!/usr/bin/python3
import os
from sklearn.metrics.cluster import adjusted_rand_score, normalized_mutual_info_score

data_size = int(os.environ.get('DATA_SIZE', '5'))


def generate_community():
    community_list = []
    cluster_num = set()
    with open("output/lpcc_output_final.txt", "r") as f:
        for line in f.readlines():
            arr = line.strip().split('\t', 1)
            v = int(arr[0])
            cluster = eval(arr[1])[1]
            community_list.append([v, cluster])
            cluster_num.add(cluster)
    community_list.sort(key=lambda x: x[0])
    with open("output/community.txt", "w") as f:
        for arr in community_list:
            f.write(f"{arr[0]}\t{arr[1]}\n")
    print(f"cluster size:{len(cluster_num)}")


def calculate_accuracy():
    generate_community()
    real_cluster = []
    cluster = []
    with open(f"dataset/{data_size}k/community.dat", "r") as f:
        for line in f.readlines():
            real_cluster.append(int(line.strip().split("\t")[1]))
    with open("output/community.txt", "r") as f:
        for line in f.readlines():
            cluster.append(int(line.strip().split("\t")[1]))
    print(f"ARI:{adjusted_rand_score(real_cluster, cluster)}")
    print(f"NMI:{normalized_mutual_info_score(real_cluster, cluster)}")


calculate_accuracy()
