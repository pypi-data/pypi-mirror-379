

def validate_data_not_empty(df_meta_with_value, df_meta_with_value_building):
    
    if df_meta_with_value.shape[0] == 0:
        raise Exception(f'The dataframe [df_meta_with_value] is empty!')
    
    if df_meta_with_value_building.shape[0] == 0:
        raise Exception(f'The dataframe [df_meta_with_value_building] is empty!')