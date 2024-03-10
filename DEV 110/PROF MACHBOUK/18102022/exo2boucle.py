n = int(input("n="))
s1 = 0
s2 = 0
s3 = 0
for i in range(1, n+1):
    # print("1/", i, end="", sep="")
    # if (i == n):
    #     print("=", end="", sep="")
    # else:
    #     print("+", end="", sep="")
    s1 += 1/i
    s2 += 1/(n-i+1)
for i in range(n, 0, -1):
    print("1/", i, end="", sep="")
    if (i == 1):
        print("=", end="", sep="")
    else:
        print("+", end="", sep="")
    s3 += 1/i
print(round(s3, 2))
# print("Somme2=", s2)
# print("Somme3=", s3)
