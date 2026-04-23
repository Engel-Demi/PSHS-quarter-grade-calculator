# Advanced Mode Script
# This file handles extended features like projections, multi-subject GWA, etc.

def percent_to_gwa(percent):
    if percent >= 97: return 1.00
    if percent >= 94: return 1.25
    if percent >= 91: return 1.50
    if percent >= 88: return 1.75
    if percent >= 85: return 2.00
    if percent >= 82: return 2.25
    if percent >= 80: return 2.50
    if percent >= 78: return 2.75
    if percent >= 75: return 3.00
    if percent >= 70: return 4.00
    return 5.00


def gwa_to_percent(gwa):
    # Approximate reverse mapping
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
    return mapping.get(gwa, None)

def grade_projection():
    print("\n--- Grade Projection ---")

    prev = float(input("Enter previous quarter percentage: "))
    target_gwa = float(input("Enter your target GWA (e.g. 1.50): "))

    target_percent = gwa_to_percent(target_gwa)

    if target_percent is None:
        print("Invalid target GWA.")
        return

    # Solve: final = (prev + 2x)/3
    # Rearranged: x = (3*target - prev)/2
    needed = (3 * target_percent - prev) / 2

    print(f"\nTo reach GWA {target_gwa:.2f},")
    print(f"You need approximately: {needed:.2f}% this quarter")

    if needed > 100:
        print("⚠️ This target may not be realistically achievable.")
    elif needed < 0:
        print("✅ You're already exceeding this target.")

def multi_subject_gwa():
    print("\n--- Multi-Subject GWA Calculator ---")

    subjects = int(input("How many subjects? "))
    total = 0

    for i in range(subjects):
        grade = float(input(f"Subject {i+1} percentage: "))
        gwa = percent_to_gwa(grade)
        total += gwa

    avg = total / subjects

    print(f"\nOverall GWA: {avg:.2f}")

def trend_simulation():
    print("\n--- Trend Simulation ---")

    current = float(input("Enter your current percentage: "))
    improvement = float(input("Expected improvement per quarter (%): "))
    quarters = int(input("How many future quarters to simulate? "))

    print("\nProjected Grades:")

    for i in range(1, quarters + 1):
        current += improvement
        gwa = percent_to_gwa(current)
        print(f"Q{i}: {current:.2f}% → GWA {gwa:.2f}")

def run():
    while True:
        print("\n=== Advanced Mode ===")
        print("1. Grade Projection")
        print("2. Multi-subject GWA")
        print("3. Trend Simulation")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            grade_projection()
        elif choice == "2":
            multi_subject_gwa()
        elif choice == "3":
            trend_simulation()
        elif choice == "4":
            print("Exiting Advanced Mode...")
            break
        else:
            print("Invalid choice. Try again.")


# Allows both import AND standalone run
if __name__ == "__main__":
    run()
