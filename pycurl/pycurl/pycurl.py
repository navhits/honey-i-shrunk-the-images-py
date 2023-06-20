import requests

def get_data(url):
    response = requests.get(url)
    return response.content

if __name__ == "__main__":
    url = input("Enter a URL: ")
    print(get_data(str(url)))
