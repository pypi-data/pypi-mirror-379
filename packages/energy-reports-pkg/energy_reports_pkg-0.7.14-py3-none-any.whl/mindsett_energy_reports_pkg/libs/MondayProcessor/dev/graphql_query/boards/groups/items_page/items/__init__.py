
from .column_values import column_values

def items(column_values_ids):
    items = f"""
                items{{
                        id
                        name
                        {column_values(column_values_ids)}
                        }}
            """
    return items