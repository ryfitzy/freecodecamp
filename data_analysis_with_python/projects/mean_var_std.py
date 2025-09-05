import numpy as np

def calculate(lst: list) -> dict:
  if len(lst) != 9:
    raise ValueError("List must contain nine numbers")
  
  arr = np.reshape(lst, (3,3))

  return {
    'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), float(arr.mean())],
    'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), float(arr.var())],
    'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), float(arr.std())],
    'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), int(arr.max())],
    'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), int(arr.min())],
    'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), int(arr.sum())]
  }