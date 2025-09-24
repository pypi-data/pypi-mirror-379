from .items import items

def items_page(column_values_ids):
    items_page = f"""
            items_page(limit:500){{
                                cursor
                                {items(column_values_ids)}
                            }}
            """
    return items_page