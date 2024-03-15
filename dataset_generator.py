import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Game_Recommendation_System.settings')
django.setup()

import json
import requests
from django.core.files.base import ContentFile
from django.apps import apps
from game.models import Game, Platform
# from django.core.wsgi import get_wsgi_application

# application = get_wsgi_application()

def import_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        for entry in data:
            platforms = entry.pop('platform', [])  # Extract and remove 'platform' from entry
            image_url = entry.pop('image', None)  # Extract and remove 'image' from entry

            game = Game.objects.create(**entry)  # Create the Game instance without 'platform' and 'image'

            # Create Platform instances and associate them with the Game
            for platform_name in platforms:
                platform, created = Platform.objects.get_or_create(name=platform_name)
                game.platforms.add(platform)

            # Download and save the image
            if image_url:
                response = requests.get(image_url)
                game.image.save(f'{game.title}_image.jpg', ContentFile(response.content), save=True)


if __name__ == '__main__':
    json_file_path = 'dataset.json'
    import_data_from_json(json_file_path)
