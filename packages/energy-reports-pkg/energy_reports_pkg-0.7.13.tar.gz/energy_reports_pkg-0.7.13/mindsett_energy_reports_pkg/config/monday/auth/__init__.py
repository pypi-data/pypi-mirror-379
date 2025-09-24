from get_conn_by_id import get_conn_by_id 

monday_com_conn = get_conn_by_id('monday_com_token')

# monday_com_conn = BaseHook.get_connection('monday_com_token')

TOKEN = monday_com_conn['token']