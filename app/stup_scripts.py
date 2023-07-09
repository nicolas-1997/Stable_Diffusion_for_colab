import os
import subprocess
from utils.functions import *
from utils.config import * 
# Agregar elementos personalizados a la lista files_to_download
agregar_elemento(
    "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_nsfw.safetensors",)

# files_to_download.append((url, filepath))

agregar_elemento(
    "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_hard.safetensors",
)
agregar_elemento(
    "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt",
)

for repo_url, repo_name in repositories:
    repo_dir = os.path.join(EXTENSIONS_DIR, repo_name)
    if not os.path.exists(repo_dir):
        subprocess.run(["git", "clone", f"https://github.com/{repo_url}.git", repo_dir])
    else:
        print(f"El repositorio {repo_name} ya existe. Omite la clonación.")

# Descargar archivos
for url, filepath in files_to_download:
    if not os.path.exists(filepath):
        subprocess.run(["curl", "-Lo", filepath, url])
    else:
        print(f"El archivo {os.path.basename(filepath)} ya existe. Omite la descarga.")

# Extraer archivos zip
zip_files_to_extract = [
    (os.path.join(EXTENSIONS_DIR, "microsoftexcel-images-browser.zip"), EXTENSIONS_DIR),
    (os.path.join(MICROSOFTEXCEL_DIR, "embeddings", "embeddings.zip"), os.path.join(MICROSOFTEXCEL_DIR, "embeddings")),
    (os.path.join(MICROSOFTEXCEL_DIR, "models", "ESRGAN", "upscalers.zip"), os.path.join(MICROSOFTEXCEL_DIR, "models", "ESRGAN"))
]

for zip_file, extract_dir in zip_files_to_extract:
    if os.path.exists(zip_file):
        subprocess.run(["unzip", zip_file, "-d", extract_dir])
        os.remove(zip_file)

print("Configuración completada.")

