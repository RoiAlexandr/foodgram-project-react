import csv
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Заливка csv прайсов'

    def handle(self, *args, **options):
        # Парсинг ингридиентов
        with open('../data/ingredients.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                status, created = Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )

        print('Все ингридиенты загружены.')