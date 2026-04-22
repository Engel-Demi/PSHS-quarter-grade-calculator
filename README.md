## Academic Grade & GWA Calculator
A PSHS utility designed to calculate quarterly grades and General Weighted Average (GWA) based on academic performance across Written Work, Performance Tasks, and Quarterly Exams.

------------------------------
## Features

* Modular Design: Uses specific functions to handle score inputs and GWA mapping.
* Weighted Scoring: Automatically applies standard academic weights:
* 25%: Written Work
   * 45%: Performance Tasks
   * 30%: Quarterly Assessment
* Quarter-on-Quarter Calculation: Includes logic to factor in previous quarter grades for a cumulative final percentage.
* Descriptive Ratings: Returns both a numerical GWA and an adjective rating (e.g., Excellent, Satisfactory, Fail).

------------------------------
## How It Works

## 1. Score Input
The program prompts for your raw scores and the total possible points for three main categories. It converts these into a tentative percentage.
## 2. Weighted Logic
It calculates the final percentage based on the current quarter:

* Quarter 1: Uses only the current tentative score.
* Quarters 2-4: Combines the previous quarter's final percentage with the current tentative score using a weighted formula:
Final = (Previous + (2 * Current)) / 3

## 3. GWA Mapping
The final percentage is mapped to a GWA scale:

| Percentage | GWA | Rating |
|---|---|---|
| 97 - 100 | 1.00 | Excellent |
| 91 - 96 | 1.25 | Very Good |
| 85 - 90 | 1.50 | Good |
| 80 - 84 | 1.75 | Satisfactory |
| 75 - 79 | 2.00 | Unsatisfactory |
| 70 - 74 | 2.50 | Conditional |
| Below 70 | 5.00 | Fail |

------------------------------
## Usage

   1. Ensure you have Python 3.x installed.
   2. Run the script:
   
   python grade_calculator.py
   
   3. Follow the on-screen prompts to enter your quarter and scores.

------------------------------
## Example Output

What quarter is it? (1-4): 2

--- Inputting Scores ---
Written Work - Your score: 22
Written Work - Total points: 25
Performance Task - Your score: 40
Performance Task - Total points: 45
Quarterly Exam - Your score: 28
Quarterly Exam - Total points: 30

Enter your Q1 Final Percentage (0-100): 88

Final Q2 Grade: 92.00%
GWA: 1.25 (Very Good)
