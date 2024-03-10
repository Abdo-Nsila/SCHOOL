h = int(input("Tapez L heure:"))
m = int(input("Tapez minute:"))

if m == 59 and h == 23 :
    h = 00
    m = 00
    print(h,":",m)

else: 
    if m < 59 and h < 23: 
       m = m + 1 
       print(h,":",m) 
  
    else :
        if  m < 59 and h == 23:
                h = 00
                m = m + 1 
                print(h,":",m) 
        else :
            if  m== 59 and h < 23 :
                h = h+1
                m = 00
                print(h,":",m)
       