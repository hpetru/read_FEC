STATE_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

STATE_CHOICES_DICT = dict(STATE_CHOICES)

STATES_FIPS_DICT = {
    'WA':'53',
    'VA':'51',
    'DE':'10',
    'DC':'11',
    'WI':'55',
    'WV':'54',
    'HI':'15',
    'FL':'12',
    'WY':'56',
    'NH':'33',
    'NJ':'34',
    'NM':'35',
    'TX':'48',
    'LA':'22',
    'NC':'37',
    'ND':'38',
    'NE':'31',
    'TN':'47',
    'NY':'36',
    'PA':'42',
    'CA':'06',
    'NV':'32',
    'CO':'08',
    'AK':'02',
    'AL':'01',
    'AR':'05',
    'VT':'50',
    'IL':'17',
    'GA':'13',
    'IN':'18',
    'IA':'19',
    'OK':'40',
    'AZ':'04',
    'ID':'16',
    'CT':'09',
    'ME':'23',
    'MD':'24',
    'MA':'25',
    'OH':'39',
    'UT':'49',
    'MO':'29',
    'MN':'27',
    'MI':'26',
    'RI':'44',
    'KS':'20',
    'MT':'30',
    'MS':'28',
    'SC':'45',
    'KY':'21',
    'OR':'41',
    'SD':'46'}

ELECTION_TYPE_CHOICES = (('G', 'General'), ('P', 'Primary'), ('PR', 'Primary Runoff'), ('GR', 'General Runoff'), ('SP', 'Special Primary'), ('OR', 'Special Primary Runoff'), ('SG', 'Special General'), ('SR', 'Special General Runoff'), ('O', 'Other'))

ELECTION_TYPE_DICT = {'G':'general' ,'P':'primary', 'PR': 'runoff (primary election)', 'GR':'runoff (general election)', 'SP':'(primary) special election', 'OR':'runoff (primary, special election)', 'SG':'special election (general)', 'SR':'runoff, special general', 'O':'other'}

CANDIDATE_STATUS_CHOICES = (('W', 'Dropped out / withdrew'),('LP', 'lost in primary'), ('PR', 'lost in primary runoff'), ('G', 'lost in general'), ('GR', 'lost in general runoff'), ('SP', 'lost in special primary'), ('SR', 'lost in special runoff'), ('SG', 'lost in special general'), ('SX', 'lost in special general runoff'), ('LC', 'lost in party convention'))

CANDIDATE_STATUS_DICT = {'LP':'Lost in primary','PR':'Lost in primary runoff', 'G':'Lost in general', 'GR':'Lost in general runoff', 'SP':'Lost in special primary', 'SR':'Lost in special runoff', 'SG':'Lost in special general', 'SX':'Lost in special general runoff', 'W': 'Withdrew or not on ballot', 'LC':'Lost in party convention'}

COMPETITIVE_INDEPENDENTS = [{'name':'SD Senate', 'district_id': 1062}, {'name':'Kansas Senate', 'district_id': 1012}]


type_hash_full={'C': 'Communication Cost',
          'D': 'Delegate',
          'E': 'Electioneering Communication',
          'H': 'House',
          'I': 'Not a Committee',
          'N': 'Non-Party, Non-Qualified',
          'O': 'Super PAC',
          'P': 'Presidential',
          'Q': 'Qualified, Non-Party',
          'S': 'Senate',
          'U': 'Single candidate super PAC',
          'V': 'Hybrid super PAC - Nonqualified',
          'W': 'Hybrid super PAC - Qualified',
          'X': 'Non-Qualified Party',
          'Y': 'Qualified Party',
          'Z': 'National Party Organization',
          }

type_hash={'C': 'Communication Cost',
        'D': 'Delegate',
        'E': 'Electioneering',
        'H': 'House',
        'I': 'Expenditure Only',
        'N': 'PAC',
        'O': 'Super PAC',
        'P': 'Presidential',
        'Q': 'PAC',
        'S': 'Senate',
        'U': 'Single candidate super PAC',
        'V': 'Hybrid super PAC',
        'W': 'Hybrid super PAC',
        'X': 'Party PAC',
        'Y': 'Party PAC',
        'Z': 'National Party PAC',
        }

committee_designation_hash = {'A':'Authorized by Candidate',
                            'J': 'Joint Fund Raiser',
                            'P': 'Principal Committee of Candidate',
                            'U': 'Unauthorized',
                            'B': 'Lobbyist/Registrant PAC',
                            'D': 'Leadership PAC'
                            }
