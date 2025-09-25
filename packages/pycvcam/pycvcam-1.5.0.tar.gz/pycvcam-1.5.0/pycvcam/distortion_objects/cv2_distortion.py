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

from typing import Optional, Tuple, List
import numpy
from numbers import Number, Integral
import cv2

from ..core import Distortion
from ..core.package import Package

class Cv2Distortion(Distortion):
    r"""

    Subclass of the :class:`pycvcam.core.Distortion` class that represents the OpenCV distortion model.

    .. note::

        This class represents the distortion transformation, which is the middle step of the process from the ``world_points`` to the ``image_points``.

    The ``Cv2Distortion`` model in the OpenCV model with radial, tangential and prism distortion.

    Lets consider ``normalized_points`` in the camera normalized coordinate system :math:`\vec{x}_n = (x_n, y_n)`, the corresponding ``distorted_points`` in the camera normalized coordinate system are given :math:`\vec{x}_d` can be obtained by :

    .. math::

        \vec{x}_d = \text{distort}(\vec{x}_n, \lambda_1, \lambda_2, \lambda_3, \ldots)

    The model of OpenCV is the following one:

    .. math::

        \begin{bmatrix}
        x_d \\
        y_d
        \end{bmatrix}
        =
        \begin{bmatrix}
        x_n \frac{1+k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6} + 2p_1 x_n y_n + p_2 (r^2 + 2x_n^2) + s_1 r^2 + s_2 r^4 \\
        y_n \frac{1+k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6} + p_1 (r^2 + 2y_n^2) + 2p_2 x_n y_n + s_3 r^2 + s_4 r^4
        \end{bmatrix}

    where :math:`r^2 = x_n^2 + y_n^2` and :math:`k_i` are the radial distortion coefficients, :math:`p_i` are the tangential distortion coefficients and :math:`s_i` are the thin prism distortion coefficients.

    Then a perspective transformation is applied using :math:`\tau_x` and :math:`\tau_y` to obtain the final distorted points.

    .. math::

        \begin{bmatrix}
        x_d \\
        y_d \\
        1
        \end{bmatrix}
        =
        \begin{bmatrix}
        R_{33}(\tau) & 0 & -R_{13}(\tau) \\
        0 & R_{33}(\tau) & -R_{23}(\tau) \\
        0 & 0 & 1
        \end{bmatrix}
        R(\tau)
        \begin{bmatrix}
        x_d \\
        y_d \\
        1
        \end{bmatrix}
    
    where :

    .. math::

        R(\tau) = \begin{bmatrix}
        cos(\tau_y) & sin(\tau_x)sin(\tau_y) & -cos(\tau_x)sin(\tau_y) \\
        0 & cos(\tau_x) & sin(\tau_x) \\
        sin(\tau_y) & -sin(\tau_x)cos(\tau_y) & cos(\tau_x)cos(\tau_y)
        \end{bmatrix}
    
    and :math:`R_{ij}(\tau)` are the elements of the rotation matrix.

    .. seealso::

        - https://docs.opencv.org/3.4/d9/d0c/group__calib3d.html for the OpenCV documentation

    OpenCV can use various models for distortion,

    - N = 4 parameters : :math:`(k_1, k_2, p_1, p_2)` : radial and tangential distortion
    - N = 5 parameters : :math:`(k_1, k_2, p_1, p_2, k_3)` : radial and tangential distortion with third order radial distortion
    - N = 8 parameters : :math:`(k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6)` : radial and tangential distortion with fractional radial distortion
    - N = 12 parameters : :math:`(k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6, s_1, s_2, s_3, s_4)` : radial and tangential distortion with thin prism distortion
    - N = 14 parameters : :math:`(k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6, s_1, s_2, s_3, s_4, \tau_x, \tau_y)` : radial and tangential distortion with thin prism distortion and perspective transformation

    If the number of input parameters is not equal to the number of parameters required by the model, the other parameters are set to 0.

    .. warning::

        If the number of parameters ``Nparams`` is given during instantiation, the given parameters are truncated or extended to the given number of parameters.

    Parameters
    ----------
    parameters : Optional[numpy.ndarray], optional
        The parameters of the distortion transformation. It should be a numpy array of shape (Nparams,) containing the distortion coefficients ordered as described above. Default is None, which means no distortion is setted.

    Nparams : Optional[Integral], optional
        The number of parameters for the distortion model. If not specified, it will be inferred from the shape of the `parameters` array.

    Examples
    --------
    Create an distortion object with a specific number of parameters:

    .. code-block:: python

        import numpy
        from pycvcam import Cv2Distortion

        parameters = numpy.array([0.1, 0.01, 0.02, 0.03, 0.001])

        distortion = Cv2Distortion(parameters=parameters)

    Then you can use the distortion object to transform ``normalized_points`` to ``distorted_points``:

    .. code-block:: python

        normalized_points = numpy.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]) # shape (Npoints, 2)

        result = distortion.transform(normalized_points)
        distorted_points = result.distorted_points # Shape (Npoints, 2)
        print(distorted_points)

    You can also access to the jacobian of the distortion transformation:

    .. code-block:: python

        result = distortion.transform(normalized_points, dx=True, dp=True)
        distorted_points_dx = result.jacobian_dx  # Shape (Npoints, 2, 2)
        distorted_points_dp = result.jacobian_dp  # Shape (Npoints, 2, Nparams = 5)
        print(distorted_points_dx) 
        print(distorted_points_dp)

    The inverse transformation can be computed using the `inverse_transform` method:

    .. code-block:: python

        inverse_result = distortion.inverse_transform(distorted_points, dx=True, dp=True)
        normalized_points = inverse_result.normalized_points  # Shape (Npoints, 2)
        print(normalized_points)

    .. note::

        The jacobian with respect to the depth is not computed.
    
    .. seealso::

        For more information about the transformation process, see:

        - :meth:`pycvcam.Cv2Distortion._transform` to transform the ``normalized_points`` to ``distorted_points``.
        - :meth:`pycvcam.Cv2Distortion._inverse_transform` to transform the ``distorted_points`` back to ``normalized_points``.

    """
    def __init__(self, parameters: Optional[numpy.ndarray] = None, Nparams: Optional[Integral] = None) -> None:
        # Initialize the Transform base class
        super().__init__(parameters=parameters, constants=None)
        if Nparams is not None:
            self.Nparams = Nparams

    # =============================================
    # Overwrite some properties from the base class
    # =============================================
    @property
    def parameters(self) -> Optional[numpy.ndarray]:
        r"""
        Get or set the parameters of the distortion model.

        If None, no distortion is applied.

        The number of parameters should be 4, 5, 8, 12 or 14.
        If the number of input parameters is not equal to the number of parameters required by the model, the other parameters are set to 0.

        The parameters are set in the following order:

        - N = 0 parameters : similar than None
        - N = 4 parameters : :math:`(k_1, k_2, p_1, p_2)` : radial and tangential distortion
        - N = 5 parameters : :math:`(k_1, k_2, p_1, p_2, k_3)` : radial and tangential distortion with third order radial distortion
        - N = 8 parameters : :math:`(k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6)` : radial and tangential distortion with fractional radial distortion
        - N = 12 parameters : :math:`(k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6, s_1, s_2, s_3, s_4)` : radial and tangential distortion with thin prism distortion
        - N = 14 parameters : :math:`(k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6, s_1, s_2, s_3, s_4, \tau_x, \tau_y)` : radial and tangential distortion with thin prism distortion and perspective transformation

        Parameters
        ----------
        parameters : numpy.ndarray, optional
            The parameters of the distortion model. If None, no distortion is applied. The default is None.

        Raises
        -------
        ValueError
            If the parameters is not a 1D numpy array.
            If more than 14 parameters are given.
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: Optional[numpy.ndarray]) -> None:
        if parameters is not None:
            parameters = numpy.asarray(parameters, dtype=Package.get_float_dtype())
            if parameters.ndim != 1:
                raise ValueError("The parameters should be a 1D numpy array.")
            if parameters.size > 14:
                raise ValueError("The number of parameters of CV2 distortion should be less than or equal to 14.")
            # Extend the number of parameters to a valid number
            valid_sizes = [0, 4, 5, 8, 12, 14]
            index = 0
            while valid_sizes[index] < parameters.size:
                index += 1
            Nparams = valid_sizes[index]
            # Extend the parameters to the next valid size
            if Nparams > parameters.size:
                parameters = numpy.concatenate((parameters, numpy.zeros(Nparams - parameters.size)))
            # Set to None if the number of parameters is 0
            if parameters.size == 0:
                parameters = None
        self._parameters = parameters

    @property
    def constants(self) -> Optional[numpy.ndarray]:
        r"""
        Always returns None for the Cv2Distortion class, as it does not have any constants.
        """
        return None
    
    @constants.setter
    def constants(self, value: Optional[numpy.ndarray]) -> None:
        if value is not None:
            raise ValueError("Cv2Distortion model has no constants, must be set to None.")
        self._constants = None

    @property
    def Nparams(self) -> int:
        r"""
        Get or set the number of parameters of the distortion model.

        The given number of parameters must be in [0, 4, 5, 8, 12, 14].

        If the given number of parameters is less than the current number of parameters, the parameters are truncated.
        If the given number of parameters is greater than the current number of parameters, the parameters are extended with zeros.

        Returns
        -------
        int
            The number of parameters of the distortion model.
        """
        if self.parameters is None:
            return 0
        else:
            return self.parameters.size
        
    @Nparams.setter
    def Nparams(self, value: Integral) -> None:
        if not isinstance(value, Integral):
            raise TypeError("The number of parameters should be an integer.")
        if value not in [0, 4, 5, 8, 12, 14]:
            raise ValueError("The number of parameters should be in [0, 4, 5, 8, 12, 14].")
        
        # If parameters is None, create a new array of zeros
        if self.parameters is None:
            self.parameters = numpy.zeros(value)
            return
        
        # Update the number of parameters instead of creating a new array
        if value == 0:
            self.parameters = None
        elif value < self.Nparams:
            self.parameters = self.parameters[:value]
        elif value > self.Nparams:
            self.parameters = numpy.concatenate((self.parameters, numpy.zeros(value - self.Nparams)))

    @property
    def parameter_names(self) -> List[str]:
        r"""
        Get the names of the parameters of the distortion transformation : ["k_1", "k_2", "p_1", "p_2", "k_3", ...]

        Returns
        -------
        List[str]
            The names of the parameters of the distortion transformation.
        """
        params = ["k_1", "k_2", "p_1", "p_2", "k_3", "k_4", "k_5", "k_6", "s_1", "s_2", "s_3", "s_4", "t_x", "t_y"]
        return params[:self.Nparams]

    @property
    def constant_names(self) -> List[str]:
        r"""
        Always returns an empty list for the Cv2Distortion class, as it does not have any constants.
        """
        return []

    def is_set(self) -> bool:
        r"""
        Check if the distortion parameters are set (always True for Cv2Distortion).

        Returns
        -------
        bool
            True if the distortion parameters are set, False otherwise.
        """
        return True

    
    # =================================================================
    # Distortion Model Coefficients
    # =================================================================
    @property
    def k1(self) -> float:
        r"""
        Get the first radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before getting the value.

        Returns
        -------
        float
            The first radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
        """
        if self.Nparams < 4: 
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before getting the k1 value.")
        return self.parameters[0]
    
    @k1.setter
    def k1(self, value: float) -> None:
        r"""
        Set the first radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before setting the value.

        Parameters
        ----------
        value : float
            The first radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 4:
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before setting the k1 value.")
        self.parameters[0] = float(value)


    @property
    def k2(self) -> float:
        r"""
        Get the second radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before getting the value.

        Returns
        -------
        float
            The second radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
        """
        if self.Nparams < 4: 
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before getting the k2 value.")
        return self.parameters[1]
    
    @k2.setter
    def k2(self, value: float) -> None:
        r"""
        Set the second radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before setting the value.

        Parameters
        ----------
        value : float
            The second radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 4:
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before setting the k2 value.")
        self.parameters[1] = float(value)

    
    @property
    def p1(self) -> float:
        r"""
        Get the first tangential distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before getting the value.

        Returns
        -------
        float
            The first tangential distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
        """
        if self.Nparams < 4: 
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before getting the p1 value.")
        return self.parameters[2]
    
    @p1.setter
    def p1(self, value: float) -> None:
        r"""
        Set the first tangential distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before setting the value.

        Parameters
        ----------
        value : float
            The first tangential distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 4:
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before setting the p1 value.")
        self.parameters[2] = float(value)

    
    @property
    def p2(self) -> float:
        r"""
        Get the second tangential distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before getting the value.

        Returns
        -------
        float
            The second tangential distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
        """
        if self.Nparams < 4: 
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before getting the p2 value.")
        return self.parameters[3]
    
    @p2.setter
    def p2(self, value: float) -> None:
        r"""
        Set the second tangential distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 4.
            Set the number of parameters to 4 or more before setting the value.

        Parameters
        ----------
        value : float
            The second tangential distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 4.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 4:
            raise ValueError("The number of parameters is less than 4. Set the number of parameters to 4 or more before setting the p2 value.")
        self.parameters[3] = float(value)

    
    @property
    def k3(self) -> Optional[float]:
        r"""
        Get the third radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 5.
            Set the number of parameters to 5 or more before getting the value.

        Returns
        -------
        float
            The third radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 5.
        """
        if self.Nparams < 5: 
            raise ValueError("The number of parameters is less than 5. Set the number of parameters to 5 or more before getting the k3 value.")
        return self.parameters[4]
    
    @k3.setter
    def k3(self, value: float) -> None:
        r"""
        Set the third radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 5.
            Set the number of parameters to 5 or more before setting the value.

        Parameters
        ----------
        value : float
            The third radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 5.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 5:
            raise ValueError("The number of parameters is less than 5. Set the number of parameters to 5 or more before setting the k3 value.")
        self.parameters[4] = float(value)

    
    @property
    def k4(self) -> Optional[float]:
        r"""
        Get the first fractional radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 8.
            Set the number of parameters to 8 or more before getting the value.

        Returns
        -------
        float
            The first fractional radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 8.
        """
        if self.Nparams < 8: 
            raise ValueError("The number of parameters is less than 8. Set the number of parameters to 8 or more before getting the k4 value.")
        return self.parameters[5]

    @k4.setter
    def k4(self, value: float) -> None:
        r"""
        Set the first fractional radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 8.
            Set the number of parameters to 8 or more before setting the value.

        Parameters
        ----------
        value : float
            The first fractional radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 8.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 8:
            raise ValueError("The number of parameters is less than 8. Set the number of parameters to 8 or more before setting the k4 value.")
        self.parameters[5] = float(value)
    

    @property
    def k5(self) -> Optional[float]:
        r"""
        Get the second fractional radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 8.
            Set the number of parameters to 8 or more before getting the value.

        Returns
        -------
        float
            The second fractional radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 8.
        """
        if self.Nparams < 8: 
            raise ValueError("The number of parameters is less than 8. Set the number of parameters to 8 or more before getting the k5 value.")
        return self.parameters[6]
    
    @k5.setter
    def k5(self, value: float) -> None:
        r"""
        Set the second fractional radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 8.
            Set the number of parameters to 8 or more before setting the value.

        Parameters
        ----------
        value : float
            The second fractional radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 8.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 8:
            raise ValueError("The number of parameters is less than 8. Set the number of parameters to 8 or more before setting the k5 value.")
        self.parameters[6] = float(value)
    

    @property
    def k6(self) -> Optional[float]:
        r"""
        Get the third fractional radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 8.
            Set the number of parameters to 8 or more before getting the value.

        Returns
        -------
        float
            The third fractional radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 8.
        """
        if self.Nparams < 8: 
            raise ValueError("The number of parameters is less than 8. Set the number of parameters to 8 or more before getting the k6 value.")
        return self.parameters[7]

    @k6.setter
    def k6(self, value: float) -> None:
        r"""
        Set the third fractional radial distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 8.
            Set the number of parameters to 8 or more before setting the value.

        Parameters
        ----------
        value : float
            The third fractional radial distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 8.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 8:
            raise ValueError("The number of parameters is less than 8. Set the number of parameters to 8 or more before setting the k6 value.")
        self.parameters[7] = float(value)


    @property
    def s1(self) -> Optional[float]:
        r"""
        Get the first thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before getting the value.

        Returns
        -------
        float
            The first thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
        """
        if self.Nparams < 12: 
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before getting the s1 value.")
        return self.parameters[8]
    
    @s1.setter
    def s1(self, value: float) -> None:
        r"""
        Set the first thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before setting the value.

        Parameters
        ----------
        value : float
            The first thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 12:
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before setting the s1 value.")
        self.parameters[8] = float(value)

    
    @property
    def s2(self) -> Optional[float]:
        r"""
        Get the second thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before getting the value.

        Returns
        -------
        float
            The second thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
        """
        if self.Nparams < 12: 
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before getting the s2 value.")
        return self.parameters[9]
    
    @s2.setter
    def s2(self, value: float) -> None:
        r"""
        Set the second thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before setting the value.

        Parameters
        ----------
        value : float
            The second thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 12:
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before setting the s2 value.")
        self.parameters[9] = float(value)


    @property
    def s3(self) -> Optional[float]:
        r"""
        Get the third thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before getting the value.

        Returns
        -------
        float
            The third thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
        """
        if self.Nparams < 12: 
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before getting the s3 value.")
        return self.parameters[10]
    
    @s3.setter
    def s3(self, value: float) -> None:
        r"""
        Set the third thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before setting the value.

        Parameters
        ----------
        value : float
            The third thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 12:
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before setting the s3 value.")
        self.parameters[10] = float(value)

    
    @property
    def s4(self) -> Optional[float]:
        r"""
        Get the fourth thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before getting the value.

        Returns
        -------
        float
            The fourth thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
        """
        if self.Nparams < 12: 
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before getting the s4 value.")
        return self.parameters[11]
    
    @s4.setter
    def s4(self, value: float) -> None:
        r"""
        Set the fourth thin prism distortion coefficient.

        .. warning::

            An error is raised if the number of parameters is less than 12.
            Set the number of parameters to 12 or more before setting the value.

        Parameters
        ----------
        value : float
            The fourth thin prism distortion coefficient.

        Raises
        -------
        ValueError
            If the number of parameters is less than 12.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 12:
            raise ValueError("The number of parameters is less than 12. Set the number of parameters to 12 or more before setting the s4 value.")
        self.parameters[11] = float(value)
    

    @property
    def tau_x(self) -> Optional[float]:
        r"""
        Get the x component of the perspective transformation.

        .. warning::

            An error is raised if the number of parameters is less than 14.
            Set the number of parameters to 14 or more before getting the value.

        Returns
        -------
        float
            The x component of the perspective transformation.

        Raises
        -------
        ValueError
            If the number of parameters is less than 14.
        """
        if self.Nparams < 14: 
            raise ValueError("The number of parameters is less than 14. Set the number of parameters to 14 or more before getting the tau_x value.")
        return self.parameters[12]
    
    @tau_x.setter
    def tau_x(self, value: float) -> None:
        r"""
        Set the x component of the perspective transformation.

        .. warning::

            An error is raised if the number of parameters is less than 14.
            Set the number of parameters to 14 or more before setting the value.

        Parameters
        ----------
        value : float
            The x component of the perspective transformation.

        Raises
        -------
        ValueError
            If the number of parameters is less than 14.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 14:
            raise ValueError("The number of parameters is less than 14. Set the number of parameters to 14 or more before setting the tau_x value.")
        self.parameters[12] = float(value)

    
    @property
    def tau_y(self) -> Optional[float]:
        r"""
        Get the y component of the perspective transformation.

        .. warning::

            An error is raised if the number of parameters is less than 14.
            Set the number of parameters to 14 or more before getting the value.

        Returns
        -------
        float
            The y component of the perspective transformation.

        Raises
        -------
        ValueError
            If the number of parameters is less than 14.
        """
        if self.Nparams < 14: 
            raise ValueError("The number of parameters is less than 14. Set the number of parameters to 14 or more before getting the tau_y value.")
        return self.parameters[13]
    
    @tau_y.setter
    def tau_y(self, value: float) -> None:
        r"""
        Set the y component of the perspective transformation.

        .. warning::

            An error is raised if the number of parameters is less than 14.
            Set the number of parameters to 14 or more before setting the value.

        Parameters
        ----------
        value : float
            The y component of the perspective transformation.

        Raises
        -------
        ValueError
            If the number of parameters is less than 14.
            If the value is not a number.
        """
        if not isinstance(value, Number):
            raise TypeError("The value should be a number.")
        if self.Nparams < 14:
            raise ValueError("The number of parameters is less than 14. Set the number of parameters to 14 or more before setting the tau_y value.")
        self.parameters[13] = float(value)
       

    def make_empty(self) -> None:
        r"""
        Set to zero the parameters of the distortion model.
        """
        self.parameters = numpy.zeros((self.Nparams, ), dtype=Package.get_float_dtype())


    # =================================================================
    # Internal methods to compute the distortion
    # =================================================================
    def _compute_tilt_matrix(self, dp: bool = True, inv: bool = True) -> Tuple[numpy.ndarray, Optional[numpy.ndarray], Optional[numpy.ndarray], Optional[numpy.ndarray]]:
        r"""
        Compute the tilt matrix for the perspective transformation for N = 14 (only).

        The tilt matrix is computed using the following equation:

        .. math::

            R_{\text{tilt}}{\tau} = R_Z[R_Y R_X] R_Y R_X

        where :math:`R_X` and :math:`R_Y` are the rotation matrices along X and Y respectively, and :math:`R_Z` is the rotation matrix along Z.

        .. math::
            R_X = \begin{pmatrix}
                1 & 0 & 0 \\
                0 & \cos(\tau_x) & \sin(\tau_x) \\
                0 & -\sin(\tau_x) & \cos(\tau_x)
            \end{pmatrix}

        .. math::
            R_Y = \begin{pmatrix}
                \cos(\tau_y) & 0 & -\sin(\tau_y) \\
                0 & 1 & 0 \\
                \sin(\tau_y) & 0 & \cos(\tau_y)
            \end{pmatrix}

        and we note that the rotation matrix along Z is given by:

        .. math::

            R_z[R] = \begin{pmatrix}
                R_{33} & 0 & -R_{13} \\
                0 & R_{33} & -R_{23} \\
                0 & 0 & 1
            \end{pmatrix}

        The derivatives of the tilt matrix with respect to :math:`\tau_x` and :math:`\tau_y` are also computed.
        The derivatives are computed using the following equations:

        .. math::

            \frac{\partial R_{\text{tilt}}}{\partial \tau_x} = R_Z [R_Y \frac{\partial R_X}{\partial \tau_x}, 0] R_Y R_X + R_Z [R_Y R_X, 1] R_Y \frac{\partial R_X}{\partial \tau_x}
        
        .. math::

            \frac{\partial R_{\text{tilt}}}{\partial \tau_y} = R_Z [\frac{\partial R_Y}{\partial \tau_y} R_X, 0] R_Y R_X + R_Z [R_Y R_X, 1] \frac{\partial R_Y}{\partial \tau_y} R_X    

        Finnally, the inverse of the tilt matrix is computed using the following equation:

        .. math::

            R_{\text{tilt}}^{-1} = (Ry Rx).T @ invRz[Ry Rx]

        Where :math:`invRz` is the inverse of the rotation matrix along Z given by:

        .. math::

            (R_z[R])^{-1} = \begin{pmatrix}
                1/R_{33} & 0 & R_{13}/R_{33} \\
                0 & 1/R_{33} & R_{23}/R_{33} \\
                0 & 0 & 1
            \end{pmatrix}

        .. note:: 

            If the model is not set to 14 parameters, the method returns a identity matrix and the derivatives are set to zero. 

        Parameters
        ----------
        dp : bool, optional
            If True, the derivatives of the tilt matrix are computed. The default is True.
            If False, the derivatives are set to None.

        inv : bool, optional
            If True, the inverse of the tilt matrix is computed. The default is True.
            If False, the inverse of the tilt matrix is set to None.

        Returns
        -------
        numpy.ndarray
            The tilt matrix.

        numpy.ndarray
            The derivative of the tilt matrix with respect to :math:`\tau_x` if ``dp`` is True, else None.

        numpy.ndarray
            The derivative of the tilt matrix with respect to :math:`\tau_y` if ``dp`` is True, else None.
        
        numpy.ndarray
            The inverse of the tilt matrix if ``inv`` is True, else None.
        """
        if not isinstance(dp, bool):
            raise TypeError("The dp parameter should be a boolean.")
        
        # Initialize the rotation matrices
        R = None
        Rdtx = None
        Rdty = None
        invR = None
    
        # If the number of parameters is not 14, return identity matrix and zero derivatives
        if self.Nparams != 14:
            R = numpy.eye(3, dtype=Package.get_float_dtype())
            if dp:
                Rdtx = numpy.zeros((3, 3), dtype=Package.get_float_dtype())
                Rdty = numpy.zeros((3, 3), dtype=Package.get_float_dtype())
            if inv:
                invR = numpy.eye(3, dtype=Package.get_float_dtype())
            return R, Rdtx, Rdty, invR

        # Prepare the cosinus and sinus of the angles
        ctx = numpy.cos(self.tau_x)
        cty = numpy.cos(self.tau_y)
        stx = numpy.sin(self.tau_x)
        sty = numpy.sin(self.tau_y)

        # Prepare the rotation matrix along X and Y
        Rx = numpy.array([
            [1, 0, 0],
            [0, ctx, stx],
            [0, -stx, ctx]
        ], dtype=Package.get_float_dtype())

        Ry = numpy.array([
            [cty, 0, -sty],
            [0, 1, 0],
            [sty, 0, cty]
        ], dtype=Package.get_float_dtype())

        if dp:
            Rxdtx = numpy.array([
                [0, 0, 0],
                [0, -stx, ctx],
                [0, -ctx, -stx]
            ], dtype=Package.get_float_dtype())

            Rydty = numpy.array([
                [-sty, 0, -cty],
                [0, 0, 0],
                [cty, 0, -sty]
            ], dtype=Package.get_float_dtype())

        # Compute the products of the rotation matrices
        Rxy = numpy.dot(Ry, Rx)

        if dp:
            Rxydtx = numpy.dot(Ry, Rxdtx)
            Rxydty = numpy.dot(Rydty, Rx)

        if inv:
            invRxy = Rxy.T
            
        # Compute the rotation along Z
        Rz = numpy.array([
            [Rxy[2, 2], 0, -Rxy[0, 2]],
            [0, Rxy[2, 2], -Rxy[1, 2]],
            [0, 0, 1]
        ], dtype=Package.get_float_dtype())

        if dp:
            Rzdtx = numpy.array([
                [Rxydtx[2, 2], 0, -Rxydtx[0, 2]],
                [0, Rxydtx[2, 2], -Rxydtx[1, 2]],
                [0, 0, 0]
            ], dtype=Package.get_float_dtype())

            Rzdty = numpy.array([
                [Rxydty[2, 2], 0, -Rxydty[0, 2]],
                [0, Rxydty[2, 2], -Rxydty[1, 2]],
                [0, 0, 0]
            ], dtype=Package.get_float_dtype())
        
        if inv:
            invRz = numpy.array([
                [1/Rxy[2, 2], 0, Rxy[0, 2]/Rxy[2, 2]],
                [0, 1/Rxy[2, 2], Rxy[1, 2]/Rxy[2, 2]],
                [0, 0, 1]
            ], dtype=Package.get_float_dtype())

        # Compute the tilt matrix and the derivatives
        R = numpy.dot(Rz, Rxy)

        if dp:
            Rdtx = numpy.dot(Rz, Rxydtx) + numpy.dot(Rzdtx, Rxy)
            Rdty = numpy.dot(Rz, Rxydty) + numpy.dot(Rzdty, Rxy)
        
        if inv:
            invR = numpy.dot(Rxy.T, invRz)

        # Return the tilt matrix and the derivatives
        return R, Rdtx, Rdty, invR

    # =================================================================
    # Implementation of the transform method
    # =================================================================
    def _transform(self, normalized_points: numpy.ndarray, *, dx: bool = False, dp: bool = False, opencv: bool = False) -> Tuple[numpy.ndarray, Optional[numpy.ndarray], Optional[numpy.ndarray]]:
        r"""
        Compute the transformation from the ``normalized_points`` to the ``distorted_points``.

        Lets consider ``normalized_points`` in the camera normalized coordinate system :math:`\vec{x}_n = (x_n, y_n)`, the corresponding ``distorted_points`` in the camera normalized coordinate system are given :math:`\vec{x}_d` can be obtained by :

        .. math::

            \vec{x}_d = \text{distort}(\vec{x}_n, \lambda_1, \lambda_2, \lambda_3, \ldots)

        The model of OpenCV is the following one:

        .. math::

            \begin{bmatrix}
            x_d \\
            y_d
            \end{bmatrix}
            =
            \begin{bmatrix}
            x_n \frac{1+k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6} + 2p_1 x_n y_n + p_2 (r^2 + 2x_n^2) + s_1 r^2 + s_2 r^4 \\
            y_n \frac{1+k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6} + p_1 (r^2 + 2y_n^2) + 2p_2 x_n y_n + s_3 r^2 + s_4 r^4
            \end{bmatrix}

        where :math:`r^2 = x_n^2 + y_n^2` and :math:`k_i` are the radial distortion coefficients, :math:`p_i` are the tangential distortion coefficients and :math:`s_i` are the thin prism distortion coefficients.

        Then a perspective transformation is applied using :math:`\tau_x` and :math:`\tau_y` to obtain the final distorted points.

        .. math::

            \begin{bmatrix}
            x_d \\
            y_d \\
            1
            \end{bmatrix}
            =
            \begin{bmatrix}
            R_{33}(\tau) & 0 & -R_{13}(\tau) \\
            0 & R_{33}(\tau) & -R_{23}(\tau) \\
            0 & 0 & 1
            \end{bmatrix}
            R(\tau)
            \begin{bmatrix}
            x_d \\
            y_d \\
            1
            \end{bmatrix}
        
        where :

        .. math::

            R(\tau) = \begin{bmatrix}
            cos(\tau_y) & sin(\tau_x)sin(\tau_y) & -cos(\tau_x)sin(\tau_y) \\
            0 & cos(\tau_x) & sin(\tau_x) \\
            sin(\tau_y) & -sin(\tau_x)cos(\tau_y) & cos(\tau_x)cos(\tau_y)
            \end{bmatrix}

        The jacobians with respect to the distortion parameters is an array with shape (Npoints, 2, Nparams), where the last dimension represents the parameters in the order of the class attributes (k1, k2, k3, p1, p2, k4, k5, k6, s1, s2, s3, s4, tau_x, tau_y).
        The jacobian with respect to the normalized points is an array with shape (Npoints, 2, 2).

        .. warning::

            This method is not intended to be used directly, but rather through the :meth:`pycvcam.core.Transform.transform` method.
            Please ensure, the shape of the input ``normalized_points`` is (Npoints, 2) before calling this method.

        To achieve the distortion transformation using openCV, set the ``opencv`` parameter to True. (``jacobian_dx`` will not be computed in this case).

        Parameters
        ----------
        normalized_points : numpy.ndarray
            The normalized points in camera normalized coordinates to be transformed. Shape (Npoints, 2).

        dx : bool, optional
            If True, the jacobian with respect to the normalized points is computed. Default is False

        dp : bool, optional
            If True, the jacobian with respect to the distortion parameters is computed. Default is False

        opencv : bool, optional
            If True, the distortion transformation is achieved using the OpenCV function ``projectPoints``.
            If False, the distortion transformation is achieved using the internal method.
            Default is False.

        Returns
        -------
        distorted_points : numpy.ndarray
            The distorted points in camera normalized coordinates. Shape (Npoints, 2).

        jacobian_dx : Optional[numpy.ndarray]
            The jacobian of the distorted points with respect to the normalized points. Shape (Npoints, 2, 2) if dx is True, otherwise None.

        jacobian_dp : Optional[numpy.ndarray]
            The jacobian of the distorted points with respect to the distortion parameters. Shape (Npoints, 2, Nparams) if dp is True, otherwise None.
        """
        # USE THE OPEN CV DISTORTION IF REQUESTED
        if not isinstance(opencv, bool):
            raise TypeError("The opencv parameter must be a boolean.")
        if opencv:
            return self._transform_opencv(normalized_points, dx=dx, dp=dp)

        # Prepare the inputs data for distortion
        x_N = normalized_points[:, 0] # shape (Npoints,)
        y_N = normalized_points[:, 1] # shape (Npoints,)
        x_N = x_N[:, numpy.newaxis] # shape (Npoints, 1)
        y_N = y_N[:, numpy.newaxis] # shape (Npoints, 1)
        Npoints = normalized_points.shape[0]
        Nparams = self.Nparams

        zero = lambda dim: numpy.zeros((Npoints, dim), dtype=Package.get_float_dtype()) # shape (Npoints, dim)
        ccat = lambda tup: numpy.concatenate(tup, axis=1) # Concatenate along the second axis
        dDdxy = None # The derivative of the distortion with respect to the normalized points
        dDdp = None # The derivative of the distortion with respect to the distortion parameters

        # Prepare some variables for the distortion
        xN_yN = x_N * y_N # shape (Npoints, 1)
        xN2 = x_N ** 2 # shape (Npoints, 1)
        yN2 = y_N ** 2 # shape (Npoints, 1)
        
        # Return a identity Jacobian and an empty jacobian if no parameters in the model
        if Nparams == 0:
            distorted_points = numpy.copy(normalized_points) # shape (Npoints, 2)
            if dx: 
                dDdxy = numpy.zeros((Npoints, 2, 2), dtype=Package.get_float_dtype()) # shape (Npoints, 2, 2)
                dDdxy[:, 0, 0] = 1.0
                dDdxy[:, 1, 1] = 1.0
            if dp:
                dDdp = numpy.empty((Npoints, 2, 0), dtype=Package.get_float_dtype()) # shape (Npoints, 2, 0)
            return distorted_points, dDdxy, dDdp
                
        # Prepare the powers of the norm (r) [only if needed] with shape (Npoints, 1)
        r2 = xN2 + yN2 # shape (Npoints, 1)
        r4 = r2 ** 2 # shape (Npoints, 1)

        if Nparams >= 5:
            r6 = r2 * r4 # shape (Npoints, 1)

        # Prepare the radial distortion coefficients [only if needed] with shape (Npoints, 1)
        if Nparams == 4:
            K = (1 + self.k1 * r2 + self.k2 * r4) # shape (Npoints, 1)

        elif Nparams == 5:
            K = (1 + self.k1 * r2 + self.k2 * r4 + self.k3 * r6) # shape (Npoints, 1)
        
        else: # Nparams >= 8
            Kup = (1 + self.k1 * r2 + self.k2 * r4 + self.k3 * r6) # shape (Npoints, 1)
            Kdown = (1 + self.k4 * r2 + self.k5 * r4 + self.k6 * r6) # shape (Npoints, 1)
            iKdown = 1 / Kdown # shape (Npoints, 1)
            i2Kdown = iKdown ** 2 # shape (Npoints, 1)
            K = Kup * iKdown # shape (Npoints, 1)
                            
        x_radial = x_N * K # shape (Npoints, 1)
        y_radial = y_N * K # shape (Npoints, 1)

        # Prepare the tangential distortion coefficients [only if needed] with shape (Npoints, 1)
        axp1 = ayp2 = 2 * xN_yN # shape (Npoints, 1)
        axp2 = r2 + 2 * xN2 # shape (Npoints, 1)
        ayp1 = r2 + 2 * yN2 # shape (Npoints, 1)
        x_tangential = self.p1 * axp1 + self.p2 * axp2 # shape (Npoints, 1)
        y_tangential = self.p1 * ayp1 + self.p2 * ayp2 # shape (Npoints, 1)

        # Prepare the prism distortion coefficients [only if needed] with shape (Npoints, 1)
        if Nparams < 12:
            x_prism = zero(1) # shape (Npoints, 1)
            y_prism = zero(1) # shape (Npoints, 1)
            
        else: # Nparams >= 12
            x_prism = self.s1 * r2 + self.s2 * r4 # shape (Npoints, 1)
            y_prism = self.s3 * r2 + self.s4 * r4 # shape (Npoints, 1)
            
        # Compute the distorted points
        x_D = x_radial + x_tangential + x_prism # shape (Npoints, 1)
        y_D = y_radial + y_tangential + y_prism # shape (Npoints, 1)

        # Prepare some variables for the jacobians
        if (dx and Nparams >= 12) or dp:
            xN_r2 = x_N * r2 # shape (Npoints, 1)
            yN_r2 = y_N * r2 # shape (Npoints, 1)

        # Compute the Jacobians with respect to the normalized points with shape (Npoints, 2)
        if dx:
            x_Ddxy = numpy.empty((Npoints, 2), dtype=Package.get_float_dtype()) # shape (Npoints, 2)
            y_Ddxy = numpy.empty((Npoints, 2), dtype=Package.get_float_dtype()) # shape (Npoints, 2)

            if Nparams == 4:
                dK_r2 = (2 * self.k1 + 4 * self.k2 * r2) # shape (Npoints, 1)
            elif Nparams == 5:
                dK_r2 = (2 * self.k1 + 4 * self.k2 * r2 + 6 * self.k3 * r4) # shape (Npoints, 1)
            else:
                dK_r2 = (2 * self.k1 + 4 * self.k2 * r2 + 6 * self.k3 * r4) * Kdown - Kup * (2 * self.k4 + 4 * self.k5 * r2 + 6 * self.k6 * r4) # shape (Npoints, 1)
                dK_r2 = dK_r2 * i2Kdown

            x_radial_dx = K + dK_r2 * xN2 # shape (Npoints, 1)
            x_radial_dy = y_radial_dx = dK_r2 * xN_yN # shape (Npoints, 1)
            y_radial_dy = K + dK_r2 * yN2 # shape (Npoints, 1)

            x_tangential_dx = (2 * self.p1) * y_N + (6 * self.p2) * x_N
            x_tangential_dy = (2 * self.p1) * x_N + (2 * self.p2) * y_N
            y_tangential_dx = (2 * self.p2) * y_N + (2 * self.p1) * x_N
            y_tangential_dy = (2 * self.p2) * x_N + (6 * self.p1) * y_N

            x_Ddxy[:, 0] = (x_radial_dx + x_tangential_dx).ravel()
            x_Ddxy[:, 1] = (x_radial_dy + x_tangential_dy).ravel()
            y_Ddxy[:, 0] = (y_radial_dx + y_tangential_dx).ravel()
            y_Ddxy[:, 1] = (y_radial_dy + y_tangential_dy).ravel()

            if Nparams >= 12:
                x_Ddxy[:, 0] += ((2 * self.s1) * x_N + (4 * self.s2) * xN_r2).ravel()
                x_Ddxy[:, 1] += ((2 * self.s1) * y_N + (4 * self.s2) * yN_r2).ravel()
                y_Ddxy[:, 0] += ((2 * self.s3) * x_N + (4 * self.s4) * xN_r2).ravel()
                y_Ddxy[:, 1] += ((2 * self.s3) * y_N + (4 * self.s4) * yN_r2).ravel()

        if dp:
            x_Ddp = numpy.empty((Npoints, Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, Nparams)
            y_Ddp = numpy.empty((Npoints, Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, Nparams)

            x_Ddp[:, 0] = xN_r2.ravel() if Nparams <= 5 else (xN_r2 * iKdown).ravel()
            x_Ddp[:, 1] = (r4 * x_N).ravel() if Nparams <= 5 else (r4 * x_N * iKdown).ravel()
            x_Ddp[:, 2] = axp1.ravel()
            x_Ddp[:, 3] = axp2.ravel()
            y_Ddp[: ,0] = yN_r2.ravel() if Nparams <= 5 else (yN_r2 * iKdown).ravel()
            y_Ddp[:, 1] = (r4 * y_N).ravel() if Nparams <= 5 else (r4 * y_N * iKdown).ravel()
            y_Ddp[:, 2] = ayp1.ravel()
            y_Ddp[:, 3] = ayp2.ravel()

            if Nparams >= 5:
                x_Ddp[:, 4] = (r6 * x_N).ravel() if Nparams <= 5 else (r6 * x_N * iKdown).ravel()
                y_Ddp[:, 4] = (r6 * y_N).ravel() if Nparams <= 5 else (r6 * y_N * iKdown).ravel()

            if Nparams >= 8:
                m_Kup_i2Kdown = -Kup * i2Kdown
                m_Kup_i2Kdown_xN = m_Kup_i2Kdown * x_N
                m_Kup_i2Kdown_yN = m_Kup_i2Kdown * y_N
                x_Ddp[:, 5] = (m_Kup_i2Kdown_xN * r2).ravel()
                x_Ddp[:, 6] = (m_Kup_i2Kdown_xN * r4).ravel() 
                x_Ddp[:, 7] = (m_Kup_i2Kdown_xN * r6).ravel()
                y_Ddp[:, 5] = (m_Kup_i2Kdown_yN * r2).ravel()
                y_Ddp[:, 6] = (m_Kup_i2Kdown_yN * r4).ravel() 
                y_Ddp[:, 7] = (m_Kup_i2Kdown_yN * r6).ravel()

            if Nparams >= 12:
                x_Ddp[:, 8] = r2.ravel()
                x_Ddp[:, 9] = r4.ravel()
                x_Ddp[:, 10:12] = 0.0
                y_Ddp[:, 8:10] = 0.0
                y_Ddp[:, 10] = r2.ravel()
                y_Ddp[:, 11] = r4.ravel()

            if Nparams >= 14:
                x_Ddp[:, 12:14] = 0.0
                y_Ddp[:, 12:14] = 0.0


        # Apply the perspective transformation [only if needed]
        # Also compute the finals derivatives with respect to the normalized points and to the parameters
        if self.Nparams >= 14:
            # Get the tilt matrix
            R, Rdtx, Rdty, _ = self._compute_tilt_matrix(dp = dp, inv=False) # shape (3, 3) ; shape (3, 3) ; shape (3, 3)

            # Apply the perspective transformation
            x_perspectD = R[0, 0] * x_D + R[0, 1] * y_D + R[0, 2] # shape (Npoints, 1)
            y_perspectD = R[1, 0] * x_D + R[1, 1] * y_D + R[1, 2] # shape (Npoints, 1)
            z_perspectD = R[2, 0] * x_D + R[2, 1] * y_D + R[2, 2] # shape (Npoints, 1)
            iz_perspectD = 1 / z_perspectD # shape (Npoints, 1)
            i2z_perspectD = iz_perspectD ** 2 # shape (Npoints, 1)
            if dx:
                x_perspectDdxy = (R[0, 0] * x_Ddxy + R[0, 1] * y_Ddxy) # shape (Npoints, 2)
                y_perspectDdxy = (R[1, 0] * x_Ddxy + R[1, 1] * y_Ddxy) # shape (Npoints, 2)
                z_perspectDdxy = (R[2, 0] * x_Ddxy + R[2, 1] * y_Ddxy) # shape (Npoints, 2)
            if dp:
                x_perspectDdp = numpy.empty((Npoints, Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, Nparams)
                x_perspectDdp[:, :12] = (R[0, 0] * x_Ddp[:, :12] + R[0, 1] * y_Ddp[:, :12]) # shape (Npoints, 12)
                x_perspectDdp[:, 12] = (Rdtx[0, 0] * x_D + Rdtx[0, 1] * y_D + Rdtx[0, 2]).ravel() # shape (Npoints, 1)
                x_perspectDdp[:, 13] = (Rdty[0, 0] * x_D + Rdty[0, 1] * y_D + Rdty[0, 2]).ravel() # shape (Npoints, 1)

                y_perspectDdp = numpy.empty((Npoints, Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, Nparams)
                y_perspectDdp[:, :12] = (R[1, 0] * x_Ddp[:, :12] + R[1, 1] * y_Ddp[:, :12]) # shape (Npoints, 12)
                y_perspectDdp[:, 12] = (Rdtx[1, 0] * x_D + Rdtx[1, 1] * y_D + Rdtx[1, 2]).ravel() # shape (Npoints, 1)
                y_perspectDdp[:, 13] = (Rdty[1, 0] * x_D + Rdty[1, 1] * y_D + Rdty[1, 2]).ravel() # shape (Npoints, 1)

                z_perspectDdp = numpy.empty((Npoints, Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, Nparams)
                z_perspectDdp[:, :12] = (R[2, 0] * x_Ddp[:, :12] + R[2, 1] * y_Ddp[:, :12]) # shape (Npoints, 12)
                z_perspectDdp[:, 12] = (Rdtx[2, 0] * x_D + Rdtx[2, 1] * y_D + Rdtx[2, 2]).ravel() # shape (Npoints, 1)
                z_perspectDdp[:, 13] = (Rdty[2, 0] * x_D + Rdty[2, 1] * y_D + Rdty[2, 2]).ravel() # shape (Npoints, 1)
            
            # Normalize the points by the perspective transformation
            x_D = x_perspectD * iz_perspectD # shape (Npoints, 1)
            y_D = y_perspectD * iz_perspectD # shape (Npoints, 1)
            if dx:
                x_Ddxy = (x_perspectDdxy * numpy.broadcast_to(z_perspectD, (Npoints, 2)) - numpy.broadcast_to(x_perspectD, (Npoints, 2)) * z_perspectDdxy) * i2z_perspectD # shape (Npoints, 2)
                y_Ddxy = (y_perspectDdxy * numpy.broadcast_to(z_perspectD, (Npoints, 2)) - numpy.broadcast_to(y_perspectD, (Npoints, 2)) * z_perspectDdxy) * i2z_perspectD # shape (Npoints, 2)
            if dp:
                x_Ddp = (x_perspectDdp * numpy.broadcast_to(z_perspectD, (Npoints, Nparams)) - numpy.broadcast_to(x_perspectD, (Npoints, Nparams)) * z_perspectDdp) * i2z_perspectD # shape (Npoints, Nparams)
                y_Ddp = (y_perspectDdp * numpy.broadcast_to(z_perspectD, (Npoints, Nparams)) - numpy.broadcast_to(y_perspectD, (Npoints, Nparams)) * z_perspectDdp) * i2z_perspectD # shape (Npoints, Nparams)
            
        # Construct the final outputs
        distorted_points = ccat((x_D, y_D)) # shape (Npoints, 2)
        if dx:
            dDdxy = numpy.zeros((Npoints, 2, 2), dtype=Package.get_float_dtype()) # shape (Npoints, 2, 2)
            dDdxy[:, 0, :] = x_Ddxy # shape (Npoints, 2)
            dDdxy[:, 1, :] = y_Ddxy # shape (Npoints, 2)
        if dp:
            dDdp = numpy.zeros((Npoints, 2, Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, 2, Nparams)
            dDdp[:, 0, :] = x_Ddp # shape (Npoints, Nparams)
            dDdp[:, 1, :] = y_Ddp # shape (Npoints, Nparams)
        
        # Return the distorted points and the derivatives
        return distorted_points, dDdxy, dDdp
    

    def _transform_opencv(self, normalized_points: numpy.ndarray, *, dx: bool = False, dp: bool = False) -> tuple[numpy.ndarray, Optional[numpy.ndarray], Optional[numpy.ndarray]]:
        r"""
        Compute the transformation from the ``normalized_points`` to the ``distorted_points`` using OpenCV's ``projectPoints`` function.

        The equation used for the transformation is given in the main documentation of the class.

        .. warning::

            This method is not intended to be used directly, but rather through the :meth:`pycvcam.core.Transform.transform` method.
            Please ensure, the shape of the input ``normalized_points`` is (Npoints, 2) before calling this method.

            The jacobian with respect to the normalized points is not computed in this case (always None).

        Parameters
        ----------
        normalized_points : numpy.ndarray
            The normalized points in camera normalized coordinates to be transformed. Shape (Npoints, 2).

        dx : bool, optional
            If True, the jacobian with respect to the normalized points is computed. Default is False

        dp : bool, optional
            If True, the jacobian with respect to the distortion parameters is computed. Default is False

        opencv : bool, optional
            If True, the distortion transformation is achieved using the OpenCV function ``projectPoints``.
            If False, the distortion transformation is achieved using the internal method.
            Default is False.

        Returns
        -------
        distorted_points : numpy.ndarray
            The distorted points in camera normalized coordinates. Shape (Npoints, 2).

        jacobian_dx : Optional[numpy.ndarray]
            Always None, since the jacobian with respect to the normalized points is not computed with OpenCV.

        jacobian_dp : Optional[numpy.ndarray]
            The jacobian of the distorted points with respect to the distortion parameters. Shape (Npoints, 2, Nparams) if dp is True, otherwise None.
        """
        if dx:
            print("\n[WARNING]: Distortion with Opencv and dx=True. The jacobian wrt normalized points cannot be computed with this method. They are always None.\n")

        Npoints = normalized_points.shape[0] # Npoints

        # Create the contiguous array of shape (Npoints, 1, 3) for cv2 compatibility
        object_points = numpy.concatenate((normalized_points, numpy.ones((normalized_points.shape[0], 1))), axis=1)
        object_points = numpy.ascontiguousarray(object_points.reshape(-1, 1, 3), dtype=Package.get_float_dtype())

        # Apply the OpenCV distortion removing rvec, tvec and intrinsic matrix
        rvec = numpy.zeros((3, 1), dtype=Package.get_float_dtype())
        tvec = numpy.zeros((3, 1), dtype=Package.get_float_dtype())
        intrinsic_matrix = numpy.eye(3, dtype=Package.get_float_dtype())
        image_points, jacobian = cv2.projectPoints(object_points, rvec, tvec, intrinsic_matrix, self.parameters) # shape (Npoints, 1, 2)

        # Reshape the image points to (2, Npoints)
        distorted_points = numpy.asarray(image_points[:,0,:], dtype=Package.get_float_dtype())
        if dp:
            jacobian = numpy.asarray(jacobian, dtype=Package.get_float_dtype())[:, -self.Nparams:] # shape (2 * Npoints, Nparams)
            jacobian_dp = numpy.zeros((Npoints, 2, self.Nparams), dtype=Package.get_float_dtype()) # shape (Npoints, 2, Nparams)
            jacobian_dp[:, 0, :] = jacobian[0::2, :] # shape (Npoints, Nparams)
            jacobian_dp[:, 1, :] = jacobian[1::2, :] # shape (Npoints, Nparams)
        else:
            jacobian_dp = None

        return distorted_points, None, jacobian_dp
    


    def _inverse_transform(self, distorted_points: numpy.ndarray, *, dx: bool = False, dp: bool = False, opencv: bool = False, max_iter: int = 10, eps: float = 1e-8) -> Tuple[numpy.ndarray, Optional[numpy.ndarray], Optional[numpy.ndarray]]:
        r"""
        Compute the inverse transformation from the ``distorted_points`` to the ``normalized_points``.

        Lets consider ``distorted_points`` in the camera normalized coordinate system :math:`\vec{x}_d = (x_d, y_d)`, the corresponding ``normalized_points`` in the camera normalized coordinate system are obtained by an ``iterative`` algorithm that finds the points :math:`\vec{x}_n` such that:

        .. math::
            \begin{bmatrix}
            x_n [\text{it }k+1]\\
            y_n [\text{it }k+1]
            \end{bmatrix}
            = 
            \begin{bmatrix}
            (x_d - \Delta x [\text{it }k]) / \text{Rad} [\text{it }k] \\
            (y_d - \Delta y [\text{it }k]) / \text{Rad}[\text{it }k]
            \end{bmatrix}

        Where :math:`\Delta x [\text{it }k]` and :math:\Delta y [\text{it }k] are the tangential and prism distortion contributions to the distorted points computed at iteration :math:k.
        And :math:`\text{Rad} [\text{it }k]` is the radial distortion contribution to the distorted points computed at iteration :math:k.

        .. math::
            \begin{bmatrix}
            \Delta x
            \Delta y
            \end{bmatrix}
            =
            \begin{bmatrix}
            2 p_1 x_n y_n + p_2 (r^2 + 2x_n^2) + s_1 r^2 + s_2 r^4 \\
            2 p_2 x_n y_n + p_1 (r^2 + 2y_n^2) + s_3 r^2 + s_4 r^4
            \end{bmatrix}

        .. math::
            \begin{bmatrix}
            \text{Rad}_x \\
            \text{Rad}_y
            \end{bmatrix}
            =
            \begin{bmatrix}
            \frac{1+k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6} \\
            \frac{1+k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6}
            \end{bmatrix}

        .. warning::

            This method is not intended to be used directly, but rather through the :meth:`pycvcam.core.Transform.transform` method.
            Please ensure, the shape of the input ``image_points`` is (Npoints, 2) before calling this method.

            The jacobians with respect to the distortion parameters and the distorted points are always None, since it is an iterative algorithm.

        .. seealso::

            - :func:`pycvcam.optimize.optimize_input_points` for an other implementation of an iterative algorithm to compute the inverse distortion transformation.

        To achieve the inverse distortion transformation using openCV, set the ``opencv`` parameter to True. 

        Parameters
        ----------
        distorted_points : numpy.ndarray
            The distorted points in camera normalized coordinates to be transformed. Shape (Npoints, 2).

        dx : bool, optional
            If True, the jacobian with respect to the distorted points is computed. Default is False

        dp : bool, optional
            If True, the jacobian with respect to the distortion parameters is computed. Default is False

        opencv : bool, optional
            If True, the inverse distortion transformation is achieved using the OpenCV function ``undistortPoints``.
            If False, the inverse distortion transformation is achieved using the internal method.
            Default is False.

        max_iter : int, optional
            The maximum number of iterations for the iterative algorithm. Default is 10.

        eps : float, optional
            The tolerance for the convergence of the iterative algorithm. Default is 1e-8.

        Returns
        -------
        normalized_points : numpy.ndarray
            The normalized points in camera normalized coordinates, which are equal to the x and y components of the image points. Shape (Npoints, 2).

        jacobian_dx : Optional[numpy.ndarray]
            Always None, since the jacobian with respect to the distorted points is not computed by an iterative algorithm.

        jacobian_dp : Optional[numpy.ndarray]
            Always None, since the jacobian with respect to the distortion parameters is not computed by an iterative algorithm.
        """
        # USE THE OPEN CV DISTORTION IF REQUESTED
        if not isinstance(opencv, bool):
            raise TypeError("The opencv parameter must be a boolean.")
        if opencv:
            return self._inverse_transform_opencv(distorted_points, dx=dx, dp=dp)
        
        if dx or dp:
            print("\n[WARNING]: Undistortion with dx=True or dp=True. The jacobians cannot be computed with this method. They are always None.\n")

        # Prepare the inputs data for undistortion
        x_D = distorted_points[:, 0] # shape (Npoints,)
        y_D = distorted_points[:, 1] # shape (Npoints,)
        x_D = x_D[:, numpy.newaxis] # shape (Npoints, 1)
        y_D = y_D[:, numpy.newaxis] # shape (Npoints, 1)
        Npoints = distorted_points.shape[0]
        Nparams = self.Nparams

        # Case of no parameters in the model
        if Nparams == 0:
            normalized_points = numpy.copy(distorted_points)
            return normalized_points, None, None

        # Get the tilt matrix [only if needed]
        if self.Nparams >= 14:
            R, _, _, invR = self._compute_tilt_matrix(dp=False, inv=True)

        # Prepare the output array:
        normalized_points = numpy.empty((Npoints, 2), dtype=Package.get_float_dtype()) # shape (Npoints, 2)

        # Create the mask for the points in computation
        mask = numpy.ones((Npoints,), dtype=numpy.bool) # shape (Npoints,)

        # Remove the perspective transformation [only if needed]
        if self.Nparams >= 14:
            x_0 = numpy.dot(invR[0, 0], x_D) + numpy.dot(invR[0, 1], y_D) + invR[0, 2] # shape (Npoints, 1)
            y_0 = numpy.dot(invR[1, 0], x_D) + numpy.dot(invR[1, 1], y_D) + invR[1, 2] # shape (Npoints, 1)
            z_0 = numpy.dot(invR[2, 0], x_D) + numpy.dot(invR[2, 1], y_D) + invR[2, 2] # shape (Npoints, 1)
            x_0 = x_0 / z_0 # shape (Npoints, 1)
            y_0 = y_0 / z_0 # shape (Npoints, 1)
        else:
            x_0 = x_D # shape (Npoints, 1)
            y_0 = y_D # shape (Npoints, 1)

        # Initialize the guess for the normalized points
        x_N = x_0.copy() # shape (Npoints, 1)
        y_N = y_0.copy() # shape (Npoints, 1)
        Nopt = Npoints # Number of points in computation

        # Run the iterative algorithm
        for it in range(max_iter):

            # Prepare the powers of the norm (r) [only if needed] with shape (Nopt, 1)
            r2 = x_N ** 2 + y_N ** 2 # shape (Nopt, 1)
            r4 = r2 ** 2 # shape (Nopt, 1)
            if Nparams >= 5:
                r6 = r2 * r4 # shape (Nopt, 1)

            # Prepare the radial distortion coefficients [only if needed] with shape (Nopt, 1)
            if Nparams == 4:
                invK = 1/(1 + self.k1 * r2 + self.k2 * r4) # shape (Nopt, 1)

            elif Nparams == 5:
                invK = 1/(1 + self.k1 * r2 + self.k2 * r4 + self.k3 * r6) # shape (Nopt, 1)
            
            else: # Nparams >= 8
                Kup = (1 + self.k1 * r2 + self.k2 * r4 + self.k3 * r6) # shape (Nopt, 1)
                Kdown = (1 + self.k4 * r2 + self.k5 * r4 + self.k6 * r6) # shape (Nopt, 1)
                invK = Kdown / Kup # shape (Nopt, 1)

            # Prepare the tangential distortion coefficients [only if needed] with shape (Nopt, 1)
            axp1 = ayp2 = 2 * x_N * y_N # shape (Nopt, 1)
            axp2 = r2 + 2 * x_N ** 2 # shape (Nopt, 1)
            ayp1 = r2 + 2 * y_N ** 2 # shape (Nopt, 1)
            x_tangential = self.p1 * axp1 + self.p2 * axp2 # shape (Nopt, 1)
            y_tangential = self.p1 * ayp1 + self.p2 * ayp2 # shape (Nopt, 1)

            # Prepare the prism distortion coefficients [only if needed] with shape (Nopt, 1)
            x_prism = numpy.zeros((Nopt, 1), dtype=Package.get_float_dtype()) # shape (Nopt, 1)
            y_prism = numpy.zeros((Nopt, 1), dtype=Package.get_float_dtype()) # shape (Nopt, 1)
            if Nparams >= 12:
                x_prism = self.s1 * r2 + self.s2 * r4 # shape (Nopt, 1)
                y_prism = self.s3 * r2 + self.s4 * r4 # shape (Nopt, 1)

            # Update the normalized points
            x_N = (x_0[mask, :] - x_tangential - x_prism) * invK # shape (Nopt, 1)
            y_N = (y_0[mask, :] - y_tangential - y_prism) * invK # shape (Nopt, 1)

            # Update the normalized points
            normalized_points[mask, 0] = x_N.ravel() # shape (Nopt,)
            normalized_points[mask, 1] = y_N.ravel() # shape (Nopt,)

            # Distortion convergence check
            distorted_points_optimized, _, _ = self._transform(numpy.concatenate((x_N, y_N), axis=1), dx=False, dp=False) # shape (Nopt, 2)

            # Compute the norm of the difference
            diff = numpy.linalg.norm(distorted_points_optimized - distorted_points[mask, :], axis=1) # shape (Nopt,)
            eps_mask = diff > eps # shape (Nopt,)
            mask[mask] = numpy.logical_and(mask[mask], eps_mask)

            # Crop the X_N and Y_N arrays
            Nopt = numpy.sum(mask)
            if Nopt == 0:
                break
            x_N = x_N[eps_mask] # shape (NewNopt, 1)
            y_N = y_N[eps_mask] # shape (NewNopt, 1)
        # Return the normalized points
        return normalized_points, None, None


    def _inverse_transform_opencv(self, distorted_points: numpy.ndarray, *, dx: bool = False, dp: bool = False) -> Tuple[numpy.ndarray, Optional[numpy.ndarray], Optional[numpy.ndarray]]:
        r"""
        Compute the inverse transformation from the ``distorted_points`` to the ``normalized_points`` using OpenCV's ``undistortPoints`` function.

        The equation used for the transformation is given in the main documentation of the class.

        .. warning::

            This method is not intended to be used directly, but rather through the :meth:`pycvcam.core.Transform.transform` method.
            Please ensure, the shape of the input ``distorted_points`` is (Npoints, 2) with float type.

            The jacobian with respect to the distorted points and the distortion parameters is not computed in this case (always None).

        Parameters
        ----------
        distorted_points : numpy.ndarray
            The distorted points in camera normalized coordinates to be transformed. Shape (Npoints, 2).

        dx : bool, optional
            If True, the jacobian with respect to the distorted points is computed. Default is False

        dp : bool, optional
            If True, the jacobian with respect to the distortion parameters is computed. Default is False

        Returns
        -------
        normalized_points : numpy.ndarray
            The normalized points in camera normalized coordinates, which are equal to the x and y components of the image points. Shape (Npoints, 2).

        jacobian_dx : Optional[numpy.ndarray]
            Always None, since the jacobian with respect to the distorted points is not computed by an iterative algorithm.

        jacobian_dp : Optional[numpy.ndarray]
            Always None, since the jacobian with respect to the distortion parameters is not computed by an iterative algorithm.

        """
        if dx or dp:
            print("\n[WARNING]: Undistortion with OpenCV and dx=True or dp=True. The jacobians cannot be computed with this method. They are always None.\n")
        
        # Create the contiguous array of shape (Npoints, 1, 2) for cv2 compatibility
        distorted_points = numpy.ascontiguousarray(distorted_points.reshape(-1, 1, 2), dtype=Package.get_float_dtype())

        # Apply the OpenCV undistortion removing rvec, tvec and intrinsic matrix
        Rmat = numpy.eye(3, dtype=Package.get_float_dtype())
        Pmat = numpy.eye(3, dtype=Package.get_float_dtype())
        intrinsic_matrix = numpy.eye(3, dtype=Package.get_float_dtype())
        normalized_points = cv2.undistortPoints(distorted_points, intrinsic_matrix, self.parameters, Rmat, Pmat) # shape (Npoints, 1, 2)

        # Reshape the normalized points to (Npoints, 2)
        normalized_points = numpy.asarray(normalized_points[:,0,:], dtype=Package.get_float_dtype())

        # Return the normalized points and the jacobian
        return normalized_points, None, None