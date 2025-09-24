
from cache_return import cache_return

@cache_return
def select_sites_and_emails(df_config, mode, reviewer_emails):

    if mode == 'publish':
        df_config_select = df_config.loc[df_config.publish]
        df_config_select['send_to'] = df_config_select.mailing_list
    elif mode == 'review':
        df_config_select = df_config.loc[df_config.publish]
        df_config_select['send_to'] = [reviewer_emails for _ in df_config_select.index] # assigning the same emails to every site
    elif mode == 'testing':
        df_config_select = df_config.loc[df_config.testing]
        df_config_select['send_to'] = [reviewer_emails for _ in df_config_select.index]
    else:
        raise Exception('Please provide the right mode [publish, review, testing].')
    
    return df_config_select