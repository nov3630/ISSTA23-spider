import time
import numpy as np
import requests
from lxml import etree
from pprint import pprint
import pandas as pd


main_page_url = 'https://conf.researchr.org/track/issta-2023/issta-2023-technical-papers#event-overview'
page_text = requests.get(main_page_url).text
tree = etree.HTML(page_text)
model_li = tree.xpath('//tr/td[2]/a[1]/@data-event-modal')

model_url = 'https://conf.researchr.org/eventDetailsModalByAjaxConferenceEdition'
for i in range(len(model_li)):
    data = {
        'form_131600131703c411e65b13378d08eb1f6672b5a0259': 1,
        'context': 'issta-2023',
        'ae03f7f6f951d515a297b161e922205d': model_li[i],
        'eventDetailsModalByAjaxConferenceEdition_ia0_3c411e65b13378d08eb1f6672b5a0259': 1,
        '__ajax_runtime_request__': 'event-modal-loader',
    }
    res = requests.post(model_url, data=data).json()
    abstract_html = res[0]['value']
    abstract_tree = etree.HTML(abstract_html)
    abstract_li = abstract_tree.xpath('//div[@class="bg-info event-description"]/p/text()')
    with open(f'abstract/{i}.txt', 'w', encoding='utf-8') as fp:
        fp.write(''.join(abstract_li))
    # break

