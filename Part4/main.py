'''working with API'''
import sys
import requests
from bs4 import BeautifulSoup
# sys.path.append('/home/jager/Documenti/GitHub/pythonCourse')
sys.path.append('..\\pythonCourse') #when on Windows

def WebScraper():
    response = requests.get('https://stackoverflow.com/questions', timeout = 2.50)
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.select(".s-post-summary")
    questionText = [{question.select_one('.s-link').getText(),question.select_one('.s-post-summary--stats-item-number').getText()} for question in questions]
    print(type(questions[0]))
    print(f"question count : {len(questionText)}")
    for item in questionText:
        print(item)


if __name__ == '__main__':
    WebScraper()
    print("starting")
