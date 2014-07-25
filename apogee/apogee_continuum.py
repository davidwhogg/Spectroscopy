import numpy as np

def weighted_median(values, weights):
    """
    """
    sindx = np.argsort(values)
    cvalues = 1. * np.cumsum(weights[sindx])
    cvalues = cvalues / cvalues[-1]
    indx = (sindx[cvalues > 0.5])[0]
    return values[indx]

def get_continuum(dataall, delta_lambda=50):
    """
    ## inputs:
    dataall:       (N_lambda, N_star, 3) wavelengths, flux densities, errors
    delta_lambda:  half-width of meadian region in angstroms

    ## output:
    continuum:     (N_lambda, N_star) continuum level

    ## bugs:
    * for loops!
    """
    N_lambda, Nstar, foo = dataall.shape
    continuum = np.zeros(N_lambda, N_star)
    assert foo == 3
    for star in range(Nstar):
        for ll, lam in enumerate(dataall[:, 0, 0]):
            assert dataall[ll, star, 0] == lam
            indx = (np.where(abs(dataall[:, star, 0] - ll) < delta_lambda))[0]
            print median_section.shape
            print median_section
            ivar = 1. / (dataall[indx, star, 2] ** 2)
            continuum[ll, star] = weighted_median(dataall[indx, star, 1], ivar)
    return continuum
