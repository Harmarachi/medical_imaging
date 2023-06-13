import os
from typing import Sequence

def filepath(filename, subfolder='HCC_002/09-26-1997-NA-ABDPELVIS-84861/4.000000-Recon 2 LIVER 3 PHASE AP-85789'):
    folder = os.path.dirname(__file__)
    return f'{folder}/{subfolder}/{filename}'


def filepath2(filename, subfolder='Project'):
    folder = os.path.dirname(__file__)
    return f'{folder}/{subfolder}/{filename}'

