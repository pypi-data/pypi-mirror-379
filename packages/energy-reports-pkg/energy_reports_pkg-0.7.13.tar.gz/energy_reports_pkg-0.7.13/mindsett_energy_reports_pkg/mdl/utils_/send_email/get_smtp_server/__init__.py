import smtplib

def get_smtp_server(server, port):

    smtp_server = smtplib.SMTP(server, port)

    # the below part is to make the code compatible in the synapse environment
    # by changing the local_hostname to all lowercase
    (code, resp) = smtp_server.helo()
    if code == 501:
        # parse the local_hostname
        localhost_with_time = str(resp).split('[')[1]
        localhost_name = localhost_with_time.split(' ')[0]

        # apply the lowercase local hostname
        localhost_in_lowercase = localhost_name.lower()
        smtp_server = smtplib.SMTP(server, port, local_hostname=localhost_in_lowercase)
        # server.ehlo(localhost_in_lowercase)
    
    return smtp_server