#!/usr/bin/python3
from  brownie.project.BrownieInterfacesTestProject import interface


def test_all_fine(bar, accounts):
    # Now on the next test file it works ok again
    tx1 = bar.testEvent()
    assert "TestEvent" in tx1.events
