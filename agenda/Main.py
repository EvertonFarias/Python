from tkinter import *
from tkinter import ttk
from Classes import *




def remover_pessoa():
    selected_index = pessoas_listbox.curselection()  # Obtem o índice da pessoa selecionada na Listbox
    if selected_index:
        index = int(selected_index[0])  # Converte o índice para um número inteiro
        selected_person = pessoas_listbox.get(index)  # Obtem a linha selecionada
        parts = selected_person.split(". ")
        unique_id = int(parts[0])  # Obtem o ID exclusivo
        name = parts[1]  # Obtem o name da pessoa

        lista_pessoas.remover(name, unique_id)

        mostrar_pessoas()

def tkAdicionarTarefa():
    get_dia = diaTarefa_entry.get()
    get_dia = int(get_dia) - 1
    selected_index = pessoas_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])  # Converte o índice para um número inteiro
        selected_person = pessoas_listbox.get(index)  # Obtem a linha selecionada
        parts = selected_person.split(". ")
        unique_id = int(parts[0])  # Obtem o ID
        name = parts[1]  # Obtem name da pessoa
        celula = lista_pessoas.primeira.elemento
        agenda = celula.agenda
        if celula.name == name and celula.unique_id == unique_id:
            agenda.adicionarTarefa(get_dia)
            agenda.exibirDias()
        else:
            print("dia invalido")
    else:
        print("Nenhuma pessoa selecioada")
    diaTarefa_entry.delete(0, END)
        


def abrir_janela(evento): #abre a janela da agenda quando clica duas vezes no name de alguma pessoa
    selected_index = pessoas_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        selected_person = pessoas_listbox.get(index)
        parts = selected_person.split(". ")
        unique_id = int(parts[0])  # Obtenha o ID exclusivo
        name = parts[1]  # Obtenha o name da pessoa

        # Abra a nova janela
        janela_agenda = Toplevel(janela)
        janela_agenda.title(f"Agenda de {name}")
        agenda_text = Label(janela_agenda, text=f'Dias da Agenda de <{name}>')
        agenda_text.pack()
        agenda_listbox = Listbox(janela_agenda)
        agenda_listbox.pack()

        # Encontre a pessoa correta na lista com base no name e no ID exclusivo
        atual = lista_pessoas.primeira
        while atual is not None:
            pessoa = atual.elemento
            if pessoa.name == name and pessoa.unique_id == unique_id:
               
                agenda = pessoa.agenda
                # Exibe os dias no Listbox da nova janela
                for dia, disponibilidade in enumerate(agenda.dias, start=1):
                    agenda_listbox.insert(END, f"Dia {dia}: {'Disponível' if disponibilidade == 0 else 'Ocupado'}")
                break
            atual = atual.proxima





def mostrar_pessoas():
    pessoas_listbox.delete(0, END)  # Limpa a Listbox
    atual = lista_pessoas.primeira  # Começa do primeiro nó da lista

    while atual is not None:
        pessoa = atual.elemento
        pessoas_listbox.insert(END, f"{pessoa.unique_id}. {pessoa.name}")
        atual = atual.proxima


def clicar():
    get_name = name_p_entry.get()
    if get_name:  # Verifica se o name não está vazio
        global unique_id_counter
        pessoa_ = People(get_name, unique_id_counter)
        unique_id_counter +=1
        lista_pessoas.adicionar(pessoa_)
        mostrar_pessoas()
        name_p_entry.delete(0, END)  # Limpa a entrada de name



def criar_reuniao():
    global id_reuniao_counter
    get_name = reuniao_name_entry.get()
    get_dia = dia_reuniao_entry.get()  # Obtenha o valor como uma string
    if not get_name:
        print("Campo 'name' Vazio")
        return
    
    if not get_dia:
        print("Campo 'Dia da Reunião' está vazio")
        return

    try:
        get_dia = int(get_dia)  # Tenta converter para um número inteiro
    except ValueError: #se não conseguir gera essa mensagem de erro
        print("Valor inválido para 'Dia da Reunião'")
        dia_reuniao_entry.delete(0, END)
        return

    if get_dia < 1 or get_dia > 31:
        print("Dia inválido")
        dia_reuniao_entry.delete(0, END)
        return
    
    nova_reuniao = Sala_Reuniao(get_name, get_dia, id_reuniao_counter)
    lista_reunioes.adicionar(nova_reuniao)
    reuniao_name_entry.delete(0, END)
    dia_reuniao_entry.delete(0, END)
    id_reuniao_counter +=1
    mostrar_reunioes()  # Chama a função para atualizar a Listbox de reuniões




def mostrar_reunioes():
    reunioes_listbox.delete(0, END)  # Limpa a Listbox de reuniões
    atual = lista_reunioes.primeira  # Começa do primeiro nó da lista de reuniões
    while atual is not None:
        reuniao = atual.elemento
        reunioes_listbox.insert(END, f'{reuniao.unique_id}. {reuniao.name}')  # Adiciona o name da reunião à Listbox
        atual = atual.proxima

def mostrar_reunioes2(r):
    r.delete(0, END)  # Limpa a Listbox de reuniões

    
    atual = lista_reunioes.primeira  # Começa do primeiro nó da lista de reuniões

    while atual is not None:
        reuniao = atual.elemento
        
        r.insert(END, f'{reuniao.unique_id}. {reuniao.name}')  # Adiciona o name da reunião à Listbox
        
        atual = atual.proxima

def abrir_janela_reuniao(evento):
    selected_index = reunioes_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        selected_reunion = reunioes_listbox.get(index)
        parts = selected_reunion.split(". ")
        unique_id = int(parts[0])  # Obtenha o ID exclusivo
        name = parts[1]  # Obtenha o name da reunião

        # Abra a nova janela
        janela_reuniao = Toplevel(janela)
        janela_reuniao.title(f"Informação da Reunião <{name}>")
        janela_reuniao.geometry("200x270")
        reuniao_text = Label(janela_reuniao, text=f'Informações da reunião\n<{name}>')
        reuniao_text.pack()

        
        atual = lista_reunioes.primeira
    
        while atual is not None:
            reuniao = atual.elemento
            if reuniao.name == name and reuniao.unique_id == unique_id:
                reuniaolabel = Label(janela_reuniao, text=f'name da Reunião: {reuniao.name}\nID da reunião: {reuniao.unique_id}\n Dia da reunião: {reuniao.dia}\nStatus da Reunião: {reuniao.status}\n Pessoas:')
                reuniaolabel.pack(pady=5)
                text = Listbox(janela_reuniao, height=6, width=12)
                text.pack()
                reuniao.pessoas
                pessoa_atual = reuniao.pessoas.primeira
                while pessoa_atual is not None:
                    text.insert(END,f"{pessoa_atual.elemento.name}\n")
                    pessoa_atual = pessoa_atual.proxima
                break
            atual = atual.proxima


def adicionarPessoaReuniao():
    selected_index = pessoas_listbox.curselection()

    if selected_index:
        index = int(selected_index[0])
        selected_person = pessoas_listbox.get(index)
        parts = selected_person.split(". ")
        unique_id = int(parts[0])  # Obtenha o ID exclusivo
        name_people = parts[1]  # Obtenha o name da pessoa

        #nova janela
        janela_ = Toplevel(janela)
        janela_.title(f"Agenda de {name_people}")
        janela_.geometry("300x400")
        text = Label(janela_, text=f'Reuniões Disponíveis:\n<{name_people}>')
        text.pack()

        r = Listbox(janela_)
        r.pack()
        mostrar_reunioes2(r)
        label = Label(janela_, text="")
        label.pack(pady=5)

        botao = Button(janela_, text=f'Adicionar {name_people} a reunião', command=lambda name=name_people, id_people=unique_id, r=r, label=label: verificarDispobinilidade(name, id_people, r, label))
        botao.pack()
        


def verificarDispobinilidade(name_people, id_people, r, label):
    selected_index = r.curselection()
    if selected_index:
        index = int(selected_index[0])
        selected_reunion = r.get(index)  # Obtenha o name da reunião a partir da Listbox 'r'
        parts = selected_reunion.split(". ")
        unique_id = int(parts[0])  # Obtenha o ID exclusivo
        name = parts[1]  # Obtenha o name da reunião
        atual__reuniao = lista_reunioes.primeira
        dia_reuniao = None
        while True:
            if atual__reuniao is not None:
                reuniao = atual__reuniao.elemento
                if reuniao.name == name and reuniao.unique_id == unique_id:
                    dia_reuniao = reuniao.dia - 1
                    break
            atual__reuniao = atual__reuniao.proxima

        atual = lista_pessoas.primeira
        while atual is not None:
            pessoa = atual.elemento
            dias = pessoa.agenda.dias
            if pessoa.name == name_people and pessoa.unique_id == id_people:
                    if dias[dia_reuniao] == 0:
                        dias[dia_reuniao] = 1
                        label.config(text=f"{name_people} foi adicionado à reunião {name}")
                        reuniao.pessoas.adicionar(pessoa)
                        if reuniao.status == "SEM_STATUS":
                            reuniao.status = "AGENDADA"
                        r.update()# Atualiza a interface gráfica
                        break
                    else:
                        print(f"<{name_people}> já tem compromisso nesse dia.")

            atual = atual.proxima
        linha()
        print(f"pessoas na reunião <{reuniao.name}>:\n")
        linha()
        reuniao.pessoas.exibirElementos()

def excluir_reuniao():
    selected_index = reunioes_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        selected_reunion = reunioes_listbox.get(index)
        parts = selected_reunion.split(". ")
        unique_id = int(parts[0])  # Obtenha o ID exclusivo
        name = parts[1]  # Obtenha o name da reunião

        # Encontre a reunião correta na lista com base no name e no ID exclusivo
        atual = lista_reunioes.primeira
        while atual is not None:
            reuniao = atual.elemento
            if reuniao.name == name and reuniao.unique_id == unique_id:
                # Lógica para desocupar os dias na agenda das pessoas dentro da reunião
                dia_reuniao = reuniao.dia - 1
                atual_pessoa = reuniao.pessoas.primeira  # Itera pela lista de pessoas na reunião
                while atual_pessoa is not None:
                    pessoa = atual_pessoa.elemento
                    pessoa.agenda.dias[dia_reuniao] = 0  # Marque o dia como disponível para essa pessoa
                    atual_pessoa = atual_pessoa.proxima  # Próxima pessoa na lista
                # Remova a reunião da lista
                lista_reunioes.remover(reuniao.name, unique_id)
                reunioes_listbox.delete(index)
                break
            atual = atual.proxima

        # Atualize a interface gráfica
        mostrar_reunioes()




def marcar_reuniao_concluida():
    selected_index = reunioes_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        selected_reunion = reunioes_listbox.get(index)
        parts = selected_reunion.split(". ")
        unique_id = int(parts[0])  # Obtenha o ID exclusivo
        name = parts[1]  # Obtenha o name da reunião

        # Encontre a reunião correta na lista com base no name e no ID exclusivo
        atual = lista_reunioes.primeira
        while atual is not None:
            reuniao = atual.elemento
            if reuniao.name == name and reuniao.unique_id == unique_id:
                # Marque a reunião como concluída
                reuniao.status = "CONCLUÍDA"
                break
            atual = atual.proxima

        # Atualize a interface gráfica
        mostrar_reunioes()



def linha():
    print(40*"-")

        
        


janela = Tk()
janela.title("Reuniões")
janela.geometry("400x500")
conj_abas = ttk.Notebook(janela)
conj_abas.pack()
lista_pessoas = ListaLigada()#Lista Ligada que armazena todos os usuários criados.
lista_reunioes = ListaLigada()#Lista Ligada que vai armazenar todas as reuniões criadas.


# Criação da aba de pessoas
aba_pessoa = Frame(conj_abas)
conj_abas.add(aba_pessoa, text='Pessoas')
labelPessoa = Label(aba_pessoa, text='Aqui estão as pessoas:')
labelPessoa.pack(pady=10)
pessoas_listbox = Listbox(aba_pessoa)  # Cria uma lista
pessoas_listbox.pack(padx=10, pady=10)
name_p = Label(aba_pessoa, text="Nome:")
name_p.pack()
name_p_entry = Entry(aba_pessoa)
name_p_entry.pack(padx=10, pady=10)
botaoAdicionar = Button(aba_pessoa, text="Adicionar Uma Pessoa", command=clicar)
botaoAdicionar.pack(padx=10, pady=10)
add_pessoa_reuniao = Button(aba_pessoa, text="Adicionar Pessoa A Uma Reunião", command=adicionarPessoaReuniao)
add_pessoa_reuniao.pack(pady=10)

# Botão para remover pessoa
botaoRemover = Button(aba_pessoa, text="Remover Pessoa", command=remover_pessoa)
botaoRemover.pack(padx=10, pady=10)
diaTarefa_entry = Entry(aba_pessoa)
diaTarefa_entry.pack()
botaoTarefa = Button(aba_pessoa, text="Adicionar uma tarefa", command=tkAdicionarTarefa)
botaoTarefa.pack()


# Vincular evento de clique duplo à função de abrir janela
pessoas_listbox.bind("<Double-1>", abrir_janela)

# Criação da aba de Reunião
aba_reuniao = Frame(conj_abas)
conj_abas.add(aba_reuniao, text='Reuniões')


labelReuniao = Label(aba_reuniao, text='Nome: ')
labelReuniao.pack(pady=10)
reuniao_name_entry = Entry(aba_reuniao)
reuniao_name_entry.pack()
diaLabel = Label(aba_reuniao, text="Dia da Reunião: ")
diaLabel.pack(pady=10)
dia_reuniao_entry = Entry(aba_reuniao)
dia_reuniao_entry.pack()
botaoCriarReuniao = Button(aba_reuniao, text="Criar Uma Reunião", command=criar_reuniao)
botaoCriarReuniao.pack(padx=10, pady=10)


todasLabel = Label(aba_reuniao, text="Todas as Reuniões: ")
todasLabel.pack()
reunioes_listbox = Listbox(aba_reuniao)
reunioes_listbox.pack(pady=10, padx=10)
reunioes_listbox.bind("<Double-1>", abrir_janela_reuniao)


botaoConcluir = Button(aba_reuniao, text="Concluir Reunião", command=marcar_reuniao_concluida)
botaoConcluir.pack()
botaoExcluir = Button(aba_reuniao, text="Excluir Reunião", command=excluir_reuniao)
botaoExcluir.pack()

conj_abas.pack(expand=1, fill='both')  # ajuste na tela
janela.mainloop()
