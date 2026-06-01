import json
import requests

def artists(artistname):
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ artistname)
    data = response.json()
    for result in data["results"]:
        print(result["trackName"])
    #This function searches for artists that have a song in the results
def searchartist(songname):
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ songname)
    data = response.json()
    for result in data["results"]:
        print(result["artistName"], result["collectionName"])
    #This function searches for songs an artist produced
def search():
    k = input("Do you wnat song or artist")
    if k.lower() == "song":
        m = input("Enter Artist or Band to get their songs")
        searchartist(m)
    elif k.lower() == "artist":
        x = input("Enter songname")
        artists(x)
    else:
        print("wrong option")
    #This function is responsible for decision making by collecting user input and using it using the rules
search()
# This is my second project in my Havard c50 lesson of libraries