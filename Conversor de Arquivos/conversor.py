from pdf2docx import Converter
from docx import Document
from fpdf import FPDF
from tkinter import Tk, filedialog
import os

def pdf_para_word(pdf_file, word_file):
    # Cria o objeto Converter e faz a conversão
    cv = Converter(pdf_file)
    cv.convert(word_file)
    cv.close()
    print(f'Arquivo {word_file} criado com sucesso!')

def word_para_pdf(word_file, pdf_file):
    # Lê o arquivo .docx
    doc = Document(word_file)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adiciona o conteúdo do Word ao PDF
    for paragraph in doc.paragraphs:
        pdf.multi_cell(0, 10, paragraph.text)

    # Salva o PDF
    pdf.output(pdf_file)
    print(f'Arquivo {pdf_file} criado com sucesso!')

def selecionar_arquivo():
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename()  # Abre a janela de diálogo para selecionar o arquivo
    root.destroy()  # Fecha a instância do Tk após a seleção do arquivo
    return file_path

def main():
    print("Bem-vindo ao Conversor de Arquivos!")
    print("Escolha uma opção:")
    print("1 - Converter PDF para Word")
    print("2 - Converter Word para PDF")
    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        pdf_file = selecionar_arquivo()
        if pdf_file:
            word_file = os.path.splitext(pdf_file)[0] + '.docx'
            pdf_para_word(pdf_file, word_file)
        else:
            print("Nenhum arquivo selecionado.")
    elif escolha == '2':
        word_file = selecionar_arquivo()
        if word_file:
            pdf_file = os.path.splitext(word_file)[0] + '.pdf'
            word_para_pdf(word_file, pdf_file)
        else:
            print("Nenhum arquivo selecionado.")
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()