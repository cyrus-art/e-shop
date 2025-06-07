from django.contrib import admin
from .models import Login, Iteam, Customer

# Register the models to make them accessible in the Django admin interface
admin.site.register(Login)
admin.site.register(Iteam)
admin.site.register(Customer)
