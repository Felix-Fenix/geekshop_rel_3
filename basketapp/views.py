from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    # content = {}
    # return render(request, "basketapp/basket.html", content)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    # print(basket, '************(((((((((((((((((((((((((((((((((((((((((((((((')
    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request):
    # content = {}
    # return render(request, "basketapp/basket.html", content)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_sum(request):
    basket_count = Basket.objects.filter(user=request.user).all()
    b1 = basket_count.filter(quantity__gt=0)
    queryset = Basket.objects.all()
    summ = sum([p.quantity for p in queryset])
    end_sum_list = []
    for i in queryset:
        d = Product.objects.get(id=i.product_id)
        pr = d.price
        end_sum_list.append(pr * i.quantity)
    return sum(end_sum_list)
