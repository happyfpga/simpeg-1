""" module SimPEG.EM.NSEM

SimPEG implementation of the natural source problem
(including magenetotelluric, tipper and ZTEM)



"""
from __future__ import absolute_import

import SimPEG.EM.NSEM.Utils
import SimPEG.EM.NSEM.SrcNSEM
from .SurveyNSEM import Survey, Data
from .RxNSEM import rxPoint_impedance1D, rxPoint_impedance3D, rxPoint_tipper3D
from .FieldsNSEM import Fields1D_ePrimSec, Fields3D_ePrimSec
from .ProblemNSEM import Problem1D_ePrimSec, Problem3D_ePrimSec