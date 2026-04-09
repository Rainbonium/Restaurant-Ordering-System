from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import Order, Table, Restaurant, Person, FoodItem
from .forms import RestaurantForm, FoodItemForm
from bson import ObjectId
from django.http import HttpResponse
from django.conf import settings
import random
import json

def getPerson():
    person = Person.objects.all()
    return person

def getFoodItems():
    foodItems = FoodItem.objects.all()
    return foodItems

def getImageSource():
    imageStoreagePath = settings.IMAGE_STORAGE
    print("Test", imageStoreagePath)
    return imageStoreagePath

# Create your views here.
def index(request):
    print(request.path)
    #return HttpResponse("<head><title>" + HttpRequest.path[1:-1] + "</title></head><body><h1>test</h1></body>")
    #always include the header
    myArr = ["One", "Two", "Three"]
    foodArr = getFoodItems()
    imageResolution = [random.random()*800, random.random()*800]
    imagesVar = getImageSource()
    return render(request, "index.html", {"array": myArr, "imageSizes": imageResolution, "foodItems": foodArr, "images": imagesVar})

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            table_number = int(data.get('table_number'))
            restaurant_id = ObjectId(data.get('restaurant_id'))
            items = data.get('items')

            restaurant = Restaurant.objects.get(_id=restaurant_id)
            table = Table.objects.get(table_number=table_number, restaurant = restaurant)

            order_items = []
            if items:
                for item in items:
                    print(item)
                    product_id = item['product_id']
                    quantity = item.get('quantity', 1)  # Default quantity to 1 if not provided
                    try:
                        food_item = FoodItem.objects.get(_id=ObjectId(product_id))  # Convert to ObjectId

                        order_items.append({
                            'food_item_id': str(food_item._id),
                            'food_item_name': food_item.name,
                            'food_item_price': str(food_item.food_price),
                            'quantity': quantity
                        })
                        # Create an OrderItem instance
                        # OrderItem.objects.create(order=order, food_item=food_item, quantity=quantity)
                    except FoodItem.DoesNotExist:
                        return JsonResponse({'error': f'Food item with ID {product_id} not found.'}, status=404)

            with transaction.atomic():
                order = Order.objects.create(
                    table=table,
                    restaurant=restaurant,
                    items=order_items
                )

            return JsonResponse({'message': 'Order placed successfully!', 'order_id': str(order._id)}, status=201)

        except Table.DoesNotExist:
            return JsonResponse({'error': 'Table not found.'}, status=404)
        except Restaurant.DoesNotExist:
            return JsonResponse({'error': 'Restaurant not found.'}, status=404)
        except FoodItem.DoesNotExist:
            return JsonResponse({'error': 'Food item not found.'}, status=404)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'An error occurred while placing the order.'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

def restaurant_data_view(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RestaurantForm()
    return render(request, 'create_restaurant.html', {'form': form})

def fooditem_data_view(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FoodItemForm()
    return render(request, 'create_fooditem.html', {'form': form})

def success(request):
    return render(request, 'success.html')