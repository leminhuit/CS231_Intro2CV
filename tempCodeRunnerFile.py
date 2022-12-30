for i in range(src.shape[0]):
#     for j in range(src.shape[1]):
#         for t in range(72):
#             T[i,j] = (1 - t/(3*24)) * src[i,j] + (t/(3*24))*des[i,j]
#             cv2.imshow('Animation', T)
#             cv2.waitKey(1)