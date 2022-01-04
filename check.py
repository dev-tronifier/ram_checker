import os
import time
import subprocess

threshold = 15.0

while(1):
    time.sleep(1)
    subprocess.run('./check.sh', shell=True)
    fptr = open('./stream/file', 'r+')
    var = list()
    for i in fptr:
        var.append(int(i))

    percentage = (var[1] / var[0]) * 100
    print(percentage)

    if(percentage > threshold):
        subprocess.run('./warning.sh', shell = True)
    os.remove('./stream/file')
