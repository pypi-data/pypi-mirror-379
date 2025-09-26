from fastapi import Depends, HTTPException
from buddybet_idpsecure.core.environment_config import AppConfig
from buddybet_idpsecure.core.i18n_config import find_resources_folder
from buddybet_idpsecure.core.settings_config import load_config
from buddybet_idpsecure.model.user_claims import UserClaims
from buddybet_idpsecure.validation.exceptions import JWTValidationError
from buddybet_idpsecure.validation.validator import TokenValidator
from buddybet_i18n.i18n_service import I18nService

class TransactionAuthorization:
    def __init__(self, token: str):
        self.token = token

    async def transaction_valid(self, config: AppConfig | None = None) -> UserClaims:
        # Configuración del directorio de recursos
        dir_resources = find_resources_folder()
        i18n = I18nService(dir_resources)

        if config is None:
            config = load_config()
        try:
            validator = TokenValidator(config)
            return validator.validate_token(self.token)
        except JWTValidationError as e:
            message = i18n.gettext(e.message_key)
            raise HTTPException(
                status_code=401,
                detail={"error": e.__class__.__name__, "message": message}
            )

