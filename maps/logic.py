import re
import requests
from bs4 import BeautifulSoup


def logic(x):

    if x == 'no_link':
        return 'Вы не указали участников'

    map_pool = ("de_cache", "de_dust2", "de_inferno", "de_mirage", "de_nuke", "de_overpass", "de_train", "de_vertigo")
    my_nicks = ('D1manZZ', 'FrayZ_3')

    pattern = r' (.+) \1'
    x = re.sub('[\n\r]', " ", " " + x)
    players_list = [i.replace(' ', '') for i in re.findall(pattern, x)]
    half_list = len(players_list) // 2
    for nick in players_list[half_list:]:
        if nick in my_nicks:
            players_list = players_list[half_list:] + players_list[:half_list]
            break
    players_data = {}
    url = 'https://faceitstats.com/player/'
    additional_dict = {}
    for player_id, nick in enumerate(players_list):
        response = requests.get(url + nick)
        data = BeautifulSoup(response.text, features="html.parser")
        total_games = int(data.find('div', id='app').find('main').find('div').find('div').contents[3].find('div').find('div').contents[3].find('h5').get_text().split(' /')[0])
        elo = int(data.find('div', id='app').find('main').find('div').find('div').contents[3].find('div').find('div').find('div').find('h5').text)
        additional_dict[nick] = {}
        additional_dict[nick]['elo'] = elo
        maps = list(data.findAll('tbody'))[1].findAll('tr')
        players_data[nick] = {}
        for map_obj in maps:
            stuff = map_obj.find_all('td')
            map_name = stuff[0].text
            if map_name not in map_pool:
                continue
            players_data[nick][map_name] = {}
            players_data[nick][map_name]['win_rate'] = stuff[3].text
            players_data[nick][map_name]['drop_probability'] = round(int(stuff[1].text) * 100 / total_games, 2)
            players_data[nick][map_name]['avg_kills'] = stuff[4].text
            players_data[nick][map_name]['kd_ratio'] = stuff[7].text
    list_of_elo = [additional_dict[k]['elo'] for k in additional_dict.keys()]
    avg_elo_1 = sum(list_of_elo[:half_list]) / half_list
    avg_elo_2 = sum(list_of_elo[half_list:]) / half_list
    detector = 'team_left'
    for key in additional_dict.keys():
        if key == players_list[len(players_list) // 2]:
            detector = 'team_right'
        additional_dict[key]['weight'] = additional_dict[key]['elo'] / (avg_elo_1 if detector == 'team_left' else avg_elo_2)
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
                if stat == 'drop_probability':
                    average_data[detector][map_name][stat] += players_data[nick][map_name][stat] * additional_dict[nick]['weight']
                else:
                    average_data[detector][map_name][stat] += float(players_data[nick][map_name][stat].strip('%')) * additional_dict[nick]['weight']
                if nick in (players_list[-1], players_list[len(players_list) // 2 - 1]):
                    average_data[detector][map_name][stat] = round(average_data[detector][map_name][stat] / (len(players_list) // 2), 2)
    differences = {}
    for map_name, stats in average_data['team_left'].items():
        differences[map_name] = {}
        total = 0
        for stat, value in stats.items():
            if stat in ('drop_probability', 'win_rate'):
                differences[map_name][stat] = round(average_data['team_left'][map_name][stat] - average_data['team_right'][map_name][stat], 2)
            else:
                differences[map_name][stat] = round(average_data['team_left'][map_name][stat] * 100 / (average_data['team_left'][map_name][stat] + average_data['team_right'][map_name][stat]) - (100 - (average_data['team_left'][map_name][stat] * 100 / (average_data['team_left'][map_name][stat] + average_data['team_right'][map_name][stat]))), 2)
            total += differences[map_name][stat]
        differences[map_name]['total'] = round(total / 3, 2)
    differences = dict(sorted(differences.items(), key=lambda k: k[1]['total'], reverse=True))

    map_list = [k for k in differences.keys()]
    stat_list = [k for k in average_data['team_left']['de_cache'].keys()]
    mega_dict = {}
    for map_name in map_list:
        mega_dict[map_name] = {'team_left': {}, 'vs': {}, 'team_right': {}}
        for side in mega_dict[map_name].keys():
            if side == 'vs':
                for stat in stat_list:
                    mega_dict[map_name][side][stat] = differences[map_name][stat]
                mega_dict[map_name][side]['total'] = differences[map_name]['total']
            else:
                for stat in stat_list:
                    mega_dict[map_name][side][stat] = average_data[side][map_name][stat]
                mega_dict[map_name][side]['total'] = '-'

    return mega_dict
