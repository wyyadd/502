# Generate output in bash
``` bash
cat adjacency_list.txt | python3 pcss_mapper.py | sort | python3 pcss_reducer.py > output.txt
```
# Generate output in Hadoop
```bash
mapred streaming \
-file /root/pcss_mapper.py \
-mapper pcss_mapper.py \
-file /root/pcss_reducer.py \
-reducer pcss_reducer.py \
-input /502/input/adjacency_list.txt \
-output /502/output
```
# Install python for Hadoop
```bash
docker exec -it namenode bash -c "echo \"deb http://archive.debian.org/debian stretch main contrib non-free\" > /etc/apt/sources.list && apt update && apt install python3 -y"
docker exec -it datanode bash -c "echo \"deb http://archive.debian.org/debian stretch main contrib non-free\" > /etc/apt/sources.list && apt update && apt install python3 -y"
docker exec -it resourcemanager bash -c "echo \"deb http://archive.debian.org/debian stretch main contrib non-free\" > /etc/apt/sources.list && apt update && apt install python3 -y"
docker exec -it nodemanager bash -c "echo \"deb http://archive.debian.org/debian stretch main contrib non-free\" > /etc/apt/sources.list && apt update && apt install python3 -y"
```