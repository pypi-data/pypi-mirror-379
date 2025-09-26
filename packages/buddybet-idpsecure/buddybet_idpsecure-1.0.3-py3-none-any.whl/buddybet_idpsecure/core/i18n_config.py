from buddybet_i18n.i18n_service import I18nService
import os
from fastapi import Header


def get_i18n(accept_language: str = Header(default="en")) -> I18nService:
    return instance_i18n(accept_language)


def instance_i18n(language: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_app_dir = os.path.abspath(os.path.join(current_dir, "..", "resources"))
    i18n = I18nService(root_dir=root_app_dir)
    i18n.set_language(language)
    return i18n
