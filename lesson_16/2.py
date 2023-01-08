import base64

url = "https://cartasense-coldchain.com/"
url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
print(url_id)
