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

    
    return np.sqrt(4/3*GRAVITY_ACCEL*height)
