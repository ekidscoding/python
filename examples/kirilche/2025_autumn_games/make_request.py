import requests


def make_request(site):
    response = requests.get(site)
    code = response.status_code
    headers = dict(response.headers)
    cont_type = headers.get('Content-Type', 'Default')

    if code == 200:
        if 'application/json' in cont_type:
            try:
                data = response.json()
                # print("JSON Data:", data)
                print(data.keys())
                print(data.values())
                print(data.items())

                data["Hello"] = "Hello World!"

                for key, value in data.items():
                    print(f"{key=}, {value=}")
            except requests.exceptions.JSONDecodeError:
                print("Error decoding JSON. Raw response:", response.content.decode('utf-8'))
        else:
            print("Response is not JSON. Content-Type:", cont_type)
            print("Raw response:", response.text)
    else:
        print(f"Request failed with status code: {code}")
        print("Raw response:", response.text)


if __name__ == '__main__':
    make_request('https://flask-render-lqjb.onrender.com/')
