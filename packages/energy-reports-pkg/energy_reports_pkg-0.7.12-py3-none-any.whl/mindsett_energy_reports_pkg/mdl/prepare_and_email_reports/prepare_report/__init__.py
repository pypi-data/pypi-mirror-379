import pandas as pd
import matplotlib
matplotlib.use('Agg') # turn off the display graphs 

from .preparing_source_data import preparing_source_data
from .generate_components import generate_components
from .generate_report import generate_report

def prepare_report(cf, site_obj, 
                   debug=False,
                   report_file_folder=None, 
                   directory_to_savefile=None):

    df_meta_with_value, df_meta_with_value_building = preparing_source_data(cf.postgresdb, 
                                                                            site_obj,
                                                                            debug=debug, 
                                                                            caching=False)

    # currently site_name is used for building_occupancy
    components = generate_components(cf.postgresdb, df_meta_with_value, df_meta_with_value_building, site_obj,
                                     fontsize=13,
                                     directory_to_savefile=directory_to_savefile)
    

    current_period = df_meta_with_value.period.max() # + pd.offsets.Week() 

    try: # handle the case where insights statement is not provided
        report_file_dict = generate_report(site_obj.site_name, current_period, 
                                           statements_list=site_obj.insight_statements, 
                                           organisation=site_obj.org_name,
                                           components=components,
                                           files_folder=directory_to_savefile,
                                           figures_folder=directory_to_savefile,
                                           report_file_folder=report_file_folder)
    except:
        report_file_dict = generate_report(site_obj.site_name, current_period, 
                                           organisation=site_obj.org_name,
                                           components=components,
                                           files_folder=directory_to_savefile,
                                           figures_folder=directory_to_savefile,
                                           report_file_folder=report_file_folder)

    return report_file_dict, current_period
