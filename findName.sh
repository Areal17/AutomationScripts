#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ~/data/list.txt | cut -d ' ' -f 3)
for file in $files; do
        fileName=$(basename "$file")
        completeFileName="$HOME/data/$fileName"
        # test -r vielleicht
        # oder mit $USER nach dem User fragen. Gruppe findet man sicher, wenn man nach ls -l im Scriptordner vewendet
        if [ -e completeFileName ]; then
                $completeFileName >> oldFiles.txt
        fi
done