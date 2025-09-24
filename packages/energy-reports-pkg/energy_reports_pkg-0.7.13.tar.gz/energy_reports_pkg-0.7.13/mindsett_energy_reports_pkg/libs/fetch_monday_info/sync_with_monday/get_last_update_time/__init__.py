
import pandas as pd
from MondayProcessor import MondayProcessor

def get_last_update_time(monday_token, board_id):

    mp = MondayProcessor(monday_token)

    js_logs = mp._fetchBoardLogsById(board_id)
    
    dct_records = js_logs['data']['boards'][0]['activity_logs']

    # print('dct_records: ', dct_records)

    if dct_records == None: # it happened on 11 Nov 24 that the activity log is not available and returned None

        print('js_logs: ', js_logs)
        print('[WARN]: using time now as last_update_time because the Monday ACTIVITY LOG is NOT AVAILABLE !')
        last_update_time = pd.Timestamp.now(tz='UTC').ceil(freq='s')
        return last_update_time
    else:
        df_logs = pd.DataFrame.from_records(dct_records)
        df_logs['created_at'] = pd.to_datetime(df_logs['created_at'].astype('int').div(10), unit='us', utc=True).dt.ceil(freq='s') 
        last_update_time = df_logs.created_at.max()

        return last_update_time