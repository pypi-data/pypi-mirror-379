

def statement_for_biggest_ooh(df_asset_group_period_sum_others, number_for_pick_out=3,  period_freq_str='week'):

    # print('df_asset_group_period_sum_others: ', df_asset_group_period_sum_others) # debug

    if (number_for_pick_out+1) > df_asset_group_period_sum_others.shape[0]: # there are two rows for "Total" and "Others", this is to avoid them to be shown.

        number_for_pick_out = df_asset_group_period_sum_others.shape[0] - 2

        print(f'[WARN]: in func [statement_for_biggest_ooh], the no. of entries in df_asset_group_period_sum_others [{df_asset_group_period_sum_others.shape[0]}] is smaller then the expected number_for_pick_out [ {number_for_pick_out}]', number_for_pick_out)

    df_ooh_biggest = df_asset_group_period_sum_others.head(number_for_pick_out+1).tail(number_for_pick_out).drop(columns=['gt_pct_others','sum_for_sort'])
    
    # pdb.set_trace()

    statement = f"""The largest out-of-hours consumers of energy over the previous {period_freq_str} were: """ #temp fix

    for index, item in enumerate(df_ooh_biggest['sum'].round().astype('int').items()):

        if item[0] not in ['Total', 'Others']: # only add valid entries, not total and others.

            statement_item = "  \t \t \t \t"+str(index+1)+'. '+item[0]+' '+str(item[1])+' kwh,'
            
            statement += statement_item
        else:
            print(f'[WARN]: statement_for_biggest_ooh - Please note that ooh category [{item[0]}] has been skipped')

    statement = statement[:-1]+'.'
    
    return statement