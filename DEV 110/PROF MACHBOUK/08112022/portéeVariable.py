# page 80 du cours

def afficher():
    x = "TOTO"  # Portée Locale
    print(x)
    print(y)


def detail():
    x = "TOTO 1"  # Portée Locale
    print(x)


y = "TITI"  # Portée Globale
afficher()
