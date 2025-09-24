
from datetime import date
import pandas as pd

from mdl.utils_ import get_group_with_others

def preprocessing_for_statement(df_meta_with_value, 
                                asset_group='asset_class',
                                # fixed_group_to_filter = [], # should be all in lower case charactor # applying the variable column directly
                                row_index_for_total = "Total", 
                                reading_interval_in_mins=10,
                                pct_level_tobe_others = 0):
    
    #Conversion into MWh
    w_to_kw_para = 1./1000
    min_to_hour_para = 1./60
    
    wm_to_kwh_parameter = w_to_kw_para * min_to_hour_para
    reading_to_kwh_parameter = reading_interval_in_mins * wm_to_kwh_parameter
    
    df_meta_with_value[asset_group] = df_meta_with_value[asset_group].str.strip()
    # print('df_meta_with_value: ', df_meta_with_value)

    df_meta_with_value_variable = df_meta_with_value.loc[df_meta_with_value['variable']==True]

    sr_pivot_asset_group = df_meta_with_value_variable.groupby([asset_group, 'period', 'out_of_hours'])["W"].sum() * reading_to_kwh_parameter  # Div 1000 for convertion to MWh

    # print('sr_pivot_asset_groupindex: ', sr_pivot_asset_group.index)
    sr_pivot_asset_group_unstack_ooh = sr_pivot_asset_group.unstack(["out_of_hours"])

    if True not in sr_pivot_asset_group_unstack_ooh.columns:
        return None
    else:
        df_pivot_asset_group_by_period_full = sr_pivot_asset_group_unstack_ooh[True].unstack(["period"])

        df_pivot_asset_group_by_period_no_fixed = df_pivot_asset_group_by_period_full

        # print("df_pivot_asset_group_by_period: ", df_pivot_asset_group_by_period) # debug
        
        # using the 'period' information from the dataframe
        period_range = df_pivot_asset_group_by_period_no_fixed.columns
        period_current = period_range[-1]

        # for avoiding the case that we don't have data for the previous week
        if len(period_range) < 2:
            period_tobe_compared = period_range[-1]
        else:
            period_tobe_compared = period_range[-2]

        # todo: check whether the result can be obtained by unstack directly
        # remove the assets that are generating energy
        df_pivot_asset_group_by_period = df_pivot_asset_group_by_period_no_fixed.loc[df_pivot_asset_group_by_period_no_fixed[period_current]>0].copy()
        df_pivot_asset_group_by_period_renamed = df_pivot_asset_group_by_period.loc[:,period_current].to_frame().rename(columns={period_current: "sum"})
        df_pivot_asset_group_by_period_renamed["sum_pre"] = df_pivot_asset_group_by_period.loc[:,period_tobe_compared]

        sr_total = df_pivot_asset_group_by_period_renamed.loc[df_pivot_asset_group_by_period_renamed['sum']>0].sum() # exclude the negative values

        df_total = sr_total.to_frame().transpose()
        df_total.index = [row_index_for_total]

        df_total.index.name = df_pivot_asset_group_by_period_renamed.index.name
        df_pivot_asset_group_by_period_renamed = pd.concat([df_pivot_asset_group_by_period_renamed, df_total])
        
        df_pivot_asset_group_by_period_renamed['sub'] = df_pivot_asset_group_by_period_renamed.loc[:,'sum'] - df_pivot_asset_group_by_period_renamed.loc[:,'sum_pre']

        df_pivot_asset_group_by_period_renamed["pct"] = df_pivot_asset_group_by_period_renamed["sum"]/df_pivot_asset_group_by_period_renamed.loc[row_index_for_total, "sum"]
        df_pivot_asset_group_by_period_renamed["gt_pct_others"] = df_pivot_asset_group_by_period_renamed["pct"].gt(pct_level_tobe_others)

        df_asset_group_period_sum = df_pivot_asset_group_by_period_renamed.reset_index()

        df_asset_group_period_sum["group_with_others"] = df_asset_group_period_sum.apply(get_group_with_others,asset_group=asset_group,axis=1)

        df_asset_group_period_sum_others = df_asset_group_period_sum.groupby(["group_with_others"]).sum(numeric_only=True)

        df_asset_group_period_sum_others["sum_for_sort"] = df_asset_group_period_sum_others["sum"] 

        df_asset_group_period_sum_others.loc["Others", "sum_for_sort"] = 0

        df_asset_group_period_sum_others.sort_values(["sum_for_sort"], ascending=False, inplace=True)
        df_asset_group_period_sum_others["sub_pct"] = df_asset_group_period_sum_others["sub"]/df_asset_group_period_sum_others["sum_pre"]
        
        return df_asset_group_period_sum_others

    

