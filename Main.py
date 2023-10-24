from Classes import Classes

p1 = Classes.People("Pedro")
p2 = Classes.People("Joao")
p3 = Classes.People("Kleber")
p4 = Classes.People("Claudio")
p5 = Classes.People("Pedro Junior")

pessoas = Classes.ListaLigada()
pessoas.adicionar(p1)
pessoas.adicionar(p2)
pessoas.adicionar(p3)
pessoas.adicionar(p4)
pessoas.adicionar(p5)

pessoas.exibirElementos()

reuniao10 = Classes.Sala_Reuniao(pessoas)
reuniao10.verificarDisponibilidade(10)

p1.agenda.exibirDias()