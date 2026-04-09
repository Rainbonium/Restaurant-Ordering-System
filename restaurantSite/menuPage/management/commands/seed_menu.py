from django.core.management.base import BaseCommand
from menuPage.models import FoodItem

class Command(BaseCommand):
    help = "Seed the FoodItem table"

    def handle(self, *args, **kwargs):
        items = [
            {"name": "Aperol Spritz", "food_type": "drinks", "food_description": "A refreshing citrus cocktail.", "food_price": 12.00, "food_thumbnail": "images/AperolSpritz.jpg"},
            {"name": "Classic Mojito", "food_type": "drinks", "food_description": "Mint, lime, and rum.", "food_price": 11.00, "food_thumbnail": "images/ClassicMojito.jpg"},
            {"name": "Margarita", "food_type": "drinks", "food_description": "Tequila, lime, and triple sec.", "food_price": 12.00, "food_thumbnail": "images/Margarita.jpg"},
            {"name": "Pina Colada", "food_type": "drinks", "food_description": "Pineapple and coconut blend.", "food_price": 12.50, "food_thumbnail": "images/PinaColada.jpg"},
            {"name": "Sangria", "food_type": "drinks", "food_description": "Wine with fruit and citrus.", "food_price": 13.00, "food_thumbnail": "images/Sangria.jpg"},
            {"name": "Moscow Mule", "food_type": "drinks", "food_description": "Vodka, ginger beer, and lime.", "food_price": 11.50, "food_thumbnail": "images/MoscowMule.jpg"},
            {"name": "Espresso Martini", "food_type": "drinks", "food_description": "Coffee-forward cocktail.", "food_price": 13.50, "food_thumbnail": "images/EspressoMartini.jpg"},
            {"name": "Strawberry Daiquiri", "food_type": "drinks", "food_description": "Sweet strawberry rum cocktail.", "food_price": 12.50, "food_thumbnail": "images/StrawberryDaiquiri.jpg"},
            {"name": "Mango Lassi", "food_type": "drinks", "food_description": "Creamy yogurt and mango drink.", "food_price": 7.00, "food_thumbnail": "images/MangoLassi.jpg"},

            {"name": "French Fries", "food_type": "food", "food_description": "Golden crispy fries.", "food_price": 6.00, "food_thumbnail": "images/FrenchFries.png"},
            {"name": "Beef Tacos", "food_type": "food", "food_description": "Seasoned beef tacos with toppings.", "food_price": 14.00, "food_thumbnail": "images/BeefTacos.jpg"},
            {"name": "Chicken Caesar Salad", "food_type": "food", "food_description": "Romaine, chicken, parmesan, and croutons.", "food_price": 15.00, "food_thumbnail": "images/ChickenCaesarSalad.jpg"},
            {"name": "Chicken Yakisoba", "food_type": "food", "food_description": "Stir-fried noodles with chicken and vegetables.", "food_price": 16.00, "food_thumbnail": "images/ChickenYakisoba.jpg"},
            {"name": "Grilled Salmon", "food_type": "food", "food_description": "Served with a light finish.", "food_price": 22.00, "food_thumbnail": "images/GrilledSalmon.jpg"},
            {"name": "Margherita Pizza", "food_type": "food", "food_description": "Tomato, mozzarella, and basil.", "food_price": 18.00, "food_thumbnail": "images/MargheritaPizza.jpg"},
            {"name": "Mushroom Risotto", "food_type": "food", "food_description": "Creamy risotto with mushrooms.", "food_price": 17.00, "food_thumbnail": "images/MushroomRisotto.jpg"},
            {"name": "Pad Thai", "food_type": "food", "food_description": "Rice noodles with tamarind sauce.", "food_price": 16.00, "food_thumbnail": "images/PadThai.jpg"},
            {"name": "Spaghetti Carbonara", "food_type": "food", "food_description": "Creamy pasta with bacon and cheese.", "food_price": 17.00, "food_thumbnail": "images/SpaghettiCarbonara.png"},
            {"name": "Vegetable Stir Fry", "food_type": "food", "food_description": "Fresh vegetables with savory sauce.", "food_price": 14.00, "food_thumbnail": "images/VegetableStirFry.jpg"},
            {"name": "Beese Churger", "food_type": "food", "food_description": "A house burger with cheese.", "food_price": 15.00, "food_thumbnail": "images/BeeseChurger.png"},

            {"name": "Apple Pie", "food_type": "dessert", "food_description": "Classic baked apple pie.", "food_price": 8.00, "food_thumbnail": "images/ApplePie.jpg"},
            {"name": "Bread Pudding", "food_type": "dessert", "food_description": "Warm bread pudding with sauce.", "food_price": 8.50, "food_thumbnail": "images/BreadPudding.jpg"},
            {"name": "Chocolate Lava Cake", "food_type": "dessert", "food_description": "Molten chocolate center.", "food_price": 9.50, "food_thumbnail": "images/ChocolateLavaCake.jpg"},
            {"name": "Churros with Chocolate Sauce", "food_type": "dessert", "food_description": "Crispy churros with dip.", "food_price": 8.50, "food_thumbnail": "images/ChurrosChocolateSauce.jpg"},
            {"name": "Creme Brulee", "food_type": "dessert", "food_description": "Vanilla custard with caramelized top.", "food_price": 9.00, "food_thumbnail": "images/CremeBrulee.jpg"},
            {"name": "Fruit Sorbet", "food_type": "dessert", "food_description": "Light and refreshing sorbet.", "food_price": 7.50, "food_thumbnail": "images/FruitSorbet.jpg"},
            {"name": "Key Lime Pie", "food_type": "dessert", "food_description": "Tart lime pie with crust.", "food_price": 8.50, "food_thumbnail": "images/KeyLimePie.jpg"},
            {"name": "Molten Chocolate Souffle", "food_type": "dessert", "food_description": "Rich chocolate dessert.", "food_price": 10.00, "food_thumbnail": "images/MoltenChocolateSouffle.jpg"},
            {"name": "New York Cheesecake", "food_type": "dessert", "food_description": "Creamy cheesecake slice.", "food_price": 9.00, "food_thumbnail": "images/NewYorkCheesecake.jpg"},
            {"name": "Tiramisu", "food_type": "dessert", "food_description": "Coffee-flavored Italian dessert.", "food_price": 9.50, "food_thumbnail": "images/Tiramisu.jpg"},
        ]

        FoodItem.objects.all().delete()
        for item in items:
            FoodItem.objects.create(**item)

        self.stdout.write(self.style.SUCCESS(f"Created {len(items)} food items."))