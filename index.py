import os
import shutil

# Define as extensões de arquivo e as pastas correspondentes
extensions = {
    ".jpg": "01 Imagens",
    ".jpeg": "01 Imagens",
    ".png": "01 Imagens",
    ".gif": "01 Imagens",
    ".webp": "01 Imagens",
    ".doc": "01 Documentos",
    ".docx": "01 Documentos",
    ".pdf": "01 Documentos",
    ".pptx": "01 Documentos",
    ".txt": "01 Documentos",
    ".mp4": "01 Videos",
    ".mov": "01 Videos",
    ".avi": "01 Videos",
    ".mp3": "01 Audio",
    ".ogg": "01 Audio",
    ".rar": "01 Arquivos",
    ".zip": "01 Arquivos",
    ".torrent": "01 Arquivos",
    ".exe": "01 Executáveis",
    ".msi": "01 Executáveis",
    ".jar": "01 Executáveis",
    ".c": "01 CODIGOS",
    ".py": "01 CODIGOS",
    ".java": "01 CODIGOS",
    ".sfk": "01 Outros",
}

# Define a pasta onde os arquivos devem ser organizados
source_folder = "D:\ktwo" # <- Coloque o caminho da pasta desejada

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
