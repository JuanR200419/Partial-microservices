import json


def hello(event, context):
    body =

    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "country": "USA",
        "status": "Active"
    }




    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def hello2(event, context):
    body =


     {
            "id": 2,
            "name": "Jane Smith",
            "age": 28,
            "country": "Canada",
            "status": "Inactive",
            "email": "jane.smith@email.com",
            "phone": "+1-555-1234",
            "city": "Toronto",
            "zip_code": "M5V 2T6",
            "registered": True
        }





    response = {"statusCode": 200, "body": json.dumps(body)}

    return response





