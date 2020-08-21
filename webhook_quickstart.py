from json import dumps

from httplib2 import Http


def quickstart(message_to_chat: str):
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAAwUkULtw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4Qr5a0_wtQXJWsLEpEyF1KpNTSWxQELOmLgAnwF21Vo%3D'
    # url for Application Errors chat room: 'https://chat.googleapis.com/v1/spaces/AAAABwSxnOU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=euU7Cd6lDvff5VWPU1u3pEmRUPeh3Y-UyWmo89pHU0M%3D'
    bot_message = {
        'text' : message_to_chat
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)
