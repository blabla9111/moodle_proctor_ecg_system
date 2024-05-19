from django.test import SimpleTestCase
from server_with_model.services import *
from server_with_model.model.siames_nn import *
from server_with_model.requstParserJson import *


class SimpleTestCase_for_RequestParserJson(SimpleTestCase):

    def test(self):
        class ReqTest:
            body = 'json={"id_transaction":"12","user_id":1,"quiz_id":2,"code":"1234","ecg_data":"54321"}'
        req = ReqTest
        parser = RequestParserJson(req, json_start_flag=True)
        self.assertEquals("12", parser.get_transaction_id())
        self.assertEquals(1, parser.get_user_id())
        self.assertEquals(2, parser.get_quiz_id())
        self.assertEquals("1234", parser.get_code())
        self.assertEquals("54321", parser.get_ecg_data())

    def test2(self):
        class ReqTest:
            body = '{"id_transaction":"12","user_id":1,"quiz_id":2,"code":"1234","ecg_data":"54321"}'
        req = ReqTest
        parser = RequestParserJson(req)
        self.assertEquals("12", parser.get_transaction_id())
        self.assertEquals(1, parser.get_user_id())
        self.assertEquals(2, parser.get_quiz_id())
        self.assertEquals("1234", parser.get_code())
        self.assertEquals("54321", parser.get_ecg_data())

    def test3(self):
        class ReqTest:
            body = '{"user_id":1,"quiz_id":2,"code":"1234","ecg_data":"54321"}'
        req = ReqTest
        parser = RequestParserJson(req)
        with self.assertRaises(KeyError):
            parser.get_transaction_id()
        self.assertEquals(1, parser.get_user_id())
        self.assertEquals(2, parser.get_quiz_id())
        self.assertEquals("1234", parser.get_code())
        self.assertEquals("54321", parser.get_ecg_data())
