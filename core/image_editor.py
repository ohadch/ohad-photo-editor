import cv2
import numpy as np
import mediapipe as mp


class ImageEditor:

    def __init__(self, img: str):
        self._mp_selfie_segmentation = mp.solutions.selfie_segmentation
        self._selfie_segmentation = self._mp_selfie_segmentation.SelfieSegmentation(model_selection=1)
        self._img = img

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