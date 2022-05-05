import os
import pandas as pd
from googletrans import Translator
from tqdm import tqdm


if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
    data = pd.read_csv(os.path.join(data_dir, 'lemmas_60k.txt'),
                       sep='\t',
                       index_col=False,
                       usecols=['lemma', 'freq'],
                       skiprows=8)

    translator = Translator()
    translations = []
    for word in tqdm(data['lemma'].to_numpy()):
        translations.append(translator.translate(word, src='en', dest='ru').text)
    data['translation'] = pd.Series(translations)
    print(data.head())

    data.to_csv(os.path.join(data_dir, 'translated.csv'), index=False)
    data.iloc[:10000, :].to_csv(os.path.join(data_dir, 'translated_10k.csv'), index=False)
    data.iloc[:100, :].to_csv(os.path.join(data_dir, 'translated_100.csv'), index=False)
