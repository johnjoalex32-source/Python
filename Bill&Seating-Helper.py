# Bill & Seating Helper

# PART 1: Define a function using positional arguments
def total_bill(bill_amount, tip_perc):
    # Calculate final bill after adding tip
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total

# PART 2: Call the function with positional arguments
total_bill(150, 20)


# PART 3: Define a recursive function with a docstring
def seating_arrangements(guests):
    '''This is a recursive function to find the number of seating arrangments for guests.'''

    # Base case
    if guests == 0 or guests == 1:
        return 1

    # Recursive case
    else:
        return guests * seating_arrangements(guests - 1)


    # PART 4: Acces and print the docstring
    print(seating_arrangements.__doc__)

    # PART 5: Display seating arrangment results
    print("Seating arrngements for 1 guest:", seating_arrangements(1))
    print("Seating arrngements for 2 guest:", seating_arrangements(2))
    print("Seating arrngements for 3 guest:", seating_arrangements(3))
    print("Seating arrngements for 5 guest:", seating_arrangements(5))
