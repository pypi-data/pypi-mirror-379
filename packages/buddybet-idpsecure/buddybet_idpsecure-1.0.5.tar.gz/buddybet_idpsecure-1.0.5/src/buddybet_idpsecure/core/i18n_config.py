from buddybet_i18n.i18n_service import I18nService
import os
from fastapi import Header
from pathlib import Path


def get_i18n(accept_language: str = Header(default="en")) -> I18nService:
    return instance_i18n(accept_language)


def instance_i18n(language: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_app_dir = os.path.abspath(os.path.join(current_dir, "..", "resources"))
    i18n = I18nService(root_dir=root_app_dir)
    i18n.set_language(language)
    return i18n



def find_resources_folder(start_path=None):
    # Si no se pasa un start_path, tomar el directorio actual
    start_path = start_path or Path(__file__).resolve()

    # Subir hasta encontrar la carpeta 'resources'
    while start_path != start_path.root:
        resources_path = start_path / 'resources'
        if resources_path.exists() and resources_path.is_dir():
            return resources_path
        start_path = start_path.parent

    raise FileNotFoundError("No se encontró la carpeta 'resources' en el proyecto")