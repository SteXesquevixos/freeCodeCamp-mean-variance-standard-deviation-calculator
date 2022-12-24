import numpy as np
import pandas as pd

'''The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 
    Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum 
    along both axes and for the flattened matrix.
    If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with 
    the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy 
    arrays.'''


def calculate(*args):

    if len(np.array(*args)) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        # Turning the list into an matrix
        matrix = np.array(*args).reshape((3, 3))

        # Calculating the mean, variance, standard deviation, max, min and sum
        calc = pd.Series([
            [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(*args)],
            [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(*args)],
            [np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(*args)],
            [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(*args)],
            [np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(*args)],
            [np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(*args)]],
            index=['mean', 'variance', 'standard deviation',
                   'max', 'min', 'sum'])

        # Turning calc into a dictionary
        return calc.to_dict()
