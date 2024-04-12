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
