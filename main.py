import os
import json

#Delete this later, Need to set up usernames
Username = "UncleUrdnot"

#Grab packs from /Data
#Packs should include a Characters.JSON & a Powers.JSON
def list_packs():
  for root, dirs, files in os.walk("./Data"):
    for name in dirs:
      print(name)
 

# function to add to JSON 
def write_json(filename, origin, name): 
  # python object to be appended 
  y = {"origin": origin, 
      "name": name, 
      "added by": Username
      } 
  with open(filename) as json_file: 
      data = json.load(json_file) 
      temp = data['Characters']
      #Check to see if the character has already been added before
      if name in data:
        print("Already exists")
      else:
        # appending data to Characters 
        temp.append(y)
        with open(filename,'w') as f: 
          json.dump(data, f, indent=4) 

#Adds a new character to a pack.
#If you do not own the pack, it should leave a notification for the pack's owner to either approve or deny it.
def add_char(filename):
  print("Input Character Name:\t")
  name = input()
  print("Input Character Origin:\t")
  origin = input()
  write_json(filename, origin, name)

list_packs()
add_char("Data/Dragon Ball/Characters.JSON")