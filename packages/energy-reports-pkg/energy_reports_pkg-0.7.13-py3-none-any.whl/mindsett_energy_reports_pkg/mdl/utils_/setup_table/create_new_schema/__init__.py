def create_new_schema(engine, schema_name):
    
    with engine.connect() as conn:
        query_create_schema = f"""CREATE SCHEMA IF NOT EXISTS {schema_name};"""
        conn.execute(query_create_schema) 
    
    print(f'New schema [{schema_name}] is created.')
    return