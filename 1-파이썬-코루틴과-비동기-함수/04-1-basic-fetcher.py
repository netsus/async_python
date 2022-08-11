import requests
import aiohttp


def fetcher(session, url):
    response = session.get(url)
    return response.text

def main():
    urls = ["https://naver.com","https://google.com","https://instagram.com"]

    with requests.Session() as sess:
        result = [fetcher(sess, url) for url in urls]
        print(result)

if __name__=="__main__":
    main()