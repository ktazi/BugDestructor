#!/bin/bash
while IFS= read -r line
do
	touch output1.c
	cat hd>output1.c
	echo $line>>output1.c
	cat tl>>output1.c
	gcc output1.c 2>/dev/null 
	if [ -f "./a.out" ]; then
		echo "1" >> res
		rm a.out
	else
		echo "0" >> res
	fi
	rm output1.c
done < "output"


