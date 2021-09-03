#!/bin/python3
import requests


def consume_api_json_id(url, beg_id=1):
    req_obj = requests.get(url + str(beg_id))
    pickle_me = []
    while req_obj.status_code == 200:
        print(f'consuming api, id = {beg_id}')
        pickle_me.append(req_obj.json())
        beg_id += 1
        req_obj = requests.get(url + str(beg_id))
    return pickle_me


if __name__ == '__main__':
    import sys
    import pickle
    api_url = sys.argv[1]
    fname = sys.argv[2]
    pickle_me = consume_api_json_id(api_url)
    with open(fname, 'wb') as fb:
        pickle.dump(pickle_me, fb)
