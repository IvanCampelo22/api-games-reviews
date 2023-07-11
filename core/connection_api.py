import requests
from loguru import logger
import os

BASE_URL = os.getenv('BASE_URL_RAWG')
API_KEY = os.getenv('API_KEY_RAWG')

class ApiGames:
    
    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.api_key = API_KEY
    
    def _make_request(self, method: str, endpoints: str) -> None:
        '''O  method recebe (GET, POST, PUT, DELETE)'''
        if method:
            try:
                response = requests.request(method.upper(), f'{self.base_url}/{endpoints}')
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

    def get_released_last_month(self, api_key = 'b0d3d942a1d44388981df557d759d3a8') -> None:
        response = self._make_request('GET', f'platforms?key={api_key}')
        return response
    
    def get_released_last_month_plataform(self, api_key= 'b0d3d942a1d44388981df557d759d3a8', start_date='', end_date='', plataform_id='') -> None:
        response = self._make_request('GET', f'games?dates={start_date},{end_date}&platforms={plataform_id}&key={api_key}')
        return response