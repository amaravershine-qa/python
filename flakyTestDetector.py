def find_flaky(runs):
    # Step 1: Create a dictionary to keep track of the results for each test.
    test_history = {}
    
    # Step 2: Iterate through every single test run tuple in the list.
    for test_name, status in runs:
        # Step 3: Check if this is the very first time we are encountering this test.
        if test_name not in test_history:
            # Initialize a new dictionary for this test to explicitly track PASS and FAIL counts.
            test_history[test_name] = {"PASS": False, "FAIL": False}
        
        # Step 4: Mark the encountered status as True for this test.
        test_history[test_name][status] = True
            
    # Step 5: Filter the tests and collect the flaky ones using a traditional for loop
    flaky_tests = []
    for test_name, statuses in test_history.items():
        if statuses["PASS"] and statuses["FAIL"]:
            flaky_tests.append(test_name)
    
    return flaky_tests

# --- Execution Test Cases ---
runs = [
    ("test_login", "PASS"),
    ("test_pay", "FAIL"),
    ("test_login", "PASS"),
    ("test_pay", "PASS"),
    ("test_cart", "FAIL"),
    ("test_cart", "FAIL"),
    ("test_pay", "FAIL"),
]

print("Flaky Tests Found:", find_flaky(runs))
# Expected Output: ['test_pay']