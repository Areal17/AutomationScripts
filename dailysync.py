#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os

def run(task):
   src = os.path.join("/Users/ingowie/Test/Movies",task)
   dest = os.path.join("/Users/ingowie/Test/Filme_backup/",task)
   subprocess.call(["rsync", "-zrvh", src, dest])



if __name__ == "__main__":
    #iteriert durch den angegebenen Ordner
    for root, dirs, files in os.walk("/Users/ingowie/Test/Movies"):
       p = Pool(len(dirs))
       p.map(run,dirs)
