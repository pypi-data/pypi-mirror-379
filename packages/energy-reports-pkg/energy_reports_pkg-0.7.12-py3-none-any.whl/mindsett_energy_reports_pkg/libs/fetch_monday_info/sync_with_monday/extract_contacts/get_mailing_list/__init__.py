

def get_mailing_list(sr_contact_row):

    # df_contact_site = df_contact.loc[(df_contact.name==(site_name).replace("''", "'")) & (df_contact.org==org_name)]
    
    monday_columns = sr_contact_row.index
    email_columns = [column for column in monday_columns if 'email' in column]
    
    # df_emails_site = df_contact_site[email_columns]

    ls_emails_site = sr_contact_row[email_columns].tolist()

    # print('ls_emails_site: ', ls_emails_site)
    
    ls_emails_site_nona = [i for i in ls_emails_site if i != None]

    # ls_emails_site_nona
    # print('ls_emails_site_nona: ', ls_emails_site_nona)

    ls_emails_site_nona_with_at = [email_str for email_str in ls_emails_site_nona if '@' in email_str]

    # print('ls_emails_site_nona: ', ls_emails_site_nona)

    return ls_emails_site_nona_with_at