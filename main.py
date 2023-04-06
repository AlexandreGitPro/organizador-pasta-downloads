import os, shutil
import tkinter as tk
def move_files_by_extension(src_folder, dst_folder):
    files_by_extension = {}
    for root, dirs, files in os.walk(src_folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1]
            if file_extension not in files_by_extension:
                files_by_extension[file_extension] = []
            files_by_extension[file_extension].append(filepath)
    for file_extension, filepaths in files_by_extension.items():
        folder_name = file_extension[1:].lower()
        folder_path = os.path.join(dst_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for filepath in filepaths:
            filename = os.path.basename(filepath)
            new_path = os.path.join(folder_path, filename)
            try:
                shutil.move(filepath, new_path)
                print(f"movendo: {filepath} para {new_path}")
            except Exception as e:
                print("erro ao mover um arquivo")
    print("Arquivos organizados com sucesso")

janela = tk.Tk()
janela.title("Organizador de arquivos")
janela.geometry("300x200")
botao = tk.Button(janela, text="Organizar arquivos")

def on_button_click():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    meus_arquivos_path = os.path.join(downloads_path, "meus_arquivos")
    move_files_by_extension(downloads_path, meus_arquivos_path)

botao.config(command=on_button_click)
botao.pack()
janela.mainloop()