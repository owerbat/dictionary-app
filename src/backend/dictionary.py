from multiprocessing.sharedctypes import Value
import numpy as np
import pandas as pd


class Dictionary:
    def __init__(self, translated_filename: str) -> None:
        self.translated = pd.read_csv(translated_filename)
        self.en_to_ru = self._make_dict('en', 'ru')
        self.ru_to_en = self._make_dict('ru', 'en')

    def _make_dict(self, key_label: str, value_label: str):
        result = {}
        for _, row in self.translated.iterrows():
            try:
                result[row[key_label]].append(row[value_label])
            except KeyError:
                result[row[key_label]] = [row[value_label],]
        return result

    def get_random_word(language: str = 'en'):
        if language not in ['en', 'ru']:
            raise ValueError(f"`language` parameter must be in ['en', ru'], got {language}")
