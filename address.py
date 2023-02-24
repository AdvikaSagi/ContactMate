

def printContact():# printing all contact

    fileHandler = open('book.txt','r')
    
    lines = fileHandler.read()

    print(lines)# printing all the read lines
    

#Function to add a new contact in book.txt file
def createContact():#creating contact
    global name, surename, age,number
    name = input("Plese enter your name: ")
    surename = input("Please enter your surname: ")
    age = input("Please enter your age: ")
    number = input("Please enter your Phone number: ")
    #getting data

    fileHandler = open("book.txt", 'a')#oppening file in append

    saveString = name+","+ surename+","+age+","+number#line neede to add in book

    fileHandler.write("""\n""")
    fileHandler.write(saveString)# writing in file0
    
    fileHandler.close()# closeing file

    print("Congragulations your data has been saved")
    print("Thank you for using our services")


def searchContacts():
    
    name = input("Enter the first name of the persons contact you want to find: ")
    fileHandler = open('book.txt','r')
    files = fileHandler.readlines()
    for line in files:
        if name in line:
          details= line.split(",")
          #print(details)
          print("Contact Number is : ",details[-1])
#Function to display menu on the screen
def displayMenu():

    showStatus = True

    while showStatus:

        print("""
        Hello all welcome to ContactMate 
         Please choose your options
           0 - Add new contact
           1 - Search Contact
           2 - Print all Contacts
           3 - Exit
           
           Please choose an option from above
           """)# welcome message
        
        choice = input("Please enter your choice")# accepts choice from user

        if choice == '3': # checking is the user wants to exit2
    
            showStatus = False #setting the shoeStatus to false 
            print("Thank you for using ContactMate Bye")

        elif choice == '0':
            createContact()# calling a function to create a new contact

        elif choice == '2':
            printContact()#showing user
            showStatus = False
            # 2


        
        elif choice == '1':
            searchContacts()
            showStatus = False

        if choice != '3':
            trueStatus = input("Whould you like to continue? y/n: ")#asking if you want to coninue
            if trueStatus == 'y':
                showStatus = True

            elif trueStatus == 'n':
                showStatus =  False

            else:
                print("Sorry, I didn't understand.")
                trueStatus = input("Whould you like to continue? y/n: ")

                if trueStatus == 'y':
                    showStatus = True

                elif trueStatus == 'n':
                    showStatus =  False
                    print("Thank you for using ContactMate Bye")
                else:
                    print("Thank you for using ContactMate Bye")



displayMenu()
