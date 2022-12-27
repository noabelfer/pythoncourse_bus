import time
from concurrent.futures import ThreadPoolExecutor

import requests
import pprint



def country_id_name (name) -> tuple:
    name = name.lstrip()
    response = requests.get(NATION_URL, params={'name':n})
    if response.status_code >= 400:
        raise Exception(f"error {response.status_code}")
    else:
        country_prob = response.json()
        country_prob = response.json()
        country_max_p = sorted(country_prob['country'], key=lambda x: x['probability'])[-1]
        code = country_max_p['country_id']
        country_url = f"https://restcountries.com/v3.1/alpha/{code}"
        if response.status_code >= 400:
            raise Exception(f"error {response.status_code}")
        if requests.get(country_url).status_code < 400:
            a = requests.get(country_url)
            js_country = a.json()
            # pprint.pprint(js_country)
            name_c = js_country[0]['name']['common']
            cnt = js_country[0]['region']
            lng = js_country[0]['languages']
    return (name_c, code, cnt, lng)




    # executer = ThreadPoolExecutor(max_workers=10)
    # futures = []
    # if response.status_code < 400:
    #     country_prob = response.json()
    #     country_max_p = sorted(country_prob['country'], key = lambda x:x['probability'])[-1]
    #     code = country_max_p['country_id']



#country_prob['probability']
if __name__ == '__main__':
    names = input("type your names: ")
    name = names.split(',')
    start = time.time()
    NATION_URL = "https://api.nationalize.io"
    end = time.time()
    for n in name:
        print(country_id_name(name))
    print(end-start)


    # names = name.split(',')
