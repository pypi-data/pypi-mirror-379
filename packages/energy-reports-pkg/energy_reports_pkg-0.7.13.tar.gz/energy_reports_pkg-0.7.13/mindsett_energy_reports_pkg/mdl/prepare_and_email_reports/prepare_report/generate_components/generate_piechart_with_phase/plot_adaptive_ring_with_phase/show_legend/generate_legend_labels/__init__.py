

from .get_formatted_sum import get_formatted_sum
from .get_formatted_arrow import get_formatted_arrow
from .get_formatted_pct import get_formatted_pct
from .get_formatted_name import get_formatted_name


def generate_legend_labels(df_asset_class_monthly_sum_others, # this dataframe is required to have asset class as index and have columns "sub_pct", "sum"
                            sum_column = None,
                            pct_column = None,
                            # space_len_long = 5,
                            space_len_short = None,
                            pct_len = None,
                            kwh_len = None):
    
    if sum_column is None:
        sum_column = "sum"
    if pct_column is None:
        pct_column = "sub_pct"
    if space_len_short is None:
        space_len_short = 1

    labels = []

    # label_space_long = "," + " "*space_len_long 
    label_space_short = " "*space_len_short

    for index, item in df_asset_class_monthly_sum_others.iterrows():

        # print(f'{index = }')

        # print(f'{item = }')
        # print(f'{pct_column = }')

        label_kwh = get_formatted_sum(item[sum_column], 
                                     sum_value_len=kwh_len)
        label_arrow = get_formatted_arrow(item[pct_column])
        label_pct = get_formatted_pct(item[pct_column],
                                      pct_len=pct_len)

        label_name = get_formatted_name(index)

        label = label_kwh + label_space_short + label_arrow+ " " + label_pct + label_space_short + label_name

        # print(f'{label = }')

        labels.append(label)
        
    return labels
