from discord_client import submit_download, open_discord
from openai_client import generate_prompt_V1, generate_prompt_V2
import os

discord_token = os.getenv('discord_token')
# select here the version to run
version = generate_prompt_V1

if __name__ == '__main__':
    # launching discord and selecting the correct channel
    open_discord.launch_discord()
    # generate the prompt
    submit_download.prompt = version.main()
    # submit the prompt into Midjourney and download the images
    submit_download.client.run(discord_token)

