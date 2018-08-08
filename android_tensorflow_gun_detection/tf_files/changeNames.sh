#!/bin/bash

name=$1

i=1
for file in ./*.jpg; do
	mv -v $file $1$i.jpg
	((i++))
done


