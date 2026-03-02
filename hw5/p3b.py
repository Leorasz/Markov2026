import sympy as sp
a = sp.symbols('a')
A = sp.Matrix([[1-a, a, 0], [a, 0, 1-a], [0, 1-a, a]])
eigvals = A.eigenvals()
eigvects = A.eigenvects()
print("Eigenvalues:", eigvals)
print("Eigenvects:", eigvects)
