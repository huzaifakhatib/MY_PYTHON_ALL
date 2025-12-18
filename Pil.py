# import requests
# from PIL import Image
# from io import BytesIO
# r = requests.get("https://in.images.search.yahoo.com/images/view;_ylt=Awr1QjnqISNpxcgx1Me9HAx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkA2NjMzBiZjE0OTIwOGY2YWIwY2IxOWFhOWMxNDYwYmM2BGdwb3MDMTAEaXQDYmluZw--?back=https%3A%2F%2Fin.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dimages%26type%3DE210IN714G0%26fr%3Dmcafee%26fr2%3Dpiv-web%26tab%3Dorganic%26ri%3D10&w=1920&h=1080&imgurl=www.pixelstalk.net%2Fwp-content%2Fuploads%2F2016%2F08%2FBest-Nature-Full-HD-Images-For-Desktop.jpg&rurl=https%3A%2F%2Fwww.pixelstalk.net%2Fbest-nature-full-hd-images-free-download%2F&size=277KB&p=images&oid=cc30bf149208f6ab0cb19aa9c1460bc6&fr2=piv-web&fr=mcafee&tt=Best+Nature+Full+HD+Images+-+PixelsTalk&b=0&ni=21&no=10&ts=&tab=organic&sigr=VcgFgJ3P24VR&sigb=9.25Nhy1Ap.Q&sigi=g3nbLikWwiCa&sigt=FaDt3BJXSaHd&.crumb=5jWMx/qx9bk&fr=mcafee&fr2=piv-web&type=E210IN714G0")
# i=image_open(BytesIO(r.content))
# fp=open('dimg1.jpg','wb')
# i=i.save(fp)
# fp.close()
import requests
from PIL import Image
from io import BytesIO

# Use the direct image URL
url = "https://www.pixelstalk.net/wp-content/uploads/2016/08/Best-Nature-Full-HD-Images-For-Desktop.jpg"

# Fetch the image
r = requests.get(url)

# Open the image from bytes
i = Image.open(BytesIO(r.content))

# Save the image to disk
i.save("dimg1.jpg")