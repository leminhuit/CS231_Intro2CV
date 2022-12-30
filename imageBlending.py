import cv2
import imageio
import numpy as np
from PIL import Image

# Theo hướng dẫn của LuyenCongML

# đọc ảnh foreground
fg = cv2.imread('./Images/foreground.png')
fg = cv2.cvtColor(fg, cv2.COLOR_BGR2RGB)
print('Kich thuoc theo tung kenh cua foreground: ', fg.shape)

# # đọc ảnh effect
eff = cv2.imread('./Images/effect.png')
print('Kich thuoc theo tung kenh cua eff: ', eff.shape)

# đọc ảnh mask
mask = cv2.imread('./Images/mask.png', cv2.IMREAD_UNCHANGED)
print('Kich thuoc theo tung kenh cua mask: ', mask.shape)

# # Resize lại ảnh cho cùng size theo ảnh nhỏ nhất
width = 417;
height = 598;
dim = (width, height);
eff_resized = cv2.resize(eff, dim, interpolation = cv2.INTER_AREA)
fg_resized = cv2.resize(fg, dim, interpolation = cv2.INTER_AREA)

# Hiện thị hai ảnh lên màn hình
cv2.imshow('Foreground', fg_resized)
cv2.imshow('Background', eff_resized)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

#Sao chép ảnh qua biến mới (nhưng cách làm 2 vòng for khá là chậm)
result_for_loop = fg_resized.copy()
alpha = 0.65
for x in range(mask.shape[0]): # result.shape[0]: chiều cao ảnh
    for y in range(mask.shape[1]): # result.shape[1]: chiều rộng ảnh
        if (mask[x,y,3] != 0): # Kiểm tra điểm ảnh
            result_for_loop[x,y] = (alpha * fg[x,y] + (1 - alpha) * eff_resized[x,y])

cv2.imshow('Result_For_loop', result_for_loop)
cv2.waitKey()

# Sử dụng cách khác
result_mix = fg_resized.copy()
alpha = 0.65
result_mix[mask[:,:,3] != 0] = fg_resized[mask[:,:,3] != 0] * alpha \
    + eff_resized[mask[:,:,3] != 0] * (1 - alpha)

cv2.imshow('Result', result_mix)
cv2.waitKey(0)

# Đọc file Gif
url = "https://media0.giphy.com/media/2vmiW6mcYgKst3QVDK/giphy.gif"
frames = imageio.mimread(imageio.core.urlopen(url).read(), '.gif')

fg_h, fg_w, fg_c = fg_resized.shape
bg_h, bg_w, bg_c = frames[0].shape
top = int((bg_h-fg_h)/2)
left = int((bg_w-fg_w)/2)
bgs = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]

results = []
alpha = 0.5
for i in range(len(bgs)):
    result = fg_resized.copy()
    result[mask[:,:,3] != 0] = alpha * result[mask[:,:,3] != 0]
    bgs[i][mask[:,:,3] == 0] = 0
    bgs[i][mask[:,:,3] != 0] = (1-alpha)*bgs[i][mask[:,:,3] != 0]
    result = result + bgs[i]
    results.append(result)

imageio.mimsave('result.gif', results)

# Nếu muốn effect nằm ngoài cơ thể
mask_invert = 255 - mask;
results_invert = [];
alpha = 0.5
for i in range(len(bgs)):
    result_invert = fg_resized.copy()
    result_invert[mask_invert[:,:,3] != 0] = alpha * result_invert[mask_invert[:,:,3] != 0]
    bgs[i][mask_invert[:,:,3] == 0] = 0
    bgs[i][mask_invert[:,:,3] != 0] = (1-alpha)*bgs[i][mask_invert[:,:,3] != 0]
    result_invert = result_invert + bgs[i]
    results_invert.append(result_invert)

imageio.mimsave('result_invert.gif', results_invert)

# Thêm Gaussian Blur để mask có sự chuyển đổi nhẹ nhàng 
mask_blur = cv2.GaussianBlur(mask, (15, 15), 0)
results_blur = []
alpha = 0.3
for i in range(len(bgs)):
    result_blur = fg_resized.copy()
    result_blur[mask_blur[:,:,3] != 0] = alpha * result_blur[mask_blur[:,:,3] != 0]
    bgs[i][mask_blur[:,:,3] == 0] = 0
    bgs[i][mask_blur[:,:,3] != 0] = (1-alpha)*bgs[i][mask_blur[:,:,3] != 0]
    result_blur = result_blur + bgs[i]
    results_blur.append(result_blur)

imageio.mimsave('result_blur.gif', results_blur)

mask_blur_invert = cv2.GaussianBlur(mask_invert, (15, 15), 0)
results_blur_invert = []
alpha = 0.3
for i in range(len(bgs)):
    result_blur_invert = fg_resized.copy()
    result_blur_invert[mask_blur_invert[:,:,3] != 0] = alpha * result_blur_invert[mask_blur_invert[:,:,3] != 0]
    bgs[i][mask_blur_invert[:,:,3] == 0] = 0
    bgs[i][mask_blur_invert[:,:,3] != 0] = (1-alpha)*bgs[i][mask_blur_invert[:,:,3] != 0]
    result_blur_invert = result_blur_invert + bgs[i]
    results_blur_invert.append(result_blur_invert)

imageio.mimsave('result_blur_invert.gif', results_blur)

