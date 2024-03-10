# Importing all the libraries
import pygame
from tkinter import Button, Label, PhotoImage, Canvas, Tk, NW
from PIL import Image, ImageTk, ImageSequence
from random import randint


# Class to load all the images
class RPSImageLoader:

    def __init__(self):
        self.load_images()
        self.load_images1()
        self.load_images2()

    def load_images(self):
        # Loading all the images
        self.image_rock = ImageTk.PhotoImage(Image.open("rock.png"))
        self.image_paper = ImageTk.PhotoImage(Image.open("paper.png"))
        self.image_scissors = ImageTk.PhotoImage(Image.open("scissors.png"))
        self.image_YouDefault = Image.open("You-Default-IMage.png")
        self.image_YouDefault.resize((200, 275))
        self.image_YouDefault = ImageTk.PhotoImage(self.image_YouDefault)
        self.image_BotDefault = Image.open("Bot-Default-IMage.png")
        self.image_BotDefault.resize((200, 275))
        self.image_BotDefault = ImageTk.PhotoImage(self.image_BotDefault)

    def load_images1(self):
        self.image_RU = Image.open("r_user.png").resize((200, 275))
        self.image_RU = ImageTk.PhotoImage(self.image_RU)
        self.image_RB = Image.open("r_bot.png").resize((200, 275))
        self.image_RB = ImageTk.PhotoImage(self.image_RB)
        self.image_PU = Image.open("p_user.png").resize((200, 275))
        self.image_PU = ImageTk.PhotoImage(self.image_PU)
        self.image_PB = Image.open("p_bot.png").resize((200, 275))
        self.image_PB = ImageTk.PhotoImage(self.image_PB)
        self.image_SU = Image.open("s_user.png").resize((200, 275))
        self.image_SU = ImageTk.PhotoImage(self.image_SU)
        self.image_SB = Image.open("s_bot.png").resize((200, 275))
        self.image_SB = ImageTk.PhotoImage(self.image_SB)

    def load_images2(self):
        self.image_celebrate_player = PhotoImage(file="celebration.gif")
        self.image_celebrate_bot = PhotoImage(file="celebration.gif")
        self.image_celebrate_tie = Image.open("tie.png").resize((500, 100))
        self.image_celebrate_tie = ImageTk.PhotoImage(self.image_celebrate_tie)


# Class for the full game functionality
class RPSGame:

    def __init__(self, window):
        self.window = window
        self.window.title("Rock, Paper & Scissors")
        self.window.configure(background="white")
        self.window.geometry('1500x850')

        # Initializing pygame for sound effects and background music
        pygame.init()

        # Setting up the pygame screen
        self.screen = pygame.display.set_mode((1500, 850))

        # Loading Backgroud animation
        self.background_animation = pygame.image.load("design_combine(2).gif")
        self.background_animation.convert()

        # Initializing player and bot scores
        self.player_score = 0
        self.bot_score = 0
        self.to_select = ["rock", "paper", "scissors"]

        # Initializing image loader to load all images
        self.image_loader = RPSImageLoader()

        # Initializing sound effects and background music using pygame mixer
        pygame.mixer.init()
        self.sound_click = pygame.mixer.Sound("click.wav")
        self.sound_player_win = pygame.mixer.Sound("you_win.wav")
        self.sound_bot_win = pygame.mixer.Sound("bot_win.wav")
        self.background_music = pygame.mixer.Sound("bg_music.mp3")

        # Setting up the user interface
        self.setup_ui()
        self.setup_ui1()

    def setup_ui(self):
        # Creating a canvas for displaying the gif animation
        self.canvas = Canvas(self.window, width=1500, height=90, bg="white")
        self.canvas.place(x=10, y=10)

        # Loading and displaying the gif animation
        self.load_gif_animation("design_combine(2).gif", 0, 0)

        # Background music
        self.background_music.play(loops=-1)  # Play infinitely (-1)
        self.background_music.set_volume(0.1)

        # Initializing default images for bot and player
        self.label_bot = Label(self.window,
                               image=self.image_loader.image_BotDefault)
        self.label_bot.place(x=1000, y=200)
        self.bot_indicator = Label(self.window, text="BOT",
                                   bg="white", fg="#DE1884",
                                   font=("arial", 20, "bold"))
        self.bot_indicator.place(x=1075, y=160)
        self.label_player = Label(self.window,
                                  image=self.image_loader.image_YouDefault)
        self.label_player.place(x=200, y=200)
        self.player_indicator = Label(self.window,
                                      text="PLAYER", bg="white", fg="#DE1884",
                                      font=("arial", 20, "bold"))
        self.player_indicator.place(x=250, y=160)

        # Initializing buttons for rock, paper, and scissors
        self.button_rock = Button(self.window, borderwidth=0, bg="white",
                                  image=self.image_loader.image_rock,
                                  command=lambda: self.on_button_click("rock"))
        self.button_rock.place(x=400, y=588)
        self.button_paper = Button(self.window, borderwidth=0, bg="white",
                                   image=self.image_loader.image_paper,
                                   command=lambda: self.on_button_click("paper"))
        self.button_paper.place(x=600, y=598)
        self.button_scissors = Button(self.window, borderwidth=0, bg="white",
                                      image=self.image_loader.image_scissors,
                                      command=lambda: self.on_button_click("scissors"))
        self.button_scissors.place(x=800, y=578)

    def setup_ui1(self):
        # Initializing labels to display player and bot scores
        self.player_score_label = Label(self.window,
                                        text=str(self.player_score),
                                        font=("arial", 20, "bold"), bg="white",
                                        fg="#663399")
        self.player_score_label.place(x=280, y=498)
        self.bot_score_label = Label(self.window,
                                     text=str(self.bot_score),
                                     font=("arial", 20, "bold"), bg="white",
                                     fg="#663399")
        self.bot_score_label.place(x=1100, y=498)

        # Initializing label to display final message
        self.final_message = Label(self.window, font=("arial", 20, "bold"),
                                   bg="white", fg="#FFCC33")
        self.final_message.place(x=625, y=550)

        # Initializing celebration labels (hidden)
        self.label_celebrate_player = Label(self.window,
                                            image=self.image_loader.image_celebrate_player,
                                            bg="white")
        self.label_celebrate_bot = Label(self.window,
                                         image=self.image_loader.image_celebrate_bot,
                                         bg="white")
        self.label_celebrate_tie = Label(self.window,
                                         image=self.image_loader.image_celebrate_tie,
                                         bg="white")

    def load_gif_animation(self, filename, x, y):
        # Loading and animating the gif animation
        self.gif_frames = []
        self.gif_index = 0
        self.gif_delay = 10  # Delay between frames in milliseconds

        # Loading Gif Frames
        gif = Image.open(filename)
        self.gif_width, self.gif_height = gif.size
        self.gif_frames = [ImageTk.PhotoImage(frame)
                           for frame in ImageSequence.Iterator(gif)]

        # Displaying GIF on canvas
        self.gif_label = self.canvas.create_image(x, y,
                                                  anchor=NW,
                                                  image=self.gif_frames[0])

        # Start GIF animation
        self.animate_gif()

    def animate_gif(self):
        # Animate the gif (displaying the next frame)
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        self.canvas.itemconfig(self.gif_label,
                               image=self.gif_frames[self.gif_index])

        # Calling the function again after the delay for smooth animation
        self.window.after(self.gif_delay, self.animate_gif)

    # Function to handle button clicks
    def on_button_click(self, choice):
        self.sound_click.play()  # Playing click sound
        self.update_choice(choice)

    def update_choice(self, choice):
        # Update player and bot choices
        bot_choice = self.to_select[randint(0, 2)]
        if bot_choice == "rock":
            self.label_bot.configure(image=self.image_loader.image_RB)
        elif bot_choice == "paper":
            self.label_bot.configure(image=self.image_loader.image_PB)
        else:
            self.label_bot.configure(image=self.image_loader.image_SB)
        if choice == "rock":
            self.label_player.configure(image=self.image_loader.image_RU)
        elif choice == "paper":
            self.label_player.configure(image=self.image_loader.image_PU)
        else:
            self.label_player.configure(image=self.image_loader.image_SU)
        self.winner_check(choice, bot_choice)

    # Checking the winner and update scores
    def winner_check(self, player_choice, bot_choice):
        winner_message = ""
        if player_choice == bot_choice:
            winner_message = "It's a tie!!"
            self.tie_update()
        elif (player_choice == "rock" and bot_choice == "paper") or \
                (player_choice == "paper" and bot_choice == "scissors") or \
                (player_choice == "scissors" and bot_choice == "rock"):
                winner_message = "Bot Wins"
                self.bot_update()
        else:
            winner_message = "Player Wins"
            self.player_update()
        self.msg_updation(winner_message)

    def bot_update(self):
        # Updating Bot Score
        self.bot_score += 1
        self.bot_score_label.config(text=str(self.bot_score))

        # Play bot win celebration sound
        self.sound_bot_win.play()

        # Show bot celebration GIF
        self.label_celebrate_bot.place(x=1000, y=200)

        # Hide after 1 second
        self.window.after(1000, self.hide_celebrate_bot)

    def player_update(self):
        # Updating Player Score
        self.player_score += 1
        self.player_score_label.config(text=str(self.player_score))

        # Play player win celebration sound
        self.sound_player_win.play()

        # Show player celebration GIF
        self.label_celebrate_player.place(x=200, y=200)

        # Hide after 1 second
        self.window.after(1000, self.hide_celebrate_player)

    # Function for displaying tie message and animation
    def tie_update(self):
        self.label_celebrate_tie.place(x=450, y=275)
        self.window.after(1000, self.hide_celebrate_tie)

    # Function to hide player celebration animation
    def hide_celebrate_player(self):
        self.label_celebrate_player.place_forget()

    # Function to hide bot celebration animation
    def hide_celebrate_bot(self):
        self.label_celebrate_bot.place_forget()

    # Function to hide tie celebration animation
    def hide_celebrate_tie(self):
        self.label_celebrate_tie.place_forget()

    # Function to update final message label
    def msg_updation(self, message):
        self.final_message.config(text=message)


if __name__ == "__main__":
    window = Tk()
    game = RPSGame(window)
    window.mainloop()
