from pathlib import Path
import os
import ast

class ClientSite:

    from .get_schedule_records import get_schedule_records
    from .get_period_range import get_period_range
    from .get_start_time import get_start_time
    from .get_start_time_co2_barchart import get_start_time_co2_barchart
    from .get_end_time import get_end_time

    pct_level_tobe_others = 0.03
    pct_hide = 4 # hide the labels smaller then the value specified by pct_hide
    currency = 'GBP'
    conv_mwh_price = 190
    timezone = 'UTC'
    size_in_sqm = True

    # setup default backup schedule info
    weekend=7
    working_start_time="08:30:00"
    working_end_time="23:59:59"

    period_offset_previous = 2 # offset between the current period and the previous finished period
    period_freq = 'W' # M for monthly and W for weekly
    period_offset = 1 # offset between the current period and the most recent finished period
    period_count = 6 # number of period to show in the co2 barchart
    group_name_column_exchange = {} # for some special (usually big) groups, to disclose further details by using its name from another column, e.g. {"Sockets": "circuit_description"}
    group_name_modification = {} # replacement name to make the long and complex name more readable

    occupancy_available = False
    asset_group = "thing_category"
    fillna_value = "Undefined"
    exception = {'link_type': ['Supply', 'Load to DB', 'Load to Exclude']}
    insight_statements = None # this will decide whether to show the insights or not

    working_start_time="00:00:00" #Default start and end time, may not be used (it is needed for the functions) if the schedule information from the database
    working_end_time="23:59:00"
    # print('group_name_modification: ', group_name_modification) # debug
    reviewer_emails = ['x.yang@cloudfmgroup.com', 
                    #    's.goud@cloudfmgroup.com',
                        's.ruthven@cloudfmgroup.com', 
    #                     'r.patel@cloudfmgroup.com',
                        'd.attoe@cloudfmgroup.com'
                      ]
    # reviewer_emails = ['x.yang@cloudfmgroup.com', 
    #                    's.goud@cloudfmgroup.com', 
    #                    's.ruthven@cloudfmgroup.com', 
    #                    'r.patel@cloudfmgroup.com']
    # cloudfm_cc_emails = ['x.yang@cloudfmgroup.com', 
    #                     's.goud@cloudfmgroup.com', 
    #                     's.ruthven@cloudfmgroup.com', 
    #                     'r.patel@cloudfmgroup.com',
    #                     'd.attoe@cloudfmgroup.com']
    
    # 12 March 2024: [Removed] ["d.attoe@cloudfmgroup.com","s.ruthven@cloudfmgroup.com", "r.patel@cloudfmgroup.com", 's.goud@cloudfmgroup.com']

    def __init__(self, site_item):

        site_dict = site_item.squeeze(axis=0).to_dict()

        # print('site_item: ', site_item)
        # print('site_dict: ', site_dict)

        # file_path = Path(site_obj.__file__)

        

        self.site_name = site_dict['building_name'].replace("'","''")
        self.org_name = site_dict['org'].replace("'","''")

        # if site_dict['bld_name_abbr'] == '':
        #     self.bld_name_abbr = self.site_name
        # else:
        #     self.bld_name_abbr = site_dict['bld_name_abbr']

        print('\n' + self.org_name + ' - ' + self.site_name + ': ')

        if site_dict['group_name_column_exchange'] != '':
            self.group_name_column_exchange = ast.literal_eval(site_dict['group_name_column_exchange'])
        
        if site_dict['group_name_modification'] != '':
            self.group_name_modification = ast.literal_eval(site_dict['group_name_modification'])

        if site_dict['insight_statements'] != '':
            self.insight_statements = ast.literal_eval(site_dict['insight_statements'])

        # monday_config = ['site_dict']

        for attribute in site_dict:
            if attribute not in ['building_name', 
                                 'publish', 
                                 'testing', 
                                 'org', 
                                 'send_to', 
                                 'mailing_list',
                                 'group_name_column_exchange', 
                                 'group_name_modification',
                                 'insight_statements',
                                 'last_update']:
                
                if 'email' not in attribute:
                    setattr(self, attribute, site_dict[attribute])
                    # print('debug ClientSite attr: ', attribute, site_dict[attribute])
        
        if self.manager_name == '':
            self.manager_name = self.site_name + ' ' + self.org_name

        
        # for attribute in dir(site_obj):
        #     if not attribute.startswith('__'):
        #         setattr(self, attribute, getattr(site_obj, attribute))

        # self.manager_emails += self.cloudfm_cc_emails

if __name__ == '__main__':
    a = ClientSite()
    print(type(a))