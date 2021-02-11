file = open("users.txt", "r")
users = file.readlines()
file.close()
file = open("passwords.txt", "r")
passwords = file.readlines()
file.close()
def login(username, password):
  if (username in users) and users[users.index(username)] == passwords[users.index(username)]:
    return [users.index(username)+1, username, password]
  return
def user_login(username=input("Enter Username: "), password=input("Enter Password: "), lst=None, return_value_type="lst"):
  for i in range(len(users)-1):
    users[i] = users[i][:-1]
    passwords[i] = passwords[i][:-1]
    fullnames[i] = fullnames[i][:-1]
  user_input = input("> ")
  if user_input == "Login":
    for i in range(5):
      ready_to_break = False
      username = input("Enter Username: ")
      for j in range(len(users)):
        if username == users[j]:
            print(f"Hello {username}!")
            ready_to_break = True
            break
      if ready_to_break:
        break
      print("Invalid Username")
    else:
      print("Locked!")
      raise SyntaxError
      while True:
        ready_to_break = False
        password = input("Enter Password: ")
        if password == passwords[users.index(username)]:
          print(f"{username}, Welcome back!")
          ready_to_break = True
          break
        else:
          print("Incorrect Password")
  elif user_input == "Add User":
    file = open("users.txt", "a")
    user = input("Set Username: ")
    file.write(f"\n{user}")
    file.close()
    file = open("passwords.txt", "a")
    password = input("Set Password: ")
    file.write(f"\n{password}")
    file.close()
    file = open("password_hints.txt", "a")
    password_hint = input("Set Password Hint: ")
    file.write(f"\n{password_hint}")
    file.close()
    print("Complete!")
  elif user_input == "Remove User":
    for i in range(5):
      ready_to_break = False
      username = input("Enter Username: ")
      for j in range(len(users)):
        if username == users[j]:
          print(f"Hello {username}!")
          ready_to_break = True
          break
      if ready_to_break:
        break
      print("Invalid Username")
    else:
      print("Locked!")
      raise SyntaxError
    for j in range(5):
      ready_to_break = False
      password = input("Enter Password: ")
      if password == passwords[users.index(username)]:
        print(f"{username}, Welcome back!")
        ready_to_break = True
        break
      else:
        print("Incorrect Password")
        if j >= 2:
          print()
      if ready_to_break:
        break
    else:
      print("Locked!")
      raise SyntaxError
    ok = input(f"Do you want to remove user '{username}'?[y/n]")
    if ok == "y":
      ok = False
      for k in range(3):
        ok1 = input("Really?[y/n]")
        if ok1 == "n":
          break
        else:
          ok = True
    if ok == True:
      print(f"Bye, {username}...")
      del users[users.index(username)]
      del passwords[passwords.index(password)]
      file = open("users.txt", "w")
      file.write(f"{users[0]}")
      for l in range(1, len(users)):
        file.write("\n")
        file.write(f"{users[l]}")
      file.close()
      file = open("passwords.txt", "w")
      file.write(f"{passwords[0]}")
      for l in range(1, len(passwords)):
        file.write("\n")
        file.write(f"{passwords[l]}")
        file.close()
        print("Complete!")
      
 