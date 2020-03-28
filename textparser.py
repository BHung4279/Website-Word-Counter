import requests
import io
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_url():
    # gets the url from the user
    url = input("Enter the url: ")
    return url

def check_url_valid(url):
    parsed_url = urlparse(url)

    # boolean that holds whether or not the inputted url is valid or not
    valid = "true"

    if len(parsed_url.scheme) == 0:
        valid = "false"
    if len(parsed_url.netloc) == 0:
        valid = "false"
    return valid

def parse_website_text(url):
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

    text.replace("."," ")
    text.replace(","," ")
    text.replace("("," ")
    text.replace(")"," ")

    # dictionary that holds the words in the webpage and the number of times that word occurs
    words = {}

    # puts the text of the website in a text file
    file = io.open("text.txt", "w+", encoding = "utf-8")
    file.write(text)
    file.close()

    # reads the words in that text file and updates the dictionary
    file1 = io.open("text.txt", encoding = "utf-8")
    for word in file1.read().split():
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    file1.close()

    # iterates through the dictionary and writes to words.txt
    file2 = io.open("words.txt", "w+", encoding = "utf-8")
    for key, value in sorted(words.items(), key = lambda item: item[1], reverse = True):
        file2.write(key + ": " + str(value) + "\n")
    file2.close()

def main():
    url = get_url()
    valid = check_url_valid(url)
    if(valid == "true"):
        parse_website_text(url)
    else:
        print("Invalid URL")

if __name__ == "__main__":
    main()
