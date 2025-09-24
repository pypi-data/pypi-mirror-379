#The below is the table definition
name = 'analysis.energy_report_config'

columns_dict = {'last_update': 'timestamptz NOT NULL', 
                'building_id': 'UUID NOT NULL',
                'item_name': 'text NOT NULL', 
                'group_name': 'text',
                'board_id': 'text',
                'hvac_board_id': 'TEXT',
                'publish': 'boolean NOT NULL', 
                'testing': 'boolean NOT NULL', 
                'industry': 'text', 
                'manager_name': 'text NOT NULL', 
                'currency': 'text NOT NULL', 
                # 'timezone': 'text NOT NULL', 
                'occupancy_available': 'boolean NOT NULL', 
                'asset_group': 'text NOT NULL', 
                'fillna_value': 'text NOT NULL', 
                'insight_statements': 'text NOT NULL', 
                'group_name_column_exchange': 'text NOT NULL', 
                'group_name_modification': 'text NOT NULL', 
                'pct_level_tobe_others': 'double precision NOT NULL', 
                'floor_sqm': 'double precision', 
                'pct_hide': 'double precision NOT NULL', 
                'conv_mwh_price': 'double precision',
                'period_freq': 'text NOT NULL',
                'mailing_list': 'text NOT NULL'}

hypertable = False 

