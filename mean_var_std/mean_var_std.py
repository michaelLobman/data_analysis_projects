import numpy as np

def calculate(list):

    if len(list) < 9:
       raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3,3)

    calculations = {
        'mean': [ arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean() ],
        'variance': [ arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var() ],
        'standard deviation': [ arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std() ],
        'max': [ arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max() ],
        'min': [ arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min() ],
        'sum': [ arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum() ]
    }

    return calculations