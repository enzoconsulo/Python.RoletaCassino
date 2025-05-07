import tkinter as tk
import random
import time

numeros_cores_roleta = {
    0: "green",
    1: "red",
    8: "black",
    2: "red",
    9: "black",
    3: "red",
    10: "black",
    4: "red",
    11: "black",
    5: "red",
    12: "black",
    6: "red",
    13: "black",
    7: "red",
    14: "black"
}

numero_escolhido = None
numero_escolhido2 = None
numero_escolhido3 = None
valor_aposta_vermelho = 0
valor_aposta_preto = 0
valor_aposta_verde = 0
valor_aposta = 0
saldo = 100
tempo_restante = 0

def iniciar_jogo():
    tela_inicio.pack_forget()
    tela_roleta.pack()
    contador_regressivo()

def contador_regressivo():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        tempo_restante_label.config(text=f"Próxima roleta em: {tempo_restante}s")
        if tempo_restante == 0:
            girar_roleta()
        root.after(1000, contador_regressivo)
    else:
        tempo_restante = 15  
        contador_regressivo()

def girar_roleta():
    valores = list(numeros_cores_roleta.keys())
    random.shuffle(valores)
    atualiza_roleta(valores)

def atualiza_roleta(valores):
    global saldo, valor_aposta_vermelho, valor_aposta_preto, valor_aposta_verde, valor_aposta
    pos_inicial = random.randint(0, 14)
    pos_atuais = [i % 15 for i in range(pos_inicial, pos_inicial + 7)]

    for _ in range(50):
        random.shuffle(valores)
        for i, pos in enumerate(pos_atuais):
            cor_fundo = numeros_cores_roleta[valores[pos]]
            cor_numero = "white"  
            if i == 3:  
                roleta_canvas.create_line(50 * i + 25, 5, 50 * i + 25, 45, fill="black", width=4)
                roleta_canvas.itemconfig(retangulos[i], fill=cor_fundo)
                roleta_canvas.itemconfig(textos[i], text=str(valores[pos]), fill=cor_numero)
            else:
                roleta_canvas.itemconfig(retangulos[i], fill=cor_fundo)
                roleta_canvas.itemconfig(textos[i], text=str(valores[pos]), fill=cor_numero)
        pos_atuais = [(pos + 1) % 15 for pos in pos_atuais]
        roleta_canvas.update()
        time.sleep(0.1)

    sorteado = valores[pos_atuais[2]]
    resultado_label.config(text=f"O número sorteado foi: {sorteado}")
    if 0 < sorteado < 8:
        sorteado = 1
    if 8 < sorteado <= 15:
        sorteado = 9
    processar_aposta(sorteado)
    
    valor_aposta_vermelho = 0
    valor_aposta_preto = 0
    valor_aposta_verde = 0
    valor_aposta = 0
    
    vermelho_button.config(text="Vermelho x2\nAposta: 0")
    preto_button.config(text="Preto x2\nAposta: 0")
    verde_button.config(text="Verde x14\nAposta: 0")
    
def selecionar_vermelho():
    global saldo, valor_aposta_vermelho, valor_aposta,numero_escolhido
    if int(valor_aposta_entry.get()) > saldo:
        aviso_saldo = tk.Toplevel()
        aviso_saldo.title("Aviso")
        mensagem_aviso_saldo = tk.Label(aviso_saldo, text="Saldo insuficiente para essa aposta!")
        mensagem_aviso_saldo.pack()
        botao_ok = tk.Button(aviso_saldo, text="OK", command=aviso_saldo.destroy)
        botao_ok.pack()
    else:
        numero_escolhido = 1
        valor_aposta += int(valor_aposta_entry.get())
        valor_aposta_vermelho += int(valor_aposta_entry.get())
        if valor_aposta_vermelho > 0:
            saldo -= int(valor_aposta_entry.get())
            saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
            vermelho_button.config(text=f"Vermelho x2\nAposta: {valor_aposta_vermelho}")

def selecionar_preto():
    global saldo, valor_aposta_preto, valor_aposta,numero_escolhido2
    if int(valor_aposta_entry.get()) > saldo:
        aviso_saldo = tk.Toplevel()
        aviso_saldo.title("Aviso")
        mensagem_aviso_saldo = tk.Label(aviso_saldo, text="Saldo insuficiente para essa aposta!")
        mensagem_aviso_saldo.pack()
        botao_ok = tk.Button(aviso_saldo, text="OK", command=aviso_saldo.destroy)
        botao_ok.pack()
    else:
        numero_escolhido2 = 9
        valor_aposta += int(valor_aposta_entry.get())
        valor_aposta_preto += int(valor_aposta_entry.get())
        if valor_aposta_preto > 0:
            saldo -= int(valor_aposta_entry.get())
            saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
            preto_button.config(text=f"Preto x2\nAposta: {valor_aposta_preto}")

def selecionar_verde():
    global saldo, valor_aposta_verde, valor_aposta, numero_escolhido3
    if int(valor_aposta_entry.get()) > saldo:
        aviso_saldo = tk.Toplevel()
        aviso_saldo.title("Aviso")
        mensagem_aviso_saldo = tk.Label(aviso_saldo, text="Saldo insuficiente para essa aposta!")
        mensagem_aviso_saldo.pack()
        botao_ok = tk.Button(aviso_saldo, text="OK", command=aviso_saldo.destroy)
        botao_ok.pack()
    else:
        numero_escolhido3 = 0
        valor_aposta += int(valor_aposta_entry.get())
        valor_aposta_verde += int(valor_aposta_entry.get())
        if valor_aposta_verde > 0:
            saldo -= int(valor_aposta_entry.get())
            saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
            verde_button.config(text=f"Verde x14\nAposta: {valor_aposta_verde}")

def processar_aposta(sorteado):
    global saldo, numero_escolhido,valor_aposta_vermelho,numero_escolhido2,valor_aposta_preto,numero_escolhido3,valor_aposta_verde
    if valor_aposta_vermelho:
        valor_aposta_vermelho = int(valor_aposta_vermelho)
        if valor_aposta_vermelho > 0:
            if numero_escolhido is not None:
                if numero_escolhido == sorteado:
                    
                    if numero_escolhido == 0:
                        saldo += 14 * valor_aposta_vermelho
                    elif numero_escolhido in range(1, 8):
                        saldo += 2 * valor_aposta_vermelho
                    elif numero_escolhido in range(8, 15):
                        saldo += 2 * valor_aposta_vermelho
                    saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
                else:
                    
                    saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
                numero_escolhido = None 
        
        
    if valor_aposta_preto:
        valor_aposta_preto = int(valor_aposta_preto)
        if valor_aposta_preto > 0:
            if numero_escolhido2 is not None:
                if numero_escolhido2 == sorteado:
                    
                    if numero_escolhido2 == 0:
                        saldo += 14 * valor_aposta_preto
                    elif numero_escolhido2 in range(1, 8):
                        saldo += 2 * valor_aposta_preto
                    elif numero_escolhido2 in range(8, 15):
                        saldo += 2 * valor_aposta_preto
                    saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
                else:
                    
                    saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
                numero_escolhido2 = None  
        
        
    if valor_aposta_verde:
        valor_aposta_verde = int(valor_aposta_verde)
        if valor_aposta_verde > 0:
            if numero_escolhido3 is not None:
                if numero_escolhido3 == sorteado:
                    
                    if numero_escolhido3 == 0:
                        saldo += 14 * valor_aposta_verde
                    elif numero_escolhido3 in range(1, 8):
                        saldo += 2 * valor_aposta_verde
                    elif numero_escolhido3 in range(8, 15):
                        saldo += 2 * valor_aposta_verde
                    saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
                else:
                    
                    saldo_label.config(text=f"Seu saldo atual é de: {saldo}")
                numero_escolhido3 = None  

    if saldo <= 0:
        aviso_saldo_zerado = tk.Toplevel()
        aviso_saldo_zerado.title("Aviso - Saldo zerado")
        mensagem_aviso_saldo_zerado = tk.Label(aviso_saldo_zerado, text="Seu saldo acabou!\n Finalizando o Programa...")
        mensagem_aviso_saldo_zerado.pack()
        botao_ok = tk.Button(aviso_saldo_zerado, text="OK", command=root.destroy)
        botao_ok.pack()



root = tk.Tk()
root.title("Roleta")
root.geometry("400x300")

tela_inicio = tk.Frame(root)
tela_inicio.pack(fill="both", expand=True)

titulo_inicio = tk.Label(tela_inicio, text="Bem-vindo à Roleta", font=("Arial", 18))
titulo_inicio.pack(pady=20)

botao_iniciar = tk.Button(tela_inicio, text="Iniciar Jogo", command=iniciar_jogo)
botao_iniciar.pack()

tela_roleta = tk.Frame(root)
roleta_canvas = tk.Canvas(tela_roleta, width=400, height=50)
roleta_canvas.pack()

retangulos = []
textos = []
for i in range(7):
    retangulo = roleta_canvas.create_rectangle(50 * i, 10, 50 * (i + 1), 40, fill="white")
    texto = roleta_canvas.create_text(50 * i + 25, 25, text="", font=("Arial", 18))
    retangulos.append(retangulo)
    textos.append(texto)

valor_aposta_label = tk.Label(tela_roleta, text="Valor da aposta:")
valor_aposta_label.pack()

valor_aposta_entry = tk.Entry(tela_roleta)
valor_aposta_entry.pack()

vermelho_button = tk.Button(tela_roleta, text="Vermelho x2\nAposta: 0", command=selecionar_vermelho)
vermelho_button.pack()

preto_button = tk.Button(tela_roleta, text="Preto x2\nAposta: 0", command=selecionar_preto)
preto_button.pack()

verde_button = tk.Button(tela_roleta, text="Verde x14\nAposta: 0", command=selecionar_verde)
verde_button.pack()

resultado_label = tk.Label(tela_roleta, text="")
resultado_label.pack()

saldo_label = tk.Label(tela_roleta, text=f"Seu saldo atual é de: {saldo}")
saldo_label.pack()

tempo_restante_label = tk.Label(tela_roleta, text=f"Próxima roleta em: {tempo_restante}s")
tempo_restante_label.pack()

root.mainloop()
