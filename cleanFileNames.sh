#!/bin/zsh

if [ -z $1 ]; then 
    echo "Enter pathname of the folder"
    exit -1
fi
directory=$1
for file in $directory/*; do 
    new_file="$(echo -n "$file" | tr ' ' '_')"
    new_file="$(echo "$new_file" | sed -e s/ä/ae/g -e s/ö/oe/g -e s/ü/ue/g  -e s/Ä/Ae/g -e s/Ö/Oe/g -e s/Ü/Ue/g -e s/ß/ss/g)"
    if [ "$new_file" = "$file" ]; then
        continue
    fi
    if [ -n "$new_file" ]; then
        mv "$file" "$new_file"
    else
        echo "empty"
    fi
done

