import hashlib
import json
import re
import smtplib

Username = ""

def pwhasher(i):
  u = str.encode(i)
  pw = hashlib.sha256()
  #Salt
  pw.update(b'Arbysfoodisgoodtoeat')
  pw.update(u)
  #Generate Hash
  return pw.hexdigest()

def isvalidpw(pw):
  reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
  # compiling regex 
  pat = re.compile(reg) 
  # searching regex
  return re.compile(reg)

def isvalidemail(email):
  reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
  # compiling regex 
  pat = re.compile(reg) 
  # searching regex                  
  return re.search(pat, email)

def create_user(u, pw, email): 
  u = u.lower()
  email = email.lower()
  filename = 'Data/sys/users.JSON'
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

def login():
  filename = 'Data/sys/users.JSON'
  while True:
    print("Menu\n\t1:\tLogin\n\t2:\tSign Up\n\t3:\tForgot Password")
    choice = input().lower()
    if choice == "1" or choice == "login":
      print("Enter Username")
      u = input().lower()
      print("Enter Password")
      pw = input().lower()
      if login_validator(u,pw):
        Username = u
        return True
      else:
        print("Invalid Login")
    elif choice == "2" or choice == "sign Up":
      while True:
        print("Enter Email")
        e = input().lower()
        if not isvalidemail(e):
          print("Invalid Email")
          continue
        if "\"email\": \"" + pwhasher(e) + "\"," in open(filename).read():
          print("User already exists")
          continue
        print("Enter Username")
        u = input().lower()
        if "\"username\": \"" + u + "\"," in open(filename).read():
          print("User already exists")
          continue
        print("Enter Password")
        pw = input().lower()
        if not isvalidpw(pw):
          print("Invalid Password")
          continue
        create_user(u, pw, e)
        break
    elif choice == "3" or choice == "forgot password":
      print("Enter Email")
      e = input().lower()
      if not isvalidemail(e):
        print("Invalid Email")
        continue
      if "\"email\": \"" + pwhasher(e) + "\"," not in open(filename).read():
        print("User not found")
        continue
        
    else:
      print("Invalid Input")