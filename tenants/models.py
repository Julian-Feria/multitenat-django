from django.db import models
from django_tenants.utils import tenant_context
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=200)
    auto_create_schema = True  

class Domain(DomainMixin):
    ...
