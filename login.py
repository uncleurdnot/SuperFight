import hashlib
import json

def pwhasher(i):
  u = str.encode(i)
  pw = hashlib.sha256()
  #Salt
  pw.update(b'Arbysfoodisgoodtoeat')
  pw.update(u)
  #Generate Hash
  return pw.hexdigest()

def create_user(u, pw, email): 
  email = email.lower()
  filename = 'Data/sys/users.JSON'
  if "\"username\": \"" + u + "\"," in open(filename).read():
    print("User already exists")
    return
  # python object to be appended
  y = {"username": u, 
      "email": pwhasher(email), 
      "hash": pwhasher(pw),
      "rating": 0,
      } 
  with open(filename) as json_file: 
    data = json.load(json_file)
    temp = data['Users']
    #appending data to Characters 
    temp.append(y)
    with open(filename,'w') as f: 
      json.dump(data, f, indent=4)  

def login_validator(u, pw):
  filename = 'Data/sys/users.JSON'
  if "\"username\": \"" + u + "\"," not in open(filename).read():
    print("User Does not exist")
    return
  else:
    pw = pwhasher(pw)
    with open(filename) as json_file: 
     data = json.load(json_file)
     #print(data["Users"])
     #This will need to be optimized with a better algorithm
     for x in data['Users']:
       #print(x['username'] +"\n" + u + "\n")
       #print(x['hash'] +"\n" + pw + "\n")
       if x['username'] == u:
        if x['hash'] == pw:
          return True
        else:
          return False