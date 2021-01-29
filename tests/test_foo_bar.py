#!/usr/bin/python3
from  brownie.project.BrownieInterfacesTestProject import interface


def test_all_fine(bar, accounts):
    # Try this - it works fine
    tx1 = bar.testEvent()
    assert "TestEvent" in tx1.events


def test_corrupted_contract(bar, accounts):
    # Ensure the interface works
    assert bar.randomFunction()

    # Try this a couple of times
    tx2 = bar.testEvent()
    assert "TestEvent" in tx2.events

    tx3 = bar.testEvent()
    assert "TestEvent" in tx3.events

    # Get an IFoo interface to the contract
    iFoo = interface.IFoo(bar)

    # Now the contract is broken
    tx4 = bar.testEvent()
    assert "TestEvent" in tx4.events


def test_still_corrupted_on_next_test(bar, accounts):
    tx5 = bar.testEvent()
    assert "TestEvent" in tx5.events
