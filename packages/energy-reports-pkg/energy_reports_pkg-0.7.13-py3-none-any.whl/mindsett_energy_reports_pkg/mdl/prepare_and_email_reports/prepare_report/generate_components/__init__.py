import matplotlib.pyplot as plt
plt.rcParams['figure.max_open_warning'] = 300

from .generate_insight_statements import generate_insight_statements
from .generate_piechart_with_phase import generate_piechart_with_phase
from .generate_energy_meter_with_benchmarking import generate_energy_meter_with_benchmarking
from .generate_daily_barchart_with_temp import generate_daily_barchart_with_temp
from .generate_period_barchart import generate_period_barchart

def generate_components(postgresdb, df_meta_with_value, df_meta_with_value_building, site_obj, 
                        fontsize=None, 
                        directory_to_savefile=None):

    insight_statements = generate_insight_statements(postgresdb, df_meta_with_value, 
                                asset_group=site_obj.asset_group, 
                                # fixed_group_to_filter=site_obj.fixed_group_to_filter,
                                directory_to_savefile=directory_to_savefile)
    
    piechart_with_phase = generate_piechart_with_phase(df_meta_with_value, 
                                fontsize=fontsize,
                                directory_to_savefig=directory_to_savefile)
    
    energy_meter_with_benchmarking = generate_energy_meter_with_benchmarking(df_meta_with_value_building, site_obj.floor_size, 
                                            size_in_sqm=site_obj.size_in_sqm, 
                                            conv_mwh_price=site_obj.conv_mwh_price,
                                            industry=site_obj.industry, 
                                            currency=site_obj.currency,
                                            fontsize=fontsize,
                                            directory_to_savefig=directory_to_savefile)

    daily_barchart_with_temp = generate_daily_barchart_with_temp(df_meta_with_value,
                                                                fontsize=fontsize,
                                                                directory_to_savefig=directory_to_savefile)

    period_barchart = generate_period_barchart(df_meta_with_value_building,
                                         fontsize=fontsize,
                                         directory_to_savefig=directory_to_savefile)
    
    # if directory_to_savefile == None:
    components = {
        **insight_statements,
        **piechart_with_phase,
        **energy_meter_with_benchmarking,
        **daily_barchart_with_temp,
        **period_barchart
        }
    return components