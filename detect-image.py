"""
An Example for detecting image responses using Content-Type from HTTP headers.

Run as follows: mitmdump -s detect-image.py
"""

import requests


class ImageInterceptor:
    async def response(self, flow):
        content_type: str = flow.response.headers.get(b'Content-Type')
        if content_type is not None and 'image' in content_type:  # detect image
            image = flow.response.content
            response = requests.post(
                'https://youmo-api.transign.co/classify',
                files={'image': image},
            )
            flow.response.content = response.content


addons = [ImageInterceptor()]
