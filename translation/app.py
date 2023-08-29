from fastapi import FastAPI, HTTPException
from transformers import MarianMTModel, MarianTokenizer
from pydantic import BaseModel

app = FastAPI()

model_name = 'Helsinki-NLP/opus-mt-en-zh'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

class TranslationRequest(BaseModel):
    input_text: str

class TranslationResponse(BaseModel):
    output_text: str


@app.post("/translate")
def translate(req: TranslationRequest) -> TranslationResponse:
    if not req.input_text:
        raise HTTPException(status_code=400, detail="Text is required for translation")

    inputs = tokenizer.encode(req.input_text, return_tensors="pt", max_length=512, truncation=True)
    translated_tokens = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return TranslationResponse(output_text=translation)
