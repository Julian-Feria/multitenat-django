# from django.contrib import admin
# from django.db import connection  # Importa para obtener el esquema activo
# from tenants.models import Client, Domain

# # Solo registrar los modelos si estamos en el esquema `public`
# if connection.schema_name == "public":
#     @admin.register(Client)
#     class ClientAdmin(admin.ModelAdmin):
#         list_display = ("schema_name", "name")

#     @admin.register(Domain)
#     class DomainAdmin(admin.ModelAdmin):
#         list_display = ("domain", "tenant", "is_primary")
