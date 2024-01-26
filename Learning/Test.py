from random import randint

print("Willkommen zu meinem Filme Generator!")
print("Disclaimer!: Nicht alle sind Filme!!")

Eingabe = input("Wählen Sie eine Genre aus!: ")
Genres = ["Action", "Horror", "Comedy", "Romance", "Scifi", "Thriller", "Dokumentationen"]

Action = ["Matrix", "Matrix: Reloaded", "Terminator 2", "Indiana Jones", "Fluch der Karibik", "Jurassic Park", "MEG", "MEG 2"]
if Eingabe == "Action":
    r = randint(0, 7)
    print(Action[r])

Horror = ["The Exorcist", "Hereditary", " The Conjuring", "The Shining", "The Texas Chainsaw Massacre", "The Ring", " Sinister", "IT"]
if Eingabe == "Horror":
    r = randint(0, 7)
    print(Horror[r])

Comedy = ["21 Jump Street", "Bad Boys", "Grown Ups", "The Wolf Of Wallstreet", "Baywatch", "Wir sind die Millers", "The Tuxedo", "Die Pinguine von Madagascar"]
if Eingabe == "Comedy":
    r = randint(0, 7)
    print(Comedy[r])

Romance = ["Violet Evergarden", "Charlotte", "Words Bubble up like soda pop", "Fifty shades of grey", "When Harry Met Sally", "Titanic", "Romeo + Juliet", "Beauty and the Beast"]
if Eingabe == "Romance":
    r = randint(0, 7)
    print(Romance[r])

Scifi = ["Men in Black", "Spider-man", "The Avenger: End Game", "Black Panther", "Interstellar", "Transformers", "James Bond", "The Adam Project"]
if Eingabe == "Scifi":
    r = randint(0, 7)
    print(Scifi[r])

Thriller = ["Bird Box", "Who Am I?", "Training Day", "The little things", "Scream", "Das perfekte verbrechen", "Lucy", "Wanted"]
if Eingabe == "Thriller":
    r = randint(0, 7)
    print(Thriller[r])

Dokumentation = ["The Last Dance", "The Redeem Team", "Seaspiracy", "The colours of infinity", "Schwarze löcher", "in der cyber-Hölle", "Rückkehr ins Weltall", "Bill Russel: Legend"]
if Eingabe == "Dokumentation":
    r = randint(0, 7)
    print(Dokumentation[r])
else:
  Eingabe == "Doku"
  r = randint(0, 7)
  print(Dokumentation[r])
