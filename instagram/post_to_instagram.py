from pathlib import Path
from instagrapi import Client


def posting():
    cl = Client()
    cl.login(username='account_name', password='password')
    image_path = Path('Desktop', 'AI_project', '../to_upload', 'sci_fi_landscape.jpg')
    cl.photo_upload(image_path, caption='IAM_AI')
