import cv2
import numpy as np
import mediapipe as mp


class ImageEditor:

    def __init__(self, img: str):
        self._mp_selfie_segmentation = mp.solutions.selfie_segmentation
        self._selfie_segmentation = self._mp_selfie_segmentation.SelfieSegmentation(model_selection=1)
        self._img = img

    def to_file(self, path: str):
        cv2.imwrite(path, self.img)

    @property
    def img(self):
        return self._img

    @classmethod
    def from_file(cls, image_file_path: str) -> "ImageEditor":
        img = cv2.imread(image_file_path)
        return cls(img)

    def segmentation_mask(self):
        RGB = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        # get the result
        results = self._selfie_segmentation.process(RGB)

        # extract segmented mask
        return results.segmentation_mask

    def without_background(self, new_background_color: int = 255):
        mask = self.segmentation_mask()
        condition = np.stack(
            (mask,) * 3, axis=-1) > 0.5
        # combine frame and background image using the condition
        return np.where(condition, self.img, 255)

    def as_cartoon(self, k: int = 8, remove_background: bool = True):
        """
        Turn the image into a cartoon.
        :param k: The number of clusters.
        :param remove_background: Whether to remove the background.
        :return: The cartoonized image.
        """
        img = self.img

        if remove_background:
            img = self.without_background()

        # Defining input data for clustering
        data = np.float32(img).reshape((-1, 3))

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        # Applying cv2.kmeans function
        _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        center = np.uint8(center)

        # Reshape the output data to the size of input image
        result = center[label.flatten()]
        result = result.reshape(img.shape)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Perform adaptive threshold
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)
        blurred = cv2.medianBlur(result, 3)

        # Combine the result and edges to get final cartoon effect
        return cv2.bitwise_and(blurred, blurred, mask=edges)