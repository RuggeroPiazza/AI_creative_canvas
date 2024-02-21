# AI_creative_canvas

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/release/python-312/)

> A fully automated application where two AIs work together to create AI art and publish it on Instagram.

## DISCLAIMER<a id="disclaimer"></a>
This project is intended solely for educational purposes.      
The creator explicitly disclaims any responsibility for any misuse or unlawful application of the code or project concept.      
Any security issues will be clearly outlined in the documentation, and failure to address them may leave user credentials vulnerable to exploitation.     
Users are strongly advised to take these warnings into consideration.       

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Prompting](#prompting)
- [Development](#development)
- [Flow](#flow)
- [Final Considerations](#considerations)

## Introduction<a id="introduction"></a>

The objective of this project is to develop an application that automate (almost) entirely the process of producing and sharing AI-generated artwork.     
It autonomously generates parameters and prompts for image creation, providing valuable insights into AI behaviour.      
The application utilizes OpenAI to generate image prompts, which are then submitted to Midjourney.      
Once the image is generated, it is automatically divided into four parts and downloaded locally. Upon completion of the download process, the program proceeds to upload the image to an Instagram profile.         


## Installation<a id="installation"></a>

Install the following packages:      
[OpenAi](https://pypi.org/project/openai/)         
The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.7+ application.
```bash
pip install openai
```      

[Discord](https://pypi.org/project/discord.py/)        
A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.
```bash
pip install discord.py
```     

[Pillow](https://pypi.org/project/pillow/)       
PIL is the Python Imaging Library by Fredrik Lundh and Contributors
```bash
pip install pillow
```     

[Pyautogui](https://pypi.org/project/PyAutoGUI/)      
PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.
```bash
pip install pyautogui
```     

[Requests](https://pypi.org/project/requests/)     
Requests is a simple, yet elegant, HTTP library.
```bash
pip install requests
```     

Create a MidJourney Discord Bot      
[Documentation](https://docs.midjourney.com/docs/add-the-bot)        


## Prompting<a id="prompting"></a>  
Prompts are generated using the OpenAI public API for text completion.       
Initially, the script utilized the text-DaVinci-003 model, which has since been deprecated.      
WARNING: OpenAI frequently deprecates older model versions.       
Presently, the program employs the gpt-3.5-turbo-instruct model. For verification of whether the current version remains suitable for this specific task, please consult the following link:       
[Deprecations](https://platform.openai.com/docs/deprecations/)


## Development<a id="development"></a>  
### Discord/MidJourney bot limitations and challenges ###      
The primary challenge encountered during development was the absence of a public API from Midjourney at that time.       
Except for third-party paid solutions, there was no apparent way to bypass Discord.       
After setting up a Discord Bot, it was discovered that simply sending a string message into the chat wouldn't trigger the desired '/imagine' command.     
In the absence of an alternative method, the decision was made to automate the interaction using pyautogui, which simulates mouse and keyboard actions.       
A basic Discord bot was employed to send a message acting as the event trigger for the automation: when a specific message is detected in the chat, the script verifies if it matches the trigger.       
If matched, a function is called to simulate user input, typing the '/imagine' command into the chat, thereby activating Midjourney's bot.     
Subsequently, the function is enhanced to paste the previously generated prompt into the chat, initiating the image creation process.      
Midjourney then generates an image comprising four versions of the same prompt. Utilizing the PIL library, this image is split into four individual images, enabling the download of one.    

### Instagram ###     
Instagram does offer a public API; however, the functionality for programmatically uploading images comes with hard limitations.       
A third-party library can be utilized.      
WARNING: This approach raises security concerns as it entails sharing Instagram credentials with a non-official library.     
As a result, this step is skipped in the current implementation, although the basic code required for performing the upload is provided.      
Users have the option to automate this final step of the process at their discretion.     


### Prompting and versions ###          

The prompt generation process has undergone various approaches, aiming to produce unique prompts with each execution.            

V1              
The initial query to OpenAI requests four key-value pairs representing categories for image generation, where each key denotes an attribute or style of figurative art, and the corresponding value represents that attribute.      
Subsequently, these key-value pairs are utilized in a subsequent query to generate the prompt for MidJourney's image generation.       
To prevent redundancy in each cycle, the categories are stored in a JSON file.       
During the initial query, OpenAI can be instructed not to employ those specific categories, thereby ensuring diversity in prompt generation.      

V2             
In this approach, OpenAI is tasked with generating 5 items for each of 6 predetermined, hard-coded categories.      
Subsequently, the script randomly selects one item per category, resulting in the creation of 6 key-value pairs.     
These pairs are then utilized as categories for generating the prompt to be submitted to MidJourney.          

Hard-coded approach       
Initially, the parameters were hardcoded into a .py file as extensive lists.      
The script would then randomly select one item from each list, resulting in a compact list of parameters for generating the final prompt.      
While this approach yielded highly detailed and extensive prompts, it relied on hardcoded elements, necessitating the parsing of large lists.     
Moreover, this method deviated from the original project goal of maximizing AI-generated content.      
During testing, examples of parameters utilized can be located in the "parameters" folder within this repository.       

V3 - work in progress       
The application has the potential to evolve into a web-based platform.     
A simple GUI can be developed to initiate the process. Throughout the execution, the GUI displays the generated prompt, provides status updates on the success or failure of different stages, and presents the resulting image via its URL.      
Users can then opt to download or save the image accordingly.      

## Flow<a id="flow"></a>
![flow diagramm](image url "ai_app")

The whole process its triggered by the app.py script. The execution can be scheduled using a bash script.      

1. Launching Discord
  
The _open_discord.py_ script utilizes the pyautogui library to automate the process of launching Discord and selecting the channel where the MidJourney bot is installed.     
Please refer to the link provided in the "installation" section for detailed instructions on setting up a MidJourney bot on Discord.    
To enable pyautogui to launch Discord, a combination of keys must be configured. An efficient method involves moving the Discord icon to the taskbar (Windows) and using the combination of 'win' + number, where the number corresponds to the position of the icon in the taskbar.    
A sleep time of 20 seconds is set to ensure Discord is fully opened before selecting the channel. This sleep time can be adjusted as needed to accommodate system performance.     

2. Querying OpenAi and generates image prompt

The _generate_prompt_V1.py_ (and _generate_prompt_V2.py_) scripts initially load data from the _categories.json_ file.     
Subsequently, a preliminary query is sent to the OpenAI model to generate parameters (avoiding those parameters already stored in the JSON file).     
These newly generated parameters are then utilized in a second query to create the complete prompt, which is subsequently submitted to MidJourney for image generation.     
The JSON file is then over-written with the latest parameters.            

3. Launching MidJourney bot, creating and processing the images

The submit_download.py script establishes a connection with the Discord bot and automatically inserts the /imagine command to submit a prompt.    
Upon submission of the prompt, the script monitors for a reply, which typically indicates the arrival of the generated image. Once the reply is detected, the script verifies the file format of the image.     
If the file is recognized as an image, the script proceeds to split it into four parts and downloads them into a designated local folder.     
While each version of the image can potentially be upscaled or resubmitted to generate four new variations, the program opts to streamline the process by selecting just one version for download.     
The selection can either be random or predetermined, depending on the configuration.     
Furthermore, no upscaling is applied since the original definition of the image is considered sufficient for uploading on Instagram.     

4. Posting on Instagram

WARNING: please read the following [disclaimer](#disclaimer)      
As previously discussed, programmatically posting on Instagram can be accomplished using third-party libraries.     
However, this entails sharing your credentials with a non-official library, which poses security risks.      
Consequently, the final step of the process, involving automated posting on Instagram, is not being implemented in the current version. Nonetheless, a snippet of the required code for this functionality is provided in the repository for reference.     


## Final considerations<a id="considerations"></a>
This project highlighted the difficulties of correct prompting to continuously generate unique results from the same set of instructions.       
Often the scripts tend to repeat themselves, if not in the choice of the categories, in the structure and definition of the final prompt itself.        
This becomes evident with the hard-coded approach, which generates much more variety and more high-quality images, because it allows the user to better control the coherence and compatibility of all the parameters given to the model. The final prompt results are more descriptive and coherent.         
Some prompts produce very interesting artistic results, due to the random nature of the parameters, producing some interesting, unconventional combinations.      
Another possible approach could be to use the chat model instead of the text-completion model, instructing it with more art-related contexts.      
Please feel free to explore new approaches and let me know what kind of result you get and what you think it could improve this project.      
