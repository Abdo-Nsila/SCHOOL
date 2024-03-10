#                                                <<<   CHRONO   >>>
import time
from gtts import gTTS
from playsound import playsound
import os

H = int(input("Enter Hours :"))
M = int(input("Enter Minutes :"))
S = int(input("Enter Second :"))
t = int(input("Enter the time would you add in Second :"))

input = True

for i in range(0,t+1) :
        time.sleep(1)
        if (S < 59 and M < 59 and H < 23) or (S < 59 and M == 59 and H < 23) or (S < 59 and M < 59 and H == 23) or (S < 59 and M == 59 and H == 23) :
            S = S + 1
        elif S == 59 and M < 59 and H < 23 :
            S = 1
            M = M + 1
        elif S == 59 and M == 59 and H < 23 :
            S = 1
            M = 1
            H = H + 1
        elif S == 59 and M == 59 and H == 23 :
            S = 1
            M = 1
            H = 00
        elif  S > 59 :
            input = False
            print("")
            print("            ):  ERREUR : Your input second is not correct : ",S," > 59   ):")
            break
        elif  M > 59 :
            input = False
            print("")
            print("            ):  ERREUR : Your input minutes is not correct : ",M," > 59   ):")
            break
        elif  H > 23 :
            input = False
            print("")
            print("             ): ERREUR : Your input hours is not correct : ",H," > 23   ):")
            break
        else :
            input = False
            print("")
            print("                       ): ERREUR :  Check your inputs time             ):")
        os.system('cls') 
        print("          ||  H: M: S:  ||")
        print("          || ",f"{H:02}:{M:02}:{S:02}"," ||")
        print("          ||____________||")
        



if input == True :
    print("")
    print("      XXX     Time is over       XXX   ")
    # text0 = "Suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuur"
    # textsound = gTTS(text = text0)
    # textsound.save('welcome.mp3')
    # playsound('D:/Files/SCHOOL/DEV 110/important !/Alarm/welcome.mp3')
