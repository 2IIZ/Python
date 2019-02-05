import numpy as np
from sklearn import preprocessing


input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

# Binarization
# preprocessing technique which is used when we need to convert our numerical values into Boolean values.
# threshold = under x is 0 above x is 1
data_binarized = preprocessing.Binarizer(threshold = 4).transform(input_data)
print("\nBinarized data:\n", data_binarized)
