#!/bin/bash
find $1 -name "*.[ch]" > output
cd ./c_files
mkdir $2
cd ..
while IFS= read -r line
do
	cp $line "./c_files/$2"
done < "output"
rm output
