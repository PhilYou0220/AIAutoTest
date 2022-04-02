import pytest_check as check
import pytest


def test_example():
    a = 1
    b = 2
    c = [2, 4, 6]
    print(check.equal(1, 3))
    check.greater(a, b)
    check.less_equal(b, a)
    check.is_in(b, c, "Is 1 in the list")
    check.is_not_in(b, c, "make sure 2 isn't in list")


if __name__ == '__main__':
    pytest.main(["-sv", "test_1.py"])
    # print(check.equal(1,1))
    # check.equal(1, 2)
    # test_example()

