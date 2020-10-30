#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:37:34 2020

@author: apple
"""

import requests
import json

def get_movies_from_tastedive(search):
    base_url = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = search
    param['type'] = 'movies'
    param['limit'] = 5
    
    req = requests.get(base_url, params = param)
    return json.loads(req.text)


def extract_movie_titles(search):
    return [item['Name'] for item in search['Similar']['Results']]
    
    
    
def get_related_titles(lst_movies):
    related_lst = []
    for movie in lst_movies:
        related_lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
        
    return list(set(related_lst))

def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    
    req = requests.get(base_url, params = param)
    
    return json.loads(req.text)


def get_movie_rating(title_dictionary):
    rating = title_dictionary['Ratings']
    for dictionary in rating:
        if dictionary['Source'] =="Rotten Tomatoes":
            return int(dictionary['Value'][:-1])
    return 0



def get_sorted_recommendations(lst_movies):
    related_lst = get_related_titles(lst_movies)
    movie_dictionary = {}
    for movie in related_lst:
        rating = get_movie_rating(get_movie_data(movie))
        movie_dictionary[movie] = rating
    return [movie[0] for movie in sorted(movie_dictionary.items(), key=lambda movie: (movie[1], movie[0]), reverse=True)]

