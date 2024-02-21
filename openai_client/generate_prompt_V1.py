from openai import OpenAI
import json
from pathlib import Path
import os


'''
V1: the script ask open_ai to generate 4 key-value pairs.
Pairs are then saved on a JSON file to avoid repetition on the next query
and they are passed to the second query that creates a prompt containing
the key-value pairs. The resulting prompt is then submitted to Midjourney
'''

client = OpenAI(
    api_key=os.getenv('api_key')
)
file_path = f"{Path.cwd()}\\{'openai_client'}\\{'categories.json'}"


def main():
    load_data = loading_data(file_path)  # previous used categories are loaded
    categories_prompt = f'''Generate 4 pairs of key-values.          
    Each key should represent an attribute or style of figurative art.
    The value should correspond to that attribute.
    One of the pair must be "subject" paired with a randomly chosen subject.                            
    Focus only on providing the key-value pairs and avoid generating any additional description.
    Make sure you are not using any of the following words {load_data}
'''

    image_prompt = ("Create a prompt for the generative artificial intelligence Midjourney "
                    "containing the following elements:\n")

    new_categories = open_ai_query(categories_prompt)  # first query: creates new categories
    print(f"Categories generated: {new_categories}\n")
    saving_data(file_path, new_categories)  # saving categories
    image_prompt += new_categories
    final_prompt = open_ai_query(image_prompt)
    return final_prompt


def open_ai_query(prompt):
    response = client.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt,
        temperature=0.8,
        max_tokens=2000
    )
    return response.choices[0].text


def saving_data(path, data_to_save):
    with open(path, 'w') as file:
        json.dump(data_to_save, file)


def loading_data(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data
