import requests
from loguru import logger
from decouple import config

class ApiFormNps:
    
    def __init__(self) -> None:
        self.url_base = config('')
        self.token = config('')
        
        self._headers = {
            'Authorization' : f'Bearer {self.token}'
        }
    
    def _make_request(self, method: str, endpoints: str) -> None:
        '''O  method recebe (GET, POST, PUT, DELETE)'''
        print(self.url_base)
        if method:
            try:
                response = requests.request(method.upper(), f'{self.url_base}/{endpoints}', headers=self._headers)
                print(response.text)
            except Exception as e:
                logger.error(f'Erro de conexão ao fazer {method} request para {endpoints}: {e}')
                raise Exception(f'Erro de conexão ao fazer {method} request para {endpoints}: {e}')
        else:
            ValueError()
        
        if response.status_code >= 200 and response.status_code <= 204:
            return response
        else:
            logger.error(f"Erro ao fazer {method} pedido para {endpoints}: {response.json()} (Erro de codigo {response.status_code})")
            return response

    def get_forms(self) -> None:
        return self._make_request('GET', 'forms')