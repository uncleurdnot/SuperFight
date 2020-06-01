import os
#Grab packs from /Data
#Packs should include a Characters.JSON & a Powers.JSON
def list_packs():
  for root, dirs, files in os.walk("./Data"):
    for name in dirs:
      print(name)

list_packs()