from bs4 import BeautifulSoup
import requests
 

r2 = requests.get('http://oldhindilyrics.com/Chale_Aaj_Tum_Jahan_Se/')
data2 = r2.text
soup1 = BeautifulSoup(data2, "html.parser")
lyrics_raw_data = [ str(link1) for link1 in  soup1.find_all('p')] #needs to convert all elements of soup to string so that slicing can be performed or else soup is non hasable
lyrics_raw_data.pop(0) #removing unwanted tag data
lyrics_clean_1 = [x.replace('<p>','') for x in lyrics_raw_data if x[:3] == '<p>']  #to diffrentiate between lyrics and other links and tags using <p> coz some use <p style ... 
lyrics_clean_2 = [x.replace('</p>','') for x in lyrics_clean_1]
print '\n\n'.join([x.replace('<br/>' , '') for x in lyrics_clean_2])
