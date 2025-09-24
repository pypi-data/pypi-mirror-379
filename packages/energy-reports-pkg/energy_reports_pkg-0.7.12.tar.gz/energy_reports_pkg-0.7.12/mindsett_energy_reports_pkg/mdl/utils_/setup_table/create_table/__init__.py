

def create_table(engine, table_name, columns_dict, hypertable=False, time_column='time', index=None, constraint=None):
    """
    Function Name: create_table
    Parameters   : sql connection engine, table name, column dictionay, hypertable required flag
    Description  : creates a new table 
    
    """
    
    if hypertable:     
        if time_column not in columns_dict:
            raise "For hypertable requires a valid time column in columns_dict defined with schema timestamp"
    
    with engine.connect() as conn: 
        
        if hypertable:
            # enable the timescaledb extension, so function create_hypertable can be used
            query_create_extensions = "CREATE EXTENSION IF NOT EXISTS timescaledb;" 
            conn.execute(query_create_extensions)
        
        columns_list = [f"{column_name} {columns_dict[column_name]}" for column_name in columns_dict]
        
        query_columns_statement = ", ".join(columns_list)
        
        query_create_normaltable = f"""CREATE TABLE {table_name} ({query_columns_statement});"""

        conn.execute(query_create_normaltable)

        table_feature_statement = ''
        
        if hypertable:
            query_create_hypertable = f"SELECT create_hypertable('{table_name}', '{time_column}');"
            conn.execute(query_create_hypertable)
            table_feature_statement += ', as hypertable'

        if index is not None:
            index_name = list(index)[0]
            if isinstance(index[index_name], list):
                index_columns_list = index[index_name]
            else:
                index_columns_list = [index[index_name]] # convert variable to list

            index_columns_str = ", ".join(index_columns_list)

            query_create_index = f"CREATE INDEX {index_name} ON {table_name} ({index_columns_str});"
            conn.execute(query_create_index)
            table_feature_statement += f', with index: {index_name} - [{index_columns_str}]'

        if constraint is not None:
            for constraint_name in list(constraint):
                if isinstance(constraint[constraint_name], list):
                    constraint_columns_list = constraint[constraint_name]
                else:
                    constraint_columns_list = [constraint[constraint_name]] # convert variable to list

                constraint_columns_str = ", ".join(constraint_columns_list)

                query_create_constraint = f"ALTER TABLE {table_name} ADD CONSTRAINT {constraint_name} UNIQUE ({constraint_columns_str});"
                
                # print('query_create_constraint: ', query_create_constraint)
                conn.execute(query_create_constraint)

                table_feature_statement += f', with constraint: {constraint_name} - [{constraint_columns_str}]'
                # conn.commit()

                # example:
                # ALTER TABLE table_name
                # ADD CONSTRAINT constraint_name
                # UNIQUE(column1,column2,..)

    print(f'New table [{table_name}] is created' + table_feature_statement + '.')
    return