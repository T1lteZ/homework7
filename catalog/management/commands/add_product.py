from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add new product and category"

    def handle(self, *args, **options):

        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Все продукты удалены из базы данных.'))

        category, _ = Category.objects.get_or_create(name="Ardor", description="Продукты компании Ardor")

        products = [
            {"name": "Корпус для пк",
             "description": "white",
             "category": category,
             "price": "5000",
             "created_at": "2025-02-12",
             "updated_at": "2025-02-12"},
            {"name": "Корпус для пк",
             "description": "black",
             "category": category,
             "price": "5000",
             "created_at": "2025-02-12",
             "updated_at": "2025-02-12"},
        ]

        for product in products:
            products, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {products.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {products.name}'))
