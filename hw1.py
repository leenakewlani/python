import os
import pywhatkit

choice =int(input("enter choice:"))
if choice==1:
    from datetime import date

    today = date.today()
    print("Today's date:", today)

elif choice==2:
    

    # specify the path for the directory – make sure to surround it with quotation marks
      path = 'c:/Users/computer/desktop'

    # create new single directory
      os.mkdir('c:/Users/computer/desktop/python2')
      print('the folder name python 2 has been created in your desktop just check')

elif choice==3:
    pywhatkit.sendwhatmsg_instantly(
    phone_no="+91 9351374891", 
    message="Howdy! This message will be sent instantly!",
)
    


else:
    print("you are out")
