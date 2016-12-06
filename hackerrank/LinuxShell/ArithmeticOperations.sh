#!/bin/bash

# https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations

read expression


printf "%.3f\n" $(echo "scale=4;"$expression | bc)