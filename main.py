# These functions exist to modularize and shorten the code, making it adaptable to all cases. Yes thats true
def get_tentative():
    print("\n--- Inputting Scores ---")
    # For each part, enter your score, then the max total
    ww_score = float(input("Written Work - Your score: "))
    ww_total = float(input("Written Work - Total points: "))

    pt_score = float(input("Performance Task - Your score: "))
    pt_total = float(input("Performance Task - Total points: "))

    qa_score = float(input("Quarterly Exam - Your score: "))
    qa_total = float(input("Quarterly Exam - Total points: "))



    ww_final = (ww_score / ww_total) * 25
    pt_final = (pt_score / pt_total) * 45
    qa_final = (qa_score / qa_total) * 30

    return ww_final + pt_final + qa_final

# GWA + Corresponding adjective ratings and also the percentages.
def get_gwa(percent):
    if percent >= 97: return 1.00, "Excellent"
    if percent >= 94: return 1.25, "Very Good"
    if percent >= 91: return 1.50, "Very Good"
    if percent >= 88: return 1.75, "Good"
    if percent >= 85: return 2.00, "Satisfactory"
    if percent >= 82: return 2.25, "Satisfactory"
    if percent >= 80: return 2.50,  "satisfactory"
    if percent >= 78: return 2.75,  "Fair"
    if percent >= 75: return 3.00,  "Pass"
    if percent >= 70: return 4.00,  "Conditional"
    if percent <= 70: return 5.00,  "FAIL"

quarter = int(input("What quarter is it? (1-4): "))
tq = get_tentative() 

# Checking if it's the first quarter so we shouldn't get the grade from the previous quarter which doesn't exist.
if quarter == 1:
    final_p = tq
else:
    prev_p = float(input(f"Enter your Q{quarter-1} Final Percentage (0-100): "))
    final_p = (prev_p + (2 * tq)) / 3

gwa, remark = get_gwa(final_p)

# Printing the results of the scholar.
print(f"\nFinal Q{quarter} Grade: {final_p:.2f}%")
print(f"GWA: {gwa:.2f} ({remark})")
