"""
1. for pair of of points find m and b with formula
2. find the average ms and bs
3. find mean squared error (MSE), given forula on instructions
y = mx + b
"""

points = [
    #  0         1
    (0.00, -8.00), 
    (-10.00, -36.00), 
    (9.00, 21.00),
    (-5.00, -20.00),
    (4.00, 6.00),
    (15.00, 35.00), 
    (30.00, 81.00),
    (-20.00, -69.00)
]

# sort by x value
points.sort()

def printPoints(points):    
    for i, (x, y) in enumerate(points):
        print(f"x[ {i}] = {x} y[ {i}] = {y}")

def get_slopes_and_intercepts(points):
    slopes, intercepts = [], []
    
    for (xi, yi), (xj, yj) in zip(points, points[1:]):
        m = (yi - yj) / (xi - xj)
        b = (xi*yj - xj*yi) / (xi - xj)
        
        slopes.append(m)
        intercepts.append(b)

    return slopes, intercepts

        
def y_hat(points, slopeAvg, interceptAvg):
    for i, (xi, yi) in enumerate(points):
        y_hat_val = (slopeAvg * xi) + interceptAvg
        print(f"yhat[ {i}] = {y_hat_val:.2f}, y[ {i}] = {yi:.2f}")

def mse(points, m, b):
    squared_error_sum = sum( ( (m*x + b) - y )**2 for x, y in points )
    print(f"\nMean Squared Error = {squared_error_sum / len(points):.6f}")

"""

function calls

"""

print("After sorting the dataset of 8 points:")
printPoints(points)

slopes, intercepts = get_slopes_and_intercepts(points)

print("\nThe pairwise slopes and Intercepts:")
for i, (m, b) in enumerate(zip(slopes, intercepts)):
    print(f"m[{i}] = {m:.2f} b[{i}] = {b:.2f}")    

slopeAvg =  sum(slopes) / len(slopes)
interceptAvg = sum(intercepts) / len(intercepts)

print("\nThe model parameters obtained by the program:")
print(f"Slope Estimate = {slopeAvg:.2f}")
print(f"Intercept Estimate = {interceptAvg:.2f}")

print("\nThe discrepancies between the model predictions and the actual values of the dataset:")
y_hat(points, slopeAvg, interceptAvg)

mse(points, slopeAvg, interceptAvg)
