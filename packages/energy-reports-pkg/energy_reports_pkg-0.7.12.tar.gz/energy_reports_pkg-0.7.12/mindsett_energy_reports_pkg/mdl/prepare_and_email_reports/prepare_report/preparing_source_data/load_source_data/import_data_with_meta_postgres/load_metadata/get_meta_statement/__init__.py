

def get_meta_statement(building_id, 
                    #    organisation=None, 
                       exception=None,
                      ):

    statement_list = [f"""root_id='{building_id}'""", "thing_id is not null", "thing_name is not null"] # please note that the mt. lt. shortname for tables are still coupled with function load_metadata. Update - 20240814, resolved.

    # if organisation != None:
    #     statement_new  = f"""btrim(org) = '{organisation}'"""
    #     statement_list.append(statement_new)

    if exception != None:
        for key in exception:
            is_list = isinstance(exception[key], list) 
            
            if is_list:
                exc_list = exception[key]
            else:
                exc_list = [exception[key]]
            
            exc_list_with_quote = [f"'{item}'" for item in exc_list]

            exc_concat_str = ', '.join(exc_list_with_quote)

            statement_new  = f"""{key} not in ({exc_concat_str})"""
            statement_list.append(statement_new)

    statement_full = " and ".join(statement_list)

    return statement_full