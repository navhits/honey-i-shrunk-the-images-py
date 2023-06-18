import requests

def get_data(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    url = input("Enter a JSON endpoint: ")
    print(get_data(str(url)))
