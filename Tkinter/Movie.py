import random
Anfrage = input("Wählen sie eine Genre aus: ")

Genre = ["Action", "Horror", "Romance", "Comedy", "Sci-fi", "Thriller", "Doku"]


Action = ["MEG2", "Matrix", "Fluch der Karibik", "End Game", "Rush hour", "MIB", "Ghost Rider", "The flash", "Lucy"]
if Anfrage == "Action":
    r = random.randint(0, 8)
    print(Action[r])

Horror = ["IT", "Conjuring", "Anbabell", "Scream", "Dabbe", "The nun", "Fnaf", "Bird Box", "The Rite", "Saw"]
if Anfrage == "Horror":
    r = random.randint(0, 8)
    print(Horror[r])

Romance = ["Violet Evergarden", "Charlotte", "Words Bubble up like soda pop", "Fifty shades of grey"]
if Anfrage == "Romance":
    r = random.randint(0, 3)
    print(Romance[r])

Comedy = ["Der chaos Dad", "Fack ju Göhte", "Der diktator", "Grown ups", "The suicide Squad", "The Lego Movie"]
if Anfrage == "Comedy":
    r = random.randint(0, 5)
    print(Comedy[r])

Scifi = ["Spider-man: A new Universe", "The Spider-man", "Interstellar", "Transformers", "Jurassic World", "The Adam project"]
if Anfrage == "Scifi":
    r = random.randint(0, 5)
    print(Scifi[r])

Thriller = ["Who am I?", "Missing", "James bond", "Wanted", "Baby Driver", "Oppenheimer", "Ufo Verschwörung"]
if Anfrage == "Thriller":
    r = random.randint(0, 6)
    print(Thriller[r])

Doku = ["Das osmanische Reich", "Das Redeem Team", "Bill Russel", "Schwarze löcher", "Apollo 17", "The colors of Infinity"]
if Anfrage == "Doku":
    r = random.randint(0, 5)
    print(Doku[r])