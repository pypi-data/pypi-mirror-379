

def preprocessing_for_phases(df_meta_with_value, 
                    reading_interval_in_mins=None):

    if reading_interval_in_mins is None:
        reading_interval_in_mins=10

    # Conversion into MWh
    w_to_kw_para = 1./1000
    min_to_hour_para = 1./60

    wm_to_kwh_parameter = w_to_kw_para * min_to_hour_para
    reading_to_kwh_parameter = reading_interval_in_mins * wm_to_kwh_parameter

    # consider only the consumed energy
    df_meta_with_value_positive = df_meta_with_value.loc[df_meta_with_value["W"] > 0]

    # group and pivot operation
    sr_group_phase = df_meta_with_value_positive.groupby(["phase"])["W"].sum() * reading_to_kwh_parameter

    # extract phase values to list and report possible anomalies
    existing_phases = sr_group_phase.index.to_list()
    phase_values_list = []

    for phase in ['L1', 'L2', 'L3']:
        if phase in existing_phases:
            phase_values_list.append(sr_group_phase[phase])
        else:
            print(f'[WARN]: missing phase "{phase}"!')
            phase_values_list.append(0)

    for phase in existing_phases:
        if phase not in ['L1', 'L2', 'L3']:
            print(f'[WARN]: unexpected phase "{phase}"!')

    return phase_values_list