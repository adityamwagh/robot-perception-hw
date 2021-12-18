import cv2
import matplotlib.pyplot as plt
import pyAprilTag

img = cv2.imread("picture1.jpg")
ids, corners, centers, Hs = pyAprilTag.find(img)
if img.ndim == 3:
    img = img[:, :, ::-1]  # BGR => RGB
print(ids)
plt.imshow(img)
plt.show()


# get calibration matrix
K = get_calib_from_log().K
distCoeffs = get_calib_from_log().distCoeffs

# get R, t from Homography
num, Rs, Ts, Ns = cv2.decomposeHomographyMat(Hs, K)

# compute camera matrix - take first 2 rows of R, and concatenate it to t
P = K @ np.concatenate((Rs[1][:, 0:2], Ts[1]), axis=1)

# add corners to an array
corners = np.r_[corners[0].T, np.array([[1, 1, 1, 1]])]

# project ponp.rounds to 3D
corners_3D = np.linalg.inv(P) @ corners
corners = corners[:2]

    
corners_3D


new_P = K @ np.c_[Rs[1], Ts[1]]
new_corners_3D = [
    [0.64362657, 0.43640331, 0.37787371, 0.56456077],
    [0.37340871, 0.41298599, 0.11923397, 0.1092112],
    [
        (0.36343648 - (0.564560770 - 0.37787371)),
        (0.58801459 - (0.564560770 - 0.37787371)),
        (0.68424048 - (0.564560770 - 0.37787371)),
        (0.47916178 - (0.564560770 - 0.37787371)),
    ,
    [1, 1, 1, 1],


new_P



new_corners = new_P @ new_corners_3D
new_corners


    
new_corners = new_corners[:2]
new_corners


    
def draw_cube(image, corners1, corners2):
    cv2.rectangle(
        image,
        (
            np.round(corners1[0][0]).astype(\"int\"),
            np.round(corners1[1][0]).astype(\"int\"),
        ),
        (
            np.round(corners1[0][2]).astype(\"int\"),
            np.round(corners1[1][2]).astype(\"int\"),
        ),
        (0, 0, 255),
        5,
    )
    cv2.rectangle(
        image,
        (
            np.round(corners2[0][0]).astype(\"int\"),
            np.round(corners2[1][0]).astype(\"int\"),
        ),
        (
            np.round(corners2[0][2]).astype(\"int\"),
            np.round(corners2[1][2]).astype(\"int\"),
        ),
        (0, 0, 255),
        5,
    )
    cv2.line(
        image,
        (np.round(corners1[0][0]).astype(\"int\"), np.round(corners1[1][0]).astype(\"int\")),
        (np.round(corners2[0][0]).astype(\"int\"), np.round(corners2[1][0]).astype(\"int\")),
        (0, 0, 255),
        5,
    )
    cv2.line(
        image,
        (np.round(corners1[0][2]).astype(\"int\"), np.round(corners1[1][2]).astype(\"int\")),
        (np.round(corners2[0][2]).astype(\"int\"), np.round(corners2[1][2]).astype(\"int\")),
        (0, 0, 255),
        5,
    )



    
draw_cube(img, corners, new_corners)
cv2.imshow(\"cube\", img)
# plt.show(temp)

# Press 0 to destroy all windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
