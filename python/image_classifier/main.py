import os
from tf import calltf


retain()

image_path = "img/d.jpg"
image_path = os.path.join(os.path.dirname(__file__), image_path)
calltf.predict(image_path)
