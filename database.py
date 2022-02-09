import sqlite3

conn = sqlite3.connect('bhhsamb.db')
curr = conn.cursor()

curr.execute("""create table bhhsamb_tb(
    product_name text,
    job_title text,
    image_url url,
    address text,
    contact_details text,
    social_accounts text,
    office text,
    languages text,
    description text
    )""")

conn.commit()
conn.close()