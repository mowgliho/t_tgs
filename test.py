import datetime

# data
flights = {'ABJ': ['ACC'], 'ACC': ['DXB', 'ABJ'], 'ADD': ['DXB'], 'ADL': ['DXB'], 'AKL': ['SYD', 'MEL', 'BNE'], 'ALG': ['DXB'], 'AMD': ['DXB'], 'AMM': ['DXB'], 'AMS': ['DXB'], 'ARN': ['DXB'], 'ATH': ['DXB'], 'BAH': ['DXB'], 'BCN': ['DXB'], 'BEY': ['DXB'], 'BGW': ['DXB'], 'BHX': ['DXB'], 'BKK': ['SYD', 'DXB', 'HKG'], 'BLR': ['DXB'], 'BNE': ['DXB', 'ROK', 'SIN', 'AKL', 'BKQ', 'LRE'], 'BOM': ['DXB'], 'BOS': ['DXB'], 'BSR': ['DXB'], 'CAI': ['DXB'], 'CAN': ['DXB'], 'CCJ': ['DXB'], 'CCU': ['DXB'], 'CDG': ['DXB'], 'CGK': ['DXB'], 'CHC': ['SYD'], 'CMB': ['MLE', 'DXB'], 'CMN': ['DXB'], 'CNS': ['GOV'], 'COK': ['DXB'], 'CPH': ['DXB'], 'CPT': ['DXB'], 'DAC': ['DXB'], 'DAR': ['DXB'], 'DEL': ['DXB'], 'DFW': ['DXB'], 'DKR': ['DXB'], 'DME': ['DXB'], 'DMM': ['DXB'], 'DOH': ['DXB'], 'DRW': ['GOV', 'ASP'], 'DUB': ['DXB'], 'DUR': ['DXB'], 'DUS': ['DXB'], 'DXB': ['ATH', 'NCE', 'KUL', 'LIS', 'AMD', 'GIG', 'PER', 'TUN', 'DUR', 'SEZ', 'VIE', 'MLA', 'CMB', 'HYD', 'MEL', 'PEW', 'DMM', 'CGK', 'GRU', 'DOH', 'MAD', 'EBB', 'NBO', 'BOS', 'PEK', 'BLR', 'DAC', 'ADL', 'KWI', 'DFW', 'MXP', 'AMS', 'DKR', 'BOM', 'WAW', 'IAD', 'BEY', 'RUH', 'SFO', 'SAH', 'JNB', 'BCN', 'IKA', 'LUN', 'DEL', 'LHR', 'AMM', 'MAN', 'MAA', 'CPT', 'CAN', 'LHE', 'ICN', 'LOS', 'ISB', 'KBP', 'SGN', 'CPH', 'HKT', 'ALG', 'CCU', 'MCT', 'HKG', 'DUS', 'TPE', 'ZRH', 'DAR', 'KBL', 'KHI', 'NCL', 'FCO', 'SYD', 'LED', 'SIN', 'DME', 'SKT', 'BHX', 'PVG', 'BAH', 'LCA', 'COK', 'ARN', 'CMN', 'LAX', 'DUB', 'TRV', 'LYS', 'NRT', 'ADD', 'EBL', 'GVA', 'FRA', 'ACC', 'BKK', 'GLA', 'CCJ', 'HND', 'CAI', 'MNL', 'KRT', 'IAH', 'IST', 'YYZ', 'PRG', 'MED', 'KIX', 'BGW', 'MLE', 'HAM', 'LGW', 'VCE', 'JED', 'SEA', 'LAD', 'MRU', 'BNE', 'MUC', 'CDG', 'JFK', 'BSR'], 'EBB': ['DXB'], 'EBL': ['DXB'], 'EZE': ['GIG'], 'FCO': ['DXB'], 'FRA': ['DXB'], 'GIG': ['DXB', 'EZE'], 'GLA': ['DXB'], 'GRU': ['DXB'], 'GVA': ['DXB'], 'HAM': ['DXB'], 'HKG': ['BKK', 'DXB'], 'HKT': ['DXB'], 'HND': ['DXB'], 'HRE': ['LUN'], 'HYD': ['DXB'], 'IAD': ['DXB'], 'IAH': ['DXB'], 'ICN': ['DXB'], 'IKA': ['DXB'], 'ISB': ['DXB'], 'IST': ['DXB'], 'JED': ['DXB'], 'JFK': ['MXP', 'DXB'], 'JNB': ['DXB'], 'KBL': ['DXB'], 'KBP': ['DXB'], 'KHI': ['DXB'], 'KIX': ['DXB'], 'KRT': ['DXB'], 'KUL': ['MEL', 'DXB'], 'KWI': ['DXB'], 'LAD': ['DXB'], 'LAX': ['DXB'], 'LCA': ['MLA', 'DXB'], 'LED': ['DXB'], 'LGW': ['DXB'], 'LHE': ['DXB'], 'LHR': ['DXB'], 'LIS': ['DXB'], 'LOS': ['DXB'], 'LUN': ['HRE', 'DXB'], 'LYS': ['DXB'], 'MAA': ['DXB'], 'MAD': ['DXB'], 'MAN': ['DXB'], 'MCT': ['DXB'], 'MED': ['DXB'], 'MEL': ['DXB', 'KUL', 'WLG', 'SIN', 'AKL'], 'MLA': ['LCA', 'TIP'], 'MLE': ['CMB', 'DXB'], 'MNL': ['DXB'], 'MRU': ['DXB'], 'MUC': ['DXB'], 'MXP': ['DXB', 'JFK'], 'NBO': ['DXB'], 'NCE': ['DXB'], 'NCL': ['DXB'], 'NRT': ['DXB'], 'PEK': ['DXB'], 'PER': ['SIN', 'DXB', 'ASP'], 'PEW': ['DXB'], 'PRG': ['DXB'], 'PVG': ['DXB'], 'ROK': ['BNE'], 'RUH': ['DXB'], 'SAH': ['DXB'], 'SEA': ['DXB'], 'SEZ': ['DXB'], 'SFO': ['DXB'], 'SGN': ['DXB'], 'SIN': ['DXB', 'PER', 'SYD', 'MEL', 'BNE'], 'SKT': ['DXB'], 'SYD': ['DXB', 'BKK', 'ZQN', 'WLG', 'SIN', 'CHC', 'AKL'], 'TIP': ['DXB'], 'TPE': ['DXB'], 'TRV': ['DXB'], 'TUN': ['DXB'], 'VCE': ['DXB'], 'VIE': ['DXB'], 'WAW': ['DXB'], 'WLG': ['SYD', 'MEL'], 'YYZ': ['DXB'], 'ZQN': ['SYD'], 'ZRH': ['DXB']}

source_airports = set([x.lower() for x in set(flights.keys())])
dest_airports = set([apt.lower() for val in flights.values() for apt in val])

def valid_date(input_text, date):
  try:
    return ((datetime.datetime.strptime(input_text,'%Y-%m-%d').date() - date).days > 0) and ((datetime.datetime.strptime(input_text,'%Y-%m-%d').date() - datetime.date.today()).days < 365)
  except:
    return False

def get_date(input_text):
  return datetime.datetime.strptime(input_text,'%Y-%m-%d').date()

# actual program

messages = {
  'from':'From:',
  'to':'To:',
  'date': 'Date yyyy-MM-dd',
  'choose': 'One-way(o), Return (r), or Multi-city(m)?',
  'return_date': 'Date yyyy-MM-dd',
  'more': 'More flights? (y/n)'
}

trip_types = ['o','r','m']

invalid_input = 'invalid input'

#initial state
state = 'from'
source_airport = None
dest_airport = None
trip_type = None
last_date = datetime.date.today()
flights = []

while True:
  print(messages[state])
  input_text = input('> ')
  if state == 'from' and input_text.lower() in source_airports:
    source_airport = input_text.lower()
    state = 'to'
  elif state == 'to' and input_text.lower() in dest_airports:
    dest_airport = input_text.lower()
    state = 'date'
  elif state == 'date' and valid_date(input_text, last_date):
    flights.append('%s To %s on %s' % (source_airport.upper(), dest_airport.upper(), input_text))
    last_date = get_date(input_text)
    if trip_type is None:
      state = 'choose'
    elif trip_type == 'r':
      break
    elif trip_type == 'm':
      state = 'more'
  elif state == 'choose' and input_text in trip_types:
    trip_type = input_text
    if trip_type == 'o':
      break
    elif trip_type == 'r':
      state = 'date'
      source_airport, dest_airport = dest_airport, source_airport
    else:
      state = 'to'
      source_airport = dest_airport
  elif state == 'more' and input_text in ['y','n']:
    if input_text == 'y':
      state = 'to'
      source_airport = dest_airport
    else:
      break
  else:
    print(invalid_input)

print('\n\n\nYour Flights:')
print('\n'.join(flights))
