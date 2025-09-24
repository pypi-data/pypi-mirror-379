
def get_mailing_list(sr_contact_row):
    
    monday_columns = sr_contact_row.index
    email_columns = [column for column in monday_columns if 'email' in column]
    ls_emails_site = sr_contact_row[email_columns].tolist()
    ls_emails_site_nona = [i for i in ls_emails_site if isinstance(i, str)]
    ls_emails_site_nona_with_at = [email_str for email_str in ls_emails_site_nona if '@' in email_str]

    return ls_emails_site_nona_with_at