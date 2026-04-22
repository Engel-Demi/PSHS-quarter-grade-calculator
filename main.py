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
    if percent >= 80: return 2.50, "Satisfactory"
    if percent >= 78: return 2.75, "Fair"
    if percent >= 75: return 3.00, "Pass"
    if percent >= 70: return 4.00, "Conditional"
    if percent <= 70: return 5.00, "FAIL"


# NEW: Convert PSHS decimal (1.00–5.00) back to percentage equivalent
def gwa_to_percent(gwa):
    # Reverse mapping (approx midpoint values for accuracy)
    mapping = {
        1.00: 98,
        1.25: 95,
        1.50: 92,
        1.75: 89,
        2.00: 86,
        2.25: 83,
        2.50: 81,
        2.75: 79,
        3.00: 76,
        4.00: 72,
        5.00: 65
    }
    return mapping.get(gwa, None)  # returns None if invalid input


quarter = int(input("What quarter is it? (1-4): "))
tq = get_tentative()

# NEW: Ask user what format they want to use
mode = input("Input previous grade as (P)ercentage or (G)WA? ").strip().upper()

# Checking if it's the first quarter so we shouldn't get the grade from the previous quarter which doesn't exist.
if quarter == 1:
    final_p = tq
else:
    if mode == "P":
        prev_p = float(input(f"Enter your Q{quarter-1} Final Percentage (0-100): "))
    elif mode == "G":
        prev_gwa = float(input(f"Enter your Q{quarter-1} GWA (1.00–5.00): "))
        prev_p = gwa_to_percent(prev_gwa)

        # Extra validation
        if prev_p is None:
            print("Invalid GWA input. Exiting...")
            exit()
    else:
        print("Invalid mode selected. Exiting...")
        exit()

    final_p = (prev_p + (2 * tq)) / 3


gwa, remark = get_gwa(final_p)

# Printing the results of the scholar.
print(f"\nFinal Q{quarter} Grade: {final_p:.2f}%")
print(f"GWA: {gwa:.2f} ({remark})")



import subprocess  # NEW: allows running another script

# Printing the results of the scholar.
print(f"\nFinal Q{quarter} Grade: {final_p:.2f}%")
print(f"GWA: {gwa:.2f} ({remark})")


# NEW: Ask user what they want to do next
print("\n--- Next Step ---")
choice = input("Do you want to access advanced features? (Y/N): ").strip().upper()

if choice == "Y":
    print("\nLaunching advanced setup...\n")
    
    # Runs the advanced script
    subprocess.run(["python", "advanced_mode.py"])

else:
    print("\nProgram finished. Goodbye!")
