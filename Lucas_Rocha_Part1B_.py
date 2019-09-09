from selenium import webdriver
import time as t
from datetime import datetime
import pandas as pd
import re
from pathlib import Path


pd.options.mode.chained_assignment = None  # default='warn'

def driver(name):
    # Driver Options for using selenium (Chromium or Firefox)
    if name == 'Firefox':
        return webdriver.Firefox(executable_path=r'.\drivers\geckodriver.exe')
    elif name == 'Chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-features=NetworkService")
        return webdriver.Chrome(executable_path=r'.\drivers\chromedriver.exe', options=chrome_options)
    else:
        return 'No driver found'


class WikiTable:
    # Class to instantiate request and implement retrying routine based on status code
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://en.wikipedia.org/wiki/List_of_production_battery_electric_vehicles_(table)'
        self.box = 'container main-section'
        self.table = '//*[@id="mw-content-text"]/div/table[4]'

    def navigate(self):
        print('* ------------ Starting navigation ----------------- ')
        url = f'{self.url}'
        try:
            self.driver.get(url)
            t.sleep(10)
            print('* ------------ Page has loaded --------------------- ')
            return 200
        except:
            return 500

    def get_table_rows(self):
        return self.driver.find_elements_by_tag_name('tr')

    def end_process(self):
        print('* ------------ Process finished -------------------- ')
        return self.driver.close()


def iterator():

    print('* ------ This project uses Selenium. See README file for more info -------')
    today = datetime.now().strftime('%Y/%m/%d')
    filename = Path('.') / 'data' / 'Lucas_Rocha_Part1B_.csv'

    print(f'* ------------ Crawling wikipedia data table - {today} ------------------- ')
    crawler = WikiTable(driver=driver('Chrome'))

    response = crawler.navigate()
    print('Request response status code: ', response)
    elements = crawler.get_table_rows()

    print('* ------------ Table crawled ------------------------ ')

    aux_list = []

    for row in elements:
        row_list = []
        col = row.find_elements_by_tag_name('td')
        names = row.find_elements_by_tag_name('th')
        for header in names:
            row_list.append(header.text)
        for item in col:
            row_list.append(item.text)
        aux_list.append(row_list)

    print('Clean dataset')
    clean_list = aux_list[3:]
    test_list = []
    for row in clean_list:
        row_list = []
        for item in row:
            auxString = item.replace('\n', '')
            row_list.append(auxString)
        test_list.append(row_list)

    # TODO: Add more sofisticated language processing to identify
    #       patterns in crawled data to improve mining quality.
    final_list = []
    for item in test_list:
        if len(item) == 7:
            final_list.append(item)

    # Subselect data for dataframe creation
    namelist = [item[0] for item in final_list]
    comments = [re.sub(r'\[(\d+)\]', '', item[1]) for item in final_list]
    prod_years = [item[2] for item in final_list]
    prod_num = [re.sub(r'\[(\d+)\]', '', item[3]) for item in final_list]
    top_speed = [re.sub(r'\[(\d+)\]', '', item[4]) for item in final_list]
    cost = [re.sub(r'\[(\d+)\]', '', item[5]) for item in final_list]
    range = [re.sub(r'\[(\d+)\]', '', item[6]) for item in final_list]

    # String replacement
    namelist = [item.replace(',', '') for item in namelist]
    comments = [item.replace(',', '') for item in comments]
    prod_years = [item.replace(',', '') for item in prod_years]
    prod_num = [item.replace(',', '') for item in prod_num]
    top_speed = [item.replace(',', '') for item in top_speed]
    cost = [item.replace(',', '') for item in cost]
    range = [item.replace(',', '') for item in range]
    namelist = [item.replace(';', '') for item in namelist]
    comments = [item.replace(';', '') for item in comments]
    prod_years = [item.replace(';', '') for item in prod_years]
    prod_num = [item.replace(';', '') for item in prod_num]
    top_speed = [item.replace(';', '') for item in top_speed]
    cost = [item.replace(';', '') for item in cost]
    range = [item.replace(';', '') for item in range]

    df_aux = pd.DataFrame(data={'Name': namelist,
                                'Comments': comments,
                                'Production_years': prod_years,
                                'Number_produced': prod_num,
                                'Top_Speed': top_speed,
                                'Cost': cost,
                                'Range': range})

    df = df_aux[1:]

    # Final missing data treatment
    df['Comments'].replace('', 'NaN', regex=True, inplace=True)
    df['Production_years'].replace('', 'NaN', regex=True, inplace=True)
    df['Top_Speed'].replace('', 'NaN', regex=True, inplace=True)
    df['Cost'].replace('', 'NaN', regex=True, inplace=True)
    df['Cost'].replace('-', 'NaN', regex=True, inplace=True)
    df['Range'].replace('', 'NaN', regex=True, inplace=True)

    # Saving dataframe
    df.to_csv(filename, sep=';', index=False, encoding='utf8')

    print("* ------------ Saving final dataframe at 'data' folder inside root project folder\n"
          "* ------------ Read CSV output file encoded as default UTF-8. Column separator type = ';' ")
    crawler.end_process()


# Main Routine call
iterator()
print('* ------------ Closing App ------------------------')
t.sleep(20)
