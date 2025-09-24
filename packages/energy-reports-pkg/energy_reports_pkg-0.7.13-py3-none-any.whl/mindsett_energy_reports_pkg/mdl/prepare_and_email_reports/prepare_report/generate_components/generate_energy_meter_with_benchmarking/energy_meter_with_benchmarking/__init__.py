
import matplotlib.pyplot as plt

from os import path

from .energy_meter_design import energy_meter_design
from .benchmarking_design import benchmarking_design


def energy_meter_with_benchmarking(consumption_mwh_cur, consumption_mwh_pre, floor_size, 
                                   image_folder=None,
                                    size_in_sqm = True,
                                    industry = "office",
                                    period = 30,
                                    conv_mwh_co2 = 0.233,
                                    conv_mwh_price = 190,
                                    fx = 0.2, # fancy box x-axis value
                                    fy = 0.3, # fancy box y-axis value
                                    fs  = 0.6, # fancy box scale factor
                                    kwh_per_sqm_good = 10.33,
                                    kwh_per_sqm_typical = 14.5,
                                    currency = 'GBP',
                                    fontsize=13, # please note that the other fontsizes haven't been tested yet
                                    # directory_to_savefig = './figures/'
                                  ):
    
    if image_folder == None:
        image_folder = path.join(path.dirname(__file__), '_assets_/')

    plt.style.use('seaborn-v0_8-white')
    fig, ax = plt.subplots(figsize=(5, 5.5))

    if size_in_sqm:
        floor_sqm = floor_size
    else:
        floor_sqm = floor_size * 0.0929

    if industry == "office":
        floor_sqm_as_office = floor_sqm
    elif industry == "food service":
        # (not working on 26 Nov 24): https://cdn2.hubspot.net/hubfs/5055051/Offers/Energy%20Benchmarking%20Report%20-%20Iota.pdf?utm_campaign=Offer%3A%20Energy%20Benchmarking%20Report&utm_medium=email&_hsmi=72631957&_hsenc=p2ANqtz-8urx_6ejMPQ25rp-u0vAHPq0cmKPTvL18SQTEf22gtrdDV2x7wGnd5kkP40_bx3M5hOWp3tysnbPI4JjWriJEp2fb5o7PzNF5D9VFqQNjYVLVxKtE&utm_content=72631957&utm_source=hs_automation
        # added on 26 Nov 24: https://www.betterbuildingspartnership.co.uk/sites/default/files/media/attachment/REEB%202023%20Benchmarks_0.pdf
        floor_sqm_as_office = floor_sqm * 56/15 # 56/15 food service/office

    floor_sqm_as_office_for_month = floor_sqm_as_office * period / 30 # default days in a month

    
    energy_meter_design(ax, consumption_mwh_cur, consumption_mwh_pre, image_folder,
                        conv_mwh_co2=conv_mwh_co2,
                        conv_mwh_price=conv_mwh_price,
                        fx=fx, fy=fy, fs=fs,
                        currency=currency,
                        fontsize=fontsize)
    benchmarking_design(ax, consumption_mwh_cur, floor_sqm_as_office_for_month,
                        fx=fx, fy=fy-0.12, fs=fs,
                        kwh_per_sqm_good=kwh_per_sqm_good,
                        kwh_per_sqm_typical=kwh_per_sqm_typical,
                        fontsize=fontsize
                       )
    ax.set_xlim(0, 1) # shouldn't be modified
    ax.set_ylim(-1, 2)

    plt.axis('off')
    # Specify the directory to save figures, if it does not exist, create it
    # Path(directory_to_savefig).mkdir(parents=True, exist_ok=True)
    # plt.savefig(directory_to_savefig+"Monthly_total_and_bm_latest.png", format='png', dpi=200,transparent=True, bbox_inches='tight', pad_inches=0)
