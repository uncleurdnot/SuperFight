import os
import json
import login
import shutil
import random
import pack

#Delete this later, Need to set up usernames
Username = login.Username
lib = []
 

#Function to modify the rating of a given JSON object
def rate(origin, name, cat, v):
  filename = pack.pack.get_fname(cat, origin)
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
  filename = pack.get_fname(origin)
  #If the desired pack is not already in lib, add it
  if filename not in lib:
    lib.append(filename)
    lib.append(ec)
  #If the desired pack is already availible, simply update the ec
  else:
    lib[lib.index(filename)+1] = ec

#Remove Pack from selection
def rem_pack(origin, ec):
  filename = pack.get_fname(origin)
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
      print(pack.list_packs())
    elif choice == "finish":
      break
    else:
      print("Invalid Entry")
  return import_packs()

def mainmenu():
  while True:
    print("Menu:\n\t1:\tPlay\n\t2:\tCreate Pack\n\t3:\tSearch Pack\n\t4:\tSettings\n\t5:\tExit")
    ch = input().lower()
    if ch == "play" or ch == "1":
      deck = select_packs()
    elif ch == "create pack" or ch == "create" or ch == "2":
      print("Input pack name:")
      o = input()
      pack.creat_pack(o)
      continue
    elif ch == "search pack" or ch == "search" or ch == "3":
      continue
    elif ch == "settings" or ch == "4":
      break
    elif ch == "exit" or ch == "5":
      break
    else:
      print("Invalid Input")

if login.login():
  mainmenu()
