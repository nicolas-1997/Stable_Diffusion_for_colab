import os 
from .config import MICROSOFTEXCEL_DIR, ruta_requirements_versions_txt, ruta_requirements_txt

# Función para agregar elementos a la lista files_to_download
def agregar_elemento(url):
    """Agregar elemento se encarga de agregar una url a files_to_dowload, ademas de darle la estructura necesaria para esta lista,
    Ejemplo: (URL), os.path.join(microsoftexcel_dir, "models", "Stable-diffusion", "nombre_extraido_de_url")
    Args:
        url (string): Link a Modelo de Stable Difussion, (Preferiblemente de huggingface)
    """
    name_model = os.path.basename(url)
    filepath= os.path.join(MICROSOFTEXCEL_DIR, "models", "Stable-diffusion", name_model)
    return (url, filepath)


def agregar_requerimiento_torchmetrics():
    """
    Agrega el requerimiento 'torchmetrics==0.11.4' a los archivos de requisitos.

    Esta función clona un repositorio y luego modifica los archivos de requisitos especificados
    en las rutas 'ruta_requirements_txt' y 'ruta_requirements_versions_txt'. Agrega el requerimiento
    'torchmetrics==0.11.4' a ambos archivos para solucionar problemas de compatibilidad.

    Nota: Asegúrate de haber reemplazado '<URL_del_repositorio>' con la URL del repositorio que deseas clonar.

    Args:
        No recibe argumentos.

    Returns:
        No retorna ningún valor.
    """

    # Leer el contenido actual de los archivos
    with open(ruta_requirements_txt, 'r') as f:
        requirements = f.readlines()

    with open(ruta_requirements_versions_txt, 'r') as f:
        version_requirements = f.readlines()

    # Agregar el requerimiento torchmetrics==0.11.4
    requirements.append('torchmetrics==0.11.4\n')
    version_requirements.append('torchmetrics==0.11.4\n')

    # Guardar los cambios actualizados
    with open(ruta_requirements_txt, 'w') as f:
        f.writelines(requirements)

    with open(ruta_requirements_versions_txt, 'w') as f:
        f.writelines(version_requirements)
