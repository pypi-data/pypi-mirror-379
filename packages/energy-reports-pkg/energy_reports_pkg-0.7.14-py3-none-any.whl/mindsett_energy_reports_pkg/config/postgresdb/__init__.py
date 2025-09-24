
from sqlalchemy import create_engine

from get_conn_by_id import get_conn_by_id 

from . import table_cache
from . import table_mailing
from . import table_iot
from . import table_meta
from . import table_schedule
from . import table_building
from . import table_org
from . import table_timezone
from . import table_sqm
from . import table_price
from . import table_on_off
from . import table_building_total
from . import table_occupancy

# credentials/setup for postgresdb

postgresdb_conn = get_conn_by_id('prod_postgres_cloudfm')

DB_URL = postgresdb_conn['host']+":"+str(postgresdb_conn['port'])
DB_DATABASE = postgresdb_conn['database']
DB_USER = postgresdb_conn['username']
DB_PASSWORD = postgresdb_conn['password']
DB_SSLMODE = postgresdb_conn["sslmode"]
ENGINE = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB_DATABASE}"

engine = create_engine(ENGINE)

# columns_for_query = ['circuit_description', 'asset_type', 'asset_class', 'asset_location', 'phase', 'channel_number', 'nid', 'site_name', 'organisation']
