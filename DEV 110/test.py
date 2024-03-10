# ----------print just value----------
t = [4,5,6,88,20]
print(* t,sep='-')

# -----------lambda------------
elm = lambda t,index : t[index]
print(elm(t,-1))

# ------------variable skip------------ 
x,_,_,y,_ = t
print(x,y)

# ---------NO---------
# a = frozenset(5)
# a += 1
# print(a)

# ----------------------
x = True
if x :
    print('OK')

# import this
# print(this)

# -----------------------------------
contries = ['Morocco','Egypt','Yamen']
c = 'Morocco'
# cond = True if c in contries else False
cond = c in contries
print(cond)

# -----------------List Comprehension------------------
t = [2,4,6,8,10]
t = [num * 2 for num in t]
print(t)

# ----------------------Python map---------------------
t = [2,4,6,8,10]
def double_it(num) :
    return num * 2
t0 = map(double_it,t)
print(*t0)
