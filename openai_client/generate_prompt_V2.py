from openai import OpenAI
import json
import random
from pathlib import Path
import os

'''
V2: the script ask open_ai to generate 5 items for 6 specific categories.
The script then randomly selects one item per category creating 6 key-value pairs.
The pairs are saved to a JSON file to avoid repetition on the next query.
The final prompt is then generated and submitted to Midjourney.
'''

client = OpenAI(
    api_key=os.getenv('api_key')
)
file_path = f"{Path.cwd()}\\{'openai_client'}\\{'categories.json'}"


def main():
    loaded_data = loading_data(file_path)
    parameters = {}
    items_list = [
        "subjects for an artistic image",
        "digital art filters",
        "photography techniques",
        "types of lightning",
        "art styles",
        "artistic medium"]
    prompt_item = ''
    categories_prompt = (f"give me a comma separated list of 5 {prompt_item}. "
                         f"Don't number the list and make sure you are not using the following {loaded_data}")

    image_prompt = ("Create a prompt for the generative artificial intelligence Midjourney "
                    "containing the following elements:\n")

    for item in items_list:
        prompt_item += item
        res = open_ai_query(categories_prompt).split(',')
        item_selected = random_generator(res)
        parameters[item] = item_selected

    saving_data(file_path, parameters)
    print(parameters)
    for item in parameters.items():
        image_prompt += str(item)
    print(image_prompt)
    final_prompt = open_ai_query(image_prompt)
    print(final_prompt)
    return final_prompt


def random_generator(list_of_items):
    selected = random.choice(list_of_items)
    return selected


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
