import requests

# def _fetchBoardLogsById(self, board_id:int):
#     headers = {"Authorization": self._token}
#     data = {"query": f'''query {{
#         boards (ids:{board_id}){
#             activity_logs (limit: 10) {
#             id
#             name
#         }}
#     }}'''}
#     r = requests.post('https://api.monday.com/v2', headers=headers, data=data)
#     return r.json()

def _fetchBoardLogsById(self, board_id, limit=1):
    headers = {"Authorization": self._token,
               "API-Version": '2024-01'}
    data = {"query": f'''query {{
        boards (ids:{board_id}){{
            activity_logs (limit: {limit}) {{
            id
            event
            created_at
        }}
        }}
    }}'''}
    r = requests.post('https://api.monday.com/v2', headers=headers, json=data)

    data = r.json()
    if 'data' not in data:
        print(data) 

    return data