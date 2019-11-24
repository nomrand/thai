import os
from tf import calltf

# requires
# * tensorflow==1.x
# * tensorflow_hub

image_path = "img/d.jpg"
image_path = os.path.join(os.path.dirname(__file__), image_path)
result = calltf.predict(image_path)


print(result)
