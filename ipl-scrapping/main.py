import json

from selenium import webdriver
from time import sleep

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.iplt20.com/")

# sleep(2)
total_teams = 8
teams = []
for item in range(0, total_teams):
    team = {}
    score_container = driver.find_element_by_class_name(f"team{item}")
    name = score_container.find_element_by_css_selector(".team .ap-team-wrp a").text
    played = score_container.find_element_by_css_selector(".pld .ap-team-name").text
    netrr = score_container.find_element_by_css_selector('.netrr .ap-team-name').text
    pts = score_container.find_element_by_css_selector('.pts .ap-team-name').text
    team['name'] = name
    team['played'] = played
    team['netrr'] = netrr
    team['pts'] = pts
    teams.append(team)

# write this data to json file

with open("teams_stats.json", "w") as file:
    file.write(json.dumps({"teams": teams}))