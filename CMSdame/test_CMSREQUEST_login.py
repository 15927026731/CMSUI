import requests
import pytest
from lib.requestlogin import *


class Test_001:

    def test_001(self):
        test = str(REQUEST().login().text)
        assert "登录成功" in test

    def test_002(self):
        test = str(REQUEST().add().text)
        assert "提交信息成功" in test

    def test_003(self):
        test = str(REQUEST().find().text)
        assert "111" in test
