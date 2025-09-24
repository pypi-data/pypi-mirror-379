from .items_page import items_page

def groups(id, column_values_ids):
    groups = f'''
            groups(ids:"{id}"){{
                            id
                            {items_page(column_values_ids)}

                        }}
            '''
    return groups