'''this script ask the user to name
his file and allows the user to type in
any text which will be saved
in the text file which was created'''


import time
import os

#accepting input for the file name
name = input("     Type any file name    ")
name = str(name)

print("  What file extension ")

print("1. Text file ,(.txt)")
print("2. Pdf file,(.pdf)")
print("3. Others file,")

#file extension options
option = input(" Pick One   :  ")
option = int(option)


#if statements for the options
if option==1:
    filename=name+'.txt'
elif option==2:
    filename=name+'.pdf'
elif option==3:
    extension=input(" Type in the Extension ")
    extension=str(extension)
    filename=name+'.'+extension 
elif option != int or option <= 4:
   print(" Please Type in the Right Option")



create_file = open(filename,'a')
Words = input("Type in All your Words : ")
create_file.write(Words)
create_file.close()


print(createfile)

