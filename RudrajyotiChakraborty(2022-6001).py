# Initialize counters for correct, wrong, and unattended questions
correct = 0
wrong = 0
unattended = 0

# A dictionary of 100 questions with their options and correct answers
questions = {
    1: ("What is the unit of electrical resistance?", ["A. Ohm", "B. Volt", "C. Ampere", "D. Watt"], "A"),
    2: ("What is the SI unit of electric charge?", ["A. Coulomb", "B. Joule", "C. Newton", "D. Watt"], "A"),
    3: ("If ‘→’ denotes increasing order of intensity, then the meaning of the words(talk → shout → scream) is analogous to (please → ________ → pander).Which one of the given options is appropriate to fill the blank?", ["A. flatter", "B. flutter", "C. fritter", "D. frizzle"], "A"),
    4: ("A shopkeeper buys shirts from a producer and sells them at 20% profit. A customerhas to pay ₹3,186.00 including 18% taxes, per shirt. At what price did theshopkeeper buy each shirt from the producer?", ["A. 2500", "B. 1000", "C. 3000", "D. 5000"], "C"),
    
    # Add more questions up to 100 as needed
}

# Loop through each question
for q_no in range(1, 101):
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

# Display the results
print("\nQuiz Completed!")
print(f"Correct Answers: {correct}")
print(f"Wrong Answers: {wrong}")
print(f"Unattended Questions: {unattended}")