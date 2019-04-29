# CS374 Final Grade Estimate Script

## GOAL: Calculate grade cutoffs when considering the end of the semester curve
## Here are a few things to note when deciding how much to trust this:
1. The final isn't considered. We don't know what the average or STD will be for it and it's unpredictable in my opinion so it's not even considered for adjusting the curve. Because exams 1 and 2 were so close in average and standard deviation, I assume the final will be as well.
2. The final 6 homework grades are simply a guess for now since they haven't been graded.
3. The class's actual standard deviation is impossible to perfectly predict. The best way to experiment with lower/higher deviations is to modify the CLASS_HW_STD variable accordingly. A smaller STD will yield a smaller grade interval while a higher STD will yield a bigger grade interval.

## What you need to do
1. Update the first section to represent your own scores for the class. This consists of the following vars:
  - EXAM1_SCORE
  - EXAM2_SCORE
  - SCORES
2. Update the next section with your own prediction for the class homework average and standard deviation. This consists of the following vars:
  - CLASS_HW_AVERAGE
  - CLASS_HW_STD
  
  
## If you have any problems with this script, talk to Brandon Willis or submit a PR

# Best of luck to you!
