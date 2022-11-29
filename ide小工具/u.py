
import os
import subprocess

medusaCMD='python tk.py'
"""
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
for line in iter(p.stdout.readline, b''):
    print(line)
p.stdout.close()
p.wait()
"""
proc = subprocess.Popen(medusaCMD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
for line in iter(proc.stdout.readline, 'b'):
    print(line)
    if not subprocess.Popen.poll(proc) is None:
        if line == "":
            break
proc.stdout.close()
