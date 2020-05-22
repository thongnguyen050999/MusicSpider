import requests

def download(url):
    r = requests.get(url,allow_redirects=True)
    with open('file.midi','wb') as f:
        f.write(r.content)

download('https://freemidi.org/getter-10887')