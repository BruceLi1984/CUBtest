import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0
test = Customer("Test User","100-1100")
test.balance = INIT_MONEY

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
# 1. 之後存款1000元, 確認帳戶總金額為1100元
# 2. 接續提款500元, 確認帳戶總金額為600元
# 3. 之後提款700元, 會出現 RuntimeError
#
##########################################################################################

    def test_step1(self):
        assert(test.name == "Test User")
        assert(test.account == "100-1100")

    def test_step2(self):
        test.balance += 1000
        assert(test.balance == 1100)

    def test_step3(self):
        assert(test.balance >= 500)
        test.balance -=500
        assert(test.balance == 600)

    def test_step4(self):
        test.balance += (test.balance * 0.1)
        assert(test.balance == 660)

    def test_ste5(self):
        assert(test.balance >= 700)
