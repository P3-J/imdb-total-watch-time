import csv
from bs4 import BeautifulSoup
import requests

#fix

show_data_list = []
watch_time = 0

# create simple list with required data
with open("ratings.csv",newline="") as csvvfile:
    csv_reader = csv.reader(csvvfile,delimiter=",")
    for row in csv_reader:
        show_data_list.append([row[4],row[5],row[7]])

print(show_data_list)
show_data_list.pop(0)

# set the right watchtime for series
for i in show_data_list:
    if str(i[1]) == "tvSeries" or str(i[1]) == "tvMiniSeries":
        if i[2] != "":
            url = str(i[0])
            response = requests.get(url)
            soup = BeautifulSoup(response.text,"html.parser")

            for x in soup.select("#title-overview-widget > div.vital > div.button_panel.navigation_panel > a > div > div > span"):
                episode_amount_nr = x.get_text().split()[0]
                print("processing")
                i[2] = int(i[2])*int(episode_amount_nr)
                print(i[2])
        else:
            i[2] = 0
    
# loop and give answer.
for i in show_data_list:
    watch_time += int(i[2])
print(watch_time/60,"; is your watch time in hours")


        



