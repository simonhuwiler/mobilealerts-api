from flask import escape
import requests
from flask_cors import cross_origin
import json
import functions_framework

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0; Android SDK built for x86 Build/MASTER)',
    'Host': 'www.data199.com',
}

@cross_origin()
@functions_framework.http
def apiproxy(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    payload = request.get_json(force=True)
    
    url = 'https://www.data199.com/api/v1/dashboard'

    r = requests.post(url, headers=headers, data=payload)
    return r.json()

    # Local File (Tests)
    # print(request.get_json(force=True))
    # # print(request.to_json())
    # data = json.load(open('./test.json', 'r', encoding='UTF-8'))
    # return data
   