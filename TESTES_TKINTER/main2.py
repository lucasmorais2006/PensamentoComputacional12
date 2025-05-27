import tkinter as tk

alternar = {"trocar": False}

def imprimirInfos():
    if alternar["trocar"]:
        rotulo.config(text="Olá mundo!")
    else:
        rotulo.config(text="Olá turma!")
    alternar["trocar"] = not alternar["trocar"] 

janela = tk.Tk()
janela.title("Exemplo botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text="Clique no botão abaixo", font=("Arial, 16"))
rotulo.pack(pady=10)
botao = tk.Button(janela, text="Clique aqui", command=imprimirInfos)

botao.pack(pady=10)
janela.mainloop()