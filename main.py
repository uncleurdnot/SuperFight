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
      if name != "users.JSON":
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
  #If the desired pack is not already in lib, add it
  if filename not in lib:
    lib.append(filename)
    lib.append(ec)
  #If the desired pack is already availible, simply update the ec
  else:
    lib[lib.index(filename)+1] = ec

#Remove Pack from selection
def rem_pack(origin, ec):
  filename = get_fname(origin)
  if filename in lib:
    lib.remove(lib.index(filename)+1)
    lib.remove(filename)

#Normally, lib is a series of {origin, ec} values.
#zipq() creates a single list of zipped tuples from the original list
def zipq(list):
  l1 = []
  l2 = []
  i = 0
  for x in list:
    if int(i)%2 == 0:
      l1.append(list[i])
    elif int(i)%2 == 1:
      l2.append(list[i])
    i += 1
  return [[a, b] for a in l1 for b in l2]

#Import Seclected Packs
def import_packs():
  flib = zipq(lib)
  print(flib)
  temp = [[],[],[],[]]
  for filename, excl in flib:
    with open(filename) as json_file: 
      data = json.load(json_file)
      print(excl[0] + ""+ excl[1]   + "" + excl[2] + "" + excl[3])
      if excl[0] == "1":
        temp[0].append(data['characters'])
      if excl[1] == "1":
        temp[1].append(data['powers'])
      if excl[2] == "1":
        temp[2].append(data['winconds'])
      if excl[3] == "1":
        temp[3].append(data['arenas'])
  return temp

def select_packs():
  while True:
    print(lib)
    print("Add, Remove, Show, Finish?")
    choice = input().lower()
    if choice == "add":
      print("Enter Pack Name")
      o = input()
      #Exclusion codes are hex values that will later be converted to binary
      print("Enter exclusion code")
      ec = int(input(), 16)
      ec = '{:04b}'.format(ec)
      add_pack(o,ec)
    elif choice == "remove":
      print("Enter Pack Name")
      o = input()
      #Exclusion codes are hex values that will later be converted to binary
      print("Enter exclusion code")
      ec = int(input(), 16)
      ec = '{:04b}'.format(ec)
      rem_pack(o,ec)
    elif choice == "show":
      print(list_packs())
    elif choice == "finish":
      break
    else:
      print("Invalid Entry")
  return import_packs()


print(select_packs())
