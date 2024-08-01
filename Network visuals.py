#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: MahirYazar
"""

import pandas as pd
import os
import plotly.graph_objects as go
import plotly.io as pio
#pio.renderers.default = 'svg'
pio.renderers.default = 'browser'


os.chdir('/Users/myazar/Desktop/Procedural_Justice_2024')

data = pd.read_csv('C40.csv')


data_inc = data[data['Procedural justice '] == '1']
data_exc = data[data['Procedural justice '] != '1']


stage_1 = data_inc[['City', 'Policy choice', 'What that entails?']].groupby(
    ['Policy choice', 'What that entails?']).size().reset_index(name='CityCount')

group_ct = stage_1.groupby('Policy choice')[
    'CityCount'].sum().reset_index(name='group_ct')

stage_1 = stage_1.merge(group_ct, 'left', on='Policy choice')

stage_1 = stage_1.sort_values(by='group_ct', ascending=False)


labels = stage_1['Policy choice'].to_list(
) + stage_1['What that entails?'].to_list()

labels_dict = {index: label for index, label in enumerate(labels)}

lables_dict_reverse = {value: key for key, value in labels_dict.items()}


stage_1['colors'] = ['plum', 'turquoise',
                     'lightgreen', 'lightsalmon',
                     'wheat', 'lavender']

color_dict_nodes = labels_dict.copy()

color_dict_nodes = {0: 'plum',
                    1: 'plum',
                    2: 'turquoise',
                    3: 'orange',
                    4: 'orange',
                    5: 'lightgreen',
                    6: 'wheat',
                    7: 'red',
                    8: 'lightsalmon',
                    9: 'blue',
                    10: 'maroon',
                    11: 'darkgreen'}


labels_dict = {0: 'Mobility oriented policy',
               1: 'Mobility oriented policy',
               2: 'Green infrastructure <br>& energy oriented policy',
               3: 'Renewable energy <br>oriented policy',
               4: 'Renewable energy <br>oriented policy',
               5: 'Green infrastructure <br>& mobility oriented policy',
               6: 'Expand cycling mobility <br>for the benefit of low-income communities',
               7: 'Increase urban bicycle infrastructure ',
               8: 'Access to green space <br>and alternative energy for low-income household',
               9: 'Alternative energy for low-income household',
               10: 'Implement community solar energy <br>in informal settlements',
               11: 'Increase green space & green mobility '}


fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=50,
        thickness=25,
        line=dict(color="plum", width=0.1),
        label=['<b>' + value + '<b>' for key, value in labels_dict.items()],
        color=[value for key, value in color_dict_nodes.items()]
    ),
    link=dict(
        # indices correspond to labels, eg A1, A2, A1, B1, ...
        source=[lables_dict_reverse[row['Policy choice']]
                for index, row in stage_1.iterrows()],
        target=[lables_dict_reverse[row['What that entails?']]
                for index, row in stage_1.iterrows()],
        value=[row['CityCount'] for index, row in stage_1.iterrows()],
        color='lightgrey'
    ))])
#[row['colors'] for index, row in stage_1.iterrows()]
fig.update_layout(font_size=16,
                  font_color='black')
fig.show()

fig.write_html("inclusive_new.html")


data = pd.read_csv('C40.csv')


data_inc = data[data['Procedural justice '] == '0']
data_exc = data[data['Procedural justice '] != '0']


stage_1 = data_exc[['City', 'Policy choice', 'What that entails?']].groupby(
    ['Policy choice', 'What that entails?']).size().reset_index(name='CityCount')

group_ct = stage_1.groupby('Policy choice')[
    'CityCount'].sum().reset_index(name='group_ct')

stage_1 = stage_1.merge(group_ct, 'left', on='Policy choice')

stage_1 = stage_1.sort_values(by='group_ct', ascending=False)


labels = stage_1['Policy choice'].to_list(
) + stage_1['What that entails?'].to_list()

labels_dict = {index: label for index, label in enumerate(set(labels))}

lables_dict_reverse = {value: key for key, value in labels_dict.items()}


stage_1['colors'] = ['lavender', 'turquoise',
                     'plum', 'lightsalmon',
                     'wheat',  'tomato', 'lightgreen'
                     ]


color_dict_nodes = {0: 'pink',
                    1: 'plum',
                    2: 'orange',
                    3: 'red',
                    4: 'darkgreen',
                    5: 'purple',
                    6: 'saddlebrown',
                    7: 'lightsalmon',
                    8: 'wheat',
                    9: 'lightgreen',
                    10: 'turquoise'}

labels_dict = {0: 'Provide charging infrastructure <br>for the residential community',
               1: 'Mobility oriented policy',
               2: 'Renewable energy oriented policy',
               3: 'Increase urban bicycle infrastructure ',
               4: 'Increase green space <br>& green mobility ',
               5: 'Target low-energy mobility zone development',
               6: 'Target solar energy expansion in buildings',
               7: 'Access to green space <br>and alternative energy for low-income household',
               8: 'Expand cycling mobility <br>for the benefit of low-income communities',
               9: 'Green infrastructure <br>& energy oriented policy',
               10: 'Green infrastructure <br>& mobility oriented policy'}

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=50,
        thickness=25,
        line=dict(color="black", width=0.1),
        label=['<b>' + value + '<b>' for key, value in labels_dict.items()],
        color=[value for key, value in color_dict_nodes.items()]
    ),
    link=dict(
        # indices correspond to labels, eg A1, A2, A1, B1, ...
        source=[lables_dict_reverse[row['Policy choice']]
                for index, row in stage_1.iterrows()],
        target=[lables_dict_reverse[row['What that entails?']]
                for index, row in stage_1.iterrows()],
        value=[row['CityCount'] for index, row in stage_1.iterrows()],
        color='lightgray'
    ))])

fig.update_layout(font_size=16,
                  font_color='black')
fig.show()

fig.write_html("non-inclusive_new.html")
