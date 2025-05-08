# Solution to the Assessment

My assumptions and solution is written in this document and the code is written in disk.py.

First, I will provide a list of assumptions made for solving the problem before presenting my solution written in Python.
There are a few assumptions made for this problem. First, we are assuming the object is a uniform solid disk that begins rolling without slipping down the incline, with air resistance neglected. Second, we are assuming the disk starts with zero translational or rotational motion. Third, the positive direction of velocity is assumed to be down and to the left, in the direction the disk is rolling down the ramp therefore it has the same magnitude as the speed. As the object is a disk, the rotational inertia would be 1/2MR^2 and the rolling condition would be v = wR where v is the translational velocity, w is the angular velocity, and R is the radius of the disk. Lastly, we are assuming the gravitational acceleration of the disk is 9.81m/s^2 (or that the disk is on the surface of the Earth).
I will solve this problem using the principle of conservation of energy as the friction force acts on the disk to prevent slipping. Here is my solution with the code below.
