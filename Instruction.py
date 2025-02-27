import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Function to display instructions with a pause between each section
def display_instructions():
    sections = [
        """
Section 1: General Information
- The GATE 2024 exam is a Computer-Based Test (CBT) lasting 3 hours, with a total of 100 marks.
- The question paper includes General Aptitude (15 marks) and subject-specific sections (85 marks).
- The exam consists of three types of questions: 
  - Multiple Choice Questions (MCQs)
  - Multiple Select Questions (MSQs)
  - Numerical Answer Type (NAT) questions.
        """,
        """
Section 2: Marking Scheme
- MCQs have negative marking:
  - +1 for a correct 1-mark answer, -1/3 for a wrong one.
  - +2 for a correct 2-mark answer, -2/3 for a wrong one.
- MSQs and NAT questions have no negative marking.
- NAT questions require entering numerical values using the virtual keyboard provided.
        """,
        """
Section 3: Examination Conduct
- Only the on-screen virtual calculator is allowed.
- Prohibited items include mobile phones, smartwatches, and other electronic devices.
- Carry your admit card and valid photo ID proof (e.g., Aadhaar, Passport, or PAN card).
- Report to the center at least 60 minutes before the exam. Late entry is prohibited after 30 minutes.
        """,
        """
Section 4: Other Important Information
- Use "Next" and "Previous" buttons to navigate between questions.
- Use the "Mark for Review" option to revisit a question later.
- The test will auto-submit after 3 hours.
- Any misconduct may result in disqualification.
        """
    ]

    for section in sections:
        print(f"{section}")
        input("Press Enter to proceed to the next section...\n")

# Initialize counters for correct, wrong, and unattended questions
correct = 0
wrong = 0
unattended = 0

# A dictionary of quiz questions with their options and correct answers
questions = {
    1: ("What is the unit of electrical resistance?", ["A. Ohm", "B. Volt", "C. Ampere", "D. Watt"], "A"),
    2: ("What is the SI unit of electric charge?", ["A. Coulomb", "B. Joule", "C. Newton", "D. Watt"], "A"),
    3: ("If ‘→’ denotes increasing order of intensity, then the meaning of the words (talk → shout → scream) is analogous to (please → ________ → pander). Which one of the given options is appropriate to fill the blank?", ["A. flatter", "B. flutter", "C. fritter", "D. frizzle"], "A"),
    4: ("A shopkeeper buys shirts from a producer and sells them at 20% profit. A customer has to pay ₹3,186.00 including 18% taxes, per shirt. At what price did the shopkeeper buy each shirt from the producer?", ["A. 2500", "B. 1000", "C. 3000", "D. 5000"], "C"),
    5: ("If, for non-zero real variables 𝑥, 𝑦, and real parameter 𝑎 > 1, 𝑥: 𝑦 = (𝑎 + 1) ∶ (𝑎 − 1), then the ratio (𝑥² − 𝑦²) ∶ (𝑥² + 𝑦²) is", ["A. 2𝑎 ∶ (𝑎² + 1)", "B. 𝑎 ∶ (𝑎² + 1)", "C. 2𝑎 ∶ (𝑎² - 1)", "D. 𝑎 ∶ (𝑎² - 1)"], "D"),
}

# Function to display an image from a file path using Tkinter
def display_image(image_path):
    root = tk.Tk()
    root.title("Image Display")

    img = Image.open(image_path)  # Open the image from the specified file path
    img_tk = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=img_tk)
    img_label.pack(pady=10)

    root.mainloop()

# Path to the image file (replace this with your actual path)
image_path = "/Users/himeshshukla/Downloads/Screenshot 2024-12-08 at 2.43.48 PM.png"

# Uncomment to display the image before quiz starts
display_image(image_path)

# Display instructions before starting the quiz
display_instructions()

# Start the quiz
for q_no in range(1, 6):  # Adjust range for the number of questions in the quiz
    if q_no in questions:
        # Fetch the question, options, and correct answer
        question, options, correct_answer = questions[q_no]

        # Display the question and options
        print(f"\nQuestion {q_no}: {question}")
        for option in options:
            print(option)

        # Get the user's answer
        user_answer = input("Your answer (A/B/C/D) or press Enter to skip: ").strip().upper()

        if user_answer == "":
            # Increment unattended counter if no answer is provided
            unattended += 1
        elif user_answer == correct_answer:
            # Increment correct counter if the answer is correct
            correct += 1
        else:
            # Increment wrong counter if the answer is incorrect
            wrong += 1
    else:
        # Handle questions without data
        print(f"\nQuestion {q_no}: This question is not available.")
        unattended += 1

# Calculate the final score
score = (4 * correct) - (1 * wrong)

# Display the results
print("\nQuiz Completed!")
print(f"Correct Answers: {correct}")
print(f"Wrong Answers: {wrong}")
print(f"Unattended Questions: {unattended}")
print(f"Score: {score}")
