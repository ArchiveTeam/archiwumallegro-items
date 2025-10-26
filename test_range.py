import json
import multiprocessing.dummy
import random
import sys

import requests


def test_id(i: int) -> bool:
    while True:
        try:
            response = requests.head('https://archiwum.allegro.pl/oferta/-i{}.html'.format(i), timeout=10, allow_redirects=False)
            break
        except Exception:
            print('Retrying', i)
            pass
    print(i, response)
    if response.status_code == 308:
        return i, True
    if response.status_code == 404:
        return i, False
    raise


def main(total: int):
    results = {}
    with multiprocessing.dummy.Pool(100) as p:
        for i, result in p.map(
            test_id,
            [int(random.random()*17318800938) for _ in range(total)]
        ):
            results[i] = result
    with open('results.json', 'w') as f:
        json.dump(results, f)


if __name__ == '__main__':
    main(int(sys.argv[1]))

