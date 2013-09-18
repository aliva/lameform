import json
import os.path

from django.core.management.base import BaseCommand, CommandError
from lameform import models

class Command(BaseCommand):
    args = '<export.json>'
    help = 'import exported db to app'
    
    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('python manage.py importdb <export.json>')
        
        file_name = os.path.abspath(args[0])
        with open(file_name, 'r') as json_file:
            json_data = json.load(json_file)
            
        for info in json_data:
            self.stdout.write('importing %d' % info['id'])
            models.Main.objects.create(
                id=info['id'],
                name=info['name'],
                family=info['family'],
                email=info['email'],
                phone=info['phone'],
                edu=info['edu'],
                work=info['work'],
                date=info['date']+'Z',
                verify=info['verify'],
                code=info['code'],
                server=info['server'],
            )
