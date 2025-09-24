import uuid
import numpy as np

from cache_return import cache_return

from .load_mailing_list import load_mailing_list
# from ..cache_result import cache_result
from .get_mailing_list import get_mailing_list

@cache_return
def extract_contacts(monday_token, 
                     board_id,
                     columns_concerned=None, 
                     email_prefix=None):
    
    # email_columns = [f'email {idx+1}' for idx in range(max_no_email)]
    # columns = [building_column, *email_columns]
    # print('columns: ', columns)

    df_contact = load_mailing_list(monday_token, board_id,
                                    columns_concerned=columns_concerned, 
                                    email_prefix=email_prefix,
                                    caching=False)

    # # make the names lower case
    df_contact.columns = [column.lower() for column in df_contact.columns]
    df_contact = df_contact.rename(columns={'name': 'item_name'})
    df_contact['building_id'] = df_contact['building_id'].apply(uuid.UUID)

    # df_contact['review'] = df_contact[role_column].str.contains('Review', na=False)
    # df_contact['receive'] = df_contact[role_column].str.contains('Receive', na=False)

    # df_receive = df_contact.loc[df_contact['receive']]
    # df_review = df_contact.loc[df_contact['review']]

    # contacts = {}

    # contacts['receivers'] = df_receive.groupby(name_column)[email_column].apply(list).reset_index().to_dict('records')
    # contacts['reviewers'] = df_review.groupby(name_column)[email_column].apply(list).reset_index().to_dict('records')
    
    # df_contact.publish = (df_contact.publish == 'v')
    # df_contact.testing = (df_contact.testing == 'v')
    # df_contact.occupancy_available = (df_contact.occupancy_available == 'v')
    df_contact.pct_level_tobe_others = df_contact.pct_level_tobe_others.astype('float')
    df_contact.pct_hide = df_contact.pct_hide.replace('', '0').astype('float')
    df_contact.conv_mwh_price = df_contact.conv_mwh_price.replace('', '0').astype('float')
    # df_contact.insight_statements = df_contact.insight_statements.replace('', None)
    df_contact.floor_sqm = df_contact.floor_sqm.replace('', np.NaN).astype('float')

    df_contact['mailing_list'] = df_contact.apply(get_mailing_list, axis=1)

    monday_columns = df_contact.columns
    email_columns = [column for column in monday_columns if 'email' in column]

    df_contact = df_contact.drop(columns=email_columns)

    return df_contact