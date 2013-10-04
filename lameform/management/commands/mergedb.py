import json
import os.path

from django.core.management.base import BaseCommand, CommandError

from lameform import models

class Command(BaseCommand):
    args = '<export.json>'
    help = 'merge data from export.json to current db'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('python manage.py mergetdb <export.json>')

        file_name = os.path.abspath(args[0])
        with open(file_name, 'r') as json_file:
            json_data = json.load(json_file)

        for imported_info in json_data:
            if imported_info['fields']['arrived'] == None:
                continue
            db_info = models.Main.objects.get(id=imported_info['pk'])
            if db_info.arrived == None:
                print 'merging :', db_info.id, ' ', db_info
                db_info.arrived = imported_info['fields']['arrived']
                db_info.save()
