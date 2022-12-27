import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor, wait

import requests
import pprint



def country_id_name (name) -> tuple:
    try:
        name = name.lstrip()
        response = requests.get(NATION_URL, params={'name':name})
        if response.status_code >= 400:
            print('ppppp')
            raise ValueError(f"error {response.status_code}")
        else:
            country_prob = response.json()
            country_prob = response.json()
            country_max_p = sorted(country_prob['country'], key=lambda x: x['probability'])[-1]
            # print(country_max_p)
            code = country_max_p['country_id']
            country_url = f"https://restcountries.com/v3.1/alpha/{code}"
            if response.status_code >= 400:
                print('papapapa')
                raise Exception(f"error {response.status_code}")
            if requests.get(country_url).status_code < 400:
                a = requests.get(country_url)
                js_country = a.json()
                # pprint.pprint(js_country)
                name_c = js_country[0]['name']['common']
                cnt = js_country[0]['region']
                lng = js_country[0]['languages']
            # print(name_c)
            # print (name, name_c)
            return(name, name_c)

    except Exception:
        print(f"unknown exception {name}")
        return None



#country_prob['probability']
if __name__ == '__main__':
    with open('names.txt', 'r') as r:
        content = r.read()
        # names = input("type your names: ")
    name = content.split(', ')

    # print(name)
    executer = ThreadPoolExecutor(max_workers=100)
    futures = []
    start = time.time()
    NATION_URL = "https://api.nationalize.io"
    # country_id_name('noa')

    for n in name:
        future = executer.submit(country_id_name,n)
        futures.append(future)


    done, not_done = wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")

    with open("names_country.txt", "w") as outfile:
        for i,f in enumerate(concurrent.futures.as_completed(futures)):
            print(i)
            print(f.result())
            outfile.write(str(f.result()))
    outfile.close()

    end = time.time()

    print(end-start)

