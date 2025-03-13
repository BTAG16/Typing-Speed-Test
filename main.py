from tkinter import *
from random import *
from tkinter import ttk
from timeit import default_timer as timer
from words import easy_words, intermediate_words, advanced_words, expert_words

cpm = 0
wpm = 0
tries = 10
count = 0
corrects = 0
global s_time
avg_cpm = []
avg_wpm = []
used_word = []

def calculate_speed(user_entry, start_time, end_time):
    global wpm, cpm

    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    cpm = round((len(user_entry) / elapsed_minutes), 2)
    wpm = round((cpm / 5), 2)

    label_cpm.config(text=f"Characters per Minute : {cpm}")
    label_wpm.config(text=f"Words per Minute : {wpm}")

    avg_cpm.append(cpm)
    avg_wpm.append(wpm)


def start_game():
    global s_time
    s_time = timer()
    selected_difficulty = check_var.get()

    if selected_difficulty == "Easy":
        word_list = easy_words
    elif selected_difficulty == "Intermediate":
        word_list = intermediate_words
    elif selected_difficulty == "Advanced":
        word_list = advanced_words
    elif selected_difficulty == "Expert":
        word_list = expert_words
    else:
        label_2.config(text="Select Difficulty")
        return

    unused_words = [word for word in word_list if word not in used_word]

    if not unused_words:
        label_2.config(text="No more words available")
        return

    new_word = choice(unused_words)
    label_2.config(text=new_word)
    entry.focus_set()

def typing_speed_game():
    global s_time, count, corrects, cpm, wpm

    word = label_2.cget("text").strip().lower()
    user_input = entry.get().strip().lower()

    if user_input == word:
        if word not in used_word:
            used_word.append(word)

        for word_list in [easy_words, intermediate_words, advanced_words, expert_words]:
            if word in word_list:
                word_list.remove(word)

        corrects += 1
        count += 1
        end = timer()
        time_taken = end - s_time
        print(f'Time taken : {time_taken:.2f} seconds')

        calculate_speed(entry.get(), s_time, end)
        entry.delete(0, len(entry.get()))
        s_time = end
        start_game()
        label_tries.config(text=f"Number of attempts: {count}/{tries}")
    else:
        count += 1
        print("Enter the word seen!!!")
        entry.delete(0, len(entry.get()))
        start_game()
        label_tries.config(text=f"Number of attempts: {count}/{tries}")

    if count == tries:
        final_cpm = sum(avg_cpm)/len(avg_cpm)
        final_wpm = sum(avg_wpm)/len(avg_wpm)

        window.destroy()

        over = Tk()
        over.geometry("450x300")
        over.config(bg="crimson")

        g_over = Label(over, text="GAME OVER", font="arial 30")
        g_over.place(x=100, y=100)
        result = Label(over, text=f"You scored {corrects} out of {tries}\n"
                                  f"Final cpm : {final_cpm:.2f}\n"
                                  f"Final wpm : {final_wpm:.2f}",
                       bg="crimson", fg="white")
        result.place(x=150, y=165)

        g_over.mainloop()

window = Tk()
window.geometry("700x400")
window.title("Typing Speed Test")
window.config(bg="crimson")

window.update_idletasks()
w_length = window.winfo_width()
separator = ttk.Separator(window, orient="horizontal")
separator.place(x=10, y=200, width=w_length-20)

label_tries = Label(window, text=f"Number of attempts: {count}/{tries}", bg="crimson", fg="white", font="arial 15")
label_tries.place(x=10, y=10)

label_cpm = Label(window, text=f"Characters per Minute : {cpm}", bg="crimson", fg="white", font="arial 10")
label_cpm.place(x=300, y=30)
label_wpm = Label(window, text=f"Words per Minute : {wpm}", bg="crimson", fg="white", font="arial 10")
label_wpm.place(x=500, y=30)

label_1 = Label(window, text="Random Word :", bg="crimson", fg="white", font="arial 10")
label_1.place(x=50, y=80)
label_2 = Label(window, text="Start Test", bg="crimson", fg="white", font="arial")
label_2.place(x=200, y=100)

check_var = StringVar()
label_check = Label(window, text="Select Difficulty", bg="crimson", fg="white", font="arial 10")
label_check.place(x=580, y=80)

check_1 = Radiobutton(window, text="Easy",bg="crimson", variable=check_var, value="Easy")
check_1.place(x=590, y=100)
check_2 = Radiobutton(window, text="Intermediate",bg="crimson", variable=check_var, value="Intermediate")
check_2.place(x=590, y=120)
check_3 = Radiobutton(window, text="Advanced",bg="crimson", variable=check_var, value="Advanced")
check_3.place(x=590, y=140)
check_4 = Radiobutton(window, text="Expert",bg="crimson", variable=check_var, value="Expert")
check_4.place(x=590, y=160)

label_3 = Label(window, text="Type Given Word :", bg="crimson", fg="white", font="arial 10")
label_3.place(x=50, y=250)
entry = Entry(window)
entry.place(x=50, y=280, height=w_length*0.1, width = w_length-100)

b1 = Button(window, text="Start", command=start_game, width=30)
b1.place(x=40, y=170)
b2 = Button(window, text="Done", command=typing_speed_game, width=20)
b2.place(x=500, y=360)

window.bind("<Return>", lambda event: typing_speed_game())
window.mainloop()