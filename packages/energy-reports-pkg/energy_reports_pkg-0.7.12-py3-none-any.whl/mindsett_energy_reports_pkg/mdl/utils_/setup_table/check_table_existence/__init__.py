def check_table_existence(engine, table_name):
    
    table_schema_name_list = table_name.split('.')

    if len(table_schema_name_list) > 1:
        table_schema = table_schema_name_list[0]
        table_non_schema_name = table_schema_name_list[1]
    else:
        table_schema = 'public'
        table_non_schema_name = table_name

    query_check_existing_tables = f"""select table_name from information_schema.tables where table_schema = '{table_schema}' 
    and table_name = '{table_non_schema_name}'"""

    with engine.connect() as conn:
        list_tables = conn.execute(query_check_existing_tables)

    table_name_list = [table_name[0] for table_name in list_tables]

    if len(table_name_list) == 1:
        # print(f'The table [{table_name}] already exists')
        return True
    else:
        # print(f'The table [{table_name}] does not exist')
        return False