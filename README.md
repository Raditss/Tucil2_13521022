# Closest Pair of Points

This program finds the closest pair of points in a list of n-dimensional points using the divide and conquer algorithm.

# Usage
* Run the program using `python "src/Closest_Pair.py"` (windows)
* Run the program using `python3 src/Closest_Pair.py` (linux/mac)
* Enter the number of elements (between 2 and 1000).
* Enter the number of dimensions (between 3 and 7).
* The program will generate a list of random n-dimensional points.
* The program will calculate the closest pair of points using the divide and conquer algorithm.
* The program will display the closest pair of points and the distance between them.
* The program will display the total Euclidean equation.
* The program will display a 3D scatter plot of the points with the closest pair of points highlighted in red.
# Dependencies
* numpy
* matplotlib

# Code
The main function closest_pair(points) takes in a list of n-dimensional points and returns the closest pair of points and the distance between them. The function uses the helper function _closest_pair(points_sorted_x) to recursively find the closest pair of points.

The helper function _closest_pair(points_sorted_x) takes in a sorted list of points sorted by the x-coordinate and recursively finds the closest pair of points. If the number of points is less than or equal to 3, the function _closest_pair_brute_force(points) is used to find the closest pair of points.

The function _closest_pair_brute_force(points) takes in a list of points and uses brute force to find the closest pair of points.

# Author
- Raditya Naufal Abiyu (13521022)