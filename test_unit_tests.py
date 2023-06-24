from unit_testing_examples import sample_code


def test_normal():
    arr = [7, 10, 4, 3, 20, 15]
    res = sample_code.Solution.kthSmallest(arr, 3)
    assert res == 7, "incorrect solution"
