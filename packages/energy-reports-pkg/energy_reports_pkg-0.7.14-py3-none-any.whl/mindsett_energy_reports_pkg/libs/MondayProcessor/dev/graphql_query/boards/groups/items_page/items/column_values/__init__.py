from .column import column

def column_values(ids):
    column_values = f"""
                column_values (ids:{ids}) {{
                            {column}
                            text
                        }}
                        """
    return column_values