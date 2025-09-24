

def exchange_group_name_column(df_meta_with_value, group_name_column_exchange, asset_group_column):

    # for the special groups where we need to use a different column_name as group_name
    for special_group_name in group_name_column_exchange:
        special_group_index = (df_meta_with_value[asset_group_column] == special_group_name)
        df_meta_with_value.loc[special_group_index, asset_group_column] = df_meta_with_value.loc[special_group_index, group_name_column_exchange[special_group_name]]

    return df_meta_with_value