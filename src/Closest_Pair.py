import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
import platform



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0]
    left = []
    right = []
    equal = []
    for elem in arr:
        if elem[0] < pivot:
            left.append(elem)
        elif elem[0] == pivot:
            equal.append(elem)
        else:
            right.append(elem)
    return quick_sort(left) + equal + quick_sort(right)


def closest_pair(points):
    points_sorted_x = quick_sort(points)
    return _closest_pair(points_sorted_x)



def _closest_pair(points_sorted_x):
    global c
    d=len(points_sorted_x[0])
    n = len(points_sorted_x)
    if n <= 3:
        return _closest_pair_brute_force(points_sorted_x)

    # Divide the points into two sets
    mid = n // 2
    left_x, right_x = points_sorted_x[:mid], points_sorted_x[mid:]


    # Recursively find the closest pair in the left and right sets
    distance_left, closest_pair_left = _closest_pair(left_x)
    distance_right, closest_pair_right = _closest_pair(right_x)
    if distance_left < distance_right:
        distance = distance_left
        closest_pair = closest_pair_left
    else:
        distance = distance_right
        closest_pair = closest_pair_right

    # Find the closest pair with one point in each set

    x_mid_point = points_sorted_x[mid]
    strip = [point for point in points_sorted_x if abs(point[0] - x_mid_point[0]) <= distance]
    n_strip = len(strip)
    for i in range(n_strip):
        j = i + 1
        while j < n_strip and (strip[j][0] - strip[i][0]) < distance:
            distance_ij = np.sqrt(np.sum([(strip[i][k] - strip[j][k])**2 for k in range(d)]))
            c+=1
            if distance_ij < distance:
                distance = distance_ij
                closest_pair = strip[i], strip[j]
            j += 1
    return distance, closest_pair


def _closest_pair_brute_force(points):
    global c
    closest_distance = float('inf')
    closest_points = None
    for i, point1 in enumerate(points):
        for point2 in points[i+1:]:
            distance = np.sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]) ** 0.5
            c+=1
            if distance < closest_distance:
                closest_distance = distance
                closest_points = (point1, point2)
    return closest_distance, closest_points

def closest_pair_brute_force(points):
    global cb
    closest_distance = float('inf')
    closest_points = None
    for i, point1 in enumerate(points):
        for point2 in points[i+1:]:
            distance = np.sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]) ** 0.5
            cb+=1
            if distance < closest_distance:
                closest_distance = distance
                closest_points = (point1, point2)
    return closest_distance, closest_points


n=int(input('Numbers of element(2-1000) : '))
d=int(input('Numbers of dimension (3-7) : '))
c=0
cb=0


# Generate a random list of 3D points
points = [[round(random.uniform(0, 100), 2) for i in range(d)] for j in range(n)]
start=time.time()
distance, closest_points = list(closest_pair(points))
end=time.time()
timed=round(end-start,2)
distance=round(distance,2)
# Print the result
print("======================Divide and Conquer======================")
print(f"The closest pair of points is {closest_points[0]} and {closest_points[1]} with a distance of {distance}")
print(f"Time: {timed*1000} ms (run on {platform.processor()})")
print(f"Total euclidian equation: {c}")
print("======================BruteForce======================")
a=time.time()
brute_distance,brute_point = list(closest_pair_brute_force(points))
b=time.time()
timeb=round(b-a,2)
print(f"The closest pair of points is {closest_points[0]} and {closest_points[1]} with a distance of {distance}")
print(f"Time: {timeb*1000} ms (run on {platform.processor()})")
print(f"Total euclidian equation: {cb}")



# Separate the x, y, and z coordinates into individual arrays
x_coords = [point[0] for point in points]
x_coords.remove(closest_points[0][0])
x_coords.remove(closest_points[1][0])
y_coords = [point[1] for point in points]
y_coords.remove(closest_points[0][1])
y_coords.remove(closest_points[1][1])
z_coords = [point[2] for point in points]
z_coords.remove(closest_points[0][2])
z_coords.remove(closest_points[1][2])

# Create a 3D scatter plot of the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, c='black')

# Highlight the first two points in red
ax.scatter(closest_points[0][0], closest_points[0][1], closest_points[0][2], c='red')
ax.scatter(closest_points[1][0], closest_points[1][1], closest_points[1][2], c='red')

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.plot([closest_points[0][0], closest_points[1][0]], [closest_points[0][1], closest_points[1][1]], [closest_points[0][2], closest_points[1][2]], c='red')

# Show the plot
plt.show()






