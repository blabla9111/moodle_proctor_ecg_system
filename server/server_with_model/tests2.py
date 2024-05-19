from django.test import SimpleTestCase
from unittest.mock import Mock, call
from server_with_model.services import *
from server_with_model.model.siames_nn import *
import numpy as np


def make_list(len, NUM=0):
    data = list()
    for i in range(len):
        data.append(NUM)

    return np.array(data)


def make_string_ecg(len, NUM):
    data = str(make_list(len, NUM)).replace(
        ",", "").replace("[", "").replace("]", "")
    return data


class SimpleTestCase_for_SiamesNN(SimpleTestCase):
    def test_prepare_ecg_return_ecg(self):
        ecg = make_list(500, 1)
        siames_NN = Siames_NN()
        ecg_expected = make_list(500, -0.49804)
        ecg_actual = siames_NN.prepare_ecg(ecg).round(5)
        self.assertTrue(np.array_equal(ecg_expected, ecg_actual))

    def test_predict_return_False(self):
        ecg_1 = make_string_ecg(500, 100)
        ecg_2 = make_string_ecg(500, 1)
        self.assertFalse(predict(ecg_1, ecg_2))

    def test_predict_return_True(self):
        ecg_1 = make_string_ecg(500, 1)
        ecg_2 = make_string_ecg(500, 1)
        self.assertTrue(predict(ecg_1, ecg_2))
