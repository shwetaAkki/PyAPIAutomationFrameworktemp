'''
Author :Shweta
Objective : Create abd verify by POST Request
Tc#1 -Verify status code
Tc#2 Verify the body -->Booking ID
Tc#3 - Verify the json schema is valid
'''
import pytest


@pytest.mark.integration
def test_create_booking_tc1():
    assert True == True


@pytest.mark.integration
def test_create_booking_tc2():
    assert True == False


@pytest.mark.integration
def test_create_booking_tc3():
    assert True == True

