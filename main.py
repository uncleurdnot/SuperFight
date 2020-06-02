import os
import json

#Delete this later, Need to set up usernames
Username = "UncleUrdnot"
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
    #Check to see if the character has already been added before
    if name in open(filename).read():
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
    if name not in open(filename).read():
      print("Object Does not exist")
    for x in temp:
      if x['name'] == name:
        x['rating'] += v
        print(x['rating'])
        with open(filename,'w') as f: 
          json.dump(data, f, indent=4)

#Add Pack to Selection
def add_pack(origin, cat):
  filename = get_fname(cat, origin)
  if filename not in lib:
    lib.append(filename)

#Remove Pack from selection
def rem_pack(origin, cat):
  filename = get_fname(cat, origin)
  if filename in lib:
    lib.remove(filename)
    
#Import Seclected Packs
def import_packs():
  temp = 0
  for filename in lib:
    with open(filename) as json_file: 
      data = json.load(json_file) 
      temp += data['Characters']
      temp += data['Powers']
      temp += data['WinCons']
      temp += data['Arenas']


