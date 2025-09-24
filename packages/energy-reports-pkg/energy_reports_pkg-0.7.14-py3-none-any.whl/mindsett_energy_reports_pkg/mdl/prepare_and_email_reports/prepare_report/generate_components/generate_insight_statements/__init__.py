from pathlib import Path
import pickle

from .preprocessing_for_statement import preprocessing_for_statement
from .insight_statements import insight_statements


def generate_insight_statements(db, df_meta_with_value, 
                                asset_group = "asset_class",
                                # fixed_group_to_filter = [],
                                directory_to_savefile=None): # todo: update the default value for directory

    df_for_statements = preprocessing_for_statement(df_meta_with_value, asset_group=asset_group)

    # print('df_for_statements: ', df_for_statements) # debug

    if df_for_statements is not None:
        # get the readable name of period frequency
        current_period_obj = df_meta_with_value.period.max()
        period_type = current_period_obj.freqstr[0]
        period_freq_str_dict = {'W': 'week', 'M': 'month'}
        period_freq_str = period_freq_str_dict[period_type]

        statements_list = insight_statements(db, df_for_statements, df_meta_with_value, period_freq_str=period_freq_str)
    else:
        statements_list = ['Auto observations for 24/7 sites are not yet available!']

    # Specify the directory to save figures, if it does not exist, create it
    # Path(directory_to_savefile).mkdir(parents=True, exist_ok=True)

    # with open(directory_to_savefile+'statements.pkl', 'wb') as f:
    #     pickle.dump(statements_list, f)

    pkl_name = 'statements.pkl'
    if directory_to_savefile == None:
        # obj_object = io.BytesIO()
        return {pkl_name: statements_list}
    else:
        pkl_path = directory_to_savefile + pkl_name
        with open(pkl_path, 'wb') as f:
            pickle.dump(statements_list, f)
        return {pkl_name: pkl_path}