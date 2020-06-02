import os
import login
import json
import shutil

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
  filename = "Data/"+ origin.lower() + ".JSON"
  return filename

#Creates a new pack
def creat_pack(origin):
  source = "./Data/sys/template.JSON"
  filename = get_fname(origin)
  if os.path.exists(filename):
    print("Already exists")
    return
  shutil.copyfile(source, filename)


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
    if i%2 == 0:
      l1.append(x)
    if i%2 == 1:
     l2.append(x)
    i += 1    
  return zip(l1, l2)

#Import Seclected Packs
def import_packs():
  flib = zipq(lib)
  #print(flib)
  temp = [[],[],[],[]]
  for filename, excl in flib:
    with open(filename) as json_file: 
      data = json.load(json_file)
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

while True:
  print("Menu:\n\t1:\tPlay\n\t2:\tCreate Pack\n\t3:\tSearch Pack\n\t4:\tExit")
  ch = input().lower()
  if ch == "play" or ch == "1":
    deck = select_packs()
  elif ch == "create pack" or ch == "create" or ch == "2":
    print("Input pack name:")
    o = input()
    creat_pack(o)
    continue
  elif ch == "search pack" or ch == "search" or ch == "3":
    continue
  elif ch == "Exit" or ch == "4":
    break
  else:
    print("Invalid Input")
