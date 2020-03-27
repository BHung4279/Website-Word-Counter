import requests
from bs4 import BeautifulSoup

# gets the url from the user
url = input("Enter the url: ")

# response text of request
res = requests.get(url)
# actual content of the web page
page = res.content
# parsed webpage (through BeautifulSoup)
soup = BeautifulSoup(page, 'html.parser')

for script in soup(["script", "style"]):
    script.extract()

# the text
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("   "))
text = '\n'.join(chunk for chunk in chunks if chunk)

# dictionary that holds the words in the webpage and the number of times that word occurs
words = {}

# puts the text of the website in a text file
file = open("text.txt", "w+")
file.write(text)
file.close()

# reads the words in that text file and updates the dictionary
file1 = open('text.txt')
for word in file1.read().split():
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
file1.close()

# iterates through the dictionary and writes to words.txt
file2 = open("words.txt", "w+")
for key, value in sorted(words.items(), key = lambda item: item[1], reverse = True):
    file2.write(key + ": " + str(value) + "\n")
file2.close()