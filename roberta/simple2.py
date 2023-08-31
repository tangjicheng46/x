from sentence_transformers import models, losses
from sentence_transformers import LoggingHandler, SentenceTransformer, util, InputExample
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
import torch

cache_dir = "./temp"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"device is {device}")

MODEL_PATH = 'nlp-waseda/roberta-large-japanese'
JA_EMBEDDING_MODEL = None

text = "近所の店の人「クレーンが上がった状態でとまっていた。ここに響くほどの音じゃなかったので、最初は気づかなかった」この事故でケガ人はいませんでした。"

word_embedding_model = models.Transformer('nlp-waseda/roberta-large-japanese', max_seq_length=128, cache_dir=cache_dir)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())

model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
model.to(device)



emb = model([text, ] * 3)
print(type(emb))
print(emb.shape)