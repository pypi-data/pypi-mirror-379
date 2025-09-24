
from get_conn_by_id import get_conn_by_id 

from . import excel

sharepoint_conn = get_conn_by_id('mindsett_sharepoint')

client_id = sharepoint_conn['client_id']
client_secret = sharepoint_conn['secret']
site_url = sharepoint_conn['host']

folder_url = "/sites/Mindsett/Shared Documents/9. Data Science/Mailing List - Energy Report"