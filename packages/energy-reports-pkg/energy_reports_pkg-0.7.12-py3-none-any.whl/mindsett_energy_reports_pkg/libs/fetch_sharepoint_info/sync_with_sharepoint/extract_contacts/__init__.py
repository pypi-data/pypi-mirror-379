
from .load_mailing_list import load_mailing_list
from .format_contacts import format_contacts

def extract_contacts(sharepoint):

    df_contact_raw = load_mailing_list(sharepoint)

    df_contact = format_contacts(df_contact_raw, 
                                 columns_concerned=sharepoint.excel.columns_concerned
                                 )

    return df_contact