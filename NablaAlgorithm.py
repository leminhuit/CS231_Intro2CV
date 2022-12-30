import cv2 
import numpy as np
from numpy import sqrt
from tqdm import tqdm
import imutils

#Ma trận năng lượng
def compute_energy_matrix(img): 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    x=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3) 
    y=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3) 
    return np.sqrt(np.square(x)+np.square(y))

# Ma trận chi phí
def compute_cost_matrix(energy):
    rows,cols=energy.shape
    cost=np.zeros(energy.shape)
    cost[0,:]=energy[0,:] # các giá trị cost tại hàng đầu tiên sẽ bằng hàng đầu tiên của ma trận năng lượng

    for i in range(1,rows):
        for j in range(cols):
            c1=max(j-1,0)      # chỉ số đầu là j-1, nếu j-1<0 thì chỉ số đầu là 0
            c2=min(cols,j+2)  # chỉ số cuối là j+1, nếu j+1>cols-1 thì chỉ số cuối là cols-1
            cost[i][j] = energy[i][j]+cost[i-1,c1:c2].min()
    return cost

def find_seam(cost):
    rows,cols=cost.shape
    seam=[]
    i_seam=cost[rows-1][:].argmin() # tìm vị trí min(cost) kết hợp với việc đây là ma trận
    # nên số dòng phải trừ đi 1, hàm argmin trả về indicie của giá trị nhỏ nhất
    seam.insert(0,i_seam) # bỏ giá trị đầu tiên vào mảng seam tại vị trí 0

    for i in range(rows-1,0,-1):
        c1=max(i_seam-1,0)   
        c2=min(cols,i_seam+2)
        i_seam=max(i_seam-1,0)+cost[i-1,c1:c2].argmin() 
        seam.insert(0,i_seam)
    return seam

# Vẽ đường seam dọc
def draw_seam(img, seam): 
    img_seam=np.copy(img)
    x,y=np.transpose([(i,j) for i,j in enumerate(seam)]) # tọa độ của tất cả các điểm ảnh trên đường seam
    img_seam[x,y]=(0,255,0) 
    return img_seam

# Loại bỏ các pixel trên đường seam
def remove_seam(img, seam): 
    rows, cols=img.shape[:2] 
    for row in range(rows): 
        for col in range(seam[row], cols-1): 
            img[row, col]=img[row, col+1] 
    img=img[:, 0:cols-1] 
    return img 
 
input=cv2.imread('./Images/fore.png') 
num_seams=int(0.1*input.shape[1]) # tỉ lệ resize ảnh là 50% chiều ngang
print(num_seams)

img=np.copy(input) 
img_overlay_seam=np.copy(input) 
energy=compute_energy_matrix(img) 
energy_before=energy
cost=compute_cost_matrix(energy)

for i in range(num_seams): 
    seam=find_seam(cost)
    img_overlay_seam=draw_seam(img_overlay_seam, seam)
    img=remove_seam(img, seam) 
    energy=compute_energy_matrix(img)
    cost=compute_cost_matrix(energy)
    print('Number of seams removed = ', i+1) 
 
cv2.imshow('Input', input) 
cv2.imshow('Seams', img_overlay_seam) 
cv2.imshow('Output', img) 
cv2.waitKey(0) 

