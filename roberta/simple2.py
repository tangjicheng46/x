from sentence_transformers import models, losses
from sentence_transformers import LoggingHandler, SentenceTransformer, util, InputExample
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
import torch
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"device is {device}")

JA_EMBEDDING_MODEL_PATH = '/Users/ctw/hug/roberta-large-japanese'
JA_EMBEDDING_MODEL = None

text = "近所の店の人「クレーンが上がった状態でとまっていた。ここに響くほどの音じゃなかったので、最初は気づかなかった」この事故でケガ人はいませんでした。"
text2 = 'Hello, world!'

word_embedding_model = models.Transformer(JA_EMBEDDING_MODEL_PATH, max_seq_length=128)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
model.to(device)

emb = model.encode([text2, ])

print(type(emb))
print(emb.shape)


def save_flattened_to_txt(arr, filename):
    """
    Save a flattened numpy array to a txt file.
    The numbers are comma-separated, with 8 numbers per line and
    are rounded to 6 decimal places.

    Parameters:
    - arr: numpy array to be saved.
    - filename: name of the output txt file.
    """
    # Flatten the array
    flattened = arr.ravel()

    # Open the file for writing
    with open(filename, 'w') as f:
        for i, val in enumerate(flattened):
            # Add comma unless it's the last value in a line or in the file
            separator = "," if i % 8 != 7 and i != len(flattened) - 1 else ""

            # Write to the file
            f.write(f"{val:.6f}{separator}")

            # Add a newline every 8 values
            if (i + 1) % 8 == 0:
                f.write("\n")


save_flattened_to_txt(emb, "origin_output.csv")
