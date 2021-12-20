import cv2
import numpy as np
import glob
from natsort import natsorted
from scipy.cluster.vq import kmeans, vq
from sklearn.neighbors import NearestNeighbors


class bovw:
    def __init__(self, train_image, query_image):
        self.train_image = train_image
        self.query_image = query_image

    # extract descriptor of all train image (database)
    def descriptor_train(self):
        des_imgtrain_list = []
        for count, image in enumerate(self.train_image):
            image_read = cv2.imread(image)
            image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
            sift = cv2.SIFT_create()
            kp, des = sift.detectAndCompute(image_gray, None)
            des_imgtrain_list.append(des)
            print(count, "t")
        # combine all descriptor in a single list
        des_train_ex = []
        for desimgtrain in des_imgtrain_list:
            print("uuuu")
            des_train_ex.extend(desimgtrain)

        return des_train_ex, des_imgtrain_list

    # extract descriptor of query image
    def descriptor_query(self):
        des_imgquery_list = []
        for count, image in enumerate(self.query_image):
            image_read = cv2.imread(image)
            image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
            sift = cv2.SIFT_create()
            kp, des = sift.detectAndCompute(image_gray, None)
            des_imgquery_list.append(des)
            print(count, "q")
        return des_imgquery_list

    def kmeans(self):
        des_train_ex, des_imgtrain_list = self.descriptor_train()
        des_imgquery_list = self.descriptor_query()
        k = 200
        print("i")
        # gives us the visual word dictionary
        visual_words, euclid_dist = kmeans(des_train_ex, k, 1)
        print("vw extracted")

        # database images
        # assigning visual word cluster by inputting image observation i.e train image descriptor
        total_histo_train = []
        for i in range(len(self.train_image)):
            print("check_t")
            assign_vw, distance = vq(des_imgtrain_list[i], visual_words)
            histo_train = (np.zeros((200)), "float32")
            for j in assign_vw:
                histo_train[j] = histo_train[j] + 1
            total_histo_train.append(histo_train[j])

        # query image
        # assigning visual word cluster by inputting image observation i.e query image descriptor
        total_histo_query = []
        for i in range(len(self.query_image)):
            print("check_q")
            assign_vw, distance = vq(des_imgquery_list[i], visual_words)
            histo_query = (np.zeros((200)), "float32")
            for j in assign_vw:
                histo_query[j] = histo_query[j] + 1
            total_histo_query.append(histo_query[j])

        # computing the index value to find the similar match of query image
        ngh = NearestNeighbors(n_neighbors=1)
        ngh.fit(total_histo_train)
        distance, nearest_index = ngh.kneighbors(total_histo_query)
        # gives 5 index values (train image) which are similar to query image
        print(nearest_index)


def main():

    # Image frames from TUM_RGB dataset
    train_image = glob.glob(
        "C:/Users/yashp/Downloads/HW2-TheDevilIsinTheDetail (1)/database/*.png"
    )
    query_image = glob.glob(
        "C:/Users/yashp/Downloads/HW2-TheDevilIsinTheDetail (1)/queries/*.png"
    )
    # image_frame = os.listdir(dataset)
    train_image = natsorted(train_image)
    query_image = natsorted(query_image)

    bagofvisualwords = bovw(train_image, query_image)

    # bagofvisualwords.descriptor()
    bagofvisualwords.kmeans()


if __name__ == "__main__":
    main()
