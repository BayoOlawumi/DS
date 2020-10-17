import bs4
import requests
import numpy
import pandas as pd


my_webpage ='https://www.toldnetwork.com/'
server_response = requests.get(my_webpage)

# Making a beautiful soup that draw stuffs
## server_response.content
    #  Gives me all the webpage code associated with the page called

soup = bs4.BeautifulSoup(server_response.text, 'html.parser')

# soup.prettify()
# Arrange in a beautiful way

# soup.children()
# Get the children in the webpage

# soup.find_all('p')
# Find all paragraph in the soup

# soup.find_all('p', class_='container')
# searching tags by class

# soup.find_all('p', id='container')
# searching tags by id

# soup.select("div p")
# search p inside the div tag

# soup.select("div p.innertext")
# search innertext class inside the div tag

# soup.select("div p#innertext")
# search innertext class inside the div tag

# soup.find_all('span', {another_attr: "value"})
# search using another attribute

#making a list from all text in the <a> tag 
my_a_links = [
    {"name": tag.text.translate({ord(i): None for i in '\n\t'}), "link": tag.get('href')}
    for tag in soup.find_all('a')
    ]
#arrayed_list = numpy.array(my_a_links)
print("**********Find all a links on the homepage***********")
#print(my_a_links)

## Creating a csv file from the data scrapped


df = pd.DataFrame()
df['action text'] = [tag.text.lstrip('\n') for tag in soup.find_all('a')]
df['links'] = [tag.get('href') for tag in soup.find_all('a')]
print(df)

df.to_csv(r'D:\my_file.csv', index=False)

"""print("**********Find a text based on a particular tag and classname***********")
my_div_tags = soup.find("div", attrs={'class' : 'container'})
print(my_div_tags)"""






