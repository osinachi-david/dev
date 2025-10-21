import json
from  django.http import JsonResponse
from django.forms.models import model_to_dict
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
    # if model_data:
    #     # Converting model instance to dictionary
    #     data = model_to_dict(model_data, fields=['id', 'title','price'])
    #     # data["id"] = model_data.id
    #     # data["title"] = model_data.title
    #     # data["content"] = model_data.content
    #     # data["price"] = model_data.price
    # return JsonResponse(data)

    # OR

    # if model_data:
    #     data = {
    #         "id": model_data.id,
    #         "title": model_data.title,
    #         "content": model_data.content,
    #         "price": model_data.price
    #     }
    #     return JsonResponse(data)
    # return JsonResponse({"message": "No product found"}, status=404)