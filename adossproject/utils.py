import numpy as np


def usefull_function(param1, param2):
    """
    Return `False` if *param1* is `True`

    :param param1: first parameter
    :type param1: bool
    :param param2: second parameter
    :type param1: int
    """
    print(param2)
    print(np.zeros(param2))
    return param1 is not True
