from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)

# from django_tenants.utils import schema_context
# from users.models import User

# with schema_context('devnest'):
#     # Crear el superusuario
#     superuser = User.objects.create_superuser(
#         email='devnest@devnest.com',
#         username='devnestinnova',
#         first_name='DevNest',
#         last_name='Innova',
#         password='kofla10*',
#   )
