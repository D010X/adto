from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.functions import send_data, retrivedata, fetch_data


# Create your views here.
@api_view(['POST'])
def getData(request):
    shop_url = request.data.get('shop_url')
    access_token = request.data.get('access_token')
    api_url = request.data.get('api')
    user_id = request.data.get('userid')

    if user_id != "none":
        product_data = retrivedata(api_url, user_id)

        response = send_data(product_data, shop_url, access_token)
        # Ensure that the status_code is an integer
        status_code = int(response.status_code)

        # Return the response with the correct status code
        return Response({"Message": "1", "Response": response.data}, status=status_code)

    else:
        product_data = fetch_data(api_url)

        response = send_data(product_data, shop_url, access_token)
        # Ensure that the status_code is an integer
        status_code = int(response.status_code)

        # Return the response with the correct status code
        return Response({"Message": "2", "Response": response.data, "original": product_data}, status=status_code)
