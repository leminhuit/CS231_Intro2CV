import cv2
import imageio

# đọc ảnh foreground
fg = cv2.imread('./Images/foreg.jpg')
print('foreground: ', fg.shape)

# đọc ảnh effect
eff = cv2.imread('./Images/eff.jpg')
eff = cv2.resize(eff, (fg.shape[1], fg.shape[0]))
print('eff: ', eff.shape)

# đọc ảnh mask
mask = cv2.imread('./Images/mask.png', cv2.IMREAD_UNCHANGED)
mask = cv2.resize(mask, (fg.shape[1], fg.shape[0]))
print('mask: ', mask.shape)

# show image
cv2.imshow('Foreground', fg)
cv2.imshow('Background', eff)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

url = "https://media0.giphy.com/media/2vmiW6mcYgKst3QVDK/giphy.gif"
frames = imageio.mimread(imageio.core.urlopen(url).read(), '.gif')

print(frames[0].shape)

# fg_h, fg_w, fg_c = fg.shape
# bg_h, bg_w, bg_c = frames[0].shape
# top = int((bg_h-fg_h)/2)
# left = int((bg_w-fg_w)/2)
# bgs = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]

# results = []
# alpha = 0.3
# for i in range(len(bgs)):
#     result = fg.copy()
#     result[mask[:,:,3] != 0] = alpha * result[mask[:,:,3] != 0]
#     bgs[i][mask[:,:,3] == 0] = 0
#     bgs[i][mask[:,:,3] != 0] = (1-alpha)*bgs[i][mask[:,:,3] != 0]
#     result = result + bgs[i]
#     results.append(result)

# imageio.mimwrite('result_from_1.gif', results)