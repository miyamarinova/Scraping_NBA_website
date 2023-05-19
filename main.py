import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import time

#Statistic for PTS leaders during this season
SEASON_YEAR = '2022-23'

FORM_URL = "https://docs.google.com/spreadsheets/d/1H-ZOYgoTHws-w5KGPhFSa0X6irSVGjyZObfdDe7YOWI/edit?usp=sharing"
NBA_URL = f"https://www.nba.com/stats/leaders?SeasonType=Regular+Season&Season={SEASON_YEAR}"
chrome_driver_path = "/Users/miyamarinova/Development/chromedriver.exe"

#Opens recipes wevsite

driver = webdriver.Chrome()
driver.get(NBA_URL)
time.sleep(5)

#Use Beautiful Soup to parse and extract information
soup = BeautifulSoup(driver.page_source, 'html.parser')

players = soup.find_all('td', class_='Crom_text__NpR1_ Crom_stickySecondColumn__29Dwf')

table_id = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody")
rows = table_id.find_elements(By.TAG_NAME, "tr")

templist = []

for x in range(0, len(rows)):
    names_obj = rows[x].find_elements(By.TAG_NAME, "td")[1]
    name = names_obj.text
    teams_obj = rows[x].find_elements(By.TAG_NAME, "td")[2]
    team = teams_obj.text
    minutes_obj = rows[x].find_elements(By.TAG_NAME, "td")[4]
    minutes = minutes_obj.text
    points_obj = rows[x].find_elements(By.TAG_NAME, "td")[5]
    points = points_obj.text
    rebounds_obj = rows[x].find_elements(By.TAG_NAME, "td")[17]
    rebounds = rebounds_obj.text
    assists_obj = rows[x].find_elements(By.TAG_NAME, "td")[17]
    assists = assists_obj.text
    eff_obj = rows[x].find_elements(By.TAG_NAME, "td")[22]
    eff = eff_obj.text
    table_dict = {
        'Name': name,
        'Team': team,
        'Minutes': minutes,
        'Points': points,
        'Rebounds': rebounds,
        'Assists': assists,
        'Efficiency': eff
    }
    templist.append(table_dict)
    df = pd.DataFrame(templist)

    print(name, team, minutes, points, rebounds, assists, eff)
df.to_csv('table.csv')