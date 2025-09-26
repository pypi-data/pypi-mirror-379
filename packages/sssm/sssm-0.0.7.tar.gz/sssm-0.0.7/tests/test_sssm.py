import unittest
import numpy as np
from sssm import Model
import mne


class TestSSSMUtilities(unittest.TestCase):
    def test_model(self):
        raw = mne.io.read_raw_edf('cap_ins5.edf')
        raw = raw.pick_channels(['C4-A1'])
        raw.load_data()
        raw.filter(0.1, 40)
        raw = raw.resample(100)
        data = raw.get_data(units="uV")

        model = Model()
        model.predict(data,step=300)
        df = model.to_pandas()
        print(df)


if __name__ == "__main__":
    unittest.main()


