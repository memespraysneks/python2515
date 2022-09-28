import pytest
from account import Account, CreditAccount, SavingsAccount
from bank import Bank
from customer import Customer

@pytest.fixture
def tim():
    """Tim is a regular customer"""
    return Customer("Tim", "84093232")

@pytest.fixture
def mybank():
    """Your typical bank"""
    return Bank("My bank")

def test_bank(mybank):
    """Check attributes"""
    assert mybank.name == "My bank"

def test_create_account(mybank, tim):
    """Check the different accounts that can be created"""
    acc = mybank.create_account("account", tim)
    assert type(acc) == Account
    assert acc.owner.name == "Tim"
    
    credit = mybank.create_account("credit", tim, 10)
    assert type(credit) == CreditAccount
    assert credit.interest == 10
    assert credit.owner.name == "Tim"

    savings = mybank.create_account("savings", tim, 5)
    assert type(savings) == SavingsAccount
    assert savings.interest == 5
    assert savings.owner.name == "Tim"

def test_compute_interest(mybank, tim):
    """Check that interest is calculated on all accounts"""
    tim_savings5 = mybank.create_account("savings", tim, 5)
    tim_savings5.deposit(1000)

    alice = Customer("Alice", "218309321")
    alice_credit10 = mybank.create_account("credit", alice, 10)
    alice_credit10.withdraw(500)

    mybank.compute_interest()
    assert tim_savings5.amount == 1050
    assert alice_credit10.amount == -560

def test_find_accounts(mybank, tim):
    """Check that the correct accounts are returned"""
    alice = Customer("Alice", "218309321")
    alice_acc = mybank.create_account("account", alice)
    alice_credit10 = mybank.create_account("credit", alice, 10)
    alice_savings5 = mybank.create_account("savings", alice, 5)
    
    tim_savings5 = mybank.create_account("savings", tim, 5)
    
    alice_accounts = mybank.find_accounts("Alice")
    assert len(alice_accounts) == 3
    assert alice_acc in alice_accounts
    assert alice_credit10 in alice_accounts
    assert alice_savings5 in alice_accounts

    tim_accounts = mybank.find_accounts("Tim")
    assert len(tim_accounts) == 1
    assert tim_accounts[0] == tim_savings5

def test_find_accounts_same_name(mybank, tim):
    """The bank can have two customers with the same name"""
    tim2 = Customer("Tim", "540954354")
    tim_acc = mybank.create_account("account", tim)
    tim2_acc = mybank.create_account("account", tim2)

    accounts = mybank.find_accounts("Tim")
    assert tim_acc in accounts
    assert tim2_acc in accounts