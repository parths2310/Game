import random

try:
    # THIS IS for python 2 users
    from Tkinter import *
except ImportError:
    #this is for python3 user
    from tkinter import *


# this upper limit and lower limit
MAX = 10
MIN = 1


class Application(Frame):
    # the gui of application

    def __init__(self, master):

        Frame.__init__(self, master)

        master.minsize(width=500, height=200)
        self.grid()

        self.create_widgets()

        #random number to be guessed by the user

        self.number = random.randrange(MIN, MAX +1)

        self.tries = 0

    def create_widgets(self):

        Label(self,
            text="I'm thinking about number between" +str(MIN)+
            "and" +str(MAX)
             ).grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,
              text="Try to guess the number Genius"
             ).grid(row=1, column=0, columnspan=2, sticky=W)
        Label(self,
              text="Number of Tries: 0"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,
              text="Guess"
              ).grid(row=2, column=0, sticky=W)

        #enter widget to allow guessing

        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, stick=W)

        Button(self,
               text="Enter",
               command=self.get_guess
               ).grid(row=2, column=2, columnspan=4, sticky=W)

        Button(self,
               text="Reset",
               command=self.reset
               ).grid(row=1, column=2, columnspan=1, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=3, column=0, columnspan=3)


    def get_guess(self):
        """Obtain the players guess to verify"""
        try:
            guess = int(self.guess_ent.get())
        except(ValueError):
            self.display_message("Invalid Entry")

        else:
            self.tries += 1
            Label(self,
                  text="Number of Tries" + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)
            self.check_guess(guess)

    def check_guess(self, guess):
        """Verify if the players guess is correct.
        Keyword Argument:
        guess - the int value to be verified"""
        if guess < MIN or guess > MAX :
           self.display_message("Invalid Input, Guess is outside the range")
           self.tries -= 1
           return

    #if guess equals the number, end the game
        if guess == self.number :
           self.resetgame()
           return
    #Otherwise, see if guess is higher or lower than the chosen number
        if guess < self.number :
            self.display_message("Guess Higher")
            return
        elif guess > self.number :
            self.display_message("Guess Lower")
            return

    def display_message(self, message):
        """
        Dispaly a message on the text box.
        Keyword Argument:

        message -- the message to be displayed

        """
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

    def reset(self):

        self.number = random.randrange(MIN, MAX +1)
        self.display_message("Game Reset. Please Enter a another number to play the game")
        self.tries = 0

        Label(self,
              text="Number of Tries" + str(self.tries)
              ).grid(row=0, column=2, columnspan=1, sticky=W)

    def resetgame(self):
        self.display_message("congrats you guessed it Right, the number was" + \
                             str(self.number) + ". and it took you " + \
                             str(self.tries)+ "tries!")



def main():
    root=Tk()
    root.title("The Guess Number")
    app=Application(root)
    root.mainloop()


main()







