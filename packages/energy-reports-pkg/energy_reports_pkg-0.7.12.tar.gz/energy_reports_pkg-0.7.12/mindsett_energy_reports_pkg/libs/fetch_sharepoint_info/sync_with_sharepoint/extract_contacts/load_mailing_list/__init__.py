
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential

from .get_excel_file_from_link import get_excel_file_from_link
from .load_excel_as_df import load_excel_as_df


def load_mailing_list(sharepoint):

    # get sharepoint context
    ctx = ClientContext(sharepoint.site_url).with_credentials(ClientCredential(sharepoint.client_id, sharepoint.client_secret))

    file_name = getattr(sharepoint.excel, 'file_name', None)
    sheet_name = getattr(sharepoint.excel, 'sheet', None)

    if file_name is None:
        raise Exception('[ERROR]: Please specify the excel file name!')

    sharepoint_link = sharepoint.folder_url + '/' + file_name 

    excel_file = get_excel_file_from_link(ctx, sharepoint_link)

    # sheet_name = sharepoint.excel.sheet
    
    df_contact = load_excel_as_df(ctx, excel_file, 
                                  sheet_name=sheet_name)

    return df_contact

