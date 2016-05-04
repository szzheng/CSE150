#!/bin/bash

WINS=0
LOSSES=0
MAX_LENGTH=10
MAX_STONES=10
COUNTER_L=3
COUNTER_S=2

while [ $COUNTER_L -lt $MAX_LENGTH ]; do
	while [ $COUNTER_S -lt $MAX_STONES ]; do
		python run_game.py $COUNTER_L $COUNTER_S -1 $1 $2 > WIG
		tail -1 WIG >> PIG
		let COUNTER_S=COUNTER_S+1
	done
	let COUNTER_S=0
	let COUNTER_L+=1
done
sort PIG | uniq -dc
rm *IG