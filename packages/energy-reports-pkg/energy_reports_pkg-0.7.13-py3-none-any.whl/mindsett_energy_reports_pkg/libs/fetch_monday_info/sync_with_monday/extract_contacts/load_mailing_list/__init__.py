import pandas as pd

from MondayProcessor import MondayProcessor
from cache_return import cache_return

@cache_return
def load_mailing_list(monday_token, board_id, 
                      columns_concerned=None, 
                      email_prefix=None):
    
    if columns_concerned is None:
        from .columns_concerned import columns_concerned


    email_prefix = email_prefix or 'email'

    mp = MondayProcessor(monday_token)

    groups_dict = mp._fetchGroups(board_id)

    columns_data = mp.monday.boards.fetch_columns_by_board_id(board_ids=board_id)

    columns_all = [column['title'] for column in columns_data['data']['boards'][0]['columns']]
    len_ep = len(email_prefix)
    columns_emails = [column for column in columns_all if column[:len_ep]==(email_prefix[:len_ep])]

    missing_columns = []
    for concerned_column in columns_concerned:
        if concerned_column not in columns_all:
            missing_columns.append(concerned_column)

    if len(missing_columns) > 0:
        raise Exception(f'[ERROR]: There are missing columns: {missing_columns}!')
    
    columns_select = columns_concerned + columns_emails # merge the two lists
    

    # print('columns_all: ', columns_all)
    # print('columns_select: ', columns_select)

    df_board = pd.DataFrame([])
    for group_id in groups_dict:
        
        board_results = mp._fetchColumnValueByGroup(board_id=board_id, groupId=group_id, columns=columns_select)

        df_group = pd.DataFrame(board_results)
        df_group['group_name'] = groups_dict[group_id]
        df_board = pd.concat([df_board, df_group])

    return df_board