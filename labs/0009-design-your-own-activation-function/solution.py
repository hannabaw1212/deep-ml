# --- cell 1 ---
import numpy as np

def activation(x):
    '''
    Apply an activation function element-wise.
    
    Args:
        x: numpy array of any shape (raw neuron outputs)
    
    Returns:
        numpy array of same shape (activated outputs)
    
    Requirements:
        - Must be non-linear (not just returning x)
        - Must work on arrays of any shape
        - Must be deterministic
    '''
    # TODO: Implement your activation function
    
    result = 0.3 * (1 / (1 + np.exp(-x))) + 0.7 * ((np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)))  # Replace with your activation
    
    return result