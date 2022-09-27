def my_unit_test(func):
    def wrapper(a):
        print(f"My unit test started with input value {a}")
        func(a)
        print("Unit test finished")
    return wrapper

@my_unit_test
def test_1(input_value):
    assert sum([1, 12], input_value) == 15

# @my_unit_test
# def test_2(input_value):
#     assert input_value in [1,2,3,4,5,6]


# test_1(2)
# test_2(8)
my_unit_test(test_1)(2)
# x(2)