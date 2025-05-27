import tkinter as tk
janela = tk.Tk()
janela.title("Minha primeira janela")
rotulo = tk.Label(janela, text="Bem vindo ao Tkinter!")
rotulo.pack(padx=20, pady=20)                  
janela.geometry("600x400")
janela.mainloop()