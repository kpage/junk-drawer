import random

# * The area of a unit circle is πr^2 = π1^2 = π.
# * A unit circle can be inscribed into a 2x2 square of area 4.
# * The ratio of the area of the inscribed circle to the area of the square is π/4.
# * Since quadrants are symmetrical, the ratio of the area of the circle to the area of the square in any quadrant is also π/4.
# * We can scatter points uniformly in a quadrant and test if they are inside the circle using x^2 + y^2 <= r^2 = 1.
# * The ratio of the points inside the circle "pi" to the total number of points "p" is equal to π/4.
# * We can solve for π with: pi/p = π/4 or π = 4pi/p.
def estimate_pi(num_runs):
    p_i = 0 # num points inside circle
    for i in range(num_runs):
        # Select x, y in [0.0, 1.0) and check if our selection is inside or outside circle
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            p_i += 1
    return 4.0 * p_i / num_runs
