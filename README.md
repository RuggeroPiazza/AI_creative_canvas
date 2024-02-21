# AI_creative_canvas

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/release/python-312/)

> A fully automated application where two AIs work together to create AI art and publish it on Instagram.

## DISCLAIMER
This project is for educational purposes only. The creator doesn’t take any responsibility for improper or illegal use of the code and the concept of this project. 
Any security concerns will be highlighted in the documentation. Ignoring them it might result in vulnerabilities to hacks. The user is advised. 

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Prompting](#prompting)
- [Development](#development)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction<a id="introduction"></a>

The goal of this project is to create an application that automates (almost) entirely the creation and publication of AI art and to offer insight into AI behaviour,
allowing it to spontaneously generate parameters and prompts for image creation.
Using openAI and MidJourney, this program creates the prompts and submits them to Midjourney. The resulting image is then split into 4 and automatically downloaded locally. 
When the download folder is populated, the program uploads the image to an Instagram profile.

## Development<a id="development"></a>

The main issue during the development was the absence of a public API from Midjourney. 
Apart from third-party solutions offering API to interact with Midjourney, I wasn’t able to find a way to bypass Discord. 
After setting up a Discord Bot, I find out that sending a simple string into the chat is not enough to trigger the Midjourney bot. 
Not able to find another way to do it, I then decided to automate the interaction using pyautogui, simulating the mouse and keyboard action. I was then able to automate the prompt submission.
The image generated is a composition of 4 images. Using the PIL library we can split the image into 4 images. Everything gets downloaded locally. 

Instagram offers a public API, but it doesn’t provide a way to programmatically upload images. This operation must be performed using a third-party library.
WARNING: This could be a security concern because it implies passing your Instagram credentials to a non-official library. 
This step is then skipped but the code necessary to perform the automatic upload is provided.
The user can then decide to automate the last step of the process.


## Installation<a id="installation"></a>

Install the following packages:
[OpenAi](https://pypi.org/project/openai/) - The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.7+ application.
```bash
pip install openai
```

[Discord](https://pypi.org/project/discord.py/) - A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.
```bash
pip install discord.py
```

[Pillow](https://pypi.org/project/pillow/) -  PIL is the Python Imaging Library by Fredrik Lundh and Contributors
```bash
pip install pillow
```

[Pyautogui](https://pypi.org/project/PyAutoGUI/) - PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.
```bash
pip install pyautogui
```

[Requests](https://pypi.org/project/requests/) - Requests is a simple, yet elegant, HTTP library.
```bash
pip install requests
```

## Prompting<a id="prompting"></a>
Prompts are generated using the openAI public API for text completion.
Originally using the text-DaVinci-003 model (now deprecated). 
WARNING: OpenAi often deprecates older versions of their models. Currently, the program uses the gpt-3.5-turbo-instruct model. 
Please refer to the following link to check if the current version is still used for this specific task:
Prompts are generated using the openAI public API for text completion.
Originally using the text-DaVinci-003 model (now deprecated). 
WARNING: OpenAi often deprecates older versions of their models. Currently, the program uses the gpt-3.5-turbo-instruct model. 
Please refer to the following link to check if the current version is still used for this specific task:
[Deprecations](https://platform.openai.com/docs/deprecations/)


## Development<a id="development"></a>
The process of generating prompts has followed many approaches, trying to create unique prompts on each execution.

V1
A first query to OpenAi asks for four key-value pairs representing the categories to be used for the image generation. 
Each key represents an attribute or style of figurative art. The value should then correspond to that attribute.
The key-value pairs are then used in a new query to generate the prompt that will be passed to MidJourney for the image generation.
To avoid repetition on each cycle, the categories are saved into a JSON file and, in the first query, OpenAI can be asked to not use those specific categories.

V2
In this approach, OpenAi is asked to generate 5 items for 6 specific hard-coded categories. The script will then randomly select one item per category, creating 6 key-value pairs.
Those pairs are then used as categories for the generation of the prompt to be submitted to MidJourney

Hard-coded approach:
Originally, the list of those parameters was hard-coded into a .py file as a collection of big lists. The script would then randomly parse one item per each list. This would generate a small list of parameters used to generate the final prompt.
This approach gave very good results, with long and detailed prompts, but included hard-coded elements, requiring to scan big lists. Furthermore, it sacrifices the original goal of the project: having as much as possible generated by the AI itself.

V3 - work in progress
The application could be extended to become a web application. 
A basic GUI can be made to start the process. During the execution, the GUI shows the prompt generated, gives confirmation of the success or failure of the various steps and then shows the image generated (using the URL). The image can then be downloaded or stored.

