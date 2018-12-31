import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
import scipy.io as sio
from skimage import measure
import sys
import os
from os.path import exists, join
from IPython import embed

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(join(curr_dir, '../tools/'))
import smpl_utils

SMPL_PATH = os.getenv('SMPL_PATH', join(curr_dir, '../tools/smpl'))
sys.path.append(SMPL_PATH)
from smpl_webuser.serialization import load_model

class meshobj:
    def __init__(self, vertices, faces):
            self.r = vertices
            self.f = faces


def mkdir_safe(directory):
    if not exists(directory):
        try:
            os.makedirs(directory)
        except:  # FileExistsError:
            pass

def main():
    # <===== PARSE ARGUMENTS
    import argparse
    parser = argparse.ArgumentParser(description='Fit SMPL body to mesh predictions.')
    parser.add_argument('--dataname', type=str, help='name of the data')

    args = parser.parse_args()
    dataname = args.dataname

    print('------- Option -------')
    print('\tdataname: %s' % dataname)
    # ======>

    # <========= LOAD SMPL MODEL
    m = load_model(join(SMPL_PATH, 'models/basicModel_neutral_lbs_10_207_0_v1.0.0.pkl'))
    # Init upright t-pose
    initial_model = m.copy()
    initial_model.pose[0:3] = np.array((np.pi, 0, 0))
    # =========>

    # <======== 
    
