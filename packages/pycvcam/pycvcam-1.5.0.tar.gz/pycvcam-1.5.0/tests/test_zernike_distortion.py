import pytest
import numpy

from pycvcam import ZernikeDistortion

@pytest.fixture
def default():
    """Creates a default Distortion object with known parameters."""
    distortion = ZernikeDistortion(Nzer=7)

    # Set Zernike coefficients
    distortion.set_Cx(0, 0, 0.017083945091492785)
    distortion.set_Cy(0, 0, -0.1093719257958107)
    distortion.set_Cx(1, 1, 0.04280641095874525)
    distortion.set_Cx(1, -1, -0.11948575638043393)
    distortion.set_Cy(1, 1, 0.0908833886027441)
    distortion.set_Cy(1, -1, 0.28585912150232207)
    distortion.set_Cx(2, 0, -0.010212748711363793)
    distortion.set_Cy(2, 0, -0.11540175375301409)
    distortion.set_Cx(2, 2, -0.00782950115774214)
    distortion.set_Cx(2, -2, -0.0020199464928398678)
    distortion.set_Cy(2, 2, 0.23398822546004996)
    distortion.set_Cy(2, -2, 0.008727018408134835)
    distortion.set_Cx(3, 1, 0.11774670344474367)
    distortion.set_Cx(3, -1, -0.03842086254300457)
    distortion.set_Cy(3, 1, 0.015958056702810412)
    distortion.set_Cy(3, -1, 0.4053713119884255)
    distortion.set_Cx(3, 3, -0.06941369934820552)
    distortion.set_Cx(3, -3, 0.06858990952409365)
    distortion.set_Cy(3, 3, -0.058872634305352195)
    distortion.set_Cy(3, -3, -0.27273893460948323)
    distortion.set_Cx(4, 0, -0.0008355538427007839)
    distortion.set_Cy(4, 0, -0.07902677499990182)
    distortion.set_Cx(4, 2, -0.002596009621418076)
    distortion.set_Cx(4, -2, -0.0004671581111743396)
    distortion.set_Cy(4, 2, 0.1622500117071097)
    distortion.set_Cy(4, -2, 0.009242023070156922)
    distortion.set_Cx(4, 4, -0.0016053903604748264)
    distortion.set_Cx(4, -4, 0.003055958197544206)
    distortion.set_Cy(4, 4, -0.16733400168088858)
    distortion.set_Cy(4, -4, -0.016179979676594455)
    distortion.set_Cx(5, 1, 0.012583260318218136)
    distortion.set_Cx(5, -1, -0.015945506008503228)
    distortion.set_Cy(5, 1, 0.005112296621836569)
    distortion.set_Cy(5, -1, 0.1653781339398673)
    distortion.set_Cx(5, 3, -0.03108848626999168)
    distortion.set_Cx(5, -3, 0.034148224370183465)
    distortion.set_Cy(5, 3, -0.029328096123159834)
    distortion.set_Cy(5, -3, -0.13984684802950417)
    distortion.set_Cx(5, 5, 0.08936881806050903)
    distortion.set_Cx(5, -5, -0.06411318032885825)
    distortion.set_Cy(5, 5, 0.0725410316989168)
    distortion.set_Cy(5, -5, 0.10346426469415285)
    distortion.set_Cx(6, 0, 0.0002924901298748926)
    distortion.set_Cy(6, 0, -0.02322855580912703)
    distortion.set_Cx(6, 2, -0.00018960015221684552)
    distortion.set_Cx(6, -2, -0.00037298295468960515)
    distortion.set_Cy(6, 2, 0.049363725455249606)
    distortion.set_Cy(6, -2, 0.003670537559413702)
    distortion.set_Cx(6, 4, 0.0006314053384830566)
    distortion.set_Cx(6, -4, 0.001597676829797511)
    distortion.set_Cy(6, 4, -0.04884846328688792)
    distortion.set_Cy(6, -4, -0.005835730813113942)
    distortion.set_Cx(6, 6, 0.001941729950393342)
    distortion.set_Cx(6, -6, -0.001298495448916161)
    distortion.set_Cy(6, 6, 0.05154502761557224)
    distortion.set_Cy(6, -6, 0.005679929634243922)
    distortion.set_Cx(7, 1, 0.0003465309056524352)
    distortion.set_Cx(7, -1, 0.00029803470070771535)
    distortion.set_Cy(7, 1, -0.0005672611158840981)
    distortion.set_Cy(7, -1, 0.0477615940060408)
    distortion.set_Cx(7, 3, -0.0011746651422660356)
    distortion.set_Cx(7, -3, 0.00704874734072278)
    distortion.set_Cy(7, 3, -0.0025490979756813974)
    distortion.set_Cy(7, -3, -0.04020174877407482)
    distortion.set_Cx(7, 5, 0.015772380855886274)
    distortion.set_Cx(7, -5, -0.017702627357461236)
    distortion.set_Cy(7, 5, 0.012448080057913424)
    distortion.set_Cy(7, -5, 0.02824867723847335)
    distortion.set_Cx(7, 7, -0.048295980450963484)
    distortion.set_Cx(7, -7, 0.028571068337471497)
    distortion.set_Cy(7, 7, -0.03981484964981821)
    distortion.set_Cy(7, -7, -0.01254678379222499)

    distortion.radius = 1
    distortion.center = numpy.array([0.5, 0.5])  # Center of the distortion
    # Ensure the square of (random.rand) is include in the unit circle

    return distortion

def test_parameters(default):
    """Test the parameters property returns the correct distortion parameters."""
    assert default.get_Cx(0, 0) == 0.017083945091492785
    assert default.get_Cy(0, 0) == -0.1093719257958107
    assert default.get_Cx(1, 1) == 0.04280641095874525
    assert default.get_Cx(1, -1) == -0.11948575638043393
    assert default.get_Cy(1, 1) == 0.0908833886027441

def test_jacobian_analytic_numeric_match(default):
    """Test that the analytic Jacobian of the distortion transform matches the numeric approximation."""
    points = numpy.random.rand(10, 2)  # Random 2D points
    result_analytic = default.transform(points, dx=True, dp=True)
    epsilon = 1e-8

    # --- dx (∂output/∂input) ---
    dx_labels = ["X", "Y"]
    for i in range(len(dx_labels)):
        points_plus = points.copy()
        points_plus[:, i] += epsilon
        result_plus = default.transform(points_plus, dx=False, dp=False)
        jacobian_numeric = (result_plus.transformed_points - result_analytic.transformed_points) / epsilon
        try:
            numpy.testing.assert_allclose(
                result_analytic.jacobian_dx[..., i], jacobian_numeric, rtol=1e-3, atol=1e-5
            )
        except AssertionError as e:
            print(f"Jacobian mismatch with respect to input coordinate '{dx_labels[i]}'")
            raise e

    # --- dp (∂output/∂distortion parameters) ---
    param_vec = default.parameters
    for i in range(default.Nparams):
        param_plus = param_vec.copy()
        param_plus[i] += epsilon
        distortion_plus = ZernikeDistortion()
        distortion_plus.parameters = param_plus
        distortion_plus.radius = default.radius
        distortion_plus.center = default.center
        result_plus = distortion_plus.transform(points, dx=False, dp=False)
        jacobian_numeric = (result_plus.transformed_points - result_analytic.transformed_points) / epsilon
        nan_mask = numpy.logical_and(numpy.any(numpy.isnan(jacobian_numeric), axis=-1), 
                                     numpy.any(numpy.isnan(result_analytic.jacobian_dp[..., i]), axis=-1))
        if numpy.sum(nan_mask) > 5:
            print(f"Warning: more than 50% of the points have NaN values in the Jacobian for parameter '{i}'")
        try:
            numpy.testing.assert_allclose(
                result_analytic.jacobian_dp[nan_mask, :, i], jacobian_numeric[nan_mask, :], rtol=1e-3, atol=1e-5
            )
        except AssertionError as e:
            print(f"Jacobian mismatch with respect to parameter '{[i]}'")
            raise e

def test_transform_inverse_transform_consistency(default):
    """Test that transforming and then inverse transforming returns the original points."""
    points = numpy.random.rand(1000, 2)  # Random 2D points

    transformed = default.transform(points)
    inverse_transformed = default.inverse_transform(transformed.transformed_points)

    # Check if the inverse transformed points match the original points
    assert numpy.allclose(inverse_transformed.transformed_points, points, rtol=1e-3, atol=1e-5)