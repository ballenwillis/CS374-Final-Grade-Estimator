'''
Author: Brandon Willis

The goal of this script is to calculate grade cutoffs when considering the end of the semester curve. Here are a few things to note when deciding how much to trust this:
1. The final isn't considered. We don't know what the average or STD will be for it and it's wildly unpredictable imo so it's not even considered for adjusting the curve. Because exams 1 and 2 were so close in average and standard deviation, I assume the final will be as well.
2. The final 6 homework grades are simply a guess for now since they haven't been graded.
3. The class's actual standard deviation is impossible to perfectly predict. The best way to experiment with lower/higher deviations is to modify the CLASS_HW_STD variable accordingly. A smaller STD will yield a smaller grade interval while a higher STD will yield a bigger grade interval.

Best of luck to you!
'''

# --------------------- TODO Put your own scores here --------------------------------
EXAM1_SCORE = 41
EXAM2_SCORE = 33.5

# NOTE If you opted out of doing an assignment, just put a 0. Will calculate the same.
SCORES = [
        70, 40, 60,     # 3, 2, 1
        85, 78, 100,    # 6, 5, 4
        20, 62.5, 69,   # 9, 8, 7...
        92, 25, 45,     # ...
        57.5, 65, 37.5, # ...
        31.5, 0, 7.5,   # ...
        12.5, 0, 62.5,  # ...
        0, 55, 92.5,    # ...
        25, 90, 100,    # 27, 26, 25
        40, 55, 52,     # 30, 29, 28
        80, 80, 80      # 33, 32, 31
]

# --------------------- TODO Play with these values to your best guess ---------------
CLASS_HW_AVERAGE = 70.998
CLASS_HW_STD = 26.43

# ------------------------------------------------------
# NOTE No need to modify below unless you really want to
# ------------------------------------------------------

EXAM1_MEAN = 56.69
EXAM1_STD = 15.36

EXAM2_MEAN = 53.86
EXAM2_STD = 21.19

# NOTE Standard deviations are weighted to their % of class grade
EXAM1_STD = EXAM1_STD * 0.21
EXAM2_STD = EXAM2_STD * 0.21
CLASS_HW_STD = CLASS_HW_STD * 0.28

CLASS_STD = (EXAM1_STD + EXAM2_STD + CLASS_HW_STD) / 0.7
CLASS_AVG = (EXAM1_MEAN * 0.21 + EXAM2_MEAN * 0.21 + CLASS_HW_AVERAGE * 0.28) / 0.7 # Doesn't consider the final

A_PLUS_CUTTOFF = CLASS_AVG + 5/3 * CLASS_STD
A_CUTTOFF = CLASS_AVG + 4/3 * CLASS_STD
A_MINUS_CUTTOFF = CLASS_AVG + CLASS_STD

B_PLUS_CUTTOFF = CLASS_AVG + 2/3 * CLASS_STD
B_CUTTOFF = CLASS_AVG + 1/3 * CLASS_STD
B_MINUS_CUTTOFF = CLASS_AVG

C_PLUS_CUTTOFF = CLASS_AVG - 1/3 * CLASS_STD
C_CUTTOFF = CLASS_AVG - 2/3 * CLASS_STD
C_MINUS_CUTTOFF = CLASS_AVG - CLASS_STD

D_PLUS_CUTTOFF = CLASS_AVG - 4/3 * CLASS_STD
D_CUTTOFF = CLASS_AVG - 5/3 * CLASS_STD
D_MINUS_CUTTOFF = CLASS_AVG - 2 * CLASS_STD

print("Class Average:", CLASS_AVG)
print("Class STD:", CLASS_STD)
print("\n'B+/A-' threshold:", A_MINUS_CUTTOFF)
print("'C+/B-' threshold:", B_MINUS_CUTTOFF)
print("'D+/C-' threshold:", C_MINUS_CUTTOFF)
print("'F+/D-' threshold (PASSING):", D_MINUS_CUTTOFF)

NUM_DROPPED_HWS = 12
SCORES.sort()
SCORES = SCORES[NUM_DROPPED_HWS:]

HW_POINTS = (sum(SCORES) / len(SCORES)) * 0.28
EXAM1_POINTS = EXAM1_SCORE * 0.21
EXAM2_POINTS = EXAM2_SCORE * 0.21

totalPreFinal = HW_POINTS + EXAM1_POINTS + EXAM2_POINTS

print("\nNeed on final for a A+:", (A_PLUS_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a A:", (A_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a A-:", (A_MINUS_CUTTOFF - totalPreFinal) / 0.3)

print("\nNeed on final for a B+:", (B_PLUS_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a B:", (B_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a B-:", (B_MINUS_CUTTOFF - totalPreFinal) / 0.3)

print("\nNeed on final for a C+:", (C_PLUS_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a C:", (C_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a C-:", (C_MINUS_CUTTOFF - totalPreFinal) / 0.3)

print("\nNeed on final for a D+:", (D_PLUS_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a D:", (D_CUTTOFF - totalPreFinal) / 0.3)
print("Need on final for a D-:", (D_MINUS_CUTTOFF - totalPreFinal) / 0.3)