"""
An Example for detecting image responses using Content-Type from HTTP headers.

Run as follows: mitmproxy -s detect-image.py
"""

class ImageInterceptor:
    def response(self, flow):
        content_type: str = flow.response.headers.get(b'Content-Type')
        if 'image' in content_type:
            flow.kill()


addons = [ImageInterceptor()]
