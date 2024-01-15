import os
import shutil

# Define as extensões de arquivo e as pastas correspondentes
extensions = {
    ".jpg" ".jpeg" ".png" ".gif" ".webp": "01 Imagens",
    ".doc" ".docx" ".pdf" ".pptx" ".txt": "01 Documentos",
    ".mp4" ".mov" ".avi": "01 Videos",
    ".mp3" ".ogg": "01 Audio",
    ".rar" ".zip" ".torrent": "01 Arquivos",
    ".exe" ".msi" ".jar": "01 Executáveis",
    ".c" ".py" ".java": "01 CODIGOS",
    ".sfk": "01 Outros",
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
