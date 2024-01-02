import requests
import json


def main():
    url = "https://udemy_deploy_api-1-s1723049.deta.app/"
    # url = "http://127.0.0.1:8000/"
    data = {"x": 4, "y": 3}
    res = requests.post(
        url, json.dumps(data), headers={"Content-Type": "application/json"}
    )
    print(res.headers)
    # print(res.json())


if __name__ == "__main__":
    main()
