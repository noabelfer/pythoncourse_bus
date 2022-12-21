import requests
import pprint
if __name__ == '__main__':
    name = input("type your name: ")
    NATION_URL = "https://api.nationalize.io"
    response = requests.get(NATION_URL, params={'name':name})
    if response.status_code < 400:
        country_prob = response.json()
    country_max_p = sorted(country_prob['country'], key = lambda x:x['probability'])[-1]
    code = country_max_p['country_id']

    country_url = f"https://restcountries.com/v3.1/alpha/{code}"
    if requests.get(country_url).status_code < 400:
        a = requests.get(country_url)
        js_country = a.json()
        # pprint.pprint(js_country)
        name_c = js_country[0]['name']['common']
        cnt = js_country[0]['region']
        lng = js_country[0]['languages']
        pprint.pprint(lng)


#country_prob['probability']
