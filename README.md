# Generate output in bash

```bash
export SIMILARITY_THRESHOLD=0.3
export DATA_SIZE=5

python3 generate_adjacency_list.py

cat output/adjacency_list.txt | python3 pcss_mapper.py | sort | python3 pcss_reducer.py > output/pcss_output.txt

python3 generate_lpcc_input.py

echo "Round: 1" 
cat output/lpcc_input.txt | python3 lpcc_mapper.py | sort | python3 lpcc_reducer.py > output/lpcc_output_1.txt

round=1
while [ $(cat output/lpcc_flag.txt) -ne 0 ]
do
    ((round++))
    echo "Round: $round"
    
    input_file="output/lpcc_output_$((round-1)).txt"
    output_file="output/lpcc_output_$round.txt"
    
    cat "$input_file" | python3 lpcc_mapper.py | sort | python3 lpcc_reducer.py > "$output_file"
done
mv "output/lpcc_output_$round.txt" "output/lpcc_output_final.txt"

/usr/bin/python3 benchmark.py
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