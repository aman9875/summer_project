#!/bin/bash
s=0
for((a=0;a<1000;a++))
do
	python setting_ships.py ships.txt
	python battleship_final2.py ships.txt no_of_moves.txt
	SUM=0
	for i in `cat no_of_moves.txt`
	do
		SUM=$(($SUM+$i))
	done
	#echo $SUM
	#echo
	s=$(($SUM+$s))
done
echo $s/1000 | bc -l