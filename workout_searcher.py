#from PyPDF2 import PdfReader

#reader = PdfReader("your/document/path.pdf")

#with open("workout.txt", "w") as f:
#    i=1    
#    for page in reader.pages:
#        if i >= 7:
#            content = page.extract_text()
#            f.write(content)
#            i+=1
#        else:
#            i+=1
#            pass
#f.close()

a1 = input("Your A1 workout: ").title()
a2 = input("Your A2 workout: ").title()
b1 = input("Your B1 workout: ").title()

# retrieve workout A1
with open("workout.txt", "r") as f:
    n=0
    
    # iterating each line of the document "workout.txt"
    for line in f:

        # making sure the the workout's name is in the line
        # it cannot be equal because of the weird set up
        # of the PDF that cointains weird formating
        if a1 in line:
            print()
            print("_________________________________________")
            #printing the workout's name as a "title"
            print(line)

            # iterating on each single following line in the document "workout.txt"
            for line in f:

                # running the conditions that the line has to meet to be printed
                # this is necessary due the weird pdf format
                if line.startswith("Level") == True:
                    print(line)
                elif line.startswith("Progression")  == True:
                    print(line)
                elif line.startswith("Photo") == True:
                    break

            # adds 1 to "n" that keeps the counting of how many "titles" there is
            # with the same name provided in A1
            n+=1
        
        # keeping the condition that "n" can only be added once so
        # it won't print two or more workouts that have similar name
        # example "Plank"
        # without this condition it would print all the workouts that cointain the name plank
        elif n == 1:
            break

# retrieve workout A2
with open("workout.txt", "r") as f:
    n=0
    for line in f:
        if a2 in line:
            print()
            print("_________________________________________")
            print(line)
            # "i" is exactly like "line" in the previous loop
            # i'm lazy to change it
            for i in f:
                if i.startswith("Level") == True:
                    print(i)
                elif i.startswith("Progression")  == True:
                    print(i)
                elif i.startswith("Photo") == True:
                    break
            n+=1
        elif n == 1:
            break

# retrieve workout B1
with open("workout.txt", "r") as f:
    n=0
    for line in f:
        if b1 in line:
            print()
            print("_________________________________________")
            print(line)
            for i in f:
                if i.startswith("Level") == True:
                    print(i)
                elif i.startswith("Progression")  == True:
                    print(i)
                elif i.startswith("Photo") == True:
                    break
            n+=1
        elif n == 1:
            break

f.close()
