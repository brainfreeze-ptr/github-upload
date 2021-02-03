#!/bin/bash

echo "Searching for lost followers..."
for USER in real_plameniak smoleniakova
do
    python3 print_followers.py $USER
    python3 find_unfollows.py $USER
    printf "\n"
done

