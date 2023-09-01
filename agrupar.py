import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog

def juntar_pdfs(caminho_pasta, nome_novo_arquivo):
    pdf_novo = PyPDF2.PdfWriter()

    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
            pdf = PyPDF2.PdfReader(caminho_arquivo)
            for pagina in pdf.pages:
                pdf_novo.add_page(pagina)

    with open(nome_novo_arquivo, 'wb') as novo_arquivo:
        pdf_novo.write(novo_arquivo)

    print(f'PDFs foram juntados em {nome_novo_arquivo}')
    root.destroy()  


def selecionar_pasta():
    caminho_pasta = filedialog.askdirectory()
    if caminho_pasta:
        nome_final = simpledialog.askstring("Nome do arquivo final", "Digite o nome do arquivo")
        if nome_final:
            nome_novo_arquivo = os.path.join(caminho_pasta, f'{nome_final}.pdf')
            juntar_pdfs(caminho_pasta, nome_novo_arquivo)


root = tk.Tk()
root.title('Juntar PDFs')

selecionar_btn = tk.Button(root, text='Selecione uma pasta', command=selecionar_pasta)
selecionar_btn.pack(padx=20, pady=20)

root.mainloop()
