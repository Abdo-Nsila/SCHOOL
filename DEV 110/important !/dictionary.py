dict = {'Name':'Abdellah' , 'Age':18 , 'City':'Marracech'}    # dict = {key:value}
print("[0]",dict['Name'])
print("[1]",dict['Age'])
print("[3]",dict['City'])

# Modifier:
dict['Name'] = 'Hamza'
dict['Age'] = 19
dict['Job'] = 'Programming'  # But the key is not present ,the just be append
print("[4]",dict)

# Delete Elements :
dict1 = {'Name':'Samir' , 'Age':20 , 'City':'Marracech'}
del dict1['Name']
print("[5]",dict1)
dict1.clear()
print("[6]",dict1)
del dict1
print("[7]","The dict1 is removed !!!")
# Properties of Dictionary keys :
# Ne pas répéter le méme key 
# Ne pas utiliser des lists dans le didtionary

# Build-in Dictionary Methods :
dict2 = {'Name':'Samir' , 'Age':20 , 'City':'Marracech'}
# dict2.clear()
dict2.copy()
f = dict2.copy()
print("[8]",f)

# a = {1,2,3,4}
# b = {1,2,3,'X'}
# print("[99]",a^b)

# print(Dict.keys())
# print(Dict.values())
# dict_keys(['Name','Age','City','contries'])
# dict_values(['Hamza',19,'Marracech','Morocco'])

languages = {
    "One" :{
        "name" :"Html",
        "progress" : "80%",
    },

    "Two" :{
        "name" :"Html",
        "progress" : "80%",
    },

    "Three" :{
        "name" :"Html",
        "progress" : "80%",
    }
}
print(languages["One"]["name"])
print(languages["Two"]["progress"])
print(languages["Three"]["name"])

# len(Dict)

# Dict.copy()

# Dict.update()

# Dict.pop()

# sauvegarder tous les element meme apres update
Dict = {
    "name" : "Osama",
}
allitems = Dict.items()
Dict["age"] = 36
print(allitems) 
# Former un Dictionary
a = ("name" , "age" , "city")
b = "X"
print(dict.fromkeys(a,b))
dict = {'name': 'X', 'age': 'X', 'city': 'X'}