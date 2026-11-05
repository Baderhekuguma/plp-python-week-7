import csv

# Try opening the CSV file safely with error handling
try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

total = 0
passed = 0
failed = 0

# Loop through each learner row to calculate scores
for row in rows:
    # Convert score from text (string) to an integer number
    score = int(row["score"])
    total += score
    
    if score >= 50:
        passed += 1
    else:
        failed += 1

# Calculate the average score (avoiding division by zero if file is missing)
if len(rows) > 0:
    average = round(total / len(rows), 1)
else:
    average = 0.0

# Write the final summary report to report.txt
with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(failed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")