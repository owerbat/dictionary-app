import os
import numpy as np
import pandas as pd

from src.backend.utils import get_dump_path, softmax


class Dictionary:
    def __init__(self, translated_filename: str, random_state: int = None) -> None:
        translated = pd.read_csv(translated_filename)
        self.en_words = translated['lemma'].to_numpy()
        self.ru_words = translated['translation'].to_numpy()
        self.freqs = translated['freq'].to_numpy()

        self.en_scores_save_path = os.path.join(get_dump_path(), 'en_scores.npy')
        self.ru_scores_save_path = os.path.join(get_dump_path(), 'ru_scores.npy')

        self._init_scores('en')
        self._init_scores('ru')

        if random_state is not None:
            np.random.seed(random_state)

    def _init_scores(self, language: str = 'en'):
        if language == 'en':
            path = self.en_scores_save_path
        elif language == 'ru':
            path = self.ru_scores_save_path
        else:
            raise ValueError(f"`language` parameter must be in ['en', ru'], got {language}")

        if os.path.exists(path):
            setattr(self, f'{language}_scores', np.load(path))
        else:
            scores = np.zeros(self.freqs.shape[0])
            max_score = 9

            batch_size = self.scores.shape[0] // (max_score + 1)
            for i in range(max_score + 1):
                start_idx = i * batch_size
                end_idx = min((i + 1) * batch_size, self.scores.shape[0])

                score = max_score - i
                scores[start_idx: end_idx] = score

            setattr(self, f'{language}_scores', scores)

    def get_random_word(self, language: str = 'en'):
        if language not in ['en', 'ru']:
            raise ValueError(f"`language` parameter must be in ['en', ru'], got {language}")

        scores = getattr(self, f'{language}_scores')
        probas = softmax(scores)
        indices = np.arange(scores.shape[0])

        sample_idx = np.random.choice(indices, 1, p=probas)

        return self.en_words[sample_idx], self.ru_words[sample_idx]
