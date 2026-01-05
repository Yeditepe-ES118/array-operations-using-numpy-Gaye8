import numpy as np

def stat():
    # load data
    data = np.loadtxt("populations.txt")

    # extract hare column (2nd column)
    hare = data[:, 1]

    # year when hare population is minimum
    min_year_hare = data[np.argmin(hare), 0]

    # average of lynx population (3rd column)
    lynx_avg = np.mean(data[:, 2])

    # create new_data with an extra column (sum of species)
    species_sum = np.sum(data[:, 1:], axis=1)
    new_data = np.column_stack((data, species_sum))

    # set carrot population below 40000 to 0
    new_data[new_data[:, 3] < 40000, 3] = 0

    return data, hare, min_year_hare, lynx_avg, new_data
