# Numpy is a multidimensional array library
# Can store data in N-dimensions

# Why use Numpy over Python lists?
# Numpy is wayyyyy faster due to its fixed types
# Numpy ints uses wayyyy less bytes than Python ints
# It's faster to read less bytes of memory
# Also no type checking when iterating through objects in lists

# Numpy uses contiguous memory (information in memory is stored next to each other) whereas python lists may not
# Benefits: 
#  SIMD (Single-Instruction, Multiple Data) Vector Processing
#  Effective Cache Utilization

# Applications of Numpy
# Mathematics (MATLAB Replacement, but you could use SciPy for more advanced features)
# Plotting (Matplotlib), Backend (Pandas, Digital Photography)
# Machine Learning

# Importing the NumPy library
import numpy as np

def numpy_attributes():
  # Initializing numpy arrays
  A = np.array([2,3,5,7])
  print(A)

  B = np.array([[1,3,5,7,9], [2,4,6,8,10]])
  print(B)

  # Getting dimensions
  print("Number of dimensions of A:", A.ndim)
  print("Number of dimensions of B:", B.ndim)

  # Getting Shape (#_of_rows, #_of_columns)
  print("Shape of A (rows, columns):", A.shape)
  print("Shape of B (rows, columns):", B.shape)

  # Get type (default is int64)
  print("Item types of A:", A.dtype)
  print("Item types of B:", B.dtype)

  # Get size (since the default item type is int64, each item size is 8 bytes)
  print("Item Size of A:", A.itemsize)
  print("Item size of B:", B.itemsize)

  # Get total size (number of elements)
  print("Number of elements in A:", A.size)
  print("Number of elements in B:", B.size)

  # Get total size in bytes 
  # (if statement is to show it can be calculated by multiplying the number of elements by the size in bytes of each element)
  if A.nbytes == A.size * A.itemsize:
    print("Total Size in bytes of A:", A.nbytes)
    print("Total Size in bytes of B:", B.nbytes)

  # We can specify the data type of each element if we know the limitations of our data
  # Note that int8 is a signed integer value that takes values from -128 to 127
  C = np.array([-127,7,127], dtype='int8')
  print("Total Size in bytes of C:", C.nbytes)

  F = np.array([[1.0,2.0,3.0],[3.0,4.0,5.0]])
  print("Default for float data types are float64 but like previously, it can be changed")
  print(F)
  print(F.dtype)
  print(F.itemsize)
  print(F.size)
  print(F.nbytes)
  return

# Accessing/Changing specific elements, rows, columns, etc.
def numpy_access_and_modification():
  a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

  # Get a specific elements [r,c]
  print(a[1,5])

  # Get a specific row
  print(a[0, :])

  # Get a specific column
  print(a[:, 2])

  # Getting a bit fancy [startindex:endindex:step]
  print(a[0, 1:6:2])
  print(a[0, 1:-1:2])

  # Element modification
  a[1,5]=20
  print(a)

  a[:,2] = 5
  print(a)
  a[:,2] = [1,2]
  print(a)

  # Work from the outside-in with multidimensional arrays
  b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
  print(b)
  print(b[0,1,1])
  print(b[:,1,:])

def array_initialization_types():
  # ALL zeros matrix (float64 datatype by default)
  a = np.zeros((5,5))
  print(a)

  # ALL ones matrix
  a = np.ones(7, dtype='int32')
  print(a)

  # Any other number
  # first parameter is the shape and the second parameter is value to fill
  a = np.full((2,3), 7, dtype='float32')
  print(a)
  # There is also full_like (uses the shape of first parameter array)
  # You could also just pass in a.shape if using regular full
  print(np.full_like(a, 13))

  # Random decimal numbers:
  print(np.random.rand(4,2))
  print(np.random.random_sample(a.shape))

  # Random integer values
  # Ints from 0 to 7(exclusive)
  print(np.random.randint(7, size=(4,3)))
  # Ints from -7 to 14(exclusive)
  print(np.random.randint(-7,14, size=(2,4)))

  # Identity matrix
  print(np.identity(5))

  # Repeating arrays
  arr = np.array([[1,2,3]])
  print(np.repeat(arr,3,axis=0))

  # Problem: Initialize an array using the tools above of the following structure:
  '''
      1 1 1 1 1
      1 0 0 0 1
      1 0 9 0 1
      1 0 0 0 1
      1 1 1 1 1
  '''
  output = np.ones((5,5))
  middle = np.zeros((3,3))
  middle[1][1] = 9
  output[1:-1, 1:-1] = middle
  print(output)

  # Copying arrays (be careful... B POINTS to the same object as A)
  a = np.array([1,2,3])
  b = a
  b[0] = 100
  print(b)
  print(a)

  # To prevent this, use copy
  b = a.copy()
  b[-1] = -1
  print(b)
  print(a)

def numpy_mathematics():
  a = np.array([1,2,3,4])
  print(a)

  # Element-wise operations
  print(a+2)
  print(a-2)
  print(a*2)
  print(a/2)
  a += 2
  print(a)

  b = np.array([1,2,3,4])
  # Note that matrices must be the same shape to element-wise operate on
  print(a+b)
  print(a*b)

  # Trig functions on arrays
  print(np.cos(a))
  print(np.sin(a))
  print(np.atan(a))

  ### Linear algebra
  a = np.ones((2,3))
  print(a)
  b = np.full((3,2), 2)
  print(b)

  # Matrix multiply (cannot use * since that only does element-wise where the same shape is required)
  print(np.matmul(a,b))

  # Finding the determinant of a matrix
  c = np.identity(3)
  print(np.linalg.det(c))

  # They also have ways to find inverses, eigenvalues, etc.


  ### Statistics
  stats = np.array([[1,2,3],[4,5,6]])
  print(stats)

  # Reminder: Think of the axis parameter as the direction:
  # axis=0 means "go down the rows" (operate column-wise)
  # axis=1 means "go down the columns" (operate row-wise)
  print(np.sum(stats, axis=0)) # Sums down the rows for each column
  print(np.sum(stats, axis=1)) # Sums across the columns for each row
  print(np.sum(stats))

  print(np.min(stats, axis=0))
  print(np.min(stats, axis=1))
  print(np.min(stats))

  print(np.max(stats, axis=0))
  print(np.max(stats, axis=1))
  print(np.max(stats))

def reorganizing_arrays():
  # You can reshape the dimensions so as long as the number of values it holds it equivalent
  before = np.array([[1,2,3,4],[5,6,7,8]])
  print(before)
  after =  before.reshape((8,1))
  print(after)
  print(before.reshape((4,2)))
  print(before.reshape(2,2,2))

  # Vertically stacking vectors (allowed with the same number of columns)
  v1 = np.array([1,2,3,4])
  v2 = np.array([5,6,7,8])

  print(np.vstack([v1,v2]))
  print(np.vstack([v1,v2,v1,v2]))

  # Horizontal stack (allowed with same number of rows)
  h1 = np.ones((2,4))
  h2 = np.zeros((2,2))
  print(np.hstack([h1, h2]))

def loading_data():
  # Loading files
  filedata = np.genfromtxt('../data/data.txt', delimiter=',')
  print(filedata)
  print(filedata.astype('int32'))
  filedata = filedata.astype('int32')
  print(filedata)

  # Indexing with a list in NumPy
  a = np.array([1,2,3,4,5,6,7,8,9])
  print(a[[0,1,2,-1]])

  # Boolean Masking and Advanced Indexing
  print(filedata < 10)
  print(filedata[filedata < 10])

  print(np.any(filedata > 10, axis=0))

  print(np.all(filedata > 5, axis=0))
  print(np.all(filedata > 5, axis=1))
  print((filedata < 10) & (filedata > 5))

  # Indexing Challenge Problem
  a = np.arange(1,31).reshape((6,5))
  print(a)
  print(a[2:4,0:2])
  print(a[[0,1,2,3], [1,2,3,4]])
  print(a[[0,-2,-1], 3:])
  
  



def main():
  #numpy_attributes()
  #numpy_access_and_modification()
  #array_initialization_types()
  #numpy_mathematics()
  #reorganizing_arrays()
  loading_data()

main()