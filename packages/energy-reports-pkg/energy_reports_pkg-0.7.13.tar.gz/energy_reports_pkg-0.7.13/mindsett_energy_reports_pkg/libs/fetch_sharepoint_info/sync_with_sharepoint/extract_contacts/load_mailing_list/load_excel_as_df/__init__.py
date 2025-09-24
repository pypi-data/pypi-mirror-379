
import pandas as pd
import io

def load_excel_as_df(ctx, excel_file, sheet_name=None):

    if sheet_name is None:
        sheet_name = 0
    
    last_update_sys = excel_file.properties['TimeLastModified']
    last_update = pd.Timestamp(last_update_sys, tz='Europe/London').tz_convert(tz='UTC') # assume that the sharepoint system time in as London time

    # print(f'{last_update = }')
    files_url = excel_file.properties['ServerRelativeUrl']

    # print(f'{last_update=}')
    # print(f'{files_url=}')

    # files_url = excel_file

    # ctx.web.get().execute_query()

    with io.BytesIO() as data:
        _myfile = (ctx.web.get_file_by_server_relative_path(files_url)
                    .download(data)
                    .execute_query() 
                    ) 
        # print(f"{type(_myfile) = }")

        data.seek(0)

        # cols_dtype = {'board_id': str, 
        #               'hvac_board_id': str}

        df_contact = pd.read_excel(data, 
                                #    dtype=cols_dtype,
                            sheet_name=sheet_name,)
        
    # _myfile = (ctx.web.get_file_by_server_relative_path(files_url)
    #                 .execute_query() 
    #                 ) 
        
    df_contact['last_update'] = last_update

    return df_contact
