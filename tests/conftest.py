#!/usr/bin/python3

import pytest


class Scenario:
    def __init__(self, ACTTest, accounts):
        self.acc_admin = accounts[0]
        self.acc_security_generator1 = accounts[1]
        self.acc_security_owner1 = accounts[7]
        self.contract_acttest = ACTTest.deploy({"from": accounts[0]})


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def scenario(ACTTest, accounts):
    return Scenario(ACTTest, accounts)
