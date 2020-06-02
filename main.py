import os
import login
import json

#Delete this later, Need to set up usernames
Username = "uncleurdnot"
lib = []

#Grab packs from /Data
#Packs should include a Characters.JSON & a Powers.JSON
def list_packs():
  l = []
  for root, dirs, files in os.walk("./Data"):
    for name in files:
      l.append(name)
  return l
 
def get_fname(origin):
  filename = "Data/"+ origin + ".JSON"
  return filename

# Adds a new object to a pack.
def write_json(origin, name, cat): 
  name = name.lower()
  origin = origin.lower()
  filename = get_fname(cat, origin)
  # python object to be appended 
  y = {"origin": origin, 
      "name": name, 
      "added by": Username,
      "rating": 0
      } 
  with open(filename) as json_file: 
    data = json.load(json_file)
    temp = data[cat]
    #Check to see if the Object has already been added before
    if "\"name\":\"" + name + "\"," in open(filename).read():
      print("Already exists")
      return
    #appending data to Characters 
    temp.append(y)
    with open(filename,'w') as f: 
      json.dump(data, f, indent=4) 

#Function to modify the rating of a given JSON object
def rate(origin, name, cat, v):
  filename = get_fname(cat, origin)
  with open(filename) as json_file: 
    data = json.load(json_file) 
    temp = data[cat]
    if "\"name\":\"" + name + "\"," not in open(filename).read():
      print("Object Does not exist")
    for x in temp:
      if x['name'] == name:
        x['rating'] += v
        print(x['rating'])
        with open(filename,'w') as f: 
          json.dump(data, f, indent=4)

#Add Pack to Selection
def add_pack(origin, ec):
  filename = get_fname(origin)
  if filename not in lib:
    lib.append(filename)
    lib.append(ec)

#Remove Pack from selection
def rem_pack(origin, ec):
  filename = get_fname(origin)
  if filename in lib:
    lib.remove(lib.index(filename)+1)
    lib.remove(filename)
    
#Import Seclected Packs
def import_packs():
  temp = ""
  for filename, excl in lib:
    with open(filename) as json_file: 
      data = json.load(json_file) 
      temp += data['Characters']
      temp += data['Powers']
      temp += data['WinCons']
      temp += data['Arenas'] 
      return temp

def select_packs():
  print("Enter Pack Name")
  o = input()
  #Exclusion codes are hex values that will later be converted to binary
  # Type: C P W A
  # 0   : 0 0 0 0 (none)
  # 1   : 0 0 0 1
  # 2   : 0 0 1 0
  # 3   : 0 0 1 1
  # 4   : 0 1 0 0
  # 5   : 0 1 0 1
  # 6   : 0 1 1 0
  # 7   : 0 1 1 1
  # 8   : 1 0 0 0
  # 9   : 1 0 0 1
  # 10  : 1 0 1 0
  # 11  : 1 0 1 1
  # 12  : 1 1 0 0
  # 13  : 1 1 0 1
  # 14  : 1 1 1 0
  # 15  : 1 1 1 1
  print("Enter exclusion code")
  ec = bin(int(input(), 16))
