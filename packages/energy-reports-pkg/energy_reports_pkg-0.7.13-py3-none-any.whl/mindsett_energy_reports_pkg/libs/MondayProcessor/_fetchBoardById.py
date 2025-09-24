import requests

def _fetchBoardById(self, board_id:int):
    headers = {"Authorization": self._token,
               "API-Version": '2024-01'}
    data = {"query": f'''query {{
        boards (ids:{board_id}){{
            id
            name
        }}
    }}'''}
    r = requests.post('https://api.monday.com/v2', headers=headers, data=data)
    return r.json()