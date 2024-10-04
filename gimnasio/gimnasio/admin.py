from django.contrib import admin

from .models import Monitor
admin.site.register(Monitor)

from .models import Maquina
admin.site.register(Maquina)

from .models import Clase
admin.site.register(Clase)
