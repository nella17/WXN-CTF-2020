from PIL import Image

mp = {}
mp[(0,0,0,255)] = '-1'
mp[(255,255,255,255)] = '1'
mp[(255,255,255,0)] = '0'
mp[(0,0,0,0)] = '0'

img = Image.open('hint.png')
pxs = img.load()
(w, h) = img.size
hint = []
for i in range(h):
    l = []
    for j in range(w):
        l.append(mp[pxs[j,i]])
    hint.append(l)

print(','.join([','.join(l) for l in hint]))
