from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from myapp.models import Iteam, Login ,Customer




# Home view
def first(request):
    return render(request, 'first.html')  # Your home page view logic

# Second view - Handles user login
def second(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')

        # Save the user details to the database
        obj = Login(user_name=user_name, phone_number=phone_number)
        obj.save()
        return redirect('third')  # Redirect to the next page
    return render(request, 'second.html')

# Third view - After login page (no logic change)
def third(request):

        # Redirect to the third page, passing all login data
    return render(request, 'third.html')

# Four view - Handle cart item addition
def four(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        total = request.POST.get('total')

        # Ensure the item data is valid before saving
        if item_name and price and total:
            # Save item details to the cart (you may want to add user association here)
            item = Iteam(item_name=item_name, price=float(price), total=float(total), user_name=request.user.username)
            item.save()
            return redirect('five')
        else:
            return HttpResponse("Missing data. Please try again.", status=400)

    return render(request, 'four.html')

# Five view - Show cart items and total value
def five(request):
    # Get all items in the cart for the logged-in user
    cart_items = Iteam.objects.filter(user_name=request.user.username)

    # Calculate the total value of the cart (if the 'total' field exists)
    total_value = sum(item.total for item in cart_items)  # Sum the 'total' field of all items
    return render(request, 'four.html', {'cart_items': cart_items, 'total_value': total_value})

# View for adding items to the cart (Improved version)
def add_to_cart(request):
    if request.method == 'POST':
        # Retrieve the form data
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        user_name = request.POST.get('user_name')
        quantity = request.POST.get('quantity', 1)  # Assume 1 if quantity is not provided

        # Ensure that the price is valid
        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            return HttpResponse("Invalid price or quantity. Please enter valid data.", status=400)

        # Calculate total price for the item (price * quantity)
        total_ordering = price * quantity

        # Create a new Iteam object and save it to the database
        obj = Iteam()
        obj.item_name = item_name
        obj.price = price
        obj.total = total_ordering
        obj.user_name = user_name  # Link item to the logged-in user
        obj.save()  # Save the new cart item

        # Redirect to the 'five' page to display the updated cart
        return redirect('five')  # Ensure you have a URL pattern for 'five'

    # If the request is not a POST, render the third page
    return render(request, 'third.html')



def remove_item_from_cart(request, item_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Get the item from the cart using item_id
        item = get_object_or_404(Iteam, id=item_id)

        # Remove the item from the cart
        item.delete()

        # Recalculate the total value of the cart for the logged-in user
        cart_items = Iteam.objects.filter(user_name=request.user.username)
        total_value = sum(item.total for item in cart_items)

        # Return success response with updated total value
        return JsonResponse({'success': True, 'total_value': total_value})
    
    # If not an AJAX request or POST method, return failure response
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def men(request):
    return render(request,'men.html')

def women(request):
    return render(request,'women.html')

def kids(request):
    return render(request,'kids.html')

def about(request):
    return render(request ,'about.html')

def contact(request):
    return render(request,'contact.html')

def help(request):
    return render(request,'help.html')



def customer_msg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        message = request.POST.get('message')


        # Create a new customer object and save it to the database
        try:
            obj = Customer()
            obj.name=name
            obj.mail=mail
            obj.message=message
            obj.save()  # Save the object to the database
            messages.success(request, "Your message was sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")
            return redirect('contact')

        return redirect('contact')


