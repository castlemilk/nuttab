import os
# from xlrd import open_workbook
# import json
from tqdm import tqdm
# import pandas as pd
from nuttab_to_norm import mapping
import sqlite3
DB_source_path = os.path.join(
    os.getcwd(), '2a. NUTTAB 2010 - Nutrient File - all foods per 100 g.txt')
        filename = DB_source_path
def insert_row(cursor, datatype, fields):
    """Inserts a row of data into a specific table based on passed datatype"""
    insert_params = "(" + ",".join(['?' for x in fields]) + ")"
    cursor.execute("insert into " + datatype + " values " + insert_params, fields)
# TODO:
# 1. create field mapping for NUTTTAB to USDA DB schemes
# 2. parse NUTTAB Data and formatting into JSON for upload
# 3. upload with specifi metadata detailing the source (NATTAB) and re-do
#    the USDA data with the same meta data about its source etc.
class NUTTAB:
    def __init__ (self, db_name):
        self.db_name = db_name
        self.database = sqlite3.connect(self.db_name)
        self.database.row_factory = sqlite3.Row
        create_table_stmt = {}
        create_table_stmt["nutrition"] = '''DROP TABLE IF EXISTS nutrition; CREATE TABLE nutrition
                                (food_ID text, nut_ID, descr, scale, value, category, nan);
                                CREATE INDEX nutrition_food_ID_idx ON nutrition (food_ID)'''
        create_table_stmt["amino_acid"] = '''DROP TABLE IF EXISTS amino_acid; CREATE TABLE amino_acid
                                (food_ID text, nut_ID, descr, scale, value);
                                CREATE INDEX amino_acid_food_ID_idx ON amino_acid (food_ID)'''
        create_table_stmt["amino_acid_meta"] = '''DROP TABLE IF EXISTS amino_acid_meta; CREATE TABLE amino_acid_meta
                                (food_ID text, food_group, food_subgroup, descr_long, NF)
                                CREATE INDEX amin_acid_meta_food_ID_idx on amin_acid_meta (food_ID)'''
        creatre_table_stmt["indigenous_food"] = '''DROP TABLE IF EXISTS indigenous_food; CREATE TABLE indigenous_food
                                (food_ID text, nut_ID, descr, scale, value);
                                CREATE INDEX indigenous_food_food_ID_idx on indigenous_food (food_ID)'''

        self.cursor = self.database.cursor()
        self.cursor.executescript(create_table_stmt["nutrition"])

    def build_table(filename, cursor):
        '''
        Build table from csv file
        filename - filename in CSV format
        cursor - database cursor
        '''
        with open(filename, 'rU') as f:
            next(f)
            for line in tqdm(f):
                fields = [unicode(field.strip().strip('"'), "cp1252") for field in line.split('\t')]
                # print fields
                fields[1] = mapping[fields[1]]
                # print fields
                insert_row(cursor, "nutrition", fields)
        self.database.commit()
    def insert_row(cursor, datatype, fields):
        """Inserts a row of data into a specific table based on passed datatype"""
        insert_params = "(" + ",".join(['?' for x in fields]) + ")"
        cursor.execute("insert into " + datatype + " values " + insert_params, fields)
