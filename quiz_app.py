import tkinter as tk
from tkinter import messagebox
import random

# Predefined quiz questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0
    },
    {
        "topic": "Loops",
        "question": "Which loop is used to iterate over a sequence?",
        "code": "?",
        "options": ["for", "while", "do-while", "if"],
        "answer": 0
    },
    {
        "topic": "Loops",
        "question": "What keyword is used to exit a loop prematurely?",
        "code": "?",
        "options": ["break", "continue", "pass", "exit"],
        "answer": 0
    },
    {
        "topic": "Lists",
        "question": "What is the output of this code?",
        "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
        "options": ["1", "2", "3", "Error"],
        "answer": 1
    },
    {
        "topic": "Lists",
        "question": "How do you add an item to the end of a list?",
        "code": "my_list = [1, 2, 3]\n?",
        "options": ["my_list.append(4)", "my_list.add(4)", "my_list.insert(4)", "my_list.push(4)"],
        "answer": 0
    },
    {
        "topic": "Lists",
        "question": "How do you remove the last item from a list?",
        "code": "my_list = [1, 2, 3]\n?",
        "options": ["my_list.pop()", "my_list.remove()", "my_list.delete()", "my_list.cut()"],
        "answer": 0
    },
    {
        "topic": "Strings",
        "question": "Which method is used to convert a string to uppercase?",
        "code": "my_string = 'hello'\nprint(my_string.???)",
        "options": ["upper()", "capitalize()", "title()", "uppercase()"],
        "answer": 0
    },
    {
        "topic": "Strings",
        "question": "How do you find the length of a string?",
        "code": "my_string = 'hello'\n?",
        "options": ["len(my_string)", "size(my_string)", "length(my_string)", "count(my_string)"],
        "answer": 0
    },
    {
        "topic": "Strings",
        "question": "How do you replace a substring in a string?",
        "code": "my_string = 'hello world'\n?",
        "options": ["my_string.replace('world', 'Python')", "my_string.sub('world', 'Python')", "my_string.change('world', 'Python')", "my_string.swap('world', 'Python')"],
        "answer": 0
    }
]

# Function to generate a quiz question
def generate_question():
    topic = topic_entry.get().strip()
    matching_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
    
    if not matching_questions:
        messagebox.showerror("Error", "No questions found for this topic!")
        return
    
    global current_question
    current_question = random.choice(matching_questions)
    
    question_label.config(text=current_question["question"])
    code_label.config(text=current_question["code"])
    
    for i, option in enumerate(current_question["options"]):
        radio_buttons[i].config(text=option, value=i)
        radio_buttons[i].pack()
    
    submit_button.pack()

# Function to check the answer
def check_answer():
    selected = answer_var.get()
    if selected == current_question["answer"]:
        messagebox.showinfo("Result", "Correct! Well done!")
    else:
        messagebox.showerror("Result", "Incorrect. Try again.")

# Create main application window
root = tk.Tk()
root.title("Python Quiz Generator")

# Topic input
tk.Label(root, text="Enter Python Topic:").pack()
topic_entry = tk.Entry(root)
topic_entry.pack()

# Generate question button
generate_button = tk.Button(root, text="Generate Python Question", command=generate_question)
generate_button.pack()

# Display question
question_label = tk.Label(root, text="")
question_label.pack()
code_label = tk.Label(root, text="", font=("Courier", 10), justify="left")
code_label.pack()

# Answer options
answer_var = tk.IntVar()
radio_buttons = [tk.Radiobutton(root, variable=answer_var) for _ in range(4)]

# Submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)

# Start the Tkinter loop
root.mainloop()
