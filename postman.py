import argparse
import sys
import json

parser = argparse.ArgumentParser(description="Postman API request counter")
parser.add_argument('file', help="JSON file path")
parser.add_argument('folder', help="Root folder to be count", nargs='?', default=None)
parser.add_argument('-l', '--list', help="Show folder list", action="store_true")
parser.add_argument('-r', '--request', help="Show Request", action="store_true")
args = parser.parse_args()
apiCount = 0

def main(jsonFile, rootFolder):
  jsonData = openFile(jsonFile)
  rootNodes = getRootNodes(jsonData, rootFolder)
  if args.list:
    showList(rootNodes)
  elif args.request:
    showRequest(rootNodes)
  else:
    counter(rootNodes)

def counter(nodes):
  countTheAPI(nodes)
  print("Total API: {}".format(apiCount))

def showList(nodes):
  hasFolder = False
  for node in nodes:
    if node.has_key('request') == False:
      hasFolder = True
      print(node['name'])
  if hasFolder == False:
    print("The current path has no folder!")

def showRequest(nodes):
  for node in nodes:
    if node.has_key('request') == True:
      if node['request'].has_key('url'):
        if hasattr(node['request']['url'], "__iter__"):
          url = node['request']['url']['raw']
        else :
          url = node['request']['url']
      else:
        url = ''
      print("{}: {}".format(node['request']['method'], url))
    else:
      showRequest(node['item'])

def getRootNodes(nodes, rootFolder):
  if (rootFolder == None):
    return nodes
  else:
    paths = rootFolder.split('.')
    rootNodes = nodes
    for path in paths:
      index = findIndex(rootNodes, path)
      if index != None:
        rootNodes = rootNodes[index]['item']
      else:
        print("Root folder '{}' can not be found".format(rootFolder))
        sys.exit(0)
    return rootNodes

def openFile(jsonFile):
  file = open(jsonFile)
  data = json.load(file)
  return data['item']

def findIndex(nodes, search):
  for index, node in enumerate(nodes):
    if node['name'] == search:
      return index

def countTheAPI(nodes):
  global apiCount
  for node in nodes:
    if node.has_key('request'):
      apiCount += 1
    elif node.has_key('item'):
      countTheAPI(node['item'])

if __name__ == "__main__":
  main(args.file, args.folder)