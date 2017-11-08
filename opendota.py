import sys
import os

import requests
import pandas
import matplotlib.pyplot as plt


def query_opendota(sql):
    resp = requests.get('https://api.opendota.com/api/explorer', params={'sql': sql})
    data = resp.json()
    if resp.status_code == 400 and data is not None:
        sys.stderr.write(data['err'])
    resp.raise_for_status()
    return pandas.DataFrame.from_records(data['rows'])


def show_dota2_map(use='local'):
    if use == 'internet':
        map_img = plt.imread(
            'https://dota2.gamepedia.com/media/dota2.gamepedia.com/' +
            'b/b7/Minimap_7.07.png?version=6257157931ee53b8de74e2e0adfac8c6'
        )
    elif use == 'local':
        path_background_image = os.path.abspath(os.path.join('static', 'minimap_707.png'))
        map_img = plt.imread(path_background_image)
    plt.imshow(map_img, extent=(64, 127+64, 64, 127+64))
