import os
import sys
import django
import time
import win32print

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurantSite.settings")
django.setup()

ENABLE_PRINTING = False  # Set to True if you have a printer

from menuPage.models import Order

def print_receipt(order):
    PRINTER = "POS-80C"
    CUT_PAPER = b'\x1D\x56\x42\x00'
    LINE_FEED = b'\n'

    restaurant_name = order.restaurant.name
    table_number = order.table.table_number

    order_text = (
        f"Hello, welcome to {restaurant_name}!\n"
        "Thank you for visiting.\n"
        "Here is your order:\n\n"
    )

    total_price = 0.0

    for item in order.items:
        food_name = item["food_item_name"]
        food_price = float(item["food_item_price"])
        quantity = item["quantity"]

        item_total = food_price * quantity
        total_price += item_total

        order_text += f"{quantity}x {food_name} - ${item_total:.2f}\n"

    order_text += (
        "\n"
        f"Total: ${total_price:.2f}\n"
        "---------------------\n"
        "Enjoy your meal!\n\n"
        f"Order ID: {order.id}\n"
        f"Table Number: {table_number}\n"
        f"Timestamp: {order.order_date}\n"
    )

    print(order_text)

    formatted_text = order_text.encode('utf-8') + LINE_FEED * 3

    if ENABLE_PRINTING:
        try:
            hPrinter = win32print.OpenPrinter(PRINTER)
            try:
                hJob = win32print.StartDocPrinter(hPrinter, 1, ("Receipt", None, "RAW"))
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, formatted_text)
                win32print.WritePrinter(hPrinter, CUT_PAPER)
                win32print.EndPagePrinter(hPrinter)
                win32print.EndDocPrinter(hJob)
                print("Receipt sent to printer.")
            finally:
                win32print.ClosePrinter(hPrinter)
        except Exception as e:
            print("Printer not available. Falling back to console output.")
            print(f"Printer error: {e}")
    else:
        print("Printing disabled. Receipt shown above.")


def watch_orders():
    print("Watching for new orders...")

    last_seen_id = None

    while True:
        if last_seen_id:
            new_orders = Order.objects.filter(id__gt=last_seen_id).order_by('id')
        else:
            new_orders = Order.objects.all().order_by('id')

        for order in new_orders:
            print("New order detected. Printing receipt...")
            print_receipt(order)
            last_seen_id = order.id

        time.sleep(3)  # check every 3 seconds


if __name__ == "__main__":
    watch_orders()