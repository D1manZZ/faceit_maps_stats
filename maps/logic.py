import re
import requests
from bs4 import BeautifulSoup


def logic(x):

    # if x == 'no_link':
    #     return 'Вы не указали участников'
    #
    # map_pool = ("de_cache", "de_dust2", "de_inferno", "de_mirage", "de_nuke", "de_overpass", "de_train", "de_vertigo")
    #
    # pattern = r' (.+) \1'
    # x = re.sub('[\n\r]', " ", " " + x)
    # players_list = [i.replace(' ', '') for i in re.findall(pattern, x)]
    #
    # players_data = {}
    # url = 'https://faceitstats.com/player/'
    # for player_id, nick in enumerate(players_list):
    #     response = requests.get(url + nick)
    #     data = BeautifulSoup(response.text)
    #     # total_games = data.find('div', class_='default-box').find('div', class_='row').find_all('div')[1].find('h5').text
    #     maps = list(data.findAll('tbody'))[1].findAll('tr')
    #     players_data[nick] = {}
    #     for map_obj in maps:
    #         stuff = map_obj.find_all('td')
    #         map_name = stuff[0].text
    #         if map_name not in map_pool:
    #             continue
    #         players_data[nick][map_name] = {}
    #         players_data[nick][map_name]['win_rate'] = stuff[3].text
    #         players_data[nick][map_name]['avg_kills'] = stuff[4].text
    #         players_data[nick][map_name]['kd_ratio'] = stuff[7].text
    players_list = ['Rize1', 'D1manZZ', 'MesnukVbuvca', 'Messageee', 'rexkiller200', '56Saven56', 'Sherkin', 'boi1234567', 'fraiheimeq', 'littlebitJim']
    players_data = {'Rize1': {'de_cache': {'win_rate': '43%', 'avg_kills': '20.97', 'kd_ratio': '1.19'}, 'de_dust2': {'win_rate': '49%', 'avg_kills': '22.05', 'kd_ratio': '1.26'}, 'de_inferno': {'win_rate': '49%', 'avg_kills': '21.48', 'kd_ratio': '1.25'}, 'de_mirage': {'win_rate': '55%', 'avg_kills': '23.28', 'kd_ratio': '1.36'}, 'de_nuke': {'win_rate': '40%', 'avg_kills': '18.63', 'kd_ratio': '1.01'}, 'de_overpass': {'win_rate': '48%', 'avg_kills': '21.25', 'kd_ratio': '1.25'}, 'de_train': {'win_rate': '44%', 'avg_kills': '20.86', 'kd_ratio': '1.12'}, 'de_vertigo': {'win_rate': '50%', 'avg_kills': '24.11', 'kd_ratio': '1.33'}}, 'D1manZZ': {'de_cache': {'win_rate': '49%', 'avg_kills': '21.45', 'kd_ratio': '1.5'}, 'de_dust2': {'win_rate': '61%', 'avg_kills': '21.56', 'kd_ratio': '1.43'}, 'de_inferno': {'win_rate': '61%', 'avg_kills': '20.99', 'kd_ratio': '1.49'}, 'de_mirage': {'win_rate': '47%', 'avg_kills': '21.54', 'kd_ratio': '1.28'}, 'de_nuke': {'win_rate': '50%', 'avg_kills': '21.62', 'kd_ratio': '1.07'}, 'de_overpass': {'win_rate': '55%', 'avg_kills': '19', 'kd_ratio': '1.1'}, 'de_train': {'win_rate': '48%', 'avg_kills': '20.6', 'kd_ratio': '1.14'}, 'de_vertigo': {'win_rate': '83%', 'avg_kills': '27', 'kd_ratio': '1.3'}}, 'MesnukVbuvca': {'de_cache': {'win_rate': '50%', 'avg_kills': '21', 'kd_ratio': '1.37'}, 'de_dust2': {'win_rate': '54%', 'avg_kills': '23.19', 'kd_ratio': '1.35'}, 'de_inferno': {'win_rate': '50%', 'avg_kills': '21.67', 'kd_ratio': '1.26'}, 'de_mirage': {'win_rate': '54%', 'avg_kills': '21.26', 'kd_ratio': '1.2'}, 'de_nuke': {'win_rate': '48%', 'avg_kills': '21.32', 'kd_ratio': '1.16'}, 'de_overpass': {'win_rate': '55%', 'avg_kills': '22.16', 'kd_ratio': '1.16'}, 'de_train': {'win_rate': '52%', 'avg_kills': '21.77', 'kd_ratio': '1.24'}, 'de_vertigo': {'win_rate': '65%', 'avg_kills': '18.82', 'kd_ratio': '1.24'}}, 'Messageee': {'de_cache': {'win_rate': '46%', 'avg_kills': '16.48', 'kd_ratio': '0.89'}, 'de_dust2': {'win_rate': '55%', 'avg_kills': '18.07', 'kd_ratio': '0.97'}, 'de_inferno': {'win_rate': '46%', 'avg_kills': '16.74', 'kd_ratio': '0.96'}, 'de_mirage': {'win_rate': '57%', 'avg_kills': '17.79', 'kd_ratio': '1.04'}, 'de_nuke': {'win_rate': '43%', 'avg_kills': '16.71', 'kd_ratio': '0.85'}, 'de_overpass': {'win_rate': '50%', 'avg_kills': '18.46', 'kd_ratio': '0.99'}, 'de_train': {'win_rate': '37%', 'avg_kills': '13.53', 'kd_ratio': '0.79'}, 'de_vertigo': {'win_rate': '42%', 'avg_kills': '17.81', 'kd_ratio': '0.98'}}, 'rexkiller200': {'de_cache': {'win_rate': '52%', 'avg_kills': '22.04', 'kd_ratio': '1.36'}, 'de_dust2': {'win_rate': '51%', 'avg_kills': '21.9', 'kd_ratio': '1.22'}, 'de_inferno': {'win_rate': '54%', 'avg_kills': '21.11', 'kd_ratio': '1.26'}, 'de_mirage': {'win_rate': '54%', 'avg_kills': '21.67', 'kd_ratio': '1.32'}, 'de_nuke': {'win_rate': '53%', 'avg_kills': '20.53', 'kd_ratio': '1.18'}, 'de_overpass': {'win_rate': '56%', 'avg_kills': '20.68', 'kd_ratio': '1.17'}, 'de_train': {'win_rate': '48%', 'avg_kills': '22.1', 'kd_ratio': '1.16'}, 'de_vertigo': {'win_rate': '86%', 'avg_kills': '20.86', 'kd_ratio': '1.12'}}, '56Saven56': {'de_cache': {'win_rate': '34%', 'avg_kills': '19.14', 'kd_ratio': '0.94'}, 'de_dust2': {'win_rate': '50%', 'avg_kills': '21.19', 'kd_ratio': '1.09'}, 'de_inferno': {'win_rate': '50%', 'avg_kills': '19.15', 'kd_ratio': '1.02'}, 'de_mirage': {'win_rate': '52%', 'avg_kills': '20.87', 'kd_ratio': '1.12'}, 'de_nuke': {'win_rate': '56%', 'avg_kills': '20.22', 'kd_ratio': '1.09'}, 'de_overpass': {'win_rate': '52%', 'avg_kills': '19.97', 'kd_ratio': '1.09'}, 'de_train': {'win_rate': '47%', 'avg_kills': '19.95', 'kd_ratio': '1.07'}, 'de_vertigo': {'win_rate': '58%', 'avg_kills': '20.84', 'kd_ratio': '1.1'}}, 'Sherkin': {'de_cache': {'win_rate': '49%', 'avg_kills': '19.73', 'kd_ratio': '1.14'}, 'de_dust2': {'win_rate': '52%', 'avg_kills': '20.22', 'kd_ratio': '1.16'}, 'de_inferno': {'win_rate': '44%', 'avg_kills': '17.34', 'kd_ratio': '1.01'}, 'de_mirage': {'win_rate': '47%', 'avg_kills': '18.91', 'kd_ratio': '1.05'}, 'de_nuke': {'win_rate': '48%', 'avg_kills': '19.1', 'kd_ratio': '1.01'}, 'de_overpass': {'win_rate': '66%', 'avg_kills': '19.97', 'kd_ratio': '1.35'}, 'de_train': {'win_rate': '40%', 'avg_kills': '18.2', 'kd_ratio': '0.99'}, 'de_vertigo': {'win_rate': '48%', 'avg_kills': '19.48', 'kd_ratio': '1.06'}}, 'boi1234567': {'de_cache': {'win_rate': '67%', 'avg_kills': '16.78', 'kd_ratio': '1.21'}, 'de_dust2': {'win_rate': '37%', 'avg_kills': '23.74', 'kd_ratio': '1.42'}, 'de_inferno': {'win_rate': '63%', 'avg_kills': '21.41', 'kd_ratio': '1.16'}, 'de_mirage': {'win_rate': '52%', 'avg_kills': '20.98', 'kd_ratio': '1.18'}, 'de_nuke': {'win_rate': '73%', 'avg_kills': '21.6', 'kd_ratio': '1.24'}, 'de_overpass': {'win_rate': '58%', 'avg_kills': '20.51', 'kd_ratio': '1.1'}, 'de_train': {'win_rate': '64%', 'avg_kills': '21.21', 'kd_ratio': '1.34'}, 'de_vertigo': {'win_rate': '57%', 'avg_kills': '17.95', 'kd_ratio': '1'}}, 'fraiheimeq': {'de_cache': {'win_rate': '49%', 'avg_kills': '17.8', 'kd_ratio': '0.94'}, 'de_dust2': {'win_rate': '38%', 'avg_kills': '15.49', 'kd_ratio': '0.77'}, 'de_inferno': {'win_rate': '40%', 'avg_kills': '15.1', 'kd_ratio': '0.76'}, 'de_mirage': {'win_rate': '49%', 'avg_kills': '16.85', 'kd_ratio': '0.88'}, 'de_nuke': {'win_rate': '44%', 'avg_kills': '17.52', 'kd_ratio': '0.86'}, 'de_overpass': {'win_rate': '63%', 'avg_kills': '18.14', 'kd_ratio': '0.93'}, 'de_train': {'win_rate': '45%', 'avg_kills': '16', 'kd_ratio': '0.76'}, 'de_vertigo': {'win_rate': '58%', 'avg_kills': '16.53', 'kd_ratio': '0.85'}}, 'littlebitJim': {'de_cache': {'win_rate': '39%', 'avg_kills': '20.14', 'kd_ratio': '1.16'}, 'de_dust2': {'win_rate': '57%', 'avg_kills': '18', 'kd_ratio': '1.07'}, 'de_inferno': {'win_rate': '40%', 'avg_kills': '20.52', 'kd_ratio': '1.22'}, 'de_mirage': {'win_rate': '43%', 'avg_kills': '20.5', 'kd_ratio': '1.16'}, 'de_nuke': {'win_rate': '51%', 'avg_kills': '21.98', 'kd_ratio': '1.31'}, 'de_overpass': {'win_rate': '65%', 'avg_kills': '21.81', 'kd_ratio': '1.43'}, 'de_train': {'win_rate': '46%', 'avg_kills': '22.21', 'kd_ratio': '1.23'}, 'de_vertigo': {'win_rate': '55%', 'avg_kills': '21.14', 'kd_ratio': '1.29'}}}
    average_data = {'team_left': {}, 'team_right': {}}
    detector = 'team_left'
    for nick, maps in players_data.items():
        if nick == players_list[len(players_list) // 2]:
            detector = 'team_right'
        for map_name, stats in maps.items():
            if map_name not in average_data[detector].keys():
                average_data[detector][map_name] = {}
            for stat, value in stats.items():
                if stat not in average_data[detector][map_name].keys():
                    average_data[detector][map_name][stat] = 0
                average_data[detector][map_name][stat] += float(players_data[nick][map_name][stat].strip('%'))
                if nick in (players_list[-1], players_list[len(players_list) // 2 - 1]):
                    average_data[detector][map_name][stat] = round(average_data[detector][map_name][stat] / (len(players_list) // 2), 2)
    differences = {}
    for 
    return average_data
