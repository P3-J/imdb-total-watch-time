import csv
from bs4 import BeautifulSoup
import requests
import time
from lxml import etree

def reader():
    watch_time = 0
    progress = 0

    with open("rating_folder/ratings.csv",newline="") as csvvfile:
        csv_reader = csv.reader(csvvfile,delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            progress += 1
            print(f"Currently processing show; {progress}")
            watch_time += process_row(row[4],row[5],row[7])
    
    print(f"{round(watch_time/60)}; is your watch time in hours")

def process_row(url : str, title_type : str, runtime : int) -> int:
   
    if title_type != "tvSeries" and title_type != "tvMiniSeries":
        if runtime == "":
            return 0
        return int(runtime)
    else:
        return series_runtime_scrape(url, runtime)

def series_runtime_scrape(url : str, runtime : int) -> int:

    print("tvshow, ", url)
    
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))

    response_list = dom.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[2]/div[1]/a/h3/span[2]')

    if len(response_list) > 0:
        return int(response_list[0].text) * int(runtime)
    return 0
  
def main():
    reader()

if __name__ == "__main__":
    main()



