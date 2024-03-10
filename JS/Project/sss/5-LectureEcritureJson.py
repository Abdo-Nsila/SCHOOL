import json
# methode1 lecture
f = open("D:\\SCHOOL\\TAMARIN\\CSV and JSON\\Json\\CsvJsonExmples\\CsvJsonExmples\\file.json", 'r')
dictexample = json.load(f)  # lecture fichier depuis pointeur  to dict
print(dictexample["menu"])
f.close()

# methode2 lecture
f = open("D:\\SCHOOL\\TAMARIN\\CSV and JSON\\Json\\CsvJsonExmples\\CsvJsonExmples\\file.json", 'r')
chaine = f.read()
dictexample = json.loads(chaine)  # convertir chaine to dict
print(dictexample)
f.close()

# méthode 1 Ecriture
f = open("file2.json", 'w')
dictexemple = {'id': 'file', 'value': 'File', 'popup': {'menuitem': [{'value': 'New', 'onclick': 'CreateNewDoc()'}, {
    'value': 'Open', 'onclick': 'OpenDoc()'}, {'value': 'Close', 'onclick': 'CloseDoc()'}]}}
chaine = json.dumps(dictexemple)  # convertir dict to chaine
f.write(chaine)
f.close()

# méthode 2 Ecriture
dictexemple = {'id': 'file', 'value': 'File', 'popup': {'menuitem': [{'value': 'New', 'onclick': 'CreateNewDoc()'}, {
    'value': 'Open', 'onclick': 'OpenDoc()'}, {'value': 'Close', 'onclick': 'CloseDoc()'}]}}
f = open("file2.json", 'w')
json.dump(dictexemple, f)
f.close()

