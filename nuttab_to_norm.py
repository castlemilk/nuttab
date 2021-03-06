# mapping = {native_key : normal_key}
mapping = {
        'ENERGY-04DF' : 'ENERC1',
        'MOIS' : 'WATER',
        'PROT' : 'PROCNT',
        'NIT' : 'NT', # no nitrogen equivalent (nitrogen factor?)
        'FAT' : 'FAT',
        'ASH' : 'ASH',
        'AOACDFTOTW' : 'FIBTG',
        'ETOHM' : 'ALC',
        'FRU': 'FRUS',
        'GLUC' : 'GLUS',
        'SUC' : 'SUCS',
        'MALT' : 'MALS',
        'LACT' : 'LACS',
        'GAL' : 'GALS',
        'MALT3' : 'MALTRS',

        'TOTALSUGARS' : 'SUGAR',
        'STARCH' : 'STARCH',
        'DEXTRIN' : 'DEXTN',
        'GLYCEROL' : 'GLYRL',
        'GLYCOGEN' : 'GLYC',
        'INULIN' : 'INULN',
        'MANNITOL' : 'MANTL',
        'MALTODEXTRIN' : 'MALTDEX',
        'OLIGOSACCH' : 'OLSAC',
        'RAFFINOSE' : 'RAFS',
        'STACHYOSE' : 'STAS',
        'SORB' : 'SORTL',
        'AVAILCHO' : 'CHOAVL',
        'AVAILCHOCNS' : 'AVAILCHOCNS',
        'CHODIFF' : 'CHOCDF',
        'ACETIC' : 'ACEAC',
        'CITRIC' : 'CITAC',
        'FUMARIC' : 'FUMAC',
        'LACTIC' : 'LACAC',
        'MALIC' : 'MALAC',
        'OXALIC' : 'OXALAC',
        'PROPIONIC' : 'PROPAC',
        'QUINIC' : 'QUINAC',
        'SHIKIMIC' : 'SHIKAC',
        'SUCCINIC' : 'SUCAC',
        'TARTARIC' : 'TARAC',
        'AL' : 'AL', # not in USDA
        'SB' : 'SB',
        'AS' : 'AS',
        'CD' : 'CD',
        'CR' : 'CR',
        'CO' : 'CO',
        'CA' : 'CA',
        'CU' : 'CU',
        'F' : 'FD',
        'I' : 'ID',
        'IODINE' : 'ID',
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
        'B1' : 'THIA', #THIAMIN (THIA)
        'B2' : 'RIBF',# RIBOFLAVIN (RIBF)
        'B3' : 'NIA', # NIACIN (NIA)
        'NIACIN EQUIVALENTS' : 'NIAEQ', #NIACIN EQUIVALENTS?
        'PANT' : 'PANTAC',
        'B6' : 'VITB6A',
        'BIOTIN' : 'BIOT', # not available in USDA
        'B12' : 'VITB12',
        'FOLFD' : 'FOLFD',
        'FOLAC' : 'FOLAC',
        'FOLATETOT' :  'FOL',
        'FOLDFE-04' : 'FOLDFE',

        'ACAR' : 'CARTA',
        'BCAR' : 'CARTB',
        'CRYP' : 'CRYPX',
        'BCAREQ-04' : 'CARTBEQ',
        'LUTIEN' : 'LUTN',
        'LYCO' : 'LYCPN',
        'XANTHOPHYL' : 'XANTHOPHYL',
        'RET' : 'RETOL',
        'RETEQ-05' : 'VITA',
        'VITC' : 'VITC',
        # vitd file
        'CHOOL' : 'CHOCAL',
        'ERGCAL' : 'ERGCAL',
        '25HCHOOL' : 'CHOCALOH',
        '25HERGCAL' : 'ERGCALOH',
        'VITAMIND3EQ' : 'VITDEQ',

        'ATOC' : 'TOCPHA',
        'ATOCOL' : 'TOCTRA',
        'BTOC' : 'TOCPHB',
        'BTOCOL' : 'TOCTRB',
        'DTOC' : 'TOCPHD',
        'DTOCOL' : 'TOCTRD',
        'GTOC' : 'TOCPHG',
        'GTOCOL' : 'TOCTRG',
        'VITE' : 'VITE',
        'S4' : 'F4D0F', #convert all of these to mg/100g (multiple by 100) essentially
        'S6' : 'F6D0F',
        'S8' : 'F8D0F',
        'S11' : 'F11D0F',
        'S10' : 'F10D0F',
        'S12' : 'F12D0F',
        'S13' :'F13D0F',
        'S14' : 'F14D0F',
        'S15' : 'F15D0F',
        'S16' : 'F16D0F', ### review
        'S17' : 'F17D0F',
        'S18' : 'F18D0F',
        'S19' : 'F19D0F',
        'S20' : 'F20D0F',
        'S21' : 'F21D0F',
        'S22' : 'F22D0F',
        'S23' : 'F23D0F',
        'S24' : 'F24D0F',

        #saturated FAT
        'TOTAL_SATURAT-04' : 'FATSAT',
        'M10' : 'F10D1F',
        'M14' : 'F14D1F',
        'M15' : 'F15D1F',
        'M16' : 'F16D1F',
        'M17' : 'F17D1F',
        'M18' : 'F18D1F',
        'M18W7' : 'F18D1N7F',
        'M181W7' : 'F18D1N7F',
        'M20' : 'F20D1F',
        'M201W11' : 'F20D1N11F',
        'M22' : 'F22D1F',
        'M24' : 'F24D1F',

        # monosaturated FAT
        'TOTAL MONOUNSATURATED FAT (%)' : 'FAMSF',
        'P182W6' : 'F18D2CN6',
        'P183W3' : 'F18D3N3F',
        'P183W6' : 'F18D3N6F',
        'P184W3' : 'F18D4N3F',
        'P202W6' : 'F20D2N6F',
        'P203W3' : 'F20D3N3F',
        'P203W6' : 'F20D3N6F',
        'P204W3' : 'P204W3',
        'P204W6' : 'F20D4N6F',
        'P205W3' : 'F20D5N3F',
        'P222W6' : 'P222W6',
        'P224W6' : 'F22D4N6F',
        'P225W3' : 'F22D5N3F',
        'P226W3' : 'F22D6N3F',


        'TOTAL POLYUNSATURATED FAT (%)' : 'FAPUF',
        'LCW3TOTAL' : 'LCW3TOTAL',
        'S4FD' : 'F4D0',
        'S6FD' : 'F6D0',
        'S8FD' : 'F8D0',
        'S10FD' : 'F10D0',
        'S11FD' : 'F11D0',
        'S12FD' : 'F12D0',
        'S13FD' : 'F13D0',
        'S14FD' : 'F14D0',
        'S15FD' : 'F15D0',
        'S16FD' : 'F16D0',
        'S17FD' : 'F17D0',
        'S18FD' : 'F18D0',
        'S19FD' : 'F19D0',
        'S20FD' : 'F20D0',
        'S21FD' : 'F21D0',
        'S22FD' : 'F22D0',
        'S23FD' : 'F23D0',
        'S24FD' : 'F24D0',

        # sat FAT
        'TOTALSATURATFD-04' : 'FASAT',
        'M10FD' : 'F10D1',
        'M14FD' : 'F14D1',
        'M15FD' : 'F15D1',
        'M16FD' : 'F16D1',
        'M17FD' : 'F17D1',
        'M18FD' : 'F18D1',
        'M18W7FD' : 'F18D1N7',
        'M181W7FD' : 'F18D1N7',
        'M20FD' : 'F20D1',
        'M201W11FD' : 'F20D1N11',
        'M22FD' : 'F22D1',
        'M24FD' : 'F24D1',


        # monosaturated fats:
        'TOTAL MONOUNSATURATED FAT (FD)' : 'FAMS',
        'P182W6FD' : 'F18D2N6',
        'P183W3FD' : 'F18D3N3',
        'P183W6FD' : 'F18D3N6',
        'P184W3FD' : 'F18D4N3',
        'P202W6FD' : 'F20D2N6',
        'P203W3FD' : 'F20D3N3',
        'P203W6FD' : 'F20D3N6',
        'P204W3FD' : 'P204W3FD',
        'P204W6FD' : 'F20D4N6',
        'P205W3FD' : 'F20D5N3',
        'P222W6FD' : 'P222W6FD',
        'P224W6FD' : 'F22D4N6',
        'P225W3FD' : 'F22D5N3',
        'P226W3FD' : 'F22D6N3',

        'TOTAL POLYUNSATURATED FAT (FD)' : 'FAPU',
        'LCW3TOTALFD' : 'LCW3TOTALFD',
        'FAUNDIFF' : 'FAUNDIFF',
        'FAUNDIFFFD' : 'FAUN',

        # transfatty acid File
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
        'M181TFD' : 'F18D1T',
        'M181T9FD' : 'F18D1TN9',
        'M181TW7FD' : 'F18D1TN7',
        'TOTAL_TRANSMONO (FD)' : 'FATRNM',
        'P182TFD' : 'F18D2T',
        'P182CLAFD' : 'P182CLAFD',
        'P182T9T12FD' : 'P182T9T12FD',
        'P182TW6FD' : 'F18D2TN6',
        'P183TFD' : 'P183TFD',
        'P183T9T12T15FD' : 'P183T9T12T15FD',
        'TOTAL_TRANSPOLY (FD)' : 'FATRNP',
        'TOTAL_TRANSFA' : 'FATRNF',
        'TOTAL_TRANSFAFD' : 'FATRN',

        # Amino Acid File - *** need to convert to not being percentage of nitrogen
        'TRYP' : 'TRPN',
        'TRYPFD' : 'TRP',
        'ALA' : 'ALAN',
        'ARG' : 'ARGN',
        'ASP' : 'ASPN',
        'CSY' : 'CSYN',
        'GLU' : 'GLUN',
        'GLY' : 'GLYN',
        'HIS' : 'HISN',
        'ILEU' : 'ILEN',
        'LEU' : 'LEUN',
        'LUTEIN' : 'LUTN',
        'LYS' : 'LYSN',
        'MET' : 'METN',
        'PHE' : 'PHEN',
        'PRO' : 'PRON',
        'SER' : 'SERN',
        'THR' : 'THRN',
        'TYR' : 'TYRN',
        'VAL' : 'VALN',



        # main File
        'CAFFEINE' : 'CAFFN',
        'CHOL' : 'CHOLE',

        'F20D5' : '',
        'CHOLE' : '',
        }
