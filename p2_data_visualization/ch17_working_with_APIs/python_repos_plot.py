#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:14:55 2019

@author: allen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:05:45 2019

@author: allen
"""

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import requests
import pygal

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Statue code:", r.status_code)

#Store API respomse in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#Explore infomarion about the repositories.
repo_dicts = response_dict['items']
print("NUmber of items:", len(repo_dicts))


#Examine the first repository.

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    description = repo_dict['description']
    if not description:
        description = "No description provided."
    plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url']
            }
    plot_dicts.append(plot_dict)
    
#Make visualization.
my_style = LS('#334455', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = -45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos_plot.svg')


"""
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'],)
"""