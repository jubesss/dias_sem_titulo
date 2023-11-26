from datetime import date


def dias_sem_titulo_internacional():

    ultima_vitoria = date(2011, 8, 24)


    dias_sem_vitoria = (date.today() - ultima_vitoria).days

    return dias_sem_vitoria


import tkinter as tk

janela = tk.Tk()
janela.title('Dias sem título')
janela.geometry('450x250')


label_vazia = tk.Label(janela, text='')

label_vazia.grid(row=0, column=0)

label_dias_sem_titulo = tk.Label(janela,
                                 text=f"O Internacional está sem um título continental há {dias_sem_titulo_internacional()} dias.")
label_dias_sem_titulo.grid(row=1, column=0, padx=65, pady=10)

janela.mainloop()
