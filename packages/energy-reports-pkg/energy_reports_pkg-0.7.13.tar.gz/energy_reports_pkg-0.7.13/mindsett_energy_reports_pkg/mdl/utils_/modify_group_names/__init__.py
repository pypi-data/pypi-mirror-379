
# modify the names in asset_group based on the provided dictionary

def modify_group_names(df_meta_with_value, group_name_column="asset_type", modification_dict={}):
    
    # the letter cases and spaces prefix/sufix will not affect the result
    df_meta_with_value[group_name_column] = df_meta_with_value[group_name_column].str.strip()

    modification_dict_with_lowercase_key = {}
    for group in modification_dict:
        modification_dict_with_lowercase_key[group.lower().strip()] = modification_dict[group]

    df_meta_with_value[group_name_column] = df_meta_with_value[group_name_column] \
                                                                            .str.lower() \
                                                                            .map(modification_dict_with_lowercase_key) \
                                                                            .fillna(df_meta_with_value[group_name_column])
    return df_meta_with_value