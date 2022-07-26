# import packages
import random
import numpy as np

# generate the dataset
def get_dataset(isFirst = False, slope = None, constant = None, data_range = None):
    if not isFirst and not (slope and constant):
        print("Warning: no guarantee of set pattern in dataset for input values")

    # number of items in the set
    num_data_points = int(random.random() * 50) + 50
    print("Total data points: %s"%num_data_points)

    # get a random range, greater than or equal to 10
    if not data_range:
        data_range = generate_data_range()

    if not constant:
        constant = generate_constant(data_range)

    if not slope:
        slope = generate_slope()

 

    x = []
    y = [] 

    for item in range(num_data_points):
        x_value = int(random.random() * data_range)

        random_error = int(random.random() * data_range * 0.1) 
        
        # print(type(x_value))
        # print(type(slope))
        # print("break")

        y_value = x_value * slope
        # print(type(y_value))
        # print(type(constant))
        # print(type(random_error))
        y_value += constant + random_error
        

        x += [x_value]
        y += [y_value]

    # print_dataset(x, y)
    if isFirst:
        return x, y, slope, constant
    
    return x, y

def generate_constant(data_range):
    # generate an approximate constant theta
    constant = int(random.random() * data_range)
    print("Approximate constant: %s"%constant)
    return constant

def generate_slope():
    # generate an approximate slope theta1
    slope = int(random.random() * 11) # randomly generate a slope, slope can be 0
    print("Approximate slope: %s"%slope)
    return slope

def generate_data_range():
    return int(random.random() * 90) + 10

# print all items from the dataset
def print_dataset(x, y):
    # print the x dataset
    print("x")
    for x_val in x:
        print(x_val)
    
    # print the y dataset
    print("y")
    for y_val in y:
        print(y_val)
    return 

def gradient_aggregate(theta0_list, theta1_list):
    return np.mean(theta0_list), np.mean(theta1_list)

# compute mean squared error: NORM(UV-M, 'fro')
def MSE(U, V, M, obs):
    s = 0
    st = 0
    nSamp = len(obs)
    for l in range(nSamp):
        i, j = obs[l]
        s += (np.dot(U[i, :], V[j, :].T) - M[i, j])**2
    return np.sqrt(s)

# compute relative Frobenius error: NORM(UV-M, 'fro')/NORM(M, 'fro')
def RelError(U, V, M, obs):
    s = 0
    st = 0
    nSamp = len(obs)
    for l in range(nSamp):
        i, j = obs[l]
        s += (np.dot(U[i, :], V[j, :].T) - M[i, j])**2
        st += (M[i, j])**2
    return np.sqrt(s)/np.sqrt(st)