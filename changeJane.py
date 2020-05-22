#!/usr/bin/env python3

import sys
import subprocess


old_files_file = sys.argv[1]
with open(old_files_file) as f:
    text_lines = f.readlines()
        for line in text_lines:
        line = line.strip()
        new_line = line.replace("jane" "jdoe")
        subprocess.run(["mv",line,new_line])
    f.close()
