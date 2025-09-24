
from .get_last_update_time import get_last_update_time
from .cache_cf_to_db import cache_cf_to_db
from .extract_contacts import extract_contacts

def sync_with_monday(engine, 
                     df_config,
                     monday_token, 
                     table_name_cache, 
                     monday_board_id,
                     columns_concerned=None, 
                     email_prefix=None):
    
    print('syncing config with monday board ...')

    # check the activity log from monday
    last_update_time = get_last_update_time(monday_token, monday_board_id)
    # print('last_update_time: ', last_update_time)

    # if activity log time > db last updates, then extract contacts from monday and update db

    flag_reload_from_monday = True

    if (df_config.shape[0] > 0) and (not df_config.last_update.isna().all()): # last_update was made null when the last_update_time was not available

        prev_update_time = df_config.last_update.max()
        print('prev_update_time: ', prev_update_time)

        if not (prev_update_time < last_update_time):

            print('[INFO]: using config from the db cache as it is up-to-date!')
            flag_reload_from_monday = False
            
    if flag_reload_from_monday:

        print('extracting contacts ... (about 3 min 30 secs)')
        df_config = extract_contacts(monday_token, monday_board_id,
                                     columns_concerned=columns_concerned, 
                                     email_prefix=email_prefix,
                                     # caching=True
                                    )
    
        # cache the result into db for the future usage and efficiency

        df_config['last_update'] = last_update_time
        # df_config = attach_id_to_buildings(engine, df_config, table_name_org, table_name_building) # df_config has to be the same name, so not renaming it here

        # print('df_config: ', df_config)
        # quit()
        cache_cf_to_db(engine, table_name_cache, df_config)

    return df_config
