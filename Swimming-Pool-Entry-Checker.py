# ===============================================
# SWIMMING POOL ENTRY CHECKER
# ===============================================


print("=== Swimming Pool EntryChecker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")


# ----------- collect the three answers ----------
# YOUR CODE HERE
#   age        <- "How old are you? "wrapped in int()
#   can_swim   <- "Can you swim 25 meters? (yes / no): "      with.lower()
#   adult_here <- "Is an adult with you? (yes / no): "with  .lower()


print()
print("=== Entry Decision ===")
print("-" * 32)


# ----------- PART 1: age group,using if / elif / else on a NUMBER -----------
# YOUR CODE HERE
#   under 4        -> Toddler   : splash pool only, always with an adult
# under 12         -> Child     : main pool with an adult
# under 18         -> Teen      : main pool alone if you can swim
# anything else    -> Adult     : all pools open to you
# Order matters here in a way it did not in class. The Instructions explain why.



# ------------- PART 2: did they actually answer yes or no? --------------
# YOUR CODE HERE
# For can_swim: if it is not "yes" AND not "no", print an input error
#   and set  swim_known = True.
# Do the same for adult_here,setting  adult_known.



# -------------- PART 3: AND - the deep pool --------------
# YOUR CODE HERE
# Allowed only when they CAN swim AND an adult is present.



#---------------- PART 4: OR - the shallow end -------------
# YOUR CODE HERE
# Warn when they are under 12 OR they cannot swim.



# ---------------- PART 5: NOT - the lifeguard reminder ----------------
# YOUR CODE HERE
# Remid when there is no adult - but only if adult_known is True.
# Think about why that extra check is needed before you write it.



# ---------------- PART 6: the final verdict --------------
# YOUR CODE HERE
# First: if either answer was not understood, refuse to decide.
# Then work through the real cases with elif, ending in a plain else.



print()
print("Have a safe swim!")