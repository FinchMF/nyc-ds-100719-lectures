import csv

RS_info = []

with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
       RS_info.append(row)

def find_album(data, album):
    # return [entry for entry in data if entry ['album'] == album]
    for entry in data:
        if entry['album'] == album: 
            return entry

def album_rank(data, number):
    # return [entry for entry in data if entry['number'] == number]
    for entry in data:
        if entry['number'] == number: 
            return entry

def album_year(data, year):
    # return [entry for entry in data if entry['year'] == year]
    for entry in data:
        if entry['year'] == year: 
            return entry

def albums_between_years(data, start_year, end_year):
    years = list(range(start_year, end_year))
    return [entry for entry in data if int(entry ['year']) in years]

def albums_between_ranks(data, start_number, end_number):
    ranks = list(range(start_number, end_number))
    return [entry for entry in data if int(entry['number']) in ranks]

def all_titles(data):
    album = []
    for entry in data:
        album.append(entry['album'])
    return album

def all_artist(data):
    artist = []
    for entry in data:
        artist.append(entry['artist'])
    return artist

import collections as c

def artist_with_most_albums(data):
    artist_collection = c.Counter(all_artist(RS_info))
    max_value = max(artist_collection.values())
    return {key:value for key, value in artist_collection.items() if value == max_value}    

def most_common_words_in_titles(data):
    list_of_words = []
    titles = all_titles(RS_info)
    for title in titles:
        list_of_words.extend(title.split())
    word_collection = c.Counter(list_of_words)
    max_value = max(word_collection.values())
    return {key:value for key, value in word_collection.items() if value == max_value}    


def list_of_years(data):
    years = []
    for entry in data:
        years.append(int(entry['year']))
    return years


import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

x = list_of_years(RS_info)
plt.hist(x, bins = 7, range = (1950, 2020))

plt.xlabel('Albums by Decade')
plt.ylabel('Number of Albums')
plt.title('Album year')
plt.show()


#having trouble turing the strings into categories on the histogram



text_file = open('top-500-songs.txt', 'r')
text_row = []
for line in text_file.readlines():
     text_row.append(line.strip().split("\t"))



def convert_txt_to_dict(data):
 
    new_lines_dict = []
    
    for i in data:
        new_dict = {'rank':i[0], 'name':i[1], 'artist':i[2], 'year':i[3]}
        new_lines_dict.append(new_dict)
    return new_lines_dict

TS_500_dict = convert_txt_to_dict(text_row)


# def song_year(data,year):   using TS_500_dict
#     for entry in data:
#         if entry["year"] == year:
#             return entry

# def album_year(data, year): using RS_info
#     # return [entry for entry in data if entry['year'] == year]
#     for entry in data:
#         if entry['year'] == year: 
#             return entry

# combined functon: 

def find_by_year(data, year):
    for entry in data:
        if entry["year"] == year:
            return entry

# specific to elements in TS_500_dict

def find_song(data, name): 
    for entry in data:
        if entry['name'] == name:
            return entry

def find_artist(data, artist):
    for entry in data:
        if entry['artist'] == artist:
            return entry

def song_rank(data, rank):
    for entry in data:
        if entry['rank'] == rank:
            return entry

def all_songs(data):
    songs = []
    for entry in data:
        songs.append(entry['name'])
    return songs

# def all_artist(data): (combined function)
#     artist = []
#     for entry in data:
#         artist.append(entry['artist'])
#     return artist
           


import json

file = open('track_data.json', 'r')
json_data = json.load(file)

