from pathlib import Path
import matplotlib.pyplot as plt
import io

from .preprocessing_for_energy_meter_with_benchmarking import preprocessing_for_energy_meter_with_benchmarking
from .energy_meter_with_benchmarking import energy_meter_with_benchmarking


def generate_energy_meter_with_benchmarking(df_meta_with_value_building, floor_size,
                                            industry = "office",
                                            size_in_sqm = True,
                                            conv_mwh_price = 190,
                                            currency = 'GBP',
                                            fontsize = 13,
                                            directory_to_savefig=None):
                                            
    consumption_mwh_cur, consumption_mwh_pre, days_in_period = preprocessing_for_energy_meter_with_benchmarking(df_meta_with_value_building)

    print('consumption_mwh_building_total: ', consumption_mwh_cur)  # debug
    energy_meter_with_benchmarking(consumption_mwh_cur, consumption_mwh_pre, floor_size, 
                                    industry=industry, 
                                    period=days_in_period, 
                                    size_in_sqm=size_in_sqm,
                                    conv_mwh_price=conv_mwh_price,
                                    currency=currency,
                                    fontsize=fontsize)
    
    png_name = 'monthly_total_and_bm_latest.png'
    if directory_to_savefig == None:
        png_object = io.BytesIO()
        plt.savefig(png_object, format='png', dpi=200,transparent=True, bbox_inches='tight', pad_inches=0)
        plt.close()
        return {png_name: png_object}
    else:
        png_path = directory_to_savefig + png_name
        plt.savefig(png_path, format='png', dpi=200,transparent=True, bbox_inches='tight', pad_inches=0)
        plt.close()
        return {png_name: png_path}


    # Path(directory_to_savefig).mkdir(parents=True, exist_ok=True)
    # plt.savefig(directory_to_savefig+"monthly_total_and_bm_latest.png", format='png', dpi=200,transparent=True, bbox_inches='tight', pad_inches=0)