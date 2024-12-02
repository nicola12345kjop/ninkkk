estudantes = [
    {"nome:": "Hermione", "casa": "Grifinoria", "patrono": "Lontra"},
    {"nome": "rony", "casa": "Grifonoria", "patrono": "veado"},
    {"nome": "rony", "casa": "Sonserina", "patrono": None},

]

for estudantes in estudantes:
    print(estudantes["nome"], estudantes["casa"], estudantes["patrono"], sep=",")