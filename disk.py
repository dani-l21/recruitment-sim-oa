import numpy as np

#define constants
GRAVITY_ACCEL = 9.81


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """
    
    #Solution Algorithm:
        #Assume rolling without slipping, friction does no work
        #Solve using conservation of energy:
            #E_initial = E_final
            #mgh = 1/2 mv^2 + 1/2 Iw^2
                #rotational inertia: I = 1/2MR^2 for disk
                #for rolling without slipping: v = rw, w = v/r
            #mgh = 1/2 mv^2 + 1/2 (1/2 mR^2) (v/R)^2
            #mgh = 1/2mv^2 + 1/4 mv^2
            #v = sqrt(4/3 gh)
        #return speed

    if (height < 0):
        print("Invalid height, height cannot be less than 0")
        return 0
    
    return np.sqrt(4/3*GRAVITY_ACCEL*height)



#-----------------------------------------------------------------------------------------------------------------

#Run tests
def test_function():
    result = final_disk_speed(1.0, 1, 30, 1, 0.2, 0.1)
    expected = np.sqrt((4/3) * GRAVITY_ACCEL * 1.0)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_zero_height():
    result = final_disk_speed(0.0, 1, 45, 1, 0.5, 0.1)
    assert result == 0.0, f"Expected 0.0, got {result}"

def test_negative_height():
    result = final_disk_speed(-1.0, 1, 45, 1, 0.5, 0.1)
    assert np.isnan(result) or result <= 0, f"Expected invalid result for negative height, got {result}"

def test_large_height():
    h = 1000000
    result = final_disk_speed(h, 0, 0, 0, 0, 0)
    expected = np.sqrt((4 / 3) * GRAVITY_ACCEL * h)
    assert np.isclose(result, expected, rtol=1e-5), f"Expected {expected}, got {result}"

def test_zero_mass():
    """Tests the scenario when mass is zero. Should not affect speed."""
    result = final_disk_speed(5, 1, 10, 0, 0.1, 0.2)
    expected = np.sqrt((4 / 3) * GRAVITY_ACCEL * 5)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_zero_friction():
    """Tests the scenario when friction is zero. Should not affect speed."""
    result = final_disk_speed(5, 1, 10, 1, 0, 0.2)
    expected = np.sqrt((4 / 3) * GRAVITY_ACCEL * 5)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_zero_radius():
    """Tests the scenario when radius is zero. Should not affect speed."""
    result = final_disk_speed(5, 1, 10, 1, 0.1, 0)
    expected = np.sqrt((4 / 3) * GRAVITY_ACCEL * 5)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"


# Run tests
if __name__ == "__main__":
    test_function()
    test_zero_height()
    test_negative_height()
    test_large_height()
    test_zero_mass()
    test_zero_friction()
    test_zero_radius()
    print("All tests passed :)")
