from bs4 import BeautifulSoup
import requests

r  = requests.get("http://oldhindilyrics.com/singers-list/")
data = r.text

soup = BeautifulSoup(data, "html.parser" )

singer_raw = []
singers_song = {}

#clean the data for a href and then one containing wwww.oldhindilyrics.com cause only singers web link have this string, makes easier to sort
for x in  soup.find_all('a'):
    link = x.get('href')
    if link[:10] == 'http://www':
        singer_raw.append(link)

#remove first 2 unimportant data links leaving only singer lists
singer_raw.pop(0)
singer_raw.pop(0)

#create dictionary for singer name and its link
for x in singer_raw:
    var = x.split('/')
    singers_song[var[-1]] = x        #-1 to fetch singer's name from last words of the url after spliting the link at '/' ##update you should use dict comprehension

#design a switch case to showcase our singers
print '\n'+'************************* Lyrics Of The Legends *************************' + '\n\n'
print '========================== Singers List =========================='
print '\n\n'.join([keys for keys in singers_song]) + '\n' #print keys i.e singers of our dictionary

singer1 = raw_input('enter a name from the given  list : ')
print '\n Searching the web for '+ singers_song.get(singer1) + ' ... .. .'
name = singer1
singer1 = singers_song.get(singer1)


#beautiful soup the singers url to get song lists

def singers_url_to_songs_url(singer1):
        songs = []
        r1 = requests.get(singer1)
        data1 = r1.text
        soup1 = BeautifulSoup(data1, "html.parser")
        for x in  soup1.find_all('a'):
                link1 = x.get('href')
                if link1[:10] == 'http://www':
                        songs.append(link1)  
        #remove first 2 unimportant data links leaving only song's lists
        songs.pop(0)
        songs.pop(0)
        return songs


#create a dictionary for the songs scraped for the singer
songs_url_raw = [x for x in singers_url_to_songs_url(singer1)]
song_lyrics={}

for x in songs_url_raw:
        var = x.split('/')
        song_lyrics[var[-1]] = x


#showcase the songs for the selected singer
print '\n'+'************************* Songs For '+ name.upper() + ' *************************' + '\n\n'
print '==========================  List =========================='
print '\n\n'.join([keys for keys in song_lyrics][:8]) + '\n' #print keys i.e singers of our dictionary  # [:8] logic that prints only 8 song names so that it is easily readable

song_name = raw_input('enter your song name (copy and paste here) : ')
song_url = song_lyrics.get(song_name,'nothing')

#Beautiful soup the song_url to get lyrics


def songs_url_to_song_lyrics(song_url):
        
        r2 = requests.get(song_url)
        data2 = r2.text
        soup1 = BeautifulSoup(data2, "html.parser")
        lyrics_raw_data = [ str(link1) for link1 in  soup1.find_all('p')] #needs to convert all elements of soup to string so that slicing can be performed or else soup is non hasable
        lyrics_raw_data.pop(0) #removing unwanted tag data
        lyrics_clean_1 = [x.replace('<p>','') for x in lyrics_raw_data if x[:3] == '<p>']  #to diffrentiate between lyrics and other links and tags using <p> coz some use <p style ... 
        lyrics_clean_2 = [x.replace('</p>','') for x in lyrics_clean_1]
        return '\n\n'.join([x.replace('<br/>' , '') for x in lyrics_clean_2])


print '\n\n ******************************* lyrics for '+ song_name +' ********************************** \n\n'
print songs_url_to_song_lyrics(song_url)
