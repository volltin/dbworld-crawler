#!/usr/bin/env python3
import json
import csv

csv_file = "./data/CCF.csv"
json_file = "CCF.json"

data = []
csv_f = open(csv_file, "r")
spamreader = csv.reader(csv_f)

for row in spamreader: data.append(row)
json_f = open(json_file, "w+")
json.dump(data, json_f)

csv_f.close()
json_f.close()
