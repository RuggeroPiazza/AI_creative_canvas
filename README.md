# AI_creative_canvas

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)](https://www.python.org/downloads/release/python-310/)

> A fully automated application where two AIs work together to create AI art and publish it on Instagram.

## DISCLAIMER
This project is for educational purposes only. The creator doesn’t take any responsibility for improper or illegal use of the code and the concept of this project. 
Any security concerns will be highlighted in the documentation. Ignoring them it might result in vulnerabilities to hacks. The user is advised. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Development](#development)
- [Prompting](#prompting)
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
This could be a security concern because implies passing your Instagram credentials to a non-official library. 
This step can be skipped altogether and the images can be manually uploaded.

## Features<a id="features"></a>

List the key features of your application. You can use bullet points for this section.

- Feature 1
- Feature 2
- Feature 3

## Installation<a id="installation"></a>

Install the following packages:

```bash
pip install openai
```
```bash
pip install discord.py
```
```bash
pip install
```

