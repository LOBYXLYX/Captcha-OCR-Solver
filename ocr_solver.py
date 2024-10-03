import requests
import base64
import re
import sys
import random

class OCRSolver:
    """
    Code:

        ocr = Solver(image_path='captcha_image.png')
        code = ocr.extract()
        print(code)
    """

    def __init__(self, *, image_base64=None, image_path=None):
        self.img_b64 = image_base64
        self.img_path = image_path

        self.session = requests.Session()
        self.session.headers = {
            'origin': 'https://www.imagetotext.cc',
            'referer': 'https://www.imagetotext.cc/',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1',
            'X-Requested-With': 'XMLHttpRequested'
        }
        self._ocr_setup()

    def _ocr_setup(self):
        site = self.session.get('https://www.utilities-online.info/image-to-text')
        
        comp = re.compile(r'"csrf-token" content=\s*"([^"]+)"')
        self.session.headers['X-Csrf-Token'] = comp.findall(site.text)[0]
        self.session.cookies = site.cookies

    def _upload_path_image(self) -> str:
        with open(self.img_path, 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        return f'data:image/png;base64,{base64_image}'

    def save_decoded_image(self, save_as=None):
        if save_as is None:
            save_as = 'ocrimage_{random.randint(100,999)}'

        decoded_image = base64.b64decode(self.img_b64.replace('data:image/jpeg;base64,', '').replace('data:image/png;base64,', '').replace('\n', ''))

        with open(save_as + '.png', 'wb') as file:
            file.write(decoded_image)

    def extract(self) -> str:
        image_base = None

        if self.img_path:
            image_base = self._upload_path_image()
        elif self.img_b64:
            image_base = self.img_b64

        solve = self.session.post(
            'https://www.utilities-online.info/image_to_text',
            data={
                'base64': image_base
            }
        )
        if not len(solve.json()['text']) > 6:
            return None

        return solve.json()['text'].split('<br />\r\n')[1]

