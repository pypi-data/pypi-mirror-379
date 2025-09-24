

def get_subgroup_sum_and_rank(df_pivot_asset_group_by_period_renamed,
                              sum_column = None, 
                              gene_column = None):
    
    if sum_column is None:
        sum_column = "sum_abs"

    if gene_column is None:
        gene_column = 'generator'

    # label the entries based on whether generator or not and add sub-group total
    df_pivot_asset_group_by_period_renamed[gene_column] = df_pivot_asset_group_by_period_renamed['sum'] < 0
    # df_pivot_asset_group_by_period_tot = df_pivot_asset_group_by_period_renamed.groupby([gene_column])['sum'].sum().rename('generator_tot')
    # df_pivot_asset_group_by_period_renamed = df_pivot_asset_group_by_period_renamed.merge(df_pivot_asset_group_by_period_tot, left_on=[gene_column], right_index=True)

    # get the rank in sub-group
    df_pivot_asset_group_by_period_renamed[sum_column] = df_pivot_asset_group_by_period_renamed['sum'].abs()
    df_pivot_asset_group_by_period_renamed['rank_in_group'] = df_pivot_asset_group_by_period_renamed.groupby(gene_column)[sum_column].rank(ascending=False, method="dense")

    return df_pivot_asset_group_by_period_renamed