def append_df_to_table(engine, table_name, df):
    
    table_schema_name_list = table_name.split(".")

    if len(table_schema_name_list) > 1:
        table_schema = table_schema_name_list[0]
        table_non_schema_name = table_schema_name_list[1]
    else:
        table_schema = "public"
        table_non_schema_name = table_name
        
    total_records = len(df)
    
  
    with engine.connect() as conn:
  
        df.to_sql(
           name=table_non_schema_name,
           con=conn,
           if_exists="append",
           schema=table_schema,
           chunksize=5000,
           index=False
           )

    print(f'The config cache in database table [{table_name}] is updated with [{total_records}] records.')
    # print(f'[{total_records}] records have been written to Table [{table_name}] successfully.')
   
    return 