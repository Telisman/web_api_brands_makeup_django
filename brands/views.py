from django.shortcuts import render
from .models import Brands
import requests


# def get_brands(request):
#     check = Brands.objects.all().order_by('-id')
#     if check.count() == 0:
#         url = 'http://makeup-api.herokuapp.com/api/v1/products.json'
#         response = requests.get(url)
#         data = response.json()
#         for result in data:
#             brand_data = Brands(
#                 name=result['name'],
#                 price=result['price'],
#                 image_link=result['image_link'],
#                 brand=result['brand'],
#                 category=result['category'],
#                 product_type=result['product_type'],
#                 description=result['description'],
#             )
#             brand_data.save()
#
#         else:
#             pass
#     return render(request, 'brands/makeup_brands.html', {"check": check})


def BootstrapFilterView(request):
    brand = Brands.objects.all()
    name_brand = request.GET.get("name")
    if brand.count() == 0:
        url = 'http://makeup-api.herokuapp.com/api/v1/products.json'
        response = requests.get(url)
        data = response.json()
        for result in data:
            brand_data = Brands(
                name=result['name'],
                price=result['price'],
                image_link=result['image_link'],
                brand=result['brand'],
                category=result['category'],
                product_type=result['product_type'],
                description=result['description'],
            )
            brand_data.save()

        else:
            pass

    if name_brand != '' and name_brand is not None:
        qs=brand.filter(brand__icontains = name_brand)
        context = {
            'gueryset': qs
        }

        return render(request,'brands/makeup_brands.html',context)

    return render(request,'brands/makeup_brands.html',{ "brand":brand })