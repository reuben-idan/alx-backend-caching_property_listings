from django.core.management.base import BaseCommand
from properties.models import Property
from decimal import Decimal


class Command(BaseCommand):
    help = 'Create sample properties for testing'

    def handle(self, *args, **options):
        # Create sample properties
        properties_data = [
            {
                'title': 'Modern Downtown Apartment',
                'description': 'Beautiful 2-bedroom apartment in the heart of downtown with city views.',
                'price': Decimal('250000.00'),
                'location': 'Downtown'
            },
            {
                'title': 'Suburban Family Home',
                'description': 'Spacious 4-bedroom family home with large backyard and garage.',
                'price': Decimal('450000.00'),
                'location': 'Suburbs'
            },
            {
                'title': 'Luxury Penthouse',
                'description': 'Exclusive penthouse with panoramic views and premium amenities.',
                'price': Decimal('850000.00'),
                'location': 'Uptown'
            },
            {
                'title': 'Cozy Studio',
                'description': 'Perfect starter home with modern appliances and great location.',
                'price': Decimal('180000.00'),
                'location': 'Midtown'
            },
            {
                'title': 'Waterfront Condo',
                'description': 'Stunning waterfront condo with private balcony and marina access.',
                'price': Decimal('650000.00'),
                'location': 'Harbor District'
            }
        ]

        created_count = 0
        for data in properties_data:
            property_obj, created = Property.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created property: {data["title"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Property already exists: {data["title"]}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new properties')
        ) 