from torchvision import models
fcn = models.segmentation.fcn_resnet101(pretrained=True).eval()

from PIL import Image
import matplotlib.pyplot as plt
import torch
 
pth = './img1.jpeg'
img = Image.open(pth)
print(img.size)
plt.imshow(img);
plt.show()

import torchvision.transforms as T
trf = T.Compose([T.Resize((256,256)),
                 T.ToTensor(), 
                 T.Normalize(mean = [0.485, 0.456, 0.406], 
                             std = [0.229, 0.224, 0.225])])
inp = trf(img).unsqueeze(0)

out = fcn(inp)['out']
print (out.shape)

import numpy as np
om = torch.argmax(out.squeeze(), dim=0).detach().cpu().numpy()
print (om.shape)

print (np.unique(om))

def decode_segmap(pth, image, nc=21):
   
    label_colors = np.array([(0, 0, 0),  # 0=background
               # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
               (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
               # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
               (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
               # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
               (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
               # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
               (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)])
 
    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)

    img = Image.open(pth)
    img1 = img.resize((256,256))
    plt.imshow(img1);
    plt.show()
    w,h = img1.size
    for x in range(w):
      for y in range(h):
        if(image[y,x] != 15):
          img1.putpixel((x,y),0)
    plt.imshow(img1);
    plt.show()
   
    for l in range(0, nc):
      idx = image == l
      r[idx] = label_colors[l, 0]
      g[idx] = label_colors[l, 1]
      b[idx] = label_colors[l, 2]
     
    rgb = np.stack([r, g, b], axis=2)
    return rgb

rgb = decode_segmap(pth, om)
plt.imshow(rgb);
plt.show()

def segment(net, path):
  img = Image.open(path)
  plt.imshow(img);
  plt.show()
  trf = T.Compose([T.Resize((256,256)), T.ToTensor(), T.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])])
  inp = trf(img).unsqueeze(0)
  out = net(inp)['out']
  om = torch.argmax(out.squeeze(), dim=0).detach().cpu().numpy()
  rgb = decode_segmap(path, om)
  plt.imshow(rgb);
  plt.show()

segment(fcn, './img1.jpeg')