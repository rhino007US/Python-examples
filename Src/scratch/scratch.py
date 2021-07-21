# defining the Class named Question:  to prompt the User with a question and accept the answer

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# I think you'd call this an array, it's the array of the questions

question_prompt = [
    "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What color are bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow \n\n",
    "What color are strawberries? \n(a) Yellow \n(b) Red \n(c) Blue \n\n",
    "What is your name? \n(a) David \n(b) Sarah \n(c) Bill \n\n"
]

# Where the Class "Question" is used to match the questions and the correct answers

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
    Question(question_prompt[3], "a")
]


# The function "run_test" loops 3 times, and compares the questions to the inputed answers



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' Correct,' str(question_answer[3]))

# Calling the function "run_test"

run_test(questions)