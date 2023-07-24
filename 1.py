import time
import numpy as np
import requests
from lxml import etree
from pprint import pprint
import pandas as pd


main_page_url = 'https://conf.researchr.org/track/issta-2023/issta-2023-technical-papers#event-overview'
profile_url = 'https://2023.issta.org/profile/'
doi_url = 'https://doi.org/'
pdf_url = 'https://dl.acm.org/doi/pdf/'


page_text = requests.get(main_page_url).text
tree = etree.HTML(page_text)
title_li = tree.xpath('//tr/td[2]/a[1]/text()')
num = len(title_li)
first_author_li = tree.xpath('//tr/td[2]/div/a[1]/text()')
first_author_profile_url_li = tree.xpath('//tr/td[2]/div/a[1]/@href')
all_author_li = []
for i in range(num):
    all_author = tree.xpath(f'//tr[{i+1}]/td[2]/div/a/text()')
    all_author_li.append(all_author)
doi_li = tree.xpath('//tr/td[2]/a[2]/@href')

country_li = []
affiliation_li = []

count = 0
# 作者主页
for profile_url in first_author_profile_url_li:
    page_text = requests.get(profile_url).text
    tree = etree.HTML(page_text)
    profile_item_heading = tree.xpath('//span[@class="profile-item-heading"]/text()')
    profile_item = tree.xpath('//div[@class="profile-item"]/text()')
    country_idx = profile_item_heading.index('Country:')
    affiliation_idx = profile_item_heading.index('Affiliation:')
    country = tree.xpath(f'//div[@class="profile-item"][{country_idx+1}]/text()')[0]
    affiliation = tree.xpath(f'//div[@class="profile-item"][{affiliation_idx + 1}]/text()')[0]
    country_li.append(country)
    affiliation_li.append(affiliation)
    # print(country, affiliation, profile_url)

    count += 1
    if count % 10 == 0:
        time.sleep(30)

df = pd.DataFrame(
    [
        title_li,
        first_author_li,
        [', '.join(all_author) for all_author in all_author_li],
        country_li,
        affiliation_li,
        doi_li,
        [doi.replace(doi_url, pdf_url) for doi in doi_li],
    ],
)
df = df.T
df.columns = ['标题', '一作', '作者', '国家', '单位', 'DOI', 'PDF']
df.to_csv('ISSTA23.csv', index=False)
df.to_excel('ISSTA23.xlsx', index=False)
