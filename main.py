
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def main(emotion):

	if(emotion == "Sad"):
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Musical"):
		urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Family"):
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Thriller"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Fear"):
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Enjoyment"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Western"):
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Love & Romance"):
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

	response = HTTP.get(urlhere)
	data = response.text
	soup = SOUP(data, "lxml")
	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
	return title

print("WELCOME TO MOVIE RECOMMENDATION SYSTEM")

print("\nCATAGORY OF MOVIE")
print("1.Sad")
print("2.Musical")
print("3.Family")
print("4.Thriller")
print("5.Fear")
print("6.Enjoyment")
print("7.Western")
print("8.Love & Romance")

if __name__ == '__main__':
	emotion = input("Enter the Catagory of movie from the above list:")
	a = main(emotion)
	count = 0
	if(emotion == "" or emotion == "" or emotion==""):
		for i in a:
			tmp = str(i).split('>;')

			if(len(tmp) == 3):
				print(tmp[1][:-3])

			if(count > 13):
				break
			count += 1
	else:
		for i in a:
			tmp = str(i).split('>')

			if(len(tmp) == 3):
				print(tmp[1][:-3])

			if(count > 11):
				break
			count+=1
