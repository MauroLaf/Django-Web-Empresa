from django.contrib import admin
from .models import Link #importo mi clase link de mi modelo

# Register your models here.
# Cremo mi modelo para administrar mi clase link
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
#activamos en el admin site el modelo link pasandole el adm de prueba
admin.site.register(Link, LinkAdmin) #le paso mi clase modelo link y la clase para administrar y doy runserver