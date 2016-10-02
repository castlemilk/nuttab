import os
from xlrd import open_workbook
# import json
from tqdm import tqdm
from nuttab_to_norm import mapping
import sqlite3
# TODO:
# 1. DONE create field mapping for NUTTTAB to USDA DB schemes
# 2. DOING parse NUTTAB Data and formatting into JSON for upload
# 3. upload with specifi metadata detailing the source (NATTAB) and re-do
#    the USDA data with the same meta data about its source etc.


class NUTTAB:
    '''
    Command line client for parsing and processing the Australian NUTTAB food
    database into a JSON format for document storage etc.
    '''
    def __init__(self, db_name):
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
                                (food_ID text, food_group, food_subgroup, derivation, descr_short, sci_name, descr_long, NF, inedible_po, edible_po);
                                CREATE INDEX amino_acid_meta_food_ID_idx on amino_acid_meta (food_ID)'''
        create_table_stmt["vit_d"] = '''DROP TABLE IF EXISTS vit_d; CREATE TABLE vit_d
                                (food_ID text, nut_ID, descr, scale, value);
                                CREATE INDEX vit_d_food_ID_idx ON vit_d (food_ID)'''
        create_table_stmt["vit_d_meta"] = '''DROP TABLE IF EXISTS vit_d_meta; CREATE TABLE vit_d_meta
                                (food_ID text, food_group, food_subgroup, derivation, descr_short, sci_name, descr_long, NF, inedible_po, edible_po);
                                CREATE INDEX vit_d_meta_food_ID_idx on vit_d_meta (food_ID)'''
        create_table_stmt["indigenous_food"] = '''DROP TABLE IF EXISTS indigenous_food; CREATE TABLE indigenous_food
                                (food_ID text, nut_ID, descr, scale, value);
                                CREATE INDEX indigenous_food_food_ID_idx on indigenous_food (food_ID)'''
        create_table_stmt["indigenous_food_meta"] = '''DROP TABLE IF EXISTS indigenous_food_meta; CREATE TABLE indigenous_food_meta
                                (food_ID text, food_group, food_subgroup, derivation, descr_short, sci_name, descr_long, NF, inedible_po, edible_po);
                                CREATE INDEX indigenous_food_meta_food_ID_idx on indigenous_food_meta (food_ID)'''

        self.cursor = self.database.cursor()
        self.cursor.executescript(create_table_stmt["nutrition"])
        self.cursor.executescript(create_table_stmt["amino_acid"])
        self.cursor.executescript(create_table_stmt["amino_acid_meta"])
        self.cursor.executescript(create_table_stmt["vit_d"])
        self.cursor.executescript(create_table_stmt["vit_d_meta"])
        self.cursor.executescript(create_table_stmt["indigenous_food"])
        self.cursor.executescript(create_table_stmt["indigenous_food_meta"])
        self.database.commit()
    def build_table_csv(self, filename, tablename):
        '''
        Build table from csv file
        filename - filename in CSV format
        tablename - name for the table created in DB
        '''
        with open(filename, 'rU') as f:
            next(f)
            for line in tqdm(f):
                fields = [unicode(field.strip().strip('"'), "cp1252") for field in line.split('\t')]
                # print fields
                fields[1] = mapping[fields[1]]
                # print fields
                self.insert_row(tablename, fields)
        self.database.commit()
    def  build_table_xls_amino_acid(self, filename, tablename):
        '''
        Build table from xls file
        specifically the amin acid file and the x number of columns per row
        filename - filename in XLS format
        schema - a dictionary defined schema for the mapping of each cell in
        the excel spread sheet
        tablename - name for the table created in DB
        '''
        amino_column_schema = ['sort', 'food_id', 'food_name',
                         'ALAN', 'ARG', 'ASP', 'CYSN',
                         'GLU', 'GLY', 'HIS', 'ILEU' , 'LEU',
                         'LYS', 'MET', 'PHE', 'PRO', 'SER',
                         'THR', 'TYR', 'TRYP', 'VAL',
                         ]
        header_row = 4  # where the titles are etc
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(0)
        units = 'mg/g'
        # parse into dict
        for rowx in range(header_row, ws.nrows):
            row_dict = {}
            row_dict['food_id'] = ws.cell(rowx,1).value
            row_dict['food_name'] = ws.cell(rowx,2).value
            row_dict['amino_acids'] = {}
            for colx in range(3, ws.ncols):
                row_dict['amino_acids'][amino_column_schema[colx]] = {
                    'descr':ws.cell(header_row-1, colx).value.rstrip('\n (mg/g N)'),
                    'value':ws.cell(rowx, colx).value
                }
        # store into DB
            for amino_acid, info in row_dict['amino_acids'].iteritems():
                db_row = [row_dict['food_id'], amino_acid, info['descr'], units, info['value']]
                self.insert_row(tablename, db_row)
        self.database.commit()
    def build_table_xls_amino_acid_meta(self, filename, tablename):
        '''
        Builds table containing the meta data for given food items in the
        amino acid file.
        filename - name of excel sheet containing amino acid info
        tablename - name of table containing the organised meta data
        '''
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(1)
        header_row = 1
        for rowx in range(header_row, ws.nrows):
            row_dict = {}
            row_dict['food_group'] = ws.cell(rowx,1).value
            row_dict['food_subgroup'] = ws.cell(rowx,2).value
            row_dict['derivation'] = ws.cell(rowx,3).value
            row_dict['food_id'] = ws.cell(rowx,4).value
            row_dict['descr_short'] = ws.cell(rowx,5).value
            row_dict['sci_name'] = ws.cell(rowx,6).value
            row_dict['descr_long'] = ws.cell(rowx,8).value
            row_dict['NF'] = ws.cell(rowx,9).value
            row_dict['inedible_po'] = ws.cell(rowx,10).value
            row_dict['edible_po'] = ws.cell(rowx,11).value
            db_row = [row_dict['food_id'], row_dict['food_group'],
                      row_dict['food_subgroup'], row_dict['derivation'],
                      row_dict['descr_short'], row_dict['sci_name'],
                      row_dict['descr_long'], row_dict['NF'],
                      row_dict['inedible_po'], row_dict['edible_po'],
                      ]
            self.insert_row("amino_acid_meta", db_row)

        self.database.commit()
    def build_table_xls_vitd(self, filename, tablename):
        '''
        Build table for vitamin d file and all the detailed values availble
        filename - name of excel sheet containing vit d info
        tablename - name of table containing the organised meta data
        '''
        vit_d_column_schema = ['food_id','food_nae', 'CHOC', 'ERGCAL', 'CHOCALOH',
                               'ERGCALOH', 'VITDEQ', 'VITEQNF']
        units = 'ug/100g'
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(0)
        header_row = 5
        for rowx in range(header_row, ws.nrows):
            row_dict = {}
            row_dict['food_id'] = ws.cell(rowx, 0).value
            row_dict['food_name'] = ws.cell(rowx, 2).value
            row_dict['nutrients'] = {}
            for colx in range (3, ws.ncols):
                row_dict['nutrients'][vit_d_column_schema[colx]] = {
                    'descr': ws.cell(header_row-1, colx).value.split('\n')[0],
                    'value': ws.cell(rowx, colx).value,
                    'scale': units,
                }

            for nutrient, info in row_dict['nutrients'].iteritems():
                db_row = [row_dict['food_id'], nutrient, info['descr'],
                          info['scale'], info['value']
                          ]
                self.insert_row(tablename, db_row)
            self.database.commit()
    def build_table_xls_vitd_meta(self, filename, tablename):
        '''
        Build table for vitamin d meta data foods etc
        filename - name of excel file containing vit d meta data (assumed sheet 2)
        tablename - name of database table to write as
        TODO: unified schema for meta data files potentially simpify to a
              consistent schema
        '''
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(1)
        header_row = 1
        for rowx in range(header_row, ws.nrows):
            row_dict = {}
            row_dict['food_group'] = ws.cell(rowx,1).value
            row_dict['food_subgroup'] = ws.cell(rowx,2).value
            row_dict['derivation'] = ws.cell(rowx,3).value
            row_dict['food_id'] = ws.cell(rowx,4).value
            row_dict['descr_short'] = ws.cell(rowx,5).value
            row_dict['sci_name'] = ws.cell(rowx,6).value
            row_dict['descr_long'] = ws.cell(rowx,8).value
            row_dict['NF'] = ws.cell(rowx,9).value
            row_dict['inedible_po'] = ws.cell(rowx,10).value
            row_dict['edible_po'] = ws.cell(rowx,11).value
            db_row = [row_dict['food_id'], row_dict['food_group'],
                      row_dict['food_subgroup'], row_dict['derivation'],
                      row_dict['descr_short'], row_dict['sci_name'],
                      row_dict['descr_long'], row_dict['NF'],
                      row_dict['inedible_po'], row_dict['edible_po'],
                      ]
            self.insert_row("vit_d_meta", db_row)
        self.database.commit()
    def build_table_xls_indig(self, filename, tablename):
        '''
        Build table from indigenous xls file
        filename - name of indigenous excel file
        tablebame - name of table where parsed data is stored
        '''
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(0)
        header_row = 6
        unit_row = 7
        indig_column_schema = ['food_id', 'food_name',
                               'ENERC1', 'WATER', 'PROT',
                               'NT', 'FAT', 'ASH',
                               'FIBTG', 'FRUS', 'GLUS',
                               'SUCS', 'MALS', 'LACS',
                               'SUGAR', 'STARCH', 'CHODIFF',
                               'CD', 'CA', 'CU', 'FE',
                               'PB', 'MG', 'MN',
                               'P', 'K', 'NA',
                               'ZN', 'THIA', 'RIBF',
                               'NIAEQ', 'FOLFD', 'FOL',
                               'FOLDFE', 'CARTA', 'CARTB',
                               'CRYP', 'CARTBEQ', 'RETOL',
                               'VITA', 'VITC', 'F6D0F',
                               'F8D0F', 'F10D0F', 'F12D0F',
                               'F14D0F', 'F16D0F', 'F18D0F',
                               'F20D0F', 'F22D0F', 'F24D0F',
                               'FASATF', 'F15D1F', 'F16D1F',
                               'F18D1F', 'F20D1F', 'F24D1F',
                               'FAMSF', 'F18D2N6F', 'F183N3F',
                               'F20D3N3F', 'F20D4N6F', 'F20D5N3F',
                               'F22D4N6F', 'F22D5N3F', 'F22D6N3F',
                               'FAPUF', 'LCW3TOTALF', 'F6D0',
                               'F8D0', 'F10D0', 'F12D0',
                               'F14D0', 'F16D0', 'F18D0',
                               'F20D0', 'F22D0', 'F24D0',
                               'FATSAT', 'F15D1', 'F16D1',
                               'F18D1', 'F20D1', 'F24D1',
                               'FAMS', 'F18D2N6', 'F18D3N3',
                               'F20D3N3', 'F20D4N6', 'F20D5N3',
                               'F22D4N6', 'F22D5N3', 'F22D6N3',
                               'FAPU', 'LCW3TOTAL',
                               ]
        for rowx in range(unit_row, ws.nrows):
            row_dict = {}
            row_dict['food_id'] = ws.cell(rowx, 0).value
            row_dict['food_name'] = ws.cell(rowx, 1).value
            row_dict['nutrients'] = {}
            for colx in range(2, ws.ncols):
                row_dict['nutrients'][indig_column_schema[colx]] = {
                    'value' : ws.cell(rowx, colx).value,
                    'units' : ws.cell(unit_row-1, colx).value,
                    'descr' : ws.cell(header_row-1, colx).value.split(' (')[0],
                }
            for nutrient, info in row_dict['nutrients'].iteritems():
                db_row = [row_dict['food_id'], nutrient, info['descr'],
                          info['units'], info['value']]
                self.insert_row(tablename, db_row)
        self.database.commit()
    def build_table_xls_indig_meta(self, filename, tablename):
        '''
        filename - name of file containing indigenous food meta data
        tablename - name of table to store data in
        '''
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(1)
        header_row = 1
        for rowx in range(header_row, ws.nrows):
            row_dict = {}
            row_dict['food_group'] = ws.cell(rowx,1).value
            row_dict['food_subgroup'] = ws.cell(rowx,2).value
            row_dict['derivation'] = ws.cell(rowx,3).value
            row_dict['food_id'] = ws.cell(rowx,4).value
            row_dict['descr_short'] = ws.cell(rowx,5).value
            row_dict['optional_name'] = ws.cell(rowx,6).value
            row_dict['sci_name'] = ws.cell(rowx,7).value
            row_dict['descr_long'] = ws.cell(rowx,8).value
            row_dict['NF'] = ws.cell(rowx,10).value
            row_dict['inedible_po'] = ws.cell(rowx,11).value
            row_dict['edible_po'] = ws.cell(rowx,12).value
            db_row = [row_dict['food_id'], row_dict['food_group'],
                      row_dict['food_subgroup'], row_dict['derivation'],
                      row_dict['descr_short'], row_dict['sci_name'],
                      row_dict['descr_long'], row_dict['NF'],
                      row_dict['inedible_po'], row_dict['edible_po'],
                      ]
            self.insert_row(tablename, db_row)
        self.database.commit()
    def build_table_xls(self, filename, table):
        '''
        Build table from xls file
        filename - filename in xls/xlsx format
        tablename - name for the table created in DB
        '''
        wb = open_workbook(filename)
        ws = wb.sheet_by_index(1)
    def insert_row(self, tablename, fields):
        """Inserts a row of data into a specific table based on passed
        datatype"""
        insert_params = "(" + ",".join(['?' for x in fields]) + ")"
        self.cursor.execute("insert into " + tablename + " values " +
                            insert_params, fields)


if __name__ == '__main__':
    dbname = "NUTTAB.db"
    nutrition_file = os.path.join(
    os.getcwd(), '2a. NUTTAB 2010 - Nutrient File - all foods per 100 g.txt')
    amino_file = os.path.join(os.getcwd(), 'NUTTAB 2010 - Amino Acid File.xls')
    vitd_file = os.path.join(os.getcwd(), 'NUTTAB 2010 - Vitamin D File fixes.xls')
    indig_file = os.path.join(os.getcwd(), 'NUTTAB 2010 - Indigenous Food updated, fixes hidden.xls')
    nuttab = NUTTAB(dbname)
    #nuttab.build_table_csv(nutrition_file, "nutrition")
    nuttab.build_table_xls_amino_acid(amino_file, "amino_acid")
    nuttab.build_table_xls_amino_acid_meta(amino_file, "amino_acid_meta")
    nuttab.build_table_xls_vitd(vitd_file, "vit_d")
    nuttab.build_table_xls_vitd_meta(vitd_file, "vit_d_meta")
    nuttab.build_table_xls_indig(indig_file, "indigenous_food")
    nuttab.build_table_xls_indig_meta(indig_file, "indigenous_food_meta")
