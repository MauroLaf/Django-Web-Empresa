from .models import Page
import unicodedata

#Normalizo el codigo por si cargan con un formato no admitido
def normalize_key(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.replace(" ", "_")
    return text

def context_dict_page(request):
    pages = Page.objects.all()
    return {
        'all_pages': {
            normalize_key(page.title): page for page in pages
        }
    }

