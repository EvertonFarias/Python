
unique_id_counter = 1
id_reuniao_counter= 1

class People():
    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id
        self.agenda = Agenda()


class Agenda(): #Agenda de cada pessoa
    def __init__(self):
        self.dias = lista = [0 for _ in range(31)]


    def adicionarTarefa(self, dia):
        if dia >=0 and dia <=31:
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
        
    def remover(self, nome, unique_id):
        atual = self.primeira
        anterior = None

        while atual is not None:
            if atual.elemento.name == nome and atual.elemento.unique_id == unique_id:
                if atual == self.primeira:
                    self.primeira = atual.proxima
                else:
                    anterior.proxima = atual.proxima

                if atual == self.ultima:
                    self.ultima = anterior

                self.tamanho -= 1
                
                return  # Pessoa encontrada e removida
            

            anterior = atual
            atual = atual.proxima

        print(f"Pessoa com o nome '{nome}' não encontrada na lista.")
        
    def exibirElementos(self):
        atual = self.primeira
        while atual != None:
            print(atual.elemento.name)
            atual = atual.proxima;

class Sala_Reuniao():
    def __init__(self, nome, dia, id_reuniao):
        self.nome = nome
        self.dia = dia
        self.pessoas = ListaLigada()
        self.status = "SEM_STATUS"
        self.unique_id = id_reuniao;
    

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

        


    

