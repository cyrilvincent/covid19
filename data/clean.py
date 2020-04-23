import pandas as pd
import csv

res = []
tnbp = None
with open("covf.txt") as f:
    r = csv.DictReader(f, delimiter=" ")
    for row in r:
        tnb = int(row["NbCas"])
        dc = int(row["DCJ"])
        if tnbp != None:
            nb = tnbp - tnb
            res.append([nb, dc])
        tnbp = tnb
    res.append([tnbp, 0])
print(res)
res.reverse()
with open("covid-france.txt","w") as f:
    f.write("ix,NbCas,DC\n")
    i = 0
    for row in res:
        f.write(f"{i},{row[0]},{row[1]}\n")
        i+=1



