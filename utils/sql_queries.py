REGION_QUERY = "SELECT slug FROM public.regions WHERE parent_slug = '{parent_slug}'"
PORT_QUERY = "SELECT code FROM public.ports WHERE parent_slug = '{parent_slug}'"
PRICE_QUERY = "SELECT price FROM public.prices WHERE orig_code = '{origin}' AND dest_code = '{destination}' AND day = '{date}'"
