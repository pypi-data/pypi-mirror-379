
def a():
    return "Practical 1: Matrix Multiplication & Eigenvalues"



def a1():
    return """import tensorflow as tf

print("Matrix Multiplication Demo")"""

def a2():
    return """x = tf.constant([1,2,3,4,5,6], shape=[2,3])
print(x)"""

def a3():
    return """y = tf.constant([7,8,9,10,11,12], shape=[3,2])
print(y)"""

def a4():
    return """z = tf.matmul(x, y)
print("Product: ", z)"""

def a5():
    return """e_matrix_A = tf.random.uniform([2,2], minval=3, maxval=10, dtype=tf.float32, name="matrixA")
print("Matrix A:\\n{}\\n\\n".format(e_matrix_A))"""

def a6():
    return """eigen_values_A, eigen_vectors_A = tf.linalg.eigh(e_matrix_A)
print("Eigen Vectors:\\n{}\\n\\nEigen Values:\\n{}\\n".format(eigen_vectors_A, eigen_values_A))"""


