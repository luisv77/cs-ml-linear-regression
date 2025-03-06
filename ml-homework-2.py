"""
1. for pair of of points find m and b with formula
2. find the average ms and bs
3. find mean squared error (MSE), given forula on instructions
y = mx + b
"""
# List of points (x, y) where each tuple is a pair representing a point
points = [
    (0.00, -8.00), 
    (-10.00, -36.00), 
    (9.00, 21.00),
    (-5.00, -20.00),
    (4.00, 6.00),
    (15.00, 35.00), 
    (30.00, 81.00),
    (-20.00, -69.00)
]

# Sorting the points by the x-coordinate to prepare for further processing
points.sort()

# Function to print the points in a readable format
def printPoints(points):    
    for i, (x, y) in enumerate(points):
        print(f"x[ {i}] = {x:.2f} y[ {i}] = {y:.2f}")

# Function to calculate the slope (m) and intercept (b) for each consecutive pair of points
def get_slopes_and_intercepts(points):
    slopes, intercepts = [], []
    
    # Looping over consecutive pairs of points in the list
    for (xi, yi), (xj, yj) in zip(points, points[1:]):
        # Calculating the slope (m) using the formula: m = (y2 - y1) / (x2 - x1)
        m = (yi - yj) / (xi - xj)
        
        # Calculating the intercept (b) using the formula: b = (x1*y2 - x2*y1) / (x1 - x2)
        b = (xi*yj - xj*yi) / (xi - xj)
        
        # Adding the calculated values to the respective lists
        slopes.append(m)
        intercepts.append(b)

    return slopes, intercepts

# Function to compute and print the predicted values of y (y_hat) using the average slope and intercept
def y_hat(points, slopeAvg, interceptAvg):
    for i, (xi, yi) in enumerate(points):
        # Calculate the predicted value y_hat using the formula: y_hat = m * x + b
        y_hat_val = (slopeAvg * xi) + interceptAvg
        print(f"yhat[ {i}] = {y_hat_val:.2f}, y[ {i}] = {yi:.2f}")

# Function to calculate and print the Mean Squared Error (MSE) for the model
def mse(points, m, b):
    # Calculate the sum of squared errors
    squared_error_sum = sum(((m*x + b) - y) ** 2 for x, y in points)
    
    # Calculate and print the Mean Squared Error (MSE) by dividing the sum of squared errors by the number of points
    print(f"\nMean Squared Error = {squared_error_sum / len(points):.6f}")

# Function calls for the above functions


print("After sorting the dataset of 8 points:")
printPoints(points)

# set slopes and intercepts equal to return values of function
slopes, intercepts = get_slopes_and_intercepts(points)

# Display the calculated slopes and intercepts for each pair of points
print("\nThe pairwise slopes and Intercepts:")
for i, (m, b) in enumerate(zip(slopes, intercepts)):
    print(f"m[{i}] = {m:.2f} b[{i}] = {b:.2f}")    

# Calculate the average slope and intercept
slopeAvg = sum(slopes) / len(slopes)
interceptAvg = sum(intercepts) / len(intercepts)

# Display average slope and intercept
print("\nThe model parameters obtained by the program:")
print(f"Slope Estimate = {slopeAvg:.2f}")
print(f"Intercept Estimate = {interceptAvg:.2f}")

# display the predicted values (y_hat) for the points using the average model parameters
print("\nThe discrepancies between the model predictions and the actual values of the dataset:")
y_hat(points, slopeAvg, interceptAvg)

# display the Mean Squared Error (MSE) for the model
mse(points, slopeAvg, interceptAvg)
