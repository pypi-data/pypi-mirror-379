
import os
import pandas as pd

pd.options.mode.chained_assignment = None

from .prepare_report import prepare_report
from .email_report import email_report
from .ClientSite import ClientSite
from .load_config import load_config
from .select_sites_and_emails import select_sites_and_emails

from mdl.utils_ import (
    delete_files_in_directory,
    setup_table
)

def prepare_and_email_reports(cf, 
                              mode='review', 
                              debug=False,
                              sync_source=None,
                              cache_in_memory=True, 
                              cache_directory=None):

    if cache_in_memory:
        report_file_folder = None
        directory_to_savefile = None
    else:
        if cache_directory == None:
            cache_directory = os.path.join(os.path.dirname(__file__), '_cache_/')

        report_file_folder = os.path.join(cache_directory, '_cached_reports_/')
        directory_to_savefile = os.path.join(cache_directory, '_cached_files_/')

    setup_table(cf.postgresdb.engine, 
                cf.postgresdb.table_mailing.name, 
                cf.postgresdb.table_mailing.columns_dict,
                hypertable=cf.postgresdb.table_mailing.hypertable)
    
    setup_table(cf.postgresdb.engine, 
                cf.postgresdb.table_cache.name, 
                cf.postgresdb.table_cache.columns_dict,
                hypertable=cf.postgresdb.table_cache.hypertable)
    
    # get contacts from db

    df_contact = load_config(cf.postgresdb.engine, 
                             cf.sharepoint,
                             cf.postgresdb.table_org.name,
                             cf.postgresdb.table_building.name,
                             cf.postgresdb.table_timezone.name,
                             cf.postgresdb.table_sqm.name,
                             cf.postgresdb.table_price.name,
                             cf.postgresdb.table_cache.name, 
                             list(cf.postgresdb.table_cache.columns_dict),
                             sync_source=sync_source)

    df_contact_select = select_sites_and_emails(df_contact, mode, cf.email.reviewer_emails)

    # print(f'{df_contact_select=}')

    # quit()
    for _, row in df_contact_select.iterrows():

        site_obj = ClientSite(row)
        df_receivers = pd.DataFrame({'email': row['send_to']})

        if df_receivers['email'].nunique() > 0:
            
            file_path_or_obj_dict, current_period_obj = prepare_report(cf, site_obj, 
                                                                    debug=debug,
                                                                    report_file_folder=report_file_folder, 
                                                                    directory_to_savefile=directory_to_savefile)    

            # print('row: ', row)
            # print("row['send_to']: ", row['send_to'])

            df_receivers = pd.DataFrame({'email': row['send_to']})
            df_receivers['name'] = site_obj.manager_name

            receivers = df_receivers.to_dict('records')

            # print('receivers: ', receivers)

            # quit()

            email_report(receivers, cf.smtp, cf.email, current_period_obj, file_path_or_obj_dict)
        else: 
            print(f'{site_obj.site_name} - {site_obj.site_name}: no email address to send to!')
        
    if not cache_in_memory:
        delete_files_in_directory(report_file_folder, ignore=['__init__.py'])
        delete_files_in_directory(directory_to_savefile, ignore=['__init__.py'])