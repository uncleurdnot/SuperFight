import login
import json
import os
import shutil

#Generate filename for JSON objects
def get_fname(origin):
  filename = "Data/"+ origin.lower() + ".JSON"
  return filename

#Grab packs from /Data
#Packs should include a Characters.JSON & a Powers.JSON
def list_packs():
  l = []
  for root, dirs, files in os.walk("./Data"):
    for name in files:
      if name != "users.JSON":
        l.append(name)
  return l

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
      "added by": login.Username,
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