
#The below is the table definition
name = 'analysis.mailing_list'

columns_def_dict = {'contact_id': 'TEXT NOT NULL', 
                    'name': 'TEXT',
                    'email': 'TEXT',
                    'board_group': 'text NOT NULL', 
                    'ids_energy_report': 'text NOT NULL'}

property_dict = {"PRIMARY KEY": "(contact_id)"}

columns_dict = {**columns_def_dict, **property_dict}

hypertable = False 