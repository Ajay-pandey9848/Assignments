import numpy as np

# Define matrix A
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

# Verify A * A_inv = I and A_inv * A = I
multiplication1 = np.dot(A, A_inv)  # Matrix product A * A^-1
multiplication2 = np.dot(A_inv, A)  # Matrix product A^-1 * A


print("\nA * A^-1 (should be close to Identity matrix):")
print(multiplication1)

print("\nA^-1 * A (should be close to Identity matrix):")
print(multiplication2)

# Check if the results are close to the identity matrix
identity = np.eye(3)  # 3x3 Identity matrix
print("\nIs A * A^-1 close to the identity matrix?")
print(np.allclose(multiplication1, identity))  # True if close

print("\nIs A^-1 * A close to the identity matrix?")
print(np.allclose(multiplication2, identity))  # True if close
