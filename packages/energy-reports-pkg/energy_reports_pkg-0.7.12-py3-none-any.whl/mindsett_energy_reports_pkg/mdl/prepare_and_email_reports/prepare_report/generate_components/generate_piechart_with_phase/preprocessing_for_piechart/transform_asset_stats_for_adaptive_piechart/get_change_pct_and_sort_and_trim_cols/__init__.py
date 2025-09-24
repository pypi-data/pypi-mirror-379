


def get_change_pct_and_sort_and_trim_cols(df_pivot_asset_group_by_period_renamed_rdx_to_keep,
                                            sum_column = None, 
                                            pct_column = None,
                                            gene_column = None,
                                            asset_group = None):
    
    if sum_column is None:
        sum_column = "sum_abs"

    if pct_column is None:
        pct_column = 'sub_pct'

    if gene_column is None:
        gene_column = 'generator'

    if asset_group is None:
        asset_group = 'thing_category'

    # calculate the percentage of changes
    df_pivot_asset_group_by_period_renamed_rdx_to_keep[pct_column] = df_pivot_asset_group_by_period_renamed_rdx_to_keep['sub'] / df_pivot_asset_group_by_period_renamed_rdx_to_keep['sum']

    # sort the list
    df_pivot_asset_group_by_period_renamed_rdx_to_keep_sort = df_pivot_asset_group_by_period_renamed_rdx_to_keep.sort_values([gene_column, 'rank_in_group'])

    # the plotting function requires asset_group to be the index
    df_pivot_asset_group_by_period_renamed_rdx_to_keep_sort_idx = df_pivot_asset_group_by_period_renamed_rdx_to_keep_sort.set_index([asset_group])

    columns_for_export = [sum_column, pct_column, gene_column]
    df_pivot_asset_group_by_period_renamed_rdx_to_keep_sort_idx_trim = df_pivot_asset_group_by_period_renamed_rdx_to_keep_sort_idx[columns_for_export]

    return df_pivot_asset_group_by_period_renamed_rdx_to_keep_sort_idx_trim