import numpy as np
from unittest import TestCase

from statsmodels.compat.python import encode_field_names


class TestPythonCompat(TestCase):
    def test_encode_field_names(self):
        descr = [(u'index', '|O'), (u'a', '|O'), (u'b', '|O')]
        result = encode_field_names(descr)
        expected = [('index', '|O'), ('a', '|O'), ('b', '|O')]
        self.assertEqual(result, expected)
        np.dtype(result)
