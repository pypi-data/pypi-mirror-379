

def get_entries_to_display(df_pivot_asset_group_by_period_renamed_rdx,
                           max_display_cnt=None,
                           gene_column=None,
                           asset_group=None):

    if max_display_cnt is None:
        max_display_cnt = 8
    
    if gene_column is None:
        gene_column = 'generator'

    if asset_group is None:
        asset_group = 'thing_category'

    # get the rows to keep/display and redundant rows to merge
    df_pivot_asset_group_by_period_renamed_rdx['to_be_merged'] = df_pivot_asset_group_by_period_renamed_rdx['rank_overall_protect'] > max_display_cnt
    df_pivot_asset_group_by_period_renamed_rdx_to_merge = df_pivot_asset_group_by_period_renamed_rdx.loc[df_pivot_asset_group_by_period_renamed_rdx['to_be_merged']]
    df_pivot_asset_group_by_period_renamed_rdx_to_keep = df_pivot_asset_group_by_period_renamed_rdx.loc[~df_pivot_asset_group_by_period_renamed_rdx['to_be_merged']]
    df_pivot_asset_group_by_period_renamed_rdx_to_merge_grp = df_pivot_asset_group_by_period_renamed_rdx_to_merge.groupby([gene_column]).agg({'sum': 'sum', 
                                                                                                                                              'sum_pre': 'sum', 
                                                                                                                                              'sub': 'sum'})

    # merge the redundant rows to "others" in the rows to keep
    for gene, sr_gene in df_pivot_asset_group_by_period_renamed_rdx_to_merge_grp.iterrows():

        idx_last_row = df_pivot_asset_group_by_period_renamed_rdx_to_keep.loc[df_pivot_asset_group_by_period_renamed_rdx_to_keep[gene_column]==gene].index.max()
        df_pivot_asset_group_by_period_renamed_rdx_to_keep.loc[idx_last_row, asset_group] = 'Other Assets' if gene==False else 'Other Sources'

        for column in df_pivot_asset_group_by_period_renamed_rdx_to_merge_grp.columns:
            df_pivot_asset_group_by_period_renamed_rdx_to_keep.loc[idx_last_row, column] += sr_gene[column]

    return df_pivot_asset_group_by_period_renamed_rdx_to_keep