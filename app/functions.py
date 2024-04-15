import json
import requests
from rest_framework.response import Response


def send_data(product_data, shop_url, access_token):
    url = f"{shop_url}/admin/api/2022-01/products.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": access_token
    }
    payload = {
        "product": product_data
    }

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    status_code = int(response.status_code)
    if status_code == 201:
        return Response({"Message": "Product created successfully:", "Response": response_data['product']}, status=status_code)
    else:
        return Response({"Message": "Failed to create product:", "Response": response_data}, status=status_code)


def retrivedata(api_url, user_id):

    # Define the request payload
    payload = {"user_id": user_id}

    # Make the POST request
    response = requests.post(api_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        return data
    else:
        return Response("Failed to fetch data. Status code:", response.status_code)


def fetch_data(api_url, user_id=None):
    # Define the request payload
    payload = {}
    
    # Include user_id in payload if provided
    if user_id is not None:
        payload["user_id"] = user_id

    # Make the POST request
    response = requests.post(api_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        return data
    else:
        return Response("Failed to fetch data. Status code:", response.status_code)
