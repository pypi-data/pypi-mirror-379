
from .check_table_existence import check_table_existence
from .create_new_schema import create_new_schema
from .empty_table import empty_table
from .create_table import create_table

def setup_table(engine, table_name, columns_dict, 
                hypertable=False, 
                index=None,
                constraint=None,
                redo_from_start=False, 
                with_log=True):
    """
    Function Name: setup_table
    Parameters   : sql connection engine, table name, redo_from_start flag
    Description  : if redo from start set inconfiguration file - emptys table 
                   otherwise creates a new table and schema if required 
    """
    
    is_exist = check_table_existence(engine, table_name)
    
    if is_exist:
        if redo_from_start:
            empty_table(engine, table_name, 
                        with_log=with_log)
    else:
        table_schema_name_list = table_name.split(".")

        if len(table_schema_name_list) > 1:

            # TODO: add check_schema_existence
            table_schema = table_schema_name_list[0]
            create_new_schema(engine, table_schema)
        
        create_table(engine, table_name, columns_dict, 
                     constraint=constraint,
                     index=index,
                     hypertable=hypertable)
        
    return