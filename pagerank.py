import os
import numpy as np
import re

def get_files(base_path: str = ".") -> list[str]:
    paths = []
    for path in os.listdir(base_path):
        if os.path.isdir(path):
            paths += get_files(path)
        else:
            paths.append(os.path.join(base_path, path))

    return paths

def should_ignore(path: str) -> bool:
    if path.startswith(".git") or path.startswith(".obsidian"):
        return True
    else:
        return False 

paths = [path for path in get_files() if not should_ignore(path)]
files = [file for file in paths if file.endswith(".md")]
names = [os.path.basename(file)[:-3].lower() for file in paths if file.endswith(".md")]
map = {}

for (i, file) in enumerate(files):
    map[file] = i

def get_links(filename: str) -> list[str]:
    links = []
    with open(filename) as file:
        for line in file:
            for match in re.finditer(r'\[\[((?:\w|\s|\.)*)#?(?:\w|\s)*\|?(?:\w|\s)*\]\]', line):
                links.append( match.group(1).lower())
    return list(set(links))

for file in files:
    print(f"file={file}", get_links(file))
# print(files, map)
