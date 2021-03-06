#!/usr/bin/env python3
import os
import sys
import re


def clean_text(filepath):
    ''' Read content of file and removed text with the given regex'''
    with open(filepath, "r+") as file:
        new_text = ""
        tag_regex = re.compile(r'#{1}[a-zA-Z/0-9-]+')
        for line in file:
            checked_text = tag_regex.sub("", line)
            new_text += checked_text
        file.write(new_text)


def files_in_folder(folder_path):
    ''' Function which list files in given folder and return filenames'''
    file_paths = []
    files = os.listdir(folder_path)
    for file in files:
        if os.path.isdir(file):
            paths = files_in_folder(file)
            file_paths.extend(paths)
        file_path = folder_path + '/' + file
        file_paths.append(file_path)
    return file_paths


if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) <= 1:
        print("Pfadname fehlt")
        sys.exit(1)
    folder_name = arguments[1]
    file_list = files_in_folder(folder_name)
    for file in file_list:
        clean_text(file)
