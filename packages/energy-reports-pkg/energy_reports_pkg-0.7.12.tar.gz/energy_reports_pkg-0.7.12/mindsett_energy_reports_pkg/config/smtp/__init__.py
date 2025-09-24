
from get_conn_by_id import get_conn_by_id 

email_conn = get_conn_by_id('mindsett_reporting_email')

server = email_conn['host']
port = email_conn['port']
send_from = email_conn['send_from']
username = email_conn['login']
password = email_conn['password']