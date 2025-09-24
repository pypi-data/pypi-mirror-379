import pickle
from PIL import ImageColor
import os
import io

import colorsys

from mdl.utils_ import color_dict
from .PDF import PDF

cd = color_dict
        
def generate_report(site_name, period, 
                    statements_list=None, 
                    organisation=None, 
                    components=None,
                    files_folder=None, 
                    figures_folder=None, 
                    report_file_folder=None,
                    assets_folder=None):
    
    if assets_folder == None:
        assets_folder = os.path.join(os.path.dirname(__file__), '_assets_/')

    pdf = PDF()
    pdf.add_page()

    pdf.image(assets_folder+'Screenshot_by_date_weekly.png', 0.3, 70, 8)
    pdf.image(assets_folder+'Screenshot_by_asset_weekly.png', 0.3, 70+65, 8)
    pdf.image(assets_folder+'Screenshot_insights_weekly.png', 0.3, 70+130, 8)
    pdf.set_font('Arial', "B", 28)
    # Line break
    pdf.ln(19)

    color_rgb = ImageColor.getcolor(cd["Mindsett Blue"], "RGB")
    color_hsv = colorsys.rgb_to_hsv(*color_rgb)
    color_rgb_changed = colorsys.hsv_to_rgb(color_hsv[0], color_hsv[1]*1.2, color_hsv[2]*0.85)
    pdf.set_text_color(*color_rgb_changed)

    pdf.cell(pdf.w - 28, 10, 'Energy Consumption', 0, 0, 'R')
    pdf.set_font('Arial', "I", 16)
    # Line break
    pdf.ln(13)

    color_rgb = ImageColor.getcolor(cd["darkgrey"], "RGB")
    color_hsv = colorsys.rgb_to_hsv(*color_rgb)
    color_rgb_changed = colorsys.hsv_to_rgb(color_hsv[0], color_hsv[1], color_hsv[2])
    pdf.set_text_color(*color_rgb_changed)

    # generate period name
    
    if period.freqstr == "M":
    
        period_str = period.strftime('%b %Y')
    else:
        # add 1 week to the current_period_obj so that the start week is not Week 00
        period_week_str = period.strftime('%W')
        period_year_str = period.strftime('%Y')
        period_str = f'Wk {(int(period_week_str)+1):02d}, {period_year_str}'
    
    REPLACEMENTS = {"""''""": """'""",
                    "Mecca Bingo": "MB",
                    "Grosvenor": "GC",
                    # "The Rank Group": "Rank",
                    "Marina Bay Financial Center, Tower 2": "MBFC T2"}

    for item in REPLACEMENTS:
        site_name = site_name.replace(item, REPLACEMENTS[item])

    site_name_update = site_name
    sub_title_name = f'{site_name_update} - {period_str} '
    
    if organisation is not None:
        for item in REPLACEMENTS:
            organisation = organisation.replace(item, REPLACEMENTS[item])
        organisation_update = organisation
        sub_title_name = f'{organisation_update} - {sub_title_name}'

    report_file_name = 'Mindsett_Energy_Report_' + sub_title_name.strip().replace(" - ", "_").replace(" ", "_").replace(",", "") + '.pdf'

    pdf.cell(pdf.w - 27, 10, sub_title_name, 0, 0, 'R')

    # if components != None:

    consumption_by_assetclass_piechart_with_phase = components['consumption_by_assetclass_piechart_with_phase.png']
    period_barchart = components['period_barchart.png']
    monthly_total_and_bm_latest = components['monthly_total_and_bm_latest.png']
    daily_barchart_with_temp = components['daily_barchart_with_temp.png']
    auto_statements_list_or_path = components['statements.pkl']

    if isinstance(auto_statements_list_or_path, str):
        with open(auto_statements_list_or_path, 'rb') as f:
            auto_statements_list = pickle.load(f)
    else:
        auto_statements_list = auto_statements_list_or_path
    # else:
    #     consumption_by_assetclass_piechart_mindsett = figures_folder+'consumption_by_assetclass_piechart_mindsett.png'
    #     total_consumption_barchart_with_co2 = figures_folder+'total_consumption_barchart_with_co2.png'
    #     monthly_total_and_bm_latest = figures_folder+'monthly_total_and_bm_latest.png'
    #     daily_consumption_barchart_with_occupancy_mar_with_pattern_mwh = figures_folder+'daily_consumption_barchart_with_occupancy_mar_with_pattern_mwh.png'

    #     with open(files_folder+'statements.pkl', 'rb') as f:
    #         auto_statements_list = pickle.load(f)

    pdf.image(consumption_by_assetclass_piechart_with_phase, 14 + 0.2, 55+69+4, 144)
    pdf.image(period_barchart, 136, 55+82-1, 60)
    pdf.image(monthly_total_and_bm_latest, 14.5, 48+9+3.5, 65-7) # here 3.5 is added to make space for the subtitle

    pdf.ln(151) #Contol on paragraphs 
    pdf.set_x(29)
    pdf.image(daily_barchart_with_temp, 71, 62+3.5, 135) # here 3.5 is added to make space for the subtitle

    # Insights statements 

    if statements_list is not None:

        insight_statements_list = statements_list

        pdf.ln(5)
        pdf.set_x(20)
        pdf.set_font('Arial', 'I', 12)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(pdf.w - 50, 10, 'Insights: \n')

        text_list = []

        for statement in insight_statements_list:

            statement_text =  [{'text': '- '+statement+' '}]
            text_list += statement_text

        pdf.set_x(29)
        pdf.write_multicell_with_styles(pdf.w-50,6,text_list)

    # Automated Observations statements
    pdf.ln(5)
    pdf.set_x(20)
    pdf.set_font('Arial', 'I', 12)
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 50, 10, 'Automated Observations: \n')

    text_list = []

    for statement in auto_statements_list:

        statement_text =  [{'text': '- '+statement+' '}]
        text_list += statement_text

    pdf.set_x(29)
    pdf.write_multicell_with_styles(pdf.w-50,6,text_list) #6


    if report_file_folder == None:
        
        pdf_object = io.BytesIO()
        pdf.output(pdf_object, 'F')
        return {report_file_name: pdf_object}
    else:

        report_file_dir = report_file_folder + report_file_name
        pdf.output(report_file_dir, 'F')
        return {report_file_name: report_file_dir}
