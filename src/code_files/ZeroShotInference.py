# -*- coding: utf-8 -*-
"""Another copy of Open-Source-LLMs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U5z6wQWwncXQUPWTqDu58hXfeqpsReUo
1. edit instruction and remove code corresponding to df_train.
"""

#You need to install the following specifications before running
#!pip install openai==0.28 tenacity

# import gradio as gr
# from gradio_client import Client
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential, RetryError
import json
import pandas as pd
import time
import re
import os
# os.environ['socks_proxy'] = 'socks5://10.5.20.149:1200'
system_message = """You are an expert medical professional.
####

"""

# Replace with your API keys and endpoint URLs
#api_keys = ["<API_KEY_1>", "<API_KEY_2>", "<API_KEY_3>"]
#endpoint_urls = ["<ENDPOINT_URL_1>", "<ENDPOINT_URL_2>", "<ENDPOINT_URL_3>"]
#llm_names = ["LLM 1", "LLM 2", "LLM 3"]

api_keys = ["EMPTY"]
endpoint_urls = ["https://bd1f-130-75-152-24.ngrok-free.app"] #mistral,llama
llm_names = []

for api_key, endpoint_url in zip(api_keys, endpoint_urls):
    if 'hf.space' in endpoint_url:
        model_name = endpoint_url.replace('https://', '').replace('.hf.space', '').replace('/', '')
    else:
        openai.api_key = api_key
        openai.api_base = f"{endpoint_url}/v1"
        model_names = openai.Model.list()
        model_name = model_names["data"][0]["id"]
    llm_names.append(model_name)

# Function to retrieve LLM outputs using the given API key and endpoint
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def get_completion(prompt, api_key, endpoint_url, top_p, max_tokens, temperature,hard_code_exception=False):
    # if new_sheet_name=='poem_properties':
    #     if hard_code_exception==True:
    #         max_tokens=128
    #     else:
    #         max_tokens=150
    # else:
    
        if 'hf.space' in endpoint_url:
            client = Client(endpoint_url)
            result = client.predict(
                            prompt, # str in 'Message' Textbox component
                            api_name="/chat"
            )
            return result.strip()
        openai.api_key = api_key
        openai.api_base = f"{endpoint_url}/v1"
        model_names = openai.Model.list()
        model_name = model_names["data"][0]["id"]

        res = openai.Completion.create(
            model=model_name,  # Replace with your model name
            prompt=system_message + prompt,
            do_sample=False, 
            max_tokens=56               #this is the maximum of length of tokens that can be generated in the output
        )
        out_text = res['choices'][0]['text'].strip()
        return out_text


def compare_llm_outputs(user_query, top_p, max_tokens, temperature,hard_code_exception=False):
    results = [get_completion(user_query,
                              api_keys[i], 
                              endpoint_urls[i], 
                              max_tokens=max_tokens,
                              top_p=top_p,
                              temperature=temperature,
                              hard_code_exception=hard_code_exception) for i in range(len(endpoint_urls))]
    return results


def truncate_list_at_marker(lst, marker="##"):      #truncates any string after delimiter '##' 
    truncated_list = []
    for item in lst:
        if marker in item:
            truncated_list.append(item.split(marker)[0] + marker)
            break
        truncated_list.append(item)
    return truncated_list

print(llm_names)

import pandas as pd
import sys
import time
import random
import re
#data = sys.argv[1]    #add sys.argv[3] and [4] for the methods and no. of ICL examples
txt_file_path = sys.argv[1] # path to folder containing txt files, 
method = sys.argv[2] 
no_of_ICL_examples = sys.argv[3]


responses_LLaMa2_7b = list()

txt_files = [f for f in os.listdir(txt_file_path) if f.endswith('.txt')]
def extract_number(filename): 
    #for  each of the filenames, extracts integer from the filenames, and sorts those, 
    #if do not find any integer in filename, then returns infinity   
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')                                 


responses_LLaMa2_7b = list()

txt_files.sort(key=extract_number)

for txt_file in txt_files:
# Iterate over each file in the directory
            try:
                with open(os.path.join(txt_file_path, txt_file), 'r') as file:
                    user_query = file.read().strip()                # Read the content of the txt file
                    max_tokens = 50
                    top_p = 0.8
                    temp = 0.1
                
            
                    tmp_list = compare_llm_outputs(user_query,top_p, max_tokens,temp)
                    tmp_list = truncate_list_at_marker(tmp_list, marker="##")
                    print('*'*50)
                    print(user_query)
                    for llm_name, output in zip(llm_names, tmp_list):
                        print('{}: {}'.format(llm_name, output))
                        print('-----------------')
                          
                    responses_LLaMa2_7b.append(tmp_list[0])
                                   
                    sleep_time = random.randint(5,10)
                    print(f'Sleeping for {sleep_time} secs....')
                    time.sleep(sleep_time)
    
            except Exception as e:
                print(e)
                responses_LLaMa2_7b.append('NO OUTPUT. ERROR')

try:
    with open(f'LLaMa2_7b_{no_of_ICL_examples}_{method}.txt', 'w', encoding='utf-8') as f:
        f.write('\n+++++++++++++++++++++++++++++\n'.join(responses_LLaMa2_7b))
    print("File written successfully.")
except UnicodeEncodeError as e:
    print(f"Unicode encoding error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
f.close()
