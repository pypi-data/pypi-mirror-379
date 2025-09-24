
from mdl.utils_ import (
    send_email,
)
import jinja2
import pandas as pd

def email_report(receivers, smtp, email, current_period_obj, file_path_or_obj_dict):

    for receiver in receivers:

        send_to = [receiver['email']]

        environment = jinja2.Environment()
        context = {}

        period_type = current_period_obj.freqstr[0]

        if period_type == "W":
            # current_period_str = (current_period_obj).strftime("Week %W, %Y") 
            # add 1 week to the current_period_obj so that the start week is not Week 00
            period_week_str = current_period_obj.strftime('%W')
            period_year_str = current_period_obj.strftime('%Y')
            current_period_str = f'Week {(int(period_week_str)+1):02d}, {period_year_str}'

        else:
            current_period_str = current_period_obj.strftime("Month %b %Y")
        context['current_period_str'] = current_period_str
        context['receiver_name'] = receiver['name']
        

        subject_template = environment.from_string(email.subject)
        email_subject = subject_template.render(ct=context)
        
        message_template = environment.from_string(email.message)
        email_message = message_template.render(ct=context)

        # file_path_or_obj_dict = {filename: file_path/file_obj}

        send_email(smtp.send_from, send_to, 
                    email_subject, email_message, 
                    # signature=email.signature,
                    files=file_path_or_obj_dict,
                    server=smtp.server,
                    port=smtp.port,
                    username=smtp.username,
                    password=smtp.password)