```python
from ocr_solver import OCRSolver

# from an existing image
ocr = OCRSolver(image_path='captcha.png')
print(ocr.extract())

# from a base64 image
ocr = OCRSolver(image_base64='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYAB......')
print(ocr.extract())

# save image png (from a base64)
ocr.save_decoded_image()
```

![cap](https://github.com/LOBYXLYX/Captcha-OCR-Solver/blob/main/TCRA.png)
![solv](https://github.com/LOBYXLYX/Captcha-OCR-Solver/blob/main/20241002_203730.jpg)
