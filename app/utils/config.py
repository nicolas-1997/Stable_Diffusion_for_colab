import os

# Directorio base del proyecto
base_dir = os.getcwd()

# Directorio de Microsoft Excel
MICROSOFTEXCEL_DIR = os.path.join(base_dir, "microsoftexcel")

# Directorio de extensiones
EXTENSIONS_DIR = os.path.join(MICROSOFTEXCEL_DIR, "extensions")


#Ruta a los archivos de Requirements. 
ruta_requirements_versions_txt = f'{MICROSOFTEXCEL_DIR}/requirements_versions.txt'
ruta_requirements_txt = f'{MICROSOFTEXCEL_DIR}/requirements.txt'

# Lista de archivos para descargar (por defecto)
files_to_download = [
    ("https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel131.zip", os.path.join(base_dir, "microsoftexcel.zip")),
    ("https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel-images-browser.zip", os.path.join(EXTENSIONS_DIR, "microsoftexcel-images-browser.zip")),
    ("https://huggingface.co/nolanaatama/colab/resolve/main/embeddings.zip", os.path.join(MICROSOFTEXCEL_DIR, "embeddings", "embeddings.zip")),
    ("https://huggingface.co/nolanaatama/colab/resolve/main/upscalers.zip", os.path.join(MICROSOFTEXCEL_DIR, "models", "ESRGAN", "upscalers.zip"))
]


# Clonar los repositorios
repositories = [
    ("nolanaatama/microsoftexcel-tunnels", "microsoftexcel-tunnels"),
    ("nolanaatama/microsoftexcel-controlnet", "microsoftexcel-controlnet"),
    ("nolanaatama/microsoftexcel-supermerger", "microsoftexcel-supermerger"),
    ("fkunn1326/openpose-editor", "openpose-editor"),
    ("hnmr293/posex", "posex"),
    ("nolanaatama/a1111-microsoftexcel-tagcomplete", "a1111-microsoftexcel-tagcomplete"),
    ("nolanaatama/a1111-microsoftexcel-locon", "a1111-microsoftexcel-locon")
]
