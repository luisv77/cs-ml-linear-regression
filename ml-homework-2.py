"""
1. for pair of of points find m and b with formula
2. find the average ms and bs
3. find mean squared error (MSE), given forula on instructions
y = mx + b


"""

points = [
    #  0         1
    (-20.00, -69.00), # 0
    (-10.00, -36.00), # 1
    (-5.00, -20.00), # 2
    (0.00, -8.00), # 3
    (4.00, 6.00), # 4
    (9.00, 21.00), # 5
    (15.00, 35.00), # 6
    (30.00, 81.00) # 7
]

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

    squared_error_sum = 0
    
    for x, y in points:
        
        y_hat = (m * x) + b
        squared_error_sum += pow(y_hat - y,2)

    mse = squared_error_sum / len(points)

    print(f"Mean Squared Error = {mse:.6f}")

"""

function calls

"""

printPoints(points)
print("")

slopes, intercepts = get_slopes_and_intercepts(points)


slopeAvg = 0
interceptAvg = 0

for i, (m, b) in enumerate(zip(slopes, intercepts)):
    print(f"m[{i}] = {m:.2f} b[{i}] = {b:.2f}")
    slopeAvg += m
    interceptAvg += b
    

slopeAvg /= len(slopes)

interceptAvg /= len(intercepts)



print(f"\nSlope Estimate = {slopeAvg:.2f}")

print(f"Intercept Estimate = {interceptAvg:.2f}")

print("")
y_hat(points, slopeAvg, interceptAvg)

print("")

mse(points, slopeAvg, interceptAvg)
