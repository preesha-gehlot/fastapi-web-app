from app.calculations import InsufficientFunds, add, subtract, multiply, divide, BankAccount
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5), 
    (7, 1, 8), 
    (12, 4, 16)
])

def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1,num2) == expected

def test_subtract():
    print("testing subtract function")
    assert subtract(5,3) == 2

def test_multiply():
    print("testing add function")
    assert multiply(5,3) == 15

def test_divide():
    print("testing subtract function")
    assert divide(6,3) == 2


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20) 
    assert bank_account.balance== 30

def test_deposit(bank_account):
    bank_account.deposit(20) 
    assert bank_account.balance== 70


def test_collect_interest(bank_account):
    bank_account.collect_interest() 
    assert round(bank_account.balance, 6)== 55

@pytest.mark.parametrize("withdrew, deposited, expected", [
    (20, 50, 80), 
    (50, 200, 200), 
    (3, 45, 92),
])

def test_bank_transaction(bank_account, withdrew, deposited, expected):
    bank_account.withdraw(withdrew)
    bank_account.deposit(deposited)
    assert bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)