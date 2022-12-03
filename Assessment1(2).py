content = input("Enter E-Note content:-")
Note = """
        Welcome to python E - Note
        press 1 : Generate Note
        press 2 : View Note
        press 3 : Exit

"""
def ab():
     try:
        while True:
        
           name = str(input("Enter E-Note Generator Name :- " ))
           
           # print("---",name)
           if name.isalpha():
                
                break
           else:
                print("Invalid input")
        return name 
    
     except Exception as e:
         print(e)
         ab()
def  cd():
     try:
         while True:
          
          title = str(input("Enter E-Note Titel :- " ))
          
          if title.isalpha():
                 
                 break
          else:
                 print("Invalid input")
         return title 

     except Exception as i:
          print(i)
          cd()


status = True 
process = True
while status:
    
       
    choice = int(input("Enter your choice : "))
    

    if choice == 1:
        print(Note)
        print("Let's Generte Note ")
        while process:
            c = ab()
            d = cd()
            ch = input("do you want to add more products : press 'y' for yes and press 'n' for no : ")
            if ch=='y':
                process = True
            else:
                process = False
    elif choice==2:
       print("",c)
       print("",d)
    else: 
        choice==3
        status=False   
   
