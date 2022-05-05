import os
import urllib.request


if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
    urllib.request.urlretrieve('https://www.wordfrequency.info/samples/lemmas_60k.txt',
                               os.path.join(data_dir, 'lemmas_60k.txt'))
