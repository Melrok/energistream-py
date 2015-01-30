import unittest
import nose
import pandas as pd
import numpy as np
from numpy.testing import assert_almost_equal, assert_allclose
from nose.tools import assert_equal, assert_raises

import energiscore as es


class TestReports(unittest.TestCase):

    idx_ranges =  [0.0, .03, 0.2, 0.58]

    def test_generate_slices(self):
        slices = es.tools.reports.generate_slices(self.idx_ranges)
        result = slices.iloc[-1]['slice']
        expected = slice(0.58, 1.0)
        assert_equal(result, expected)

    def test_generate_slices_with_labels(self):
        slices = es.tools.reports.generate_slices(self.idx_ranges,
                                                  label='Op. Zone ')
        result = ' | '.join(slices['label'].tolist())
        expected = 'Op. Zone 0 | Op. Zone 1 | Op. Zone 2 | Op. Zone 3'
        assert_equal(result, expected)

    def test_time_bounds(self):
        eim_time = '14-Nov-2013 4:25'
        eim_time = pd.to_datetime(eim_time).tz_localize('US/Pacific')
        tb = es.tools.reports.time_bounds(eim_time, pd.offsets.Week(3))
        result = pd.DatetimeIndex(tb).to_julian_date().values
        expected = np.array([2456589.72569,  2456631.68403])
        assert_almost_equal(result, expected, 5)


if __name__ == '__main__':
    nose.runmodule(argv=[__file__, '-vvs', '-x', '--pdb', '--pdb-failure'],
                   exit=False)
