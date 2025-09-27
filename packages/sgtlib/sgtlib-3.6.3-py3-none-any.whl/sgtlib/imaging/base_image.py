# SPDX-License-Identifier: GNU GPL v3

"""
Processes of an image by applying filters to it and converting it to a binary version.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from cv2.typing import MatLike
from dataclasses import dataclass
from skimage.morphology import disk
from skimage.filters.rank import autolevel, median

from ..utils.config_loader import load_img_configs
from ..utils.sgt_utils import safe_uint8_image



class BaseImage:
    """
    A class that is used to binarize an image by applying filters to it and converting it to a binary version.

    Args:
        raw_img (MatLike): Raw image in OpenCV format
        scale_factor (float): Scale factor used to downsample/up-sample the image.
    """

    @dataclass
    class ScalingKernel:
        """A data class for storing scaling kernel parameters."""
        image_patches: list[MatLike]
        kernel_shape: tuple
        # stride: tuple

    def __init__(self, raw_img: MatLike|None, cfg_file="", scale_factor=1.0):
        """
        A class that is used to binarize an image by applying filters to it and converting it to a binary version.

        Args:
            raw_img: Raw image in OpenCV format
            cfg_file (str): Configuration file path
            scale_factor (float): Scale factor used to downsample/up-sample the image.
        """
        self._configs: dict = load_img_configs(cfg_file)  # image processing configuration parameters and options.
        self._img_raw: MatLike | None = safe_uint8_image(raw_img)
        self._img_2d: MatLike | None = None
        self._img_bin: MatLike | None = None
        self._img_mod: MatLike | None = None
        self._img_hist: MatLike | None = None
        self._has_alpha_channel: bool = False
        self._scale_factor: float = scale_factor
        self._image_filters: list[BaseImage.ScalingKernel] = []
        self.init_image()

    @property
    def configs(self) -> dict:
        """Returns the image processing configuration parameters and options."""
        return self._configs

    @configs.setter
    def configs(self, configs: dict) -> None:
        """Sets the image processing configuration parameters and options."""
        self._configs = configs

    @property
    def img_raw(self) -> MatLike | None:
        """Returns the raw image in OpenCV format."""
        return self._img_raw

    @property
    def img_2d(self) -> MatLike | None:
        """Returns the processed image in OpenCV format."""
        return self._img_2d

    @img_2d.setter
    def img_2d(self, img_2d: MatLike | None) -> None:
        """Sets the processed image in OpenCV format."""
        self._img_2d = img_2d

    @property
    def img_bin(self) -> MatLike | None:
        """Returns the binary image in OpenCV format."""
        return self._img_bin

    @img_bin.setter
    def img_bin(self, img_bin: MatLike | None) -> None:
        """Sets the binary image in OpenCV format."""
        self._img_bin = img_bin

    @property
    def img_mod(self) -> MatLike | None:
        """Returns the modified image in OpenCV format."""
        return self._img_mod

    @img_mod.setter
    def img_mod(self, img_mod: MatLike | None) -> None:
        """Sets the modified image in OpenCV format."""
        self._img_mod = img_mod

    @property
    def img_hist(self) -> MatLike | None:
        """Returns the histogram of the processed image."""
        return self._img_hist

    @property
    def has_alpha_channel(self) -> bool:
        """Returns whether the image has an alpha channel."""
        return self._has_alpha_channel

    @property
    def scale_factor(self) -> float:
        """Returns the scale factor used to downsample/up-sample the image."""
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, scale_factor: float) -> None:
        """Sets the scale factor used to downsample/up-sample the image."""
        self._scale_factor = scale_factor

    @property
    def image_filters(self) -> list["BaseImage.ScalingKernel"]:
        """Returns the list of scaling kernels used to the image."""
        return self._image_filters

    @image_filters.setter
    def image_filters(self, image_filters: list["BaseImage.ScalingKernel"]) -> None:
        """Sets the list of scaling kernels used to the image."""
        self._image_filters = image_filters

    def reset_img_configs(self, cfg_file: str = "") -> None:
        """Resets the image processing configuration parameters and options."""
        self._configs = load_img_configs(cfg_file)

    def init_image(self) -> None:
        """
        Initialize the class member variables (or attributes).
        Returns:

        """
        if self._img_raw is None:
            return
        img_data = self._img_raw.copy()

        self._has_alpha_channel, _ = BaseImage.check_alpha_channel(self._img_raw)
        self._img_2d = img_data

    def get_pixel_width(self) -> None:
        """Compute pixel dimension in nanometers to estimate and update the width of graph edges."""

        def compute_pixel_width(scalebar_val: float, scalebar_pixel_count: int) -> float:
            """
            Compute the width of a single pixel in nanometers.

            :param scalebar_val: Unit value of the scale in nanometers.
            :param scalebar_pixel_count: Pixel count of the scalebar width.
            :return: Width of a single pixel in nanometers.
            """

            val_in_meters = scalebar_val / 1e9
            pixel_width = val_in_meters / scalebar_pixel_count
            return pixel_width

        opt_img = self._configs
        pixel_count = int(opt_img["scalebar_pixel_count"]["value"])
        scale_val = float(opt_img["scale_value_nanometers"]["value"])
        if (scale_val > 0) and (pixel_count > 0):
            px_width = compute_pixel_width(scale_val, pixel_count)
            opt_img["pixel_width"]["value"] = px_width / self._scale_factor

    def apply_img_crop(self, x: int, y: int, crop_width: int, crop_height: int, actual_w: int, actual_h: int) -> None:
        """
        A function that crops images into a new box dimension.

        :param x: Left coordinate of cropping box.
        :param y: Top coordinate of cropping box.
        :param crop_width: Width of cropping box.
        :param crop_height: Height of cropping box.
        :param actual_w: Width of actual image.
        :param actual_h: Height of actual image.
        """

        # Resize image
        scaled_img = cv2.resize(self._img_2d.copy(), (actual_w, actual_h))

        # Crop image
        self._img_2d = scaled_img[y:y + crop_height, x:x + crop_width]

    def process_img(self, image: MatLike) -> MatLike | None:
        """
        Apply filters to the image.

        :param image: OpenCV image.
        :return: None
        """

        opt_img = self._configs
        if image is None:
            return None

        def control_brightness(img: MatLike):
            """
            Apply contrast and brightness filters to the image

            param img: OpenCV image
            :return:
            """

            brightness_val = opt_img["brightness_level"]["value"]
            contrast_val = opt_img["contrast_level"]["value"]
            brightness = ((brightness_val / 100) * 127)
            contrast = ((contrast_val / 100) * 127)

            # img = np.int16(img)
            # img = img * (contrast / 127 + 1) - contrast + brightness
            # img = np.clip(img, 0, 255)
            # img = np.uint8(img)

            if brightness != 0:
                if brightness > 0:
                    shadow = brightness
                    max_val = 255
                else:
                    shadow = 0
                    max_val = 255 + brightness
                alpha_b = (max_val - shadow) / 255
                gamma_b = shadow
                img = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)

            if contrast != 0:
                alpha_c = float(131 * (contrast + 127)) / (127 * (131 - contrast))
                gamma_c = 127 * (1 - alpha_c)
                img = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)

            # text string in the image.
            # cv2.putText(new_img, 'B:{},C:{}'.format(brightness, contrast), (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            # 1, (0, 0, 255), 2)
            return img

        def apply_filter(filter_type: str, img: MatLike, fil_grad_x, fil_grad_y):
            """"""
            if filter_type == 'scharr' or filter_type == 'sobel':
                abs_grad_x = cv2.convertScaleAbs(fil_grad_x)
                abs_grad_y = cv2.convertScaleAbs(fil_grad_y)
                fil_dst = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
                fil_abs_dst = cv2.convertScaleAbs(fil_dst)
                result_img = cv2.addWeighted(img, 0.75, fil_abs_dst, 0.25, 0)
                return cv2.convertScaleAbs(result_img)
            return img

        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply brightness/contrast
        filtered_img = control_brightness(image)

        if float(opt_img["apply_gamma"]["dataValue"]) != 1.00:
            inv_gamma = 1.00 / float(opt_img["apply_gamma"]["dataValue"])
            inv_gamma = float(inv_gamma)
            lst_tbl = [((float(i) / 255.0) ** inv_gamma) * 255.0 for i in np.arange(0, 256)]
            table = np.array(lst_tbl).astype('uint8')
            filtered_img = cv2.LUT(filtered_img, table)

        # applies a low-pass filter
        if opt_img["apply_lowpass_filter"]["value"] == 1:
            h, w = filtered_img.shape
            ham1x = np.hamming(w)[:, None]  # 1D hamming
            ham1y = np.hamming(h)[:, None]  # 1D hamming
            ham2d = np.sqrt(np.dot(ham1y, ham1x.T)) ** int(
                opt_img["apply_lowpass_filter"]["dataValue"])  # expand to 2D hamming
            f = cv2.dft(filtered_img.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)
            f_shifted = np.fft.fftshift(f)
            f_complex = f_shifted[:, :, 0] * 1j + f_shifted[:, :, 1]
            f_filtered = ham2d * f_complex
            f_filtered_shifted = np.fft.fftshift(f_filtered)
            inv_img = np.fft.ifft2(f_filtered_shifted)  # inverse F.T.
            filtered_img = np.abs(inv_img)
            filtered_img -= filtered_img.min()
            filtered_img = filtered_img * 255 / filtered_img.max()
            filtered_img = filtered_img.astype(np.uint8)

        # applying median filter
        if opt_img["apply_median_filter"]["value"] == 1:
            # making a 5x5 array of all 1's for median filter
            med_disk = disk(5)
            filtered_img = median(filtered_img, med_disk)

        # applying gaussian blur
        if opt_img["apply_gaussian_blur"]["value"] == 1:
            b_size = int(opt_img["apply_gaussian_blur"]["dataValue"])
            filtered_img = cv2.GaussianBlur(filtered_img, (b_size, b_size), 0)

        # applying auto-level filter
        if opt_img["apply_autolevel"]["value"] == 1:
            # making a disk for the auto-level filter
            auto_lvl_disk = disk(int(opt_img["apply_autolevel"]["dataValue"]))
            filtered_img = autolevel(filtered_img, footprint=auto_lvl_disk)

        # applying a scharr filter,
        if opt_img["apply_scharr_gradient"]["value"] == 1:
            # applying a scharr filter, and then taking that image and weighting it 25% with the original,
            # this should bring out the edges without separating each "edge" into two separate parallel ones
            d_depth = cv2.CV_16S
            grad_x = cv2.Scharr(filtered_img, d_depth, 1, 0)
            grad_y = cv2.Scharr(filtered_img, d_depth, 0, 1)
            filtered_img = apply_filter('scharr', filtered_img, grad_x, grad_y)

        # applying sobel filter
        if opt_img["apply_sobel_gradient"]["value"] == 1:
            scale = 1
            delta = 0
            d_depth = cv2.CV_16S
            grad_x = cv2.Sobel(filtered_img, d_depth, 1, 0, ksize=int(opt_img["apply_sobel_gradient"]["dataValue"]),
                               scale=scale,
                               delta=delta, borderType=cv2.BORDER_DEFAULT)
            grad_y = cv2.Sobel(filtered_img, d_depth, 0, 1, ksize=int(opt_img["apply_sobel_gradient"]["dataValue"]),
                               scale=scale,
                               delta=delta, borderType=cv2.BORDER_DEFAULT)
            filtered_img = apply_filter('sobel', filtered_img, grad_x, grad_y)

        # applying laplacian filter
        if opt_img["apply_laplacian_gradient"]["value"] == 1:
            d_depth = cv2.CV_16S
            dst = cv2.Laplacian(filtered_img, d_depth, ksize=int(opt_img["apply_laplacian_gradient"]["dataValue"]))
            # dst = cv2.Canny(img_filtered, 100, 200); # canny edge detection test
            abs_dst = cv2.convertScaleAbs(dst)
            filtered_img = cv2.addWeighted(filtered_img, 0.75, abs_dst, 0.25, 0)
            filtered_img = cv2.convertScaleAbs(filtered_img)

        return filtered_img

    def binarize_img(self, image: MatLike) -> MatLike | None:
        """
        Convert image to binary.

        :param image:
        :return: None
        """

        if image is None:
            return None

        img_bin = None
        opt_img = self._configs
        otsu_res = 0  # only needed for the OTSU threshold

        # Applying the universal threshold, checking if it should be inverted (dark foreground)
        if opt_img["threshold_type"]["value"] == 0:
            if opt_img["apply_dark_foreground"]["value"] == 1:
                img_bin = \
                cv2.threshold(image, int(opt_img["global_threshold_value"]["value"]), 255, cv2.THRESH_BINARY_INV)[1]
            else:
                img_bin = cv2.threshold(image, int(opt_img["global_threshold_value"]["value"]), 255, cv2.THRESH_BINARY)[
                    1]

        # adaptive threshold generation
        elif opt_img["threshold_type"]["value"] == 1:
            if self._configs["adaptive_local_threshold_value"]["value"] <= 1:
                # Bug fix (crushes app)
                self._configs["adaptive_local_threshold_value"]["value"] = 3

            if opt_img["apply_dark_foreground"]["value"] == 1:
                img_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY_INV,
                                                int(opt_img["adaptive_local_threshold_value"]["value"]), 2)
            else:
                img_bin = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY,
                                                int(opt_img["adaptive_local_threshold_value"]["value"]), 2)

        # OTSU threshold generation
        elif opt_img["threshold_type"]["value"] == 2:
            if opt_img["apply_dark_foreground"]["value"] == 1:
                temp = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                img_bin = temp[1]
                otsu_res = temp[0]
            else:
                temp = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                img_bin = temp[1]
                otsu_res = temp[0]
        self._configs["otsu"]["value"] = otsu_res
        return img_bin

    def evaluate_img_binary(self) -> tuple[float, np.ndarray] | tuple[None, None]:
        """A function that evaluates the pre-processed image binary by overlaying the binary image on top of the
        original image and masking sections of the image that do not intersect with "white" (255) pixels in the
        binary image. The unmasked sections are typically where generated graph edges and nodes are located. So, the 
        unmasked sections should have fairly the same pixel values in the original image and the binary image. In the 
        binary image the pixel values are 255 "white", while in the original image they are typically 0-255, but with 
        small variations. The Standard Deviation (SD) can help identify how different the pixel values are in the 
        unmasked sections of the original image. Also, a histogram of the pixel values in the unmasked sections of the 
        original image can help identify the distribution of pixel values.
        
        :return: The Standard Deviation and Histogram of the unmasked sections (in the original image).
        """
        
        if self._img_2d is None:
            return None, None
        
        if self._img_bin is None:
            return None, None

        # Find pixel positions where the binary image is white (255)
        white_pixel_pos = np.argwhere(self._img_bin == 255)  # (row, col)

        # Retrieve corresponding pixel values from img_2d
        img_rgb = self._img_2d
        if self._has_alpha_channel:
            img_rgb = self._img_2d[..., :3]
        pixel_values = [img_rgb[tuple(p)] for p in white_pixel_pos]
        pixel_values = np.array(pixel_values)

        # Calculate standard deviation of original values
        std_dev = np.std(pixel_values)

        # Create the histogram of original values at white pixel positions
        eval_hist = cv2.calcHist([pixel_values], [0], None, [256], [0, 256])
        return float(std_dev), eval_hist

    def plot_img_histogram(self, axes=None, curr_view="") -> plt.Figure:
        """
        Uses Matplotlib to plot the histogram of the processed image.

        :param axes: A Matplotlib axes object.
        :param curr_view: The current visualization type of the image (Original, Processed, Binary).
        """
        fig = plt.figure()
        plt_title = "Processed Image"
        if curr_view != "":
            plt_title = f"{curr_view} image"

        if axes is None:
            ax = fig.add_subplot(1, 1, 1)
        else:
            ax = axes
        ax.set(yticks=[], xlabel='Pixel values', ylabel='Counts')
        ax.set_title(plt_title)

        if curr_view == "original":
            img = self._img_2d
            # Evaluate the binary image
            eval_std, eval_hist = self.evaluate_img_binary()
            if eval_std is not None:
                print(f"Evaluating Histogram of Binary Image (Std. Dev.): {eval_std}")
                ax.plot(eval_hist, color='c', label='Evaluated Binary Histogram')
                ax.legend(loc='upper right')
        elif curr_view == "binary":
            img = self._img_bin
        else:
            img = self._img_mod

        if img is None:
            return fig

        self._img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        ax.plot(self._img_hist, label='Image Histogram')
        ax.legend(loc='upper right')
        if self._configs["threshold_type"]["value"] == 0:
            global_val = int(self._configs["global_threshold_value"]["value"])
            thresh_arr = np.array([[global_val, global_val], [0, max(self._img_hist)]], dtype='object')
            ax.plot(thresh_arr[0], thresh_arr[1], ls='--', color='black')
        elif self._configs["threshold_type"]["value"] == 2:
            otsu_val = self._configs["otsu"]["value"]
            thresh_arr = np.array([[otsu_val, otsu_val], [0, max(self._img_hist)]], dtype='object')
            ax.plot(thresh_arr[0], thresh_arr[1], ls='--', color='black')
        fig.tight_layout()
        return fig

    def get_config_info(self) -> str:
        """
        Get the user selected parameters and options information.
        :return:
        """

        opt_img = self._configs

        run_info = "***Image Filter Configurations***\n"
        if opt_img["threshold_type"]["value"] == 0:
            run_info += "Global Threshold (" + str(opt_img["global_threshold_value"]["value"]) + ")"
        elif opt_img["threshold_type"]["value"] == 1:
            run_info += "Adaptive Threshold, " + str(opt_img["adaptive_local_threshold_value"]["value"]) + " bit kernel"
        elif opt_img["threshold_type"]["value"] == 2:
            run_info += "OTSU Threshold"

        if opt_img["apply_gamma"]["value"] == 1:
            run_info += f" || Gamma = {opt_img["apply_gamma"]["dataValue"]}"
        run_info += "\n"
        if opt_img["apply_median_filter"]["value"]:
            run_info += "Median Filter ||"
        if opt_img["apply_gaussian_blur"]["value"]:
            run_info += "Gaussian Blur, " + str(opt_img["apply_gaussian_blur"]["dataValue"]) + " bit kernel || "
        if opt_img["apply_autolevel"]["value"]:
            run_info += "Autolevel, " + str(opt_img["apply_autolevel"]["dataValue"]) + " bit kernel || "
        run_info = run_info[:-3] + '' if run_info.endswith('|| ') else run_info
        run_info += "\n"
        if opt_img["apply_dark_foreground"]["value"]:
            run_info += "Dark Foreground || "
        if opt_img["apply_laplacian_gradient"]["value"]:
            run_info += "Laplacian Gradient || "
        if opt_img["apply_scharr_gradient"]["value"]:
            run_info += "Scharr Gradient || "
        if opt_img["apply_sobel_gradient"]["value"]:
            run_info += "Sobel Gradient || "
        if opt_img["apply_lowpass_filter"]["value"]:
            run_info += "Low-pass filter, " + str(opt_img["apply_lowpass_filter"]["dataValue"]) + " window size || "
        run_info = run_info[:-3] + '' if run_info.endswith('|| ') else run_info
        run_info += "\n\n"

        run_info += "***Microscopy Parameters***\n"
        run_info += f"Scalebar Value = {opt_img["scale_value_nanometers"]["value"]} nm"
        run_info += f" || Scalebar Pixel Count = {opt_img["scalebar_pixel_count"]["value"]}\n"
        run_info += f"Resistivity = {opt_img["resistivity"]["value"]}" + r"$\Omega$m"
        run_info += "\n\n"

        if self._img_raw is not None:
            run_info += "***Image Scale***\n"
            run_info += f"Size = {self._img_2d.shape[0]} x {self._img_2d.shape[1]} px"
            run_info += f" || Scale Factor = {self._scale_factor}"

        return run_info

    @staticmethod
    def check_alpha_channel(img: MatLike) -> tuple[bool, str | None]:
        """
        A function that checks if an image has an Alpha channel or not. Only works for images with up to 4-Dimensions.

        :param img: OpenCV image.
        """

        if img is None:
            return False, None

        if len(img.shape) == 2:
            return False, "Grayscale"

        if len(img.shape) == 3:
            channels = img.shape[2]
            if channels == 4:
                return True, "RGBA"
            elif channels == 3:
                return False, "RGB"
            elif channels == 2:
                return True, "Grayscale + Alpha"
            elif channels == 1:
                return False, "Grayscale"

        # Unknown Format
        return False, None

    @staticmethod
    def resize_img(size: int, image: MatLike) -> tuple[MatLike | None, float | None]:
        """
        Resizes image to specified size.

        :param size: new image pixel size.
        :param image: OpenCV image.
        :return: rescaled image
        """
        if image is None:
            return None, None
        h, w = image.shape[:2]
        if h > w:
            scale_factor = size / h
        else:
            scale_factor = size / w
        std_width = int(scale_factor * w)
        std_height = int(scale_factor * h)
        std_size = (std_width, std_height)
        std_img = cv2.resize(image, std_size)
        return std_img, scale_factor
