#!/usr/bin/python

import json

with open('nodes_stats.txt') as json_file, open('taxList.txt','w') as taxList:
    data = json.load(json_file)

    for p in data['nodes']:
        taxList.write( p['name']+","+ p['taxid']+"\n")
        # print('taxid: ' + p['taxid'])
