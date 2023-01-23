import os

IS_TESTING = os.environ.get("TESTING", False)
IS_TESTING = True if IS_TESTING == "True" else False

regions_table = "regions" if not IS_TESTING else "regions_test"
ports_table = "ports" if not IS_TESTING else "ports_test"
prices_table = "prices" if not IS_TESTING else "prices_test"

REGION_QUERY = f"SELECT slug FROM public.{regions_table} WHERE parent_slug = %s"
PORT_QUERY = f"SELECT code FROM public.{ports_table} WHERE parent_slug = %s"
PRICE_QUERY = f"SELECT price FROM public.{prices_table} WHERE orig_code = %s AND dest_code = %s AND day = %s"
PORT_CODES_QUERY = f"SELECT code FROM public.{ports_table};"
REGION_NAMES_QUERY = f"SELECT slug FROM public.{regions_table};"
