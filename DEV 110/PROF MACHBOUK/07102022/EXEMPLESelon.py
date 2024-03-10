x = 13
match x:
    case 13 | 16:
        print("ok")
    case 15:
        print("Not ok")
    case _:
        print("error")
