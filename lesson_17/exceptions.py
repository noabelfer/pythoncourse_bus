
class VTmnger:
    def __init__(self):
        pass

    def get_url_anal(self, url):
        response = requests.get(url)
        if response.status_code > 400:
            raise Exception("cannot get to api")

