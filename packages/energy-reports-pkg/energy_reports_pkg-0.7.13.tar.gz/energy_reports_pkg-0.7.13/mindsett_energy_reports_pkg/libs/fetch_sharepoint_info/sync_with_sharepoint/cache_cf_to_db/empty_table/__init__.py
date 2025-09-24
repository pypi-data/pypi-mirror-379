def empty_table(engine, table_name, with_log=True):
    
    with engine.connect() as conn:

        # delete data (empty) in the table
        query_empty_table = f"""DELETE FROM {table_name};"""
        conn.execute(query_empty_table) 

    if with_log:
        print(f'The table [{table_name}] is empty now.')
    return