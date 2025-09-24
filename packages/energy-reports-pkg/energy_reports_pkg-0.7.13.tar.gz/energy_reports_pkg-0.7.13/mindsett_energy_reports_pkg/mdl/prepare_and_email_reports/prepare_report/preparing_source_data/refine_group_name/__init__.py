
from mdl.utils_ import modify_group_names
from .exchange_group_name_column import exchange_group_name_column

def refine_group_name(df_meta_with_value, 
                      asset_group, 
                      group_name_column_exchange, 
                      fillna_value,
                      group_name_modification):
    
    df_meta_with_value = exchange_group_name_column(df_meta_with_value, 
                                                    group_name_column_exchange, 
                                                    asset_group)
    
    df_meta_with_value[asset_group] = df_meta_with_value[asset_group].fillna(fillna_value) 

    df_meta_with_value = modify_group_names(df_meta_with_value, 
                                            group_name_column=asset_group,
                                            modification_dict=group_name_modification) 
    return df_meta_with_value