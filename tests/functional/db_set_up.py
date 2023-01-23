from dotenv import load_dotenv

load_dotenv()

from utils.connect_db import cursor


def db_set_up():
    create_regions_table_query = """
        CREATE TABLE IF NOT EXISTS public.regions_test (
            slug VARCHAR(255),
            name VARCHAR(255),
            parent_slug VARCHAR(255)
        );
    """

    create_ports_table_query = """
        CREATE TABLE IF NOT EXISTS public.ports_test (
            code VARCHAR(5),
            name VARCHAR(255),
            parent_slug VARCHAR(255)
        );
    """

    create_prices_table_query = """
        CREATE TABLE IF NOT EXISTS public.prices_test (
            orig_code VARCHAR(5),
            dest_code VARCHAR(5),
            day DATE NOT NULL,
            price INTEGER
        );
    """

    cursor.execute(create_regions_table_query)
    cursor.execute(create_ports_table_query)
    cursor.execute(create_prices_table_query)

    insert_ports_query = """
        INSERT INTO public.ports_test (code, name, parent_slug)
        VALUES ('IESNN', 'Shannon', 'north_europe_sub'),
                ('FRLVE', 'Le Verdon-sur-Mer', 'north_europe_sub'),
                ('CNCWN', 'Chiwan', 'china_south_main');
    """

    insert_regions_query = """
        INSERT INTO public.regions_test (slug, name, parent_slug)
        VALUES ('north_europe_sub', 'North Europe Sub', 'north_europe'),
                ('china_south_main', 'China South Main', 'china_main'),
                ('north_europe', 'Northern Europe', NULL),
                ('china_main', 'China Main', NULL);
    """

    insert_prices_query = """
        INSERT INTO public.prices_test (orig_code, dest_code, day, price)
        VALUES ('FRLVE', 'CNCWN', '2020-01-01', 100),
                ('IESNN', 'CNCWN', '2020-01-01', 50),
                ('IESNN', 'CNCWN', '2020-01-01', 150),
                ('FRLVE', 'CNCWN', '2020-01-02', 200),
                ('FRLVE', 'CNCWN', '2020-01-02', 200),
                ('IESNN', 'CNCWN', '2020-01-03', 200),
                ('IESNN', 'CNCWN', '2020-01-03', 120),
                ('IESNN', 'CNCWN', '2020-01-03', 250);
    """

    cursor.execute(insert_ports_query)
    cursor.execute(insert_regions_query)
    cursor.execute(insert_prices_query)


def db_tear_down():
    drop_prices_table_query = """
        DROP TABLE IF EXISTS public.prices_test;
    """

    drop_ports_table_query = """
        DROP TABLE IF EXISTS public.ports_test;
    """

    drop_regions_table_query = """
        DROP TABLE IF EXISTS public.regions_test;
    """

    cursor.execute(drop_prices_table_query)
    cursor.execute(drop_ports_table_query)
    cursor.execute(drop_regions_table_query)
