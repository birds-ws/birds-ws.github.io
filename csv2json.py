#! /usr/bin/env python

# from https://pythonexamples.org/python-csv-to-json/

import sys
import csv
import json

def csv_to_json(csvFilePath):
    jsonArray = []

    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        #convert each csv row into python dict
        for row in csvReader:
            #print (row)
            #add this python dict to json array
            jsonArray.append(row)

    print (json.dumps(jsonArray, indent=4));

    #convert python jsonArray to JSON String and write to file
    #with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    #    jsonString = json.dumps(jsonArray, indent=4)
    #    jsonf.write(jsonString)

csvFilePath =  sys.argv[1];
#jsonFilePath = r'data.json'
csv_to_json(csvFilePath)
