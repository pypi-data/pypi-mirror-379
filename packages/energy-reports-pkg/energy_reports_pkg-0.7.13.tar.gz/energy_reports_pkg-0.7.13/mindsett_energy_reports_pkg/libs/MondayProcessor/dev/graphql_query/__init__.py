
from .boards import boards

def graphql_query(board_id, group_id, column_values_ids):

    graphql_query = f'''query {{
            {boards(board_id, group_id, column_values_ids)} 
        }}'''
    
    return graphql_query
    