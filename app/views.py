from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.functions import send_data


# Create your views here.
@api_view(['POST'])
def getData(request):
    shop_url = request.data.get('shop_url')
    access_token = request.data.get('access_token')
    product_data = {
        "title": "jeweleryssssssssssssssssss",
        "body_html": "<p>This is a sample product description.</p>",
        "vendor": "Sample Vendor",
        "product_type": "Sample Type",
        "variants": [
            {
                "option1": "Blue",
                "price": "10.00",
                "sku": "SAMPLE-BLUE"
            },
            {
                "option1": "Red",
                "price": "12.00",
                "sku": "SAMPLE-RED"
            }
        ]
    }

    response = send_data(product_data, shop_url, access_token)
    # Ensure that the status_code is an integer
    status_code = int(response.status_code)

    # Return the response with the correct status code
    return Response(response.data, status=status_code)
