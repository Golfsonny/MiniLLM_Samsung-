import ollama
import os
import json
from mini_gpt_unstructured import get_samsung_urls

'''STRUCTURED'''
def set_prompt(query):
	current_path = os.path.dirname(__file__)
	json_path = os.path.join(current_path, "data/edge.json")

	with open(json_path, "r") as json_file:
		json_data = json.load(json_file)

	promotion_chunk = get_samsung_urls()

	prompt = f"""
You are an expert of Samsung Galaxy products.
You have to explain the product based on given contexts.
WARNING: Do not answer if the given product does not exists in the given contexts. 

Product Information : {json_data}


Product Promotion (Buy Benefits): {promotion_chunk}


Question; {query}

Answer:
"""

	return prompt

query = input("Please put your query: ").strip()

stream = ollama.chat(
		model='llama3.2',
		messages=[{'role': 'user', 'content': set_prompt(query)}],
		stream=True
)

for chunk in stream: 
	print(chunk['message']['content'], end='', flush=True)


