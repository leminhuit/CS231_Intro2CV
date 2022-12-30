import cv2
import numpy as np

array_H = cv2.imread("test.jpg");
array_F = [[1,2,3],[4,5,6],[7,8,9]];
array_F = np.array(array_F);

# Cross Correlation
def crossCorrelation(H: np.array, F:np.array) -> np.array:
    Hshape, Fshape = H.shape, F.shape
    result = np.zeros((Hshape[0] - Fshape[0], Hshape[1] - Fshape[1]))
    for i in range(Hshape[0] - Fshape[0]):
        for j in range(Hshape[1] - Fshape[1]):
            result[i][j] = np.sum(H[i:i + Fshape[0], j : j + Fshape[1]] * F)
    return result

result_cCorr = crossCorrelation(array_H, array_F);
cv2.imshow("Result", result_cCorr);
cv2.waitKey()
# Convolution

# Flip the filter 180 degrees
flipFilter = np.flipud(np.fliplr(array_F));
# print(flipFilter);

# Since we already flipped the filter, we can use the same code as Cross Correlation
# results = []
# u = 0;
# for i in range(3, array_H.shape[0], 1):
#     p = 0;
#     result = [];
#     for j in range(3, array_H.shape[1], 1):
#         result.append(sum(sum(array_H[u:i, p:j] * array_F)));
#         p += 1;
#     results.append(result);
#     u += 1;

# result_img = np.array(results);
# result_img = result_img.astype(np.uint8);
# cv2.imshow("Result", result_img);
# cv2.waitKey();