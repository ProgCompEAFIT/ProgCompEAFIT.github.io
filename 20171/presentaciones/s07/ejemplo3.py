from PIL import Image
import numpy as np
import ejemplo2 as ej

datos = ej.cll(1000,1000,0,255)
img = Image.fromarray(np.uint8(datos))
img.show()
