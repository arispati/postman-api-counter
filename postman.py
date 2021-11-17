import argparse
import sys
import json

parser = argparse.ArgumentParser(description="Postman API request counter")
parser.add_argument('file', help="JSON file path")
parser.add_argument('folder', help="Root folder to be count", nargs='?', default=None)
args = parser.parse_args()

apiCount = 0

def main(jsonFile, rootFolder):
    file = open(jsonFile)
    data = json.load(file)
    node = data['item']

    if (rootFolder != None):
        index = findIndex(node, rootFolder)
        
        if index != None:
            node = node[index]['item']
        else:
            print("Root folder '{}' can not be found".format(rootFolder))
            sys.exit(0)
    
    countTheAPI(node)

    print("Total API: {}".format(apiCount))

def findIndex(nodes, search):
    for index, node in enumerate(nodes):
        if node['name'] == search:
            return index

def countTheAPI(nodes):
    global apiCount

    for node in nodes:
        if node.has_key('request'):
            apiCount += 1
        else:
            countTheAPI(node['item'])

if __name__ == "__main__":
    main(args.file, args.folder)