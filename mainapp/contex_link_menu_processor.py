from .models import ProductCategory

def links_menu(request):
    links_menu = ProductCategory.objects.filter(is_active=True)

    return {
        "links_menu": links_menu
    }