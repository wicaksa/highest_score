# Ask user to input scores and store them in a list. 
student_scores = input("Input a list of student scores ").split()

# Print out the list. 
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Input : A list of int which represents students student scores.
# Output: Print statement that shows the highest score in the list.

# Psuedocode.
# 1. Traverse through the list and keep track of the highest number in a variable.
# 2. Compare that number with each number in the list and replace it if it is lower than the current number.
# 3. Print out the result.

high_score = 0 
for index in range(0, len(student_scores)):
    if student_scores[index] > high_score: # if value of the index > high_score
        high_score = student_scores[index]  # set high_score as that value 
print(f"The highest score in the class is: {high_score}")

# End
