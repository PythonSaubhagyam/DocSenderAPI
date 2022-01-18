
from PIL import Image
from io import BytesIO
import base64
from datetime import datetime
import io

file= BytesIO(base64.b64decode("/home/parth/Documents/DocSenderAPI/upload_images/sample1.png"))
# now=datetime.now()
# ext='.jpeg'
# filename = secure_filename(str(now)+ext)
file_converted=base64.b64decode(file)
image=Image.open(io.BytesIO(file_converted))