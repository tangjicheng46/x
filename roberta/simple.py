import time
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForMaskedLM

cache_dir = "./temp"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"device is {device}")

tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese", cache_dir=cache_dir)
model = AutoModelForMaskedLM.from_pretrained("nlp-waseda/roberta-base-japanese", cache_dir=cache_dir)
model.to(device)

text = "ほとんどの国民がその名を知り、人びとを笑顔にするために尽くしていると信じた。"

text1 = "ほとんどの国民がその名を知り、人びとを笑顔にするために尽くしていると信じた。"
text2 = "ほとんどの国民がその名を知り"


if __name__ == "__main__":
    encoding = tokenizer([text1, text2] , return_tensors='pt', padding=True, truncation=True)

    print(encoding["input_ids"].shape)

    encoding.to(device)  # Move encoding to CUDA if available
    with torch.no_grad():
        output = model(**encoding)

    print(output.logits.shape)
