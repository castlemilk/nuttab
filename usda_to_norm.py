# mapping = {native_key : normal_key}
mapping = {
        'ENERC_KCAL' : 'ENERC_KCAL',
        'ENERC_KJ' : 'ENERC',
        'WATER' : 'WATER',
        'PROCNT' : 'PROCNT,
        'NT' : 'NT', # no nitrogen equivalent (nitrogen factor?)
        'FAT' : 'FAT',
        'ASH' : 'ASH',
        'FIBTG' : 'FIBTG',
        'ALC' : 'ALC',
        'FRUS': 'FRUS',
        'GLUS' : 'GLUS',
        'SUCS' : 'SUCS',
        'MALS' : 'MALS',
        'LACS' : 'LACS',
        'GALS' : 'GALS',
        #'MALT3' : 'MALTRS',

        'SUGAR' : 'SUGAR',
        'STARCH' : 'STARCH',
        'DEXTN' : 'DEXTN',
        'GLYR' : 'GLYRL',
        'GLYC' : 'GLYC',
        'INULN' : 'INULN',
        'MANTL' : 'MANTL',
        'MALTDEX' : 'MALTDEX',
        'OLSAC' : 'OLSAC',
        'RAFS' : 'RAFS',
        'STAS' : 'STAS',
        'SORTL' : 'SORTL',
        'CHOAVL' : 'CHOAVL',
        #'AVAILCHOCNS' : 'AVAILCHOCNS',
        'CHOCDF' : 'CHOCDF',
        'ACEAC' : 'ACEAC',
        'CITAC' : 'CITAC',
        'FUMAC' : 'FUMAC',
        'LACAC' : 'LACAC',
        'MALAC' : 'MALAC',
        'OXALAC' : 'OXALAC',
        'PROPAC' : 'PROPAC',
        'QUINAC' : 'QUINAC',
        'SHIKAC' : 'SHIKAC',
        'SUCAC' : 'SUCAC',
        'TARAC' : 'TARAC',
        'AL' : 'AL', # not in USDA
        'SB' : 'SB',
        'AS' : 'AS',
        'CD' : 'CD',
        'CR' : 'CR',
        'CO' : 'CO'
        'CA' : 'CA',
        'CU' : 'CU',
        'F' : 'FD',
        'I' : 'ID'
        'PB' : 'PB',
        'FE' : 'FE',
        'MG' : 'MG',
        'MN' : 'MN',
        'HG' : 'HG',
        'MO' : 'MO',
        'NI' : 'NI',
        'P' : 'P',
        'K' : 'K',
        'SE' : 'SE',
        'NA' : 'NA',
        'S' : 'S', # not found
        'SN' : 'SN',
        'ZN' : 'ZN',
        'THIA' : 'THIA', #THIAMIN (THIA)
        'RIBF' : 'RIBF',# RIBOFLAVIN (RIBF)
        'NIA' : 'NIA', # NIACIN (NIA)
        'NIAEQ' : 'NIAEQ', #NIACIN EQUIVALENTS?
        'PANTAC' : 'PANTAC',
        'VITB6A' : 'VITB6A',
        'BIOT' : 'BIOT', # not available in USDA
        'VITB12' : 'VITB12',
        'FOL' : 'FOL', # folate total
        'FOLAC' : 'FOLAC',
        'FOLDFE' : 'FOLDFE',

        'CARTA' : 'CARTA',
        'CARTB' : 'CARTB',
        'CRYPX' : 'CRYPX',
        'CARTBEQ' : 'CARTBEQ',
        'LUT+ZEA' : 'LUT+ZEA,
        'LYCPN' : 'LYCPN',
        #'XANTHOPHYL' : 'XANTHOPHYL',
        'RETOL' : 'RETOL',
        'VITA_IU' : 'VITA',
        'VITC' : 'VITC',
        # vitd file
        'CHOCAL' : 'CHOCAL',
        'ERGCAL' : 'ERGCAL',
        '25HCHOOL' : 'CHOCALOH',
        '25HERGCAL' : 'ERGCALOH',
        'VITAMIND3EQ' : 'VITDEQ',
        'VITD' : 'VITD',

        #sterols
        'PHYSTR' : 'PHYSTR',
        'STID7' : 'STID7',
        'CAMD5' : 'CAMD5'
        'SITSTR' : 'SITSTR',

        'TOCPHA' : 'TOCPHA', # VIT E
        'TOCTRA' : 'TOCTRA',
        'TOCPHB' : 'TOCPHB',
        'TOCTRB' : 'TOCTRB',
        'TOCPHD' : 'TOCPHD',
        'TOCTRD' : 'TOCTRD',
        'TOCPHG' : 'TOCPHG',
        'TOCTRG' : 'TOCTRG',
        'F4D0' : 'F4D0',
        'F6D0' : 'F6D0',
        'F10D0' : 'F10D0',
        'F12D0' : 'F12D0',
        'F13D0' : 'F13D0',
        'F14D0' : 'F14D0',
        'F15D0' : 'F15D0',
        'F16D0' : 'F16D0', ### review
        'F17D0' : 'F17D0',
        'F18D0' : 'F18D0',
        'F19D0' : 'F19D0',
        'F20D0' : 'F20D0',
        'F21D0' : 'F21D0',
        'F22D0' : 'F22D0',
        'F23D0' : 'F23D0',
        'F24D0' : 'F24D0',

        #saturated FAT
        'FASAT' : 'FASAT',
        'F10D1' : 'F10D1',
        'F14D1' : 'F14D1',
        'F15D1' : 'F15D1',
        'F16D1' : 'F16D1',
        'F17D1' : 'F17D1',
        'F18D1' : 'F18D1',
        'F18D4' : 'F18D4'
        'F18D1TN7' : 'F18D1N7', #USDA USES A TOTAL
        'F20D1' : 'F20D1',
        'F20D1N11' : 'F20D1N11F', #NA
        'F22D1' : 'F22D1',
        'F24D1' : 'F24D1',

        # monosaturated FAT in g
        'FAMS' : 'FAMS',
        'P182W6' : 'F18D2CN6',
        'F18D3CN3' : 'F18D3N3F',
        'F18D3CN6' : 'F18D3N6',
        'F18D4CN3' : 'F18D4N3',
        'F20D2CN6' : 'F20D2N6',
        'F20D3N3' : 'F20D3N3',
        'F20D3N6' : 'F20D3N6',
        'P204W3' : 'P204W3', # not in USDA but in NUTTAB 20:4 n-3
        'F20D4N6' : 'F20D4N6',
        'F20D5' : 'F20D5N3',
        'F22D1C' : 'F22D1C',
        'F22D6' : 'F22DN3',
        'F22D4' : 'F22D6',
        'P224W6' : 'F22D4N6F',
        'P225W3' : 'F22D5N3F',
        'F22D6' : 'F22D6N3', # DHA


        'FAPU' : 'FAPU',
        'LCW3TOTAL' : 'LCW3TOTAL',
        'S4FD' : 'F4D0',
        'S6FD' : 'F6D0',
        'S8FD' : 'F8D0',
        'S10FD' : 'F10D0',
        'S11D' : 'F11D0',
        'S12FD' : 'F12D0',
        'S13FD' : 'F13D0',
        'S14FD' : 'F14D0',
        'F15D0' : 'F15D0',
        'S16FD' : 'F16D0',
        'F17D0' : 'F17D0',
        'S18FD' : 'F18D0',
        'S19FD' : 'F19D0',
        'S20FD' : 'F20D0',
        'S21FD' : 'F21D0',
        'S22FD' : 'F22D0',
        'S23FD' : 'F23D0',
        'F24D0' : 'F24D0',


        # monosaturated fats:
        'TOTAL MONOUNSATURATED FAT (FD)' : 'FAMS',
        'P182W6FD' : 'F18D2N6',
        'F18D3CN3' : 'F18D3N3', # ALA
        'P183W6FD' : 'F18D3N6',
        'P184W3FD' : 'F18D4N3',
        'P202W6FD' : 'F20D2N6',
        'F20D3N3' : 'F20D3N3',
        'F20D3N6' : 'F20D3N6',
        'F20D4N6' : 'P204W3FD',
        'P204W6FD' : 'F20D4N6',
        'P205W3FD' : 'F20D5N3',
        'P222W6FD' : 'P222W6FD',
        'P224W6FD' : 'F22D4N6',
        'F22D5' : 'F22D5N3', # DPA
        'F20D3' : 'F20D3' #undifferentiated
        'P226W3FD' : 'F22D6N3',


        'TOTAL POLYUNSATURATED FAT (FD)' : 'FAPU',
        'LCW3TOTALFD' : 'LCW3TOTALFD',
        'FAUNDIFF' : 'FAUNDIFF',
        'FAUNDIFFFD' : 'FAUN',

        # transfatty acid File
        'F16D1T': 'F16D1T'
        'M161T6' : 'F16D1TF',
        'M18T' : 'F18D1TF',
        'M181T9' : 'F18D1TN9F',
        'M181TW7' : 'F18D1TN7F',
        'TOTAL_TRANSMONO (%)' : 'FATRNMF',
        'P182T' : 'F18D2TF',
        'P182CLA' : 'P182CLA',
        'P182T9T12' : 'P182T9T12',
        'P182TW6' : 'F18D2TN6F',
        'P183T' : 'P183T',
        'P183T9T12T15' : 'P183T9T12T15',
        'TOTAL_TRANSPOLY (%)' : 'FATRNPF',
        'M161T6FD' : 'F16D1T',
        'F18D1T' : 'F18D1T',
        'M181T9FD' : 'F18D1TN9',
        'M181TW7FD' : 'F18D1TN7',
        'TOTAL_TRANSMONO (FD)' : 'FATRNM',
        'P182TFD' : 'F18D2T',
        'P182CLAFD' : 'P182CLAFD',
        'P182T9T12FD' : 'P182T9T12FD',
        'P182TW6FD' : 'F18D2TN6',
        'P183TFD' : 'P183TFD',
        'P183T9T12T15FD' : 'P183T9T12T15FD',
        'FATRNP' : 'FATRNP',
        'TOTAL_TRANSFA' : 'FATRNF',
        'TOTAL_TRANSFAFD' : 'FATRN',
        'FATRNM' : 'FATRNM',

        # Amino Acid File
        'TRP_G' : 'TRP',
        'ALA_G' : 'ALA',
        'ARG_G' : 'ARG',
        'ASP_G' : 'ASP',
        'CYS_G' : 'CYS',
        'GLU_G' : 'GLU',
        'GLY_G' : 'GLY',
        'HIS_G' : 'HIS',
        'ILE_G' : 'ILE',
        'LEU_G' : 'LEU',
        'LYS_G' : 'LYS',
        'MET_G' : 'MET',
        'PHE_G' : 'PHE',
        'PRO_G' : 'PRO',
        'SER_G' : 'SER',
        'THR_G' : 'THR',
        'TYR_G' : 'TYR',
        'VAL_G' : 'VAL',



        # main File
        'CAFFN' : 'CAFFN',
        'CHOL' : 'CHOLE',

        'F20D5' : '',
        'CHOLE' : '',
        }


data_matrix = pd.read_csv(DB_source_path,
                                            header=None,
                                            # encoding=encoding_type,
                                            delimiter=r'\s+',
                                            quotechar=r'"',
                                            )




print data_matrix[0:6][0:6]
