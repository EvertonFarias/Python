
class People(): #Classe responsável por criar o objeto de Pessoa
    def __init__(self, name):
        self.name = name;
        self.agenda = Agenda()
        



class Agenda(): #Agenda de cada pessoa
    def __init__(self):
        self.dias = lista = [0 for _ in range(31)]


    def adicionarTarefa(self, dia):
        if dia >1 and dia <31:
            if self.dias[dia] !=1:
                self.dias[dia] = 1;
            else:
                print(f"o dia {dia} já está ocupado!")
        else:
            print("Dia fora do intervalo válido(entre 1 e 31)")

    def exibirDias(self):
        c = 0
        while c < len(self.dias):
            print(f"dia{c}:{self.dias[c]}")
            c+=1


class Celula():#Instancia de pessoas
    def __init__(self, proxima, elemento):
        self.proxima = proxima;
        self.elemento = elemento;




class ListaLigada: #Lista para armazear as instancias de pessoas
    def __init__(self):
        self.primeira = None
        self.ultima = None
        self.tamanho = 0

    def adicionar(self, elemento):
        novaCelula = Celula(None, elemento)
        if self.primeira is None:
            self.primeira = novaCelula
            self.ultima = novaCelula
        else:
            self.ultima.proxima = novaCelula
            self.ultima = novaCelula
        self.tamanho += 1
        
    def exibirElementos(self):
        atual = self.primeira
        while atual != None:
            print(atual.elemento.name)
            atual = atual.proxima;

class Sala_Reuniao():
    def __init__(self, pessoas):
        self.pessoas = pessoas;
    

    def verificarDisponibilidade(self, diaReuniao):
        celula = self.pessoas.primeira
        while celula != None:

            pessoa = celula.elemento
            agenda = pessoa.agenda
            disponibilidade = agenda.dias
            if diaReuniao <1 or diaReuniao >len(disponibilidade):
                print("Dia fora do intervalo válido(entre 1 e 31 dias)")
                return;
            
            if disponibilidade[diaReuniao] == 1:
                print("A data não está disponível para a reunião")
                return
            celula = celula.proxima

            disponibilidade[diaReuniao] = 1
            
        print(f"Reunião marcada para o dia {diaReuniao} com sucesso!")

        


    

