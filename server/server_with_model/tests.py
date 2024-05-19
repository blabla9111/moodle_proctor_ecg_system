from django.test import SimpleTestCase
from unittest.mock import Mock, call
from server_with_model.services import *
from server_with_model.models import *


def create_proctor_user_expected(user_id=None, quiz_id=None, gen_code=None,
                                 id_transaction=None, proctor_flag=None,
                                 proctor_result=None, proctor_start_flag=None,
                                 start_time=None, end_time=None):
    proctor_user = MdlProctorUser()
    proctor_user.user_id = user_id
    proctor_user.quiz_id = quiz_id
    proctor_user.gen_code = gen_code
    proctor_user.id_transaction = id_transaction
    proctor_user.proctor_flag = proctor_flag
    proctor_user.proctor_result = proctor_result
    proctor_user.proctor_start_flag = proctor_start_flag
    proctor_user.start_time = start_time
    proctor_user.end_time = end_time

    return proctor_user


class SimpleTestCase(SimpleTestCase):

    def test_create_proctor_user_return_None(self):
        proctor_users = Mock()
        proctor_user_tmp = Mock()
        proctor_users.filter.return_value = proctor_user_tmp
        proctor_user_tmp.exclude.return_value = True
        self.assertIsNone(
            create_proctor_user(proctor_users, 1, 1))

    def test_create_proctor_user_return_not_None_and_update(self):
        proctor_users = Mock()
        proctor_user_tmp = Mock()
        proctor_users.filter.return_value = proctor_user_tmp
        proctor_user_tmp.exclude.return_value = False
        self.assertIsNotNone(
            create_proctor_user(proctor_users, 1, 1))
        self.assertEquals(1, proctor_user_tmp.update.call_count)
        self.assertEquals(0, proctor_users.create.call_count)

    def test_create_proctor_user_return_not_None_and_create(self):
        proctor_users = Mock()
        proctor_user_tmp = Mock()
        proctor_user_tmp.update = Mock()
        proctor_users.filter.return_value = None
        proctor_users.create.return_value = proctor_user_tmp
        self.assertIsNotNone(
            create_proctor_user(proctor_users, 1, 1))
        self.assertEquals(0, proctor_user_tmp.update.call_count)
        self.assertEquals(1, proctor_users.create.call_count)

    def test_create_proctor_ecg_return_proctor_user(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        proctor_user_expected = Mock()
        proctor_users.filter.return_value = proctor_user_expected
        self.assertIsNotNone(create_proctor_ecg(
            proctor_users, proctor_ecgs, "1"))
        self.assertEquals(1, proctor_ecgs.create.call_count)
        self.assertEquals(1, proctor_user_expected.update.call_count)

    def test_create_proctor_ecg_return_None(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        proctor_users.filter.return_value = None
        self.assertIsNone(create_proctor_ecg(
            proctor_users, proctor_ecgs, "1"))
        self.assertEquals(0, proctor_ecgs.create.call_count)

    def test_save_ecg_data_return_proctor_ecg(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        proctor_user = Mock()
        proctor_ecg = Mock()
        proctor_ecgs.filter.return_value = proctor_ecg
        proctor_users.filter.return_value = proctor_user
        self.assertIsNotNone(save_ecg_data(
            proctor_ecgs, proctor_users, "1", "1"))
        self.assertEquals(1, proctor_ecg.update.call_count)
        self.assertEquals(2, proctor_user.update.call_count)

    def test_save_ecg_data_return_None(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        proctor_ecgs.filter.return_value = None
        self.assertIsNone(save_ecg_data(
            proctor_ecgs, proctor_users, "1", "1"))

    def test_check_ecg_return_None(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        bad_results = Mock()
        proctor_ecgs.filter.first.return_value = Mock()
        proctor_users.filter.first.return_value = Mock()
        self.assertIsNone(
            identify_ecg(proctor_ecgs, proctor_users, bad_results, "1", "1"))

    def test_close_proctoring_return_proctor_user(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        proctor_user = Mock()
        proctor_ecg = Mock()
        proctor_ecgs.filter.return_value = proctor_ecg
        proctor_users.filter.return_value = proctor_user
        self.assertIsNotNone(close_proctoring(
            proctor_users, proctor_ecgs, 1, 1))
        self.assertEquals(1, proctor_user.get.call_count)
        self.assertEquals(1, proctor_ecg.delete.call_count)

    def test_close_proctoring_return_None(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        proctor_ecg = Mock()
        proctor_ecgs.filter.return_value = proctor_ecg
        proctor_users.filter.return_value = None
        self.assertIsNone(close_proctoring(
            proctor_users, proctor_ecgs, 1, 1))
        self.assertEquals(0, proctor_ecg.delete.call_count)

    def test_proctor_user_close_desktop_return_not_None(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        bad_results = Mock()
        proctor_user = Mock()
        proctor_ecg = Mock()
        proctor_ecgs.filter.return_value = proctor_ecg
        proctor_users.filter.return_value = proctor_user
        proctor_user.get.return_value = proctor_user
        proctor_ecg.delete.return_value = proctor_ecg
        self.assertIsNotNone(
            proctor_user_close_desktop(proctor_ecgs, proctor_users, bad_results, "1"))
        self.assertEquals(1, proctor_user.save.call_count)
        self.assertEquals(1, proctor_ecg.delete.call_count)
        self.assertEquals(1, bad_results.create.call_count)

    def test_proctor_user_close_desktop_return_None(self):
        proctor_users = Mock()
        proctor_ecgs = Mock()
        bad_results = Mock()
        proctor_user = Mock()
        proctor_ecg = Mock()
        proctor_ecgs.filter.return_value = None
        proctor_users.filter.return_value = proctor_user
        proctor_user.get.return_value = proctor_user
        proctor_ecg.delete.return_value = proctor_ecg
        self.assertIsNone(
            proctor_user_close_desktop(proctor_ecgs, proctor_users, bad_results, "1"))
        self.assertEquals(0, proctor_user.save.call_count)
        self.assertEquals(0, proctor_ecg.delete.call_count)
        self.assertEquals(0, bad_results.create.call_count)
