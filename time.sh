#!/bin/bash
now=$(date)
read -p "file:" i
if [ $i -eq 1 ]; then folder="ordered"; fi
if [ $i -eq 2 ]; then folder="reverse"; fi
if [ $i -eq 3 ]; then folder="random"; fi
echo $folder".txt"

for j in {0..5}
do
    num=$((10**j))    
    for _ in {0..4}
    do
	time cat $folder-10e$j.txt | swift main.swift  >> words.txt
	echo $now // $num"words"
    done
done

