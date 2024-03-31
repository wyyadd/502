#!/usr/bin/python3
import sys

label_flag = 0

current_vertex = None
# status, label, adjacency list
current_struct_info = None
smallest_label = None


def update_vertex():
    # If the smallest label from its neighbors is less than its current label
    if smallest_label and smallest_label < current_struct_info[1]:
        # Set the vertex as activated and update the label in the structure information as the smallest label;
        current_struct_info[0] = 1
        current_struct_info[1] = smallest_label
        # update flag
        global label_flag
        label_flag = 1
    else:
        # Update the status as inactivated in structure information of the vertex;
        current_struct_info[0] = 0
    print(current_vertex, "\t", current_struct_info)


for line in sys.stdin:
    arr = line.strip().split('\t')

    vertex = eval(arr[0])
    value = eval(arr[1])

    if current_vertex != vertex:
        if current_vertex:
            update_vertex()
        current_vertex = vertex
        smallest_label = None
        current_struct_info = None

    if type(value) is list:
        # If the value is the structure information, Store the structure information temporarily;
        current_struct_info = value
    else:
        # Find the smallest label from the neighbors;
        smallest_label = min(smallest_label, value) if smallest_label is not None else value

# update the last element
if current_vertex:
    update_vertex()

# write label_flag, to determine whether there is no label updated in one iteration.
with open("output/lpcc_flag.txt", "w") as f:
    f.write(str(label_flag))
