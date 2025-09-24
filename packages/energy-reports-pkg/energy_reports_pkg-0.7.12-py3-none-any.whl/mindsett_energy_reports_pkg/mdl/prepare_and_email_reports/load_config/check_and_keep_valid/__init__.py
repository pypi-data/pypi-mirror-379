
def check_and_keep_valid(df_config):

    df_config = df_config.fillna('')

    # df_config = keep_valid(df_config, columns=['industry', 'floor_size', 'conv_mwh_price', 'timezone'])

    no_industry = (df_config.industry == '')
    no_floor_size = (df_config.floor_size.isna())

    # print('df_config.conv_mwh_price: ', df_config.conv_mwh_price)

    no_conv_mwh_price = (df_config.conv_mwh_price == 0)
    no_timezone = (df_config.timezone.isna())

    not_ready = (no_industry | no_floor_size | no_conv_mwh_price | no_timezone)

    to_report = (df_config.publish | df_config.testing)

    not_ready_but_report = (not_ready & to_report)

    df_not_ready_but_report = df_config.loc[not_ready_but_report]

    if df_not_ready_but_report.shape[0] > 0:
        
        print('df_not_ready_but_report.T: ', df_not_ready_but_report.T)

        raise Exception('df_not_ready_but_report is not empty, please double check the config of [industry, floor_size, conv_mwh_price, timezone] for these sites!')
    
    df_config_ready = df_config.loc[~not_ready]

    # quit()

    return df_config_ready


