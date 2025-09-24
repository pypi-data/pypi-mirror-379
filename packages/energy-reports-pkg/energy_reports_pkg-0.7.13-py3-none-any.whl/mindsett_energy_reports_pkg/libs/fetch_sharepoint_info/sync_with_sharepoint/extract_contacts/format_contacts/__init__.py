
import uuid

from .uuid_for_nona import uuid_for_nona
from .extract_id import extract_id
from .get_mailing_list import get_mailing_list

def format_contacts(df_contact, 
                    columns_concerned=None):

    if columns_concerned is None:
        from .columns_concerned import columns_concerned

    pct_level_tobe_others_default = 0.03
    pct_hide_default = 4
    conv_mwh_price_default = 190

    # standardize the column names
    df_contact.columns = [column.lower() for column in df_contact.columns]
    df_contact = df_contact.rename(columns={'building_name': 'item_name', 'org': 'group_name'})

    # fill the names for null values
    df_contact['group_name'] = df_contact['group_name'].ffill()
    df_contact['insight_statements'] = df_contact['insight_statements'].fillna('')
    df_contact['group_name_column_exchange'] = df_contact['group_name_column_exchange'].fillna('')
    df_contact['group_name_modification'] = df_contact['group_name_modification'].fillna('')
    df_contact['manager_name'] = df_contact['manager_name'].fillna('')

    # columns type formatting
    df_contact['publish'] = (df_contact['publish'] == 'v')
    df_contact['testing'] = (df_contact['testing'] == 'v')
    df_contact['occupancy_available'] = (df_contact['occupancy_available'] == 'v')
    df_contact['building_id'] = df_contact['building_id'].apply(uuid_for_nona)

    df_contact['pct_level_tobe_others'] = df_contact['pct_level_tobe_others'].fillna(pct_level_tobe_others_default).astype('float')
    df_contact['floor_sqm'] = df_contact['floor_sqm'].astype('float')

    df_contact['pct_hide'] = df_contact['pct_hide'].fillna(pct_hide_default).astype('float')

    df_contact['conv_mwh_price'] = df_contact['conv_mwh_price'].fillna(conv_mwh_price_default).astype('float')

    # format the monday board ids
    df_contact['board_id'] = df_contact['board_id'].apply(extract_id)
    df_contact['hvac_board_id'] = df_contact['hvac_board_id'].apply(extract_id)

    # get_mailing_list
    df_contact['mailing_list'] = df_contact.apply(get_mailing_list, axis=1)

    # drop the email related columns
    monday_columns = df_contact.columns
    email_columns = [column for column in monday_columns if 'email' in column]
    df_contact = df_contact.drop(columns=email_columns)

    # select the concerned columns
    df_contact_sel = df_contact[columns_concerned]

    return df_contact_sel