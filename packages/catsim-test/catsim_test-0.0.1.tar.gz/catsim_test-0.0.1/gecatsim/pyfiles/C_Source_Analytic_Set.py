import numpy as np
from ctypes import *
from numpy.ctypeslib import ndpointer
    
def C_Source_Analytic_Set(cfg, SourceWeights = None,NumberOfSubSources = None): 
    print('Setting the source info for an ANALYTIC phantom in C global variables.')
    #cfgnew = cfg.get_current_cfg();
    func = cfg.clib.set_src_info
    sourceWeights = np.copy(cfg.src.weights.astype(np.double), order='C')
    #NumberOfSubSources = 
    NumberOfSubSources = np.int32(NumberOfSubSources)
    func.argtypes = [ndpointer(c_double), c_int]
    func.restype = None
    #ret_SourceWeights= np.zeros(sourceWeights.shape, dtype=np.double)
    func(sourceWeights,NumberOfSubSources)

    return sourceWeights
