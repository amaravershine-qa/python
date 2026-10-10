def flaky_detector(runs):
    test_history = {}
    for test_name,status in runs:
        if  test_name not in test_history:
            test_history[test_name]  = {"PASS":False,"FAIL":False}
        test_history[test_name][status] = True
    flaky_test = []
    for test_name,statuses in test_history.items():
        if statuses["PASS"] and statuses["FAIL"]:
            flaky_test.append(test_name)
    return flaky_test

runs = [
    ("test_login", "PASS"),
    ("test_pay", "FAIL"),
    ("test_login", "PASS"),
    ("test_pay", "PASS"),
    ("test_cart", "FAIL"),
    ("test_cart", "FAIL"),
    ("test_pay", "FAIL"),
]

print("Flaky Tests Found:", flaky_detector(runs))
# Expected Output: ['test_pay']