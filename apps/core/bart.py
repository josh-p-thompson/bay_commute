import requests
import os
from datetime import datetime, timedelta
import pprint
bart_key = os.getenv("BART_API_KEY")
# cach.set
# cach.get 

# BART API 
def station_arrivals(stn_abbr="ALL"): 
    """
    DEFINITIONS
    update_datetime - DATETIME - time when data was updated
    station_name - STRING - station where train is arriving
    station_abbr - STRING - abbreviated station name where train is arriving
    destination_name - STRING - final destination station of train
    destination_abbr - STRING - abbreviated final destination station of train
    arrival_minutes - STRING - minutes until train arrives (Note: <1 is "Leaving" rather than "0")
    arrival_datetime - DATETIME - estimated arrival time of the train
    platform - STRING - platform number where train is 
    direction - STRING - direciton train is traveling (Note: either "North" or "South")
    length - STRING - number of train cars
    color - STRING - color of line (e.g., "BLUE")
    hexcolor - STRING - color of line as a hexcolor (e.g., "#0099cc")
    delay_seconds - STRING - number of seconds the train has deviated from the original schedule
    """
    params = {'key': bart_key, 'cmd': 'etd', 'orig': stn_abbr, 'json': 'y'}
    response = requests.get('http://api.bart.gov/api/etd.aspx', params=params)
    # print(f'Status code: {response.status_code}')
    # print(f'Headers: {response.headers}')
    result = response.json()['root']

    update_datetime = datetime.combine(
        datetime.strptime(result['date'], "%m/%d/%Y"),
        datetime.strptime(result['time'][0:11],"%I:%M:%S %p").time()
    )
    arrivals = {}
    for station in result['station']: 
        arrivals[station['abbr']] = []
        for destination in station['etd']: 
            for train in destination['estimate']: 
                arrivals[station['abbr']].append({
                    'update_datetime': update_datetime,
                    'station_name': station['name'],
                    'station_abbr': station['abbr'],
                    'destination_name': destination['destination'],
                    'destination_abbr': destination['abbreviation'],
                    'arrival_minutes': train['minutes'],
                    'arrival_datetime': estimate_arrival(update_datetime, train['minutes']), 
                    'arrival_time': estimate_arrival(update_datetime, train['minutes']).strftime('%-I:%M'), 
                    'platform': train['platform'],
                    'direction': train['direction'],
                    'length': train['length'],
                    'color': train['color'],
                    'hexcolor': train['hexcolor'], 
                    'delay_seconds': train['delay'],   
                })
    return arrivals

def estimate_arrival(update_datetime, arrival_minutes): 
    try: 
        arrival = int(arrival_minutes)
    except ValueError: 
        arrival = 0
    return update_datetime + timedelta(minutes=arrival)

def stations(): 
    return [{'abbr': '12TH', 'name': '12th St. Oakland City Center'},
            {'abbr': '16TH', 'name': '16th St. Mission'},
            {'abbr': '19TH', 'name': '19th St. Oakland'},
            {'abbr': '24TH', 'name': '24th St. Mission'},
            {'abbr': 'ANTC', 'name': 'Antioch'},
            {'abbr': 'ASHB', 'name': 'Ashby'},
            {'abbr': 'BALB', 'name': 'Balboa Park'},
            {'abbr': 'BAYF', 'name': 'Bay Fair'},
            {'abbr': 'CAST', 'name': 'Castro Valley'},
            {'abbr': 'CIVC', 'name': 'Civic Center/UN Plaza'},
            {'abbr': 'COLS', 'name': 'Coliseum'},
            {'abbr': 'COLM', 'name': 'Colma'},
            {'abbr': 'CONC', 'name': 'Concord'},
            {'abbr': 'DALY', 'name': 'Daly City'},
            {'abbr': 'DBRK', 'name': 'Downtown Berkeley'},
            {'abbr': 'DUBL', 'name': 'Dublin/Pleasanton'},
            {'abbr': 'PLZA', 'name': 'El Cerrito Plaza'},
            {'abbr': 'DELN', 'name': 'El Cerrito del Norte'},
            {'abbr': 'EMBR', 'name': 'Embarcadero'},
            {'abbr': 'FRMT', 'name': 'Fremont'},
            {'abbr': 'FTVL', 'name': 'Fruitvale'},
            {'abbr': 'GLEN', 'name': 'Glen Park'},
            {'abbr': 'HAYW', 'name': 'Hayward'},
            {'abbr': 'LAFY', 'name': 'Lafayette'},
            {'abbr': 'LAKE', 'name': 'Lake Merritt'},
            {'abbr': 'MCAR', 'name': 'MacArthur'},
            {'abbr': 'MLBR', 'name': 'Millbrae'},
            {'abbr': 'MONT', 'name': 'Montgomery St.'},
            {'abbr': 'NBRK', 'name': 'North Berkeley'},
            {'abbr': 'NCON', 'name': 'North Concord/Martinez'},
            {'abbr': 'ORIN', 'name': 'Orinda'},
            {'abbr': 'PCTR', 'name': 'Pittsburg Center'},
            {'abbr': 'PITT', 'name': 'Pittsburg/Bay Point'},
            {'abbr': 'PHIL', 'name': 'Pleasant Hill/Contra Costa Centre'},
            {'abbr': 'POWL', 'name': 'Powell St.'},
            {'abbr': 'RICH', 'name': 'Richmond'},
            {'abbr': 'ROCK', 'name': 'Rockridge'},
            {'abbr': 'SBRN', 'name': 'San Bruno'},
            {'abbr': 'SFIA', 'name': "San Francisco Int'l Airport"},
            {'abbr': 'SANL', 'name': 'San Leandro'},
            {'abbr': 'SHAY', 'name': 'South Hayward'},
            {'abbr': 'SSAN', 'name': 'South San Francisco'},
            {'abbr': 'UCTY', 'name': 'Union City'},
            {'abbr': 'WCRK', 'name': 'Walnut Creek'},
            {'abbr': 'WARM', 'name': 'Warm Springs/South Fremont'},
            {'abbr': 'WDUB', 'name': 'West Dublin/Pleasanton'},
            {'abbr': 'WOAK', 'name': 'West Oakland'}]      

def station_dict(): 
    station_dict = {station['abbr']: station['name'] for station in stations()}
    # add sorting
    return {k: v for k, v in sorted(station_dict.items(), key=lambda item: item[1])}

def main(): 
    arrivals = station_arrivals_nested()
    pprint.pprint(arrivals)


if __name__ == '__main__': 
    main()