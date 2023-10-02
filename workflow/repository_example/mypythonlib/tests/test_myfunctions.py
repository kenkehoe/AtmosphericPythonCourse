import numpy as np

from mypythonlib import myfunctions


def test_haversine():
    # Amsterdam to Berlin
    assert np.isclose(myfunctions.haversine(4.895168, 52.370216, 13.404954, 52.520008), 576.662581)
