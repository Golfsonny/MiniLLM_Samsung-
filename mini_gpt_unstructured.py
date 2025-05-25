import os
from bs4 import BeautifulSoup
import requests
import sys


'''UNSTRUCTURED'''

#If there are no Structured Json data at the "Data" directory, then overwrite response.text on edge.json
#EX: data/edge.json -> data/response.text
def get_unstructured_data(url: str,st_file_path: str)->None:
    response = requests.get(url)
    #convert byte data to utf-8 from the web-server
    Samsung_html_content = response.text

    with open(st_file_path, "w") as f:
        f.write(Samsung_html_content)


def get_samsung_urls():

    #Unstructured Data from the URL
    url = "https://www.samsung.com/uk/smartphones/galaxy-s25-edge/buy/"
    
    #Unstructured Data saved as json: data/edge.html
    #Base path that the data from the url will be saved.
    current_path = os.path.dirname(__file__)

    #Save data from the url into HERE!
    html_file_path = os.path.join(current_path, "data/edge.html")

    #get Unstructured Data
    if not os.path.exists(html_file_path):
        get_unstructured_data(url, html_file_path)
        #After: html_file_path = ~~ data/response.text

    #Exist Structured Data
    with open(html_file_path, "r") as f:
        json_content = f.read()
    
    #Strip HTML tags and cleanly collect only text
    soup = BeautifulSoup(json_content, "html.parser")

    content = ""

    for item in soup:

        #item = utf-8
        #if item.text is empty or None, return False
        if item.text:
            '''
            item.text.split() → ["Galaxy", "S25", "Edge"]
            " ".join(...) → "Galaxy S25 Edge"
            '''
            chunk = " ".join(item.text.split())
            chunk += "\n"
            content += chunk
    return content



def main():
    get_samsung_urls()

if __name__ == "__main__":
    main()

    


