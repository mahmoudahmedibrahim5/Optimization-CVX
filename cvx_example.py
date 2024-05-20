import cvxpy as cp

# Define the variables
x1 = cp.Variable()
x2 = cp.Variable()

# Define the objective function
objective = cp.Minimize(x1 + x2)

# Define the constraints
constraints = [
    x1 + 4*x2 == 2,
    x2 >= 0
]

# Formulate the problem
problem = cp.Problem(objective, constraints)

# Solve the problem
result = problem.solve()

# Print the results
print("Optimal value:", result)
print("Optimal x1:", x1.value)
print("Optimal x2:", x2.value)
