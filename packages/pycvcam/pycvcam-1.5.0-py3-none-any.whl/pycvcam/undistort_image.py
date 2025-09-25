# Copyright 2025 Artezaru
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional
import numpy
import cv2
import scipy

from .core.distortion import Distortion
from .core.intrinsic import Intrinsic
from .core.package import Package

from .distortion_objects.no_distortion import NoDistortion
from .intrinsic_objects.no_intrinsic import NoIntrinsic


def undistort_image(
        src: numpy.ndarray,
        intrinsic: Optional[Intrinsic],
        distortion: Optional[Distortion],
        interpolation: str = "linear",
        **kwargs
    ) -> numpy.ndarray:
    r"""
    Undistort an image using the camera intrinsic and distortion coefficients.

    This method use the same architecture as the `cv2.undistort` function from OpenCV, but it is implemented in a more flexible way to allow the use of different distortion models.
    
    .. seealso::

        - :func:`pycvcam.undistort_image` for a more general undistort function that can handle different types of points and transformations (extrinsic, intrinsic, distortion).

    The process to undistort an image is as follows:

    1. The output pixels are converted to a normalized coordinate system using the inverse intrinsic transformation.
    2. The normalized points are distorted by the distortion model using the coefficients :math:`\{\lambda_1, \lambda_2, \lambda_3, \ldots\}`.
    3. The distorted points are projected back to the input image coordinate system using the same intrinsic transformation.
    4. The undistorted image is obtained by mapping the pixels from the original image to the undistorted points.

    The given image ``src`` is assumed to be in the image coordinate system and expressed in 2D coordinates with shape (H, W, [C], [D]).
    If the user gives an identity matrix K, it is equivalent to giving directly the normalized points.

    Fill Values for the output image are set to 0.0.

    The mapping is performed using using OpenCV's `cv2.remap` function (or ``scipy.interpolate``), which requires the source image and the mapping of pixel coordinates.

    Different interpolation methods can be used, such as "linear", "nearest", etc. The default is "linear".
    The table below shows the available interpolation methods:

    +----------------+----------------------------------------------------------------------------------------------------------------+
    | Interpolation  | Description                                                                                                    |
    +================+================================================================================================================+
    | "linear"       | Linear interpolation (default). Use cv2.INTER_LINEAR.                                                          |
    +----------------+----------------------------------------------------------------------------------------------------------------+
    | "nearest"      | Nearest neighbor interpolation. Use cv2.INTER_NEAREST.                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------+
    | "cubic"        | Bicubic interpolation. Use cv2.INTER_CUBIC.                                                                    |
    +----------------+----------------------------------------------------------------------------------------------------------------+
    | "area"         | Resampling using pixel area relation. Use cv2.INTER_AREA.                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------+
    | "lanczos4"     | Lanczos interpolation over 8x8 pixel neighborhood. Use cv2.INTER_LANCZOS4.                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------+
    | "spline3"      | Spline interpolation. Use scipy.interpolate.RectBivariateSpline for kx=ky=3                                    |
    +----------------+----------------------------------------------------------------------------------------------------------------+
    
    .. note::

        - For an image the X dimension corresponds to the width and the Y dimension corresponds to the height.
        - Pixel [0, 1] is at XY = [1, 0] in the image coordinate system.

    .. warning::

        - For scipy, output values are not positive integer values (even if the input image is integer).
    
    Parameters
    ----------
    src : numpy.ndarray
        The input image to be undistorted. Shape (H, W, ...) where H is the height, W is the width.

    intrinsic : Optional[Intrinsic]
        The intrinsic transformation to be applied to the image points.
        If None, a zero intrinsic is applied (i.e., identity transformation).

    distortion : Optional[Distortion]
        The distortion model to be applied. If None, no distortion is applied.

    interpolation : str, optional
        The interpolation method to be used for remapping the pixels. Default is "linear".

    kwargs : dict
        Additional arguments to be passed to the distortion model "distort" method.
    
    Returns
    -------
    numpy.ndarray
        The undistorted image. Shape (H, W, ...) where H is the height, W is the width.
    
    Example
    -------

    .. code-block:: python

        import numpy
        from pycvcam import undistort_image, Cv2Distortion, Cv2Intrinsic

        # Define the intrinsic camera matrix
        K = numpy.array([[1000.0, 0.0, 320.0],
                        [0.0, 1000.0, 240.0],
                        [0.0, 0.0, 1.0]])

        # Create the intrinsic object
        intrinsic = Cv2Intrinsic.from_matrix(K)

        # Define the distortion model (optional)
        distortion = Cv2Distortion([0.1, 0.2, 0.3, 0.4, 0.5])

        # Load the image to be undistorted
        src = cv2.imread('image.jpg')

        # Undistort the image
        undistorted_image = undistort_image(src, intrinsic=intrinsic, distortion=distortion)

    """   
    # Set the default values if None
    if intrinsic is None:
        intrinsic = NoIntrinsic()
    if distortion is None:
        distortion = NoDistortion()

    # Check the types of the parameters
    if not isinstance(intrinsic, Intrinsic):
        raise ValueError("intrinsic must be an instance of the Intrinsic class")
    if not intrinsic.is_set():
        raise ValueError("The intrinsic object must be ready to transform the points, check is_set() method.")
    if not isinstance(distortion, Distortion):
        raise ValueError("distortion must be an instance of the Distortion class.")
    if not distortion.is_set():
        raise ValueError("The distortion object must be ready to transform the points, check is_set() method.")
    
    # Check if the input image is a valid numpy array
    if not isinstance(src, numpy.ndarray):
        raise ValueError("src must be a numpy array")
    
    if src.ndim < 2 or src.ndim > 4:
        raise ValueError("src must have 2 to 4 dimensions (H, W, [C], [D])")
    
    # Get the interpolation method
    use_remap = False
    use_bivariate_spline = False
    if interpolation == "linear":
        interpolation_method = cv2.INTER_LINEAR
        use_remap = True
    elif interpolation == "nearest":
        interpolation_method = cv2.INTER_NEAREST
        use_remap = True
    elif interpolation == "cubic":
        interpolation_method = cv2.INTER_CUBIC
        use_remap = True
    elif interpolation == "area":
        interpolation_method = cv2.INTER_AREA
        use_remap = True
    elif interpolation == "lanczos4":
        interpolation_method = cv2.INTER_LANCZOS4
        use_remap = True
    elif interpolation == "spline3":
        interpolation_method = scipy.interpolate.RectBivariateSpline
        use_bivariate_spline = True
    else:
        raise ValueError(f"Invalid interpolation method: {interpolation}. Available methods: 'linear', 'nearest', 'cubic', 'area', 'lanczos4', 'spline3'.")
    
    # Construct the pixel points in the image coordinate system
    height, width = src.shape[:2]
    points = numpy.indices((height, width), dtype=Package.get_float_dtype()) # shape (2, H, W)
    points = points.reshape(2, -1).T  # shape (2, H, W) [2, Y, X] -> shape (Npoints, 2) [Y, X]
    points = points[:, [1, 0]]  # Switch to [X, Y] format, shape (Npoints, 2) [Y, X] -> shape (Npoints, 2) [X, Y]

    # Distort the pixel points using the distortion model
    if not isinstance(intrinsic, NoIntrinsic):
        points, _, _ = intrinsic._inverse_transform(points, dx=False, dp=False) # shape (Npoints, 2) [X, Y] -> shape (Npoints, 2) [X/Z, Y/Z]
    if not isinstance(distortion, NoDistortion):
        points, _, _ = distortion._transform(points, dx=False, dp=False, **kwargs) # shape (Npoints, 2) [X/Z, Y/Z] -> shape (Npoints, 2) [X'/Z', Y'/Z']
    if not isinstance(intrinsic, NoIntrinsic):
        points, _, _ = intrinsic._transform(points, dx=False, dp=False) # shape (Npoints, 2) [X'/Z', Y'/Z'] -> shape (Npoints, 2) [X', Y']

    # Reshape the distorted image points for cv2.remap
    points = points[:, [1, 0]]  # Switch to [Y, X] format, shape (Npoints, 2) [X', Y'] -> shape (Npoints, 2) [Y', X']
    points = points.T.reshape(2, height, width) # shape (Npoints, 2) [Y', X'] -> shape (2, H, W) [Y', X']

    if use_remap:
        # Create the map for cv2.remap
        # dst(x, y) = src(map_x(x, y), map_y(x, y))
        map_x = points[1, :, :]  # X' coordinates, shape (H, W)
        map_y = points[0, :, :]  # Y' coordinates, shape (H, W)

        # Remap the image using OpenCV
        undistorted_image = cv2.remap(src, map_x.astype(numpy.float32), map_y.astype(numpy.float32), interpolation=interpolation_method, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))

        return undistorted_image
    

    elif use_bivariate_spline:
        # Create the values and the image (H, W, 1 * [C] * [D])
        values = src.reshape(height, width, -1).astype(Package.get_float_dtype()) # shape (H, W, 1 * [C] * [D])

        # Initialize the distorted image
        undistorted_image = numpy.zeros_like(values, dtype=Package.get_float_dtype()) # shape (H, W, 1 * [C] * [D])

        # For all image data dimensions, interpolate the undistorted pixel points in the src image
        for i in range(values.shape[-1]):
            # Create the interpolator for the undistorted pixel points
            interp = scipy.interpolate.RectBivariateSpline(
                numpy.arange(height),
                numpy.arange(width),
                values[:, :, i],
                kx=3, ky=3, s=0 # Spline interpolation with kx=ky=3
            )

            # Create the mask for points that are within the image bounds and finite
            mask = numpy.isfinite(points[0, :, :]) & numpy.isfinite(points[1, :, :]) & (0.0 <= points[0, :, :]) & (points[0, :, :] <= height-1.0) & (0.0 <= points[1, :, :]) & (points[1, :, :] <= width-1.0)

            # Interpolate the pixel points in the distorted image
            result = interp.ev(points[0, mask], points[1, mask])
            undistorted_image[mask, i] = result

        # Reshape the distorted image to the original shape
        undistorted_image = undistorted_image.reshape(height, width, *src.shape[2:]) # (H, W, 1 * [C] * [D]) -> (H, W, [C], [D])
        return undistorted_image






    

    
