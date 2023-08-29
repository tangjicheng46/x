import time
import transformers
from transformers import AutoTokenizer, AutoModelForMaskedLM

cache_dir = "./temp"

tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese", cache_dir=cache_dir)
model = AutoModelForMaskedLM.from_pretrained("nlp-waseda/roberta-base-japanese", cache_dir=cache_dir)

def embedding_func(text: str):
    encoding = tokenizer([text,] * 5, return_tensors='pt')
    output = model(**encoding)
    return output

def benchmark(N, input_list, input_func, warmup=10):
    for i in range(warmup):
        for item in input_list:
            result = input_func(item)
        print(f"warmup {i}: {time.time()}")

    start_time = time.time()

    for i in range(N):
        for item in input_list:
            result = input_func(item)
        print(f"{i}: {time.time()}")

    end_time = time.time()

    elapsed_time = end_time - start_time
    average_time_per_element = elapsed_time / (N * len(input_list))

    print(f"Average time per input: {average_time_per_element:.6f} seconds")

def read_lines_to_list(filename):
    lines_list = []
    with open(filename, 'r') as file:
        for line in file:
            lines_list.append(line.strip())
    return lines_list

if __name__ == "__main__":
    input_text = "./input_text.txt"
    input_list = read_lines_to_list(input_text)

    benchmark(50, input_list, embedding_func)

