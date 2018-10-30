from django.core.management.base import BaseCommand, CommandError
import json


class Command(BaseCommand):
    help = 'Json to SQLite'

    def handle(self, *args, **options):

        # uri_videos = Video.objects.all().filter(online=True)
        filepath = 'data/images/minerals.json'
        with open(filepath, 'r') as soccer:
            players = json.load(soccer)
            print(players)
        print ("You are legal now! Yay.")