from django.core.management.base import BaseCommand, CommandError
import json
import os
from pathlib import Path, PurePath




class Command(BaseCommand):
    help = 'Json to SQLite'

    def handle(self, *args, **options):

        # uri_videos = Video.objects.all().filter(online=True)
        #filepath = '/static/data/minerals.json'

        p = Path(__file__).parents[4]
        p = PurePath(p, 'config/assets/data/test.txt')
        print(p)
        p = ''
        p = PurePath(p, 'config/assets/data/minerals.json')
        print (p)
        # p = os.getcwd()
        # p = p + '/config/assets/data/test.txt'
        """
        filename = p
        file = open(filename, "r")
        for line in file:
            print (line)
        """
        with open(p, 'r') as soccer:
            players = json.load(soccer)
            print(players[0])
        print ("You are legal now! Yay.")