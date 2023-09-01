import os
import tkinter as tk
from tkinter import filedialog
import comtypes.client as cc
from tkinter import messagebox

def convert_pdf_to_word(pdf_path, word_path):
    wdFormatPDF = 17
    wdFormatDocumentDefault = 16

    word = cc.CreateObject("Word.Application")
    doc = word.Documents.Open(pdf_path)
    doc.SaveAs(word_path, FileFormat=wdFormatDocumentDefault)
    doc.Close()
    word.Quit()
    return word_path

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showinfo("Welcome", "Welcome to the PDF to Word Converter!")

    pdf_file_paths = filedialog.askopenfilenames(
        title="Choose PDF files to convert",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if pdf_file_paths:
        messagebox.showinfo("PDF Selection", f"{len(pdf_file_paths)} PDF files selected successfully.")

        for pdf_path in pdf_file_paths:
            base_name = os.path.basename(pdf_path)
            word_file_path = filedialog.asksaveasfilename(
                defaultextension=".docx",
                title=f"Choose where to save the converted Word file for '{base_name}'"
            )

            if word_file_path:
                converted_file_path = convert_pdf_to_word(pdf_path, word_file_path)
                messagebox.showinfo("Conversion Complete", f"The Word file for '{base_name}' has been saved at:\n{converted_file_path}")

if __name__ == "__main__":
    main()
