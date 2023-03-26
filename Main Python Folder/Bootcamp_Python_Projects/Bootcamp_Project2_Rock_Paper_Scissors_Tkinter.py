#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import tkinter as tk
# create a window
window=tk.Tk()
window.title("Rock Paper Scissors Game")

# define choices
choices=['rock','paper','scissors']

# define the function to generate computer choice
def computer_choice(choices):
    return random.choice(choices)

# define the function to determine the winner
def determine_winner(player_choice):
    computer=computer_choice(choices)
    if player_choice==computer:
        result_label.config(text="Its a tie!")
    elif (player_choice=="rock" and computer=="scissors") or (player_choice=="paper" and computer=="rock") or (player_choice=="scissors" and computer=="paper"):
        result_label.config(text="You win")
    else:
        result_label.config(text="Computer wins!")
        
# define the function for the button click event
def button_click(player_choice):
    player_label.config(text="You chose " + player_choice)
    determine_winner(player_choice)

# create labels and buttons
player_label = tk.Label(window,text="Choose rock,paper, or scissors:")
player_label.pack()

rock_button=tk.Button(window,text="Rock",command=lambda:button_click("rock"))
rock_button.pack()
paper_button=tk.Button(window,text="Paper",command=lambda:button_click("paper"))
paper_button.pack()
scissors_button=tk.Button(window,text="Scissors",command=lambda:button_click("scissors"))
scissors_button.pack()

result_label = tk.Label(window,text="")
result_label.pack()

# Start the GUI
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




