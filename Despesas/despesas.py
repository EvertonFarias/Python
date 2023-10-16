import tkinter as tk
from tkinter import ttk
import json

def salvar():
    # Lê os valores dos campos da interface gráfica
    salario = float(salario_entry.get())
    pais = float(pais_entry.get())
    
    # Atualiza os valores no dicionário
    dados["salario"] = salario
    dados["pais"] = pais
    
    # Atualiza os valores das despesas
    for despesa, entry in despesas_entries.items():
        valor = float(entry.get())
        dados["despesas"][despesa] = valor

    # Escreve os dados atualizados no arquivo JSON
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

    # Atualiza a exibição dos valores na interface gráfica
    salario_label.config(text=f"Salário: R$ {salario}")
    pais_label.config(text=f"Pais: R$ {pais}")
    for despesa, label in despesas_labels.items():
        label.config(text=f"{despesa}: R$ {dados['despesas'][despesa]}")

def adicionar_despesa():
    nova_despesa_nome = nova_despesa_entry.get()
    if nova_despesa_nome:
        nova_despesa_valor = float(nova_despesa_valor_entry.get())
        dados["despesas"][nova_despesa_nome] = nova_despesa_valor
        atualizar_interface_despesas()
        salvar()

def deletar_despesa():
    despesa_a_deletar = despesa_para_deletar_entry.get()
    if despesa_a_deletar in dados["despesas"]:
        del dados["despesas"][despesa_a_deletar]
        atualizar_interface_despesas()
        salvar()

def atualizar_interface_despesas():
    for entry in despesas_entries.values():
        entry.destroy()
    for label in despesas_labels.values():
        label.destroy()
    
    despesas_labels.clear()
    despesas_entries.clear()
    
    for despesa, valor in dados['despesas'].items():
        despesa_label = tk.Label(aba_edicao, text=f"{despesa}: R$ {valor}")
        despesa_label.pack()
        despesas_labels[despesa] = despesa_label
        
        despesa_entry = tk.Entry(aba_edicao)
        despesa_entry.insert(0, str(valor))
        despesa_entry.pack()
        despesas_entries[despesa] = despesa_entry

def calcular_total():
    # Calcula o total das despesas
    despesas_total = sum(dados["despesas"].values())
    despesas_total_label.config(text=f"Total das Despesas: R$ {despesas_total}")

    # Calcula o total do salário
    salario_total = dados["salario"] + dados["pais"]
    salario_total_label.config(text=f"Total do Salário: R$ {salario_total}")

    # Calcula a sobra
    sobra = salario_total - despesas_total
    sobra_label.config(text=f"Sobra: R$ {sobra}")

def highlight_tab(tab):
    tab.bind("<Enter>", lambda e: abas.tab(tab, option="TButton.highlightColor", value="black"))
    tab.bind("<Leave>", lambda e: abas.tab(tab, option="TButton.highlightColor", value=""))
    tab.tab(tab, option="TButton.borderwidth", value=2)

def create_tab_content(tab, label_text, content):
    frame = ttk.Frame(tab)
    abas.add(frame, text=label_text)
    label = tk.Label(frame, text=content)
    label.pack(fill='both', expand=True)
    highlight_tab(frame)

# Lê os dados do arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Cria a janela da interface gráfica
janela = tk.Tk()
janela.title("Editar Dados")

# Cria um gerenciador de abas
abas = ttk.Notebook(janela)
abas.pack(fill='both', expand='yes')

# Cria a primeira aba para editar os valores
aba_edicao = ttk.Frame(abas)
abas.add(aba_edicao, text='Editar Valores')

# Cria os campos de entrada para edição
salario_label = tk.Label(aba_edicao, text=f"Salário: R$ {dados['salario']}")
salario_label.pack()
salario_entry = tk.Entry(aba_edicao)
salario_entry.insert(0, str(dados['salario']))
salario_entry.pack()

pais_label = tk.Label(aba_edicao, text=f"Pais: R$ {dados['pais']}")
pais_label.pack()
pais_entry = tk.Entry(aba_edicao)
pais_entry.insert(0, str(dados['pais']))
pais_entry.pack()

# Cria campos de entrada para todas as despesas
despesas_labels = {}
despesas_entries = {}
for despesa, valor in dados['despesas'].items():
    despesa_label = tk.Label(aba_edicao, text=f"{despesa}: R$ {valor}")
    despesa_label.pack()
    despesas_labels[despesa] = despesa_label
    
    despesa_entry = tk.Entry(aba_edicao)
    despesa_entry.insert(0, str(valor))
    despesa_entry.pack()
    despesas_entries[despesa] = despesa_entry

# Botão para salvar as alterações
salvar_button = tk.Button(aba_edicao, text="Salvar", command=salvar)
salvar_button.pack()

# Cria a segunda aba para calcular os totais
aba_calculo = ttk.Frame(abas)
abas.add(aba_calculo, text='Calcular Totais', padding = 30)

# Cria labels para mostrar os totais
despesas_total_label = tk.Label(aba_calculo, text="Total das Despesas:")
despesas_total_label.pack()
salario_total_label = tk.Label(aba_calculo, text="Total do Salário:")
salario_total_label.pack()
sobra_label = tk.Label(aba_calculo, text="Sobra:")
sobra_label.pack()

# Botão para calcular e atualizar os totais
calcular_button = tk.Button(aba_calculo, text="Calcular Totais", command=calcular_total)
calcular_button.pack()

# Cria a terceira aba para adicionar e deletar despesas
aba_despesas = ttk.Frame(abas)
abas.add(aba_despesas, text='Adicionar/Deletar Despesas', padding = 30)

# Campos para adicionar nova despesa
nova_despesa_label = tk.Label(aba_despesas, text="Nova Despesa:")
nova_despesa_label.pack()
nova_despesa_entry = tk.Entry(aba_despesas)
nova_despesa_entry.pack()
nova_despesa_valor_label = tk.Label(aba_despesas, text="Valor:")
nova_despesa_valor_label.pack()
nova_despesa_valor_entry = tk.Entry(aba_despesas)
nova_despesa_valor_entry.pack()
adicionar_despesa_button = tk.Button(aba_despesas, text="Adicionar Despesa", command=adicionar_despesa)
adicionar_despesa_button.pack()

# Campo para deletar despesa
despesa_para_deletar_label = tk.Label(aba_despesas, text="Deletar Despesa:")
despesa_para_deletar_label.pack()
despesa_para_deletar_entry = tk.Entry(aba_despesas)
despesa_para_deletar_entry.pack()
deletar_despesa_button = tk.Button(aba_despesas, text="Deletar Despesa", command=deletar_despesa)
deletar_despesa_button.pack()


# Inicializa a interface gráfica
janela.mainloop()
