# Calculating Monthly payment to pay off Credit Card Balance in a year

balance = float(input("Enter outstanding balance on the credit card"))
annualInterestRate = float(input("Enter annual interest rate as a decimal"))

# Calculating monthly interest rate
MonthlyInterestRate = annualInterestRate / 12.0

# Calculating lower and upper bound for guessing monthly payment
lowerbound = balance / 12.0
upperbound = balance*((1+MonthlyInterestRate)**12) / 12.0

# Continuous loop till break
while True:

    # Taking a guess
    guess = (lowerbound+upperbound) / 2.0

    # Month counter
    month = 1

    # Variable to keep balance amount constant
    samplebalance = balance

    # Loop running for 12 months
    while month <= 12:

        # Calculating balance left after minimum payment
        samplebalance -= guess

        # Calculating updated balance after interest
        samplebalance += MonthlyInterestRate * samplebalance

        # Moving to next month
        month += 1

    # Checking if guessed value is correct
    if samplebalance > 0.001:

        # Increment in amount
        lowerbound = guess

    elif samplebalance < -0.001:

        # Decrease in amount
        upperbound = guess

    else:

        # Printing amount to be paid per month, breaking from loop
        print ('Lowest Payment: ' + str(round(guess,2)))
        break