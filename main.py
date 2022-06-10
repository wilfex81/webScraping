import time
import requests
from bs4 import BeautifulSoup

print("Enter some skills that you do not have experince in: ")
notApplicableSkills = input('>')
print(f'Filtering out {notApplicableSkills}......')

def find_jobs():
    '''A simple function to scrap information  off a Job advert site'''
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ ='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if notApplicableSkills not in skills:
                '''Save the alerts created in a folder'''
                with open(f'alerts_created/{index}.txt', 'w')as f:

                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}")
                print(f"file saved as {index}.txt")

if __name__ == '__main__':
    '''Make it run every {number of times you want} to get the latest updates every time the portal is updated'''
    while True:
        find_jobs()
        break
        #commented out because it i do not require it at the moment.
        # time_wait = 10
        # print(f"Waiting {time_wait} minutes...")
        # time.sleep(time_wait * 600)
        


