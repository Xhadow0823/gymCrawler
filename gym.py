# gym.py
import requests
import time
import csv
import os
import pathlib

print("cd to ", pathlib.Path(__file__).parent.absolute())
os.chdir(pathlib.Path(__file__).parent.absolute())


def getRow():
    re = requests.post('https://tccsc.cyc.org.tw/api')
    ts = time.ctime()
    if re.status_code != requests.codes.ok:
        print("ERROR: requests failed!!")
        return False
        # exit(1)
    row = [ re.json()['gym'][0],
            re.json()['swim'][0],
            re.json()['ice'][0],
            ts ]
    return row

def tiLog():
    try:
        fh = open('log.csv', 'a', newline='')
        writer = csv.writer(fh)
        print("Press CTRL + C to interrupt")
        while True:
            row = getRow()
            if row:
                writer.writerow(row)
                time.sleep(1)
            # print(row)
    except KeyboardInterrupt:
        print("Interrupt!!")
        fh.close()

tiLog()