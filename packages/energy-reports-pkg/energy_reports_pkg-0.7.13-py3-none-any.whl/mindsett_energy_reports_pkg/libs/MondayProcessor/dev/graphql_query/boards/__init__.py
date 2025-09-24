
from .groups import groups

def boards(id, group_id, column_values_ids):
    boards = f'''
    boards (ids:{id}){{
                id
                name
                {groups(group_id, column_values_ids)}
            }}
    '''
    return boards