import os
import numpy as np
import pandas as pd
from enum import Enum

from src.backend.utils import get_dump_path, softmax


class Language(Enum):
    en = 'en'
    ru = 'ru'


class Dictionary:
    def __init__(self,
                 translated_filename: str,
                 random_state: int = None,
                 load_if_possible: bool = True):
        translated = pd.read_csv(translated_filename)
        self.en_words = translated['lemma'].to_numpy()
        self.ru_words = translated['translation'].to_numpy()
        self.freqs = translated['freq'].to_numpy()

        self.en_scores_save_path = os.path.join(get_dump_path(), 'en_scores.npy')
        self.ru_scores_save_path = os.path.join(get_dump_path(), 'ru_scores.npy')

        self._init_scores('en', load_if_possible)
        self._init_scores('ru', load_if_possible)

        if random_state is not None:
            np.random.seed(random_state)

    def _init_scores(self, language: Language, load_if_possible: bool):
        path = getattr(self, f'{language.value}_scores_save_path')

        if os.path.exists(path) and load_if_possible:
            setattr(self, f'{language.value}_scores', np.load(path))
        else:
            scores = np.zeros(self.freqs.shape[0])
            max_score = 9

            batch_size = self.scores.shape[0] // (max_score + 1)
            for i in range(max_score + 1):
                start_idx = i * batch_size
                end_idx = min((i + 1) * batch_size, self.scores.shape[0])

                score = max_score - i
                scores[start_idx: end_idx] = score

            setattr(self, f'{language.value}_scores', scores)
            self._save_scores(scores, language)

    def _save_scores(self, scores, language: Language):
        path = getattr(self, f'{language.value}_scores_save_path')
        np.save(path, scores)

    def get_random_word(self, language: Language):
        scores = getattr(self, f'{language.value}_scores')
        probas = softmax(scores)
        indices = np.arange(scores.shape[0])

        sample_idx = np.random.choice(indices, 1, p=probas)

        return self.en_words[sample_idx], self.ru_words[sample_idx], sample_idx

    def modify_score(self, idx: int, increment: int, language: Language):
        scores = getattr(self, f'{language.value}_scores')

        new_score = scores[idx] + increment
        if new_score < 0 or new_score > 9:
            raise ValueError('The increment is too large')
        scores[idx] = new_score

        self._save_scores(scores, language)
