import os
import shutil

# Define as extensões de arquivo e as pastas correspondentes
extensions = {
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".webp": "Imagens",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".pdf": "Documentos",
    ".pptx": "Documentos",
    ".txt": "Documentos",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mp3": "Audio",
    ".ogg": "Audio",
    ".rar": "Arquivos",
    ".zip": "Arquivos",
    ".exe": "Executáveis",
    ".sfk": "Outros",
}

# Define a pasta onde os arquivos devem ser organizados
source_folder = "D:\ktwo"

# Percorre todos os arquivos na pasta fonte
for filename in os.listdir(source_folder):
    # Obtém a extensão do arquivo
    extension = os.path.splitext(filename)[1].lower()

    # Verifica se a extensão está na lista de extensões
    if extension in extensions:
        # Define o caminho da pasta de destino
        destination_folder = os.path.join(source_folder, extensions[extension])

        # Cria a pasta de destino, se ela não existir
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move o arquivo para a pasta de destino
        shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
