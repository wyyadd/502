def pre_work():
    adjacency_list = [[] for _ in range(5001)]
    with open("dataset/5k/network-5k.dat", "r") as f:
        for line in f.readlines()[1:]:
            arr = line.strip().split('\t')
            v1 = int(arr[0])
            v2 = int(arr[1])
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)
    with open("adjacency_list.txt", "w") as f:
        for i, l in enumerate(adjacency_list[1:], start=1):
            f.write(f"{i}\t{l}\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pre_work()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
