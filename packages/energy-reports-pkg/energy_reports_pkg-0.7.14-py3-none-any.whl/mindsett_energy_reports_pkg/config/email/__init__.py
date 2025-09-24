# email template setting, note: all of the available variables for email subject and message templates can be accessed from context object ct

# monday_board_id = '6323575451'

reviewer_emails = ['x.yang@cloudfmgroup.com', 
                  #  's.goud@cloudfmgroup.com',
                    #    'a.green@cloudfmgroup.com',
                    #    'a.grimmett@cloudfmgroup.com',
                    #    's.blank@cloudfmgroup.com',
                    #    's.ruthven@cloudfmgroup.com'
                       ]

subject= """Energy Consumption Report - {{ ct['current_period_str'] }}"""
# message= """ Hi {{ ct['receiver_name'] }},

# Please see the energy report for {{ ct['current_period_str'] }}.

# Kind regards,

# Cloudfm Mindsett Team

# """

message = """
<html>
<body>
<p>Hi {{ ct['receiver_name'] }},<br></p>
<p>Please see the energy report for {{ ct['current_period_str'] }}.</p>
<p>Kind regards,</p>
<p>Cloudfm Mindsett Team</p>
</body>
</html>
"""




