# Import madules
from qrcode import *
import random
import string
import os

# generate the QRcode
def qr_generator(data) :

    # Make a random name for output file
    letters = string.digits
    result_str = ''.join(random.choice(letters) for _ in range(6))
    file_name = 'QRcode%s.png'%(result_str)
    folder_name = 'QR%s'%(result_str)
    distanation = 'QR%s/'%(result_str)

    # Make the folders
    os.makedirs('QRcode',exist_ok = True)
    os.makedirs(folder_name)

    # Make readme file
    txt_file = open('readme.txt','w')
    txt_file.write("QRcoded text :%s"%(data))
    txt_file.close()

    # Get the background from user
    bg = input("Please enter the background color :")

    # Grid of QRcode
    qr = QRCode(version=5,box_size=10,border=5)

    # Send data
    qr.add_data(data)

    # Make QRcode
    qr.make(fit=True)

    # Exception handling(background color)
    try :
        img= qr.make_image(back_color = bg)
    except :
        print("Something went wrong! please enter the correct color.")
    else :
        img.save(file_name)

        # Replace the maked file
        os.rename(file_name,distanation+file_name)
        os.rename('readme.txt',distanation+'readme.txt')
        os.rename(folder_name,'QRcode/'+folder_name)

# Welcome title
print("""Hello dude.welcome to QRcode generator.
_______________________________________
***************************************
""")

# Program loop
while True :

    # Get the operator name
    st = input("Please enter a text or url to make a barcode :")
    qr_generator(st)

    # Get a order to continue
    order = input("Do you wanna play again? please enter (y/n) :")

    # Exit the program
    if order == 'n' :
        print("Goodluck!")
        break
        
    # Play again
    elif order == 'y' :
        pass
        
    # Exeption handling(y/n)
    else :
        print("Somthing went wrong! You didn't enter y or n.")
        break