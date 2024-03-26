'''working with API'''
import sys
import requests
import json
from bs4 import BeautifulSoup
# sys.path.append('/home/jager/Documenti/GitHub/pythonCourse')
sys.path.append('..\\pythonCourse') #when on Windows
from Classes.FileManagement import FileManagement


def WebScraper():
    response = requests.get('https://stackoverflow.com/questions', timeout = 2.50)
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.select(".s-post-summary")
    questionText = {question.select_one('.s-link').getText() : question.select_one('.s-post-summary--stats-item-number').getText() for question in questions}
    print(type(questionText))
    print(f"question count : {len(questionText)}")
    path = "Files/FileManagement"
    fileManager = FileManagement(path)
    fileManager.WriteDictToJsonFile(questionText,"SO")


if __name__ == '__main__':
    WebScraper()
    print("starting")
