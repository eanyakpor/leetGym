from slidingWindow.permutation import checkInclusion

def test_case(input, s2,expected):
    actual = checkInclusion(input,s2)
    passed = actual == expected

    print("input:   ", input,s2)
    print("actual:  ", actual)
    print("expected:", expected)
    print("passed:  ", passed)
    print()


if __name__ == "__main__":

    tests = [
        (
            "ab",
            "eidbaooo",
            True
        ),
        (
            "ab",
            "eidboaoo",
            False
        )

    ]

    for input,s2, expected in tests:
        test_case(input,s2,expected)
