list = ['Ahmed','Ali','Mohamed',7,2004]
list[1] = 20.4
del list[3]
print("[0]",list)

# Built-in list Methods :
print("[1]",len(list))             
print("[2]",list.index('Ahmed'))

list.insert(0, 'Abdellah')
print("[3]",list)

list.append(2004)
print("[4]",list)

print("[5]",list.count(2004))

print("[6]",list.pop()) # remove last item or remove to index
print("[7]",(list))

list.reverse()
print("[8]",list)

list.remove(2004)
print("[9]",list)

list2 = ["kamal","hamza",500]
print("[10]",list + list2)

print("[11]",list2 * 3) 

list2.extend(list)
print("[12]",list2)



# Ajouter Le carée des nombres dans la list  en utilisent une boucle normale
list = []

for number in range(1,11) :
    list.append(number**2)
print(list)


# List Comprehension :
list = [ number**2 for number in range(1,11) ]
print(list)


# List Comprehension avec condition:
even_numbers = [ number for number in range(1,21) if number % 2 == 0 ]
print(even_numbers)