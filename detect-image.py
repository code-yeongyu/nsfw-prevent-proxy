"""
An Example for detecting image responses using Content-Type from HTTP headers.

Run as follows: mitmdump -s detect-image.py
"""

import time, requests


class ImageInterceptor:
    def response(self, flow):
        start = time.time()  # 시작 시간 저장
        content_type: str = flow.response.headers.get(b'Content-Type')
        if content_type is not None and 'image' in content_type:  # detect image
            image = flow.response.content
            response = requests.post(
                'https://youmo-api.transign.co/classify',
                files={
                    'image': image,
                },
                data={
                    'content_type': content_type,
                },
            )
            flow.response.content = response.content
            print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


addons = [ImageInterceptor()]
