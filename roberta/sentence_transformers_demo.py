import torch
from sentence_transformers import models, losses
from sentence_transformers import LoggingHandler, SentenceTransformer, util, InputExample
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator

cache_dir = "./temp"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"device is {device}")

MODEL_PATH = 'nlp-waseda/roberta-large-japanese'
JA_EMBEDDING_MODEL = None

def load_model(model_path):
    word_embedding_model = models.Transformer(model_path, max_seq_length=128,
                                              cache_dir=cache_dir)
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    model.to(device)
    return model

def ja_embedding_func(text_list):
    global JA_EMBEDDING_MODEL
    return JA_EMBEDDING_MODEL(text_list)

text = "近所の店の人「クレーンが上がった状態でとまっていた。ここに響くほどの音じゃなかったので、最初は気づかなかった」この事故でケガ人はいませんでした。"

if __name__ == "__main__":
    JA_EMBEDDING_MODEL = load_model(MODEL_PATH)
    output = ja_embedding_func([text, ] * 3)
    print(output.shape)

