command = ""
while command != "quit":
 command = input(">").lower()
 if command == "start":
  print("Car stated...")
 elif command =="stoped":
  print("Car stopped...")
 elif command == "help":
  print(""" 
         start - to start the car
         stop - to stop the car
          quit - to quit 
        """)
 else:
  print("Sorry ,i dont understand that")
 

 #  Not a complete Code...