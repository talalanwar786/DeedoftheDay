import tkinter as tk
import random

# List of 100 good deeds
good_deeds = [
    "Compliment someone's sneakers",
    "Hold the door open for someone",
    "Give a genuine smile to a stranger",
    "Send a thank you message to someone you appreciate",
    "Donate to a charity you care about",
    "Offer to help someone with their groceries",
    "Leave a positive comment on a friend's post",
    "Call a friend or family member to check in on them",
    "Help a friend/classmate with an assignment at college",
    "Give a homeless person a meal",
    "Offer to walk someone's dog",
    "Send a handwritten note to someone",
    "Give a compliment to someone you don’t know well",
    "Make a donation to a cause you're passionate about",
    "Help someone carry something heavy",
    "Surprise a friend with their favorite snack",
    "Offer to run an errand for someone",
    "Leave a positive review for a small business",
    "Help an elderly person with their shopping",
    "Give someone a hug if they need one",
    "Thank a teacher for their guidance",
    "Write an encouraging message on someone's social media",
    "Plant a tree or flowers in your neighborhood",
    "Offer a seat to someone in need",
    "Give an unexpected gift to a friend",
    "Volunteer at a local charity",
    "Give blood if you're eligible",
    "Make a handmade gift for someone",
    "Tell someone how much you appreciate them",
    "Share an inspiring story with a friend",
    "Give a book to someone who loves to read",
    "Pay for someone's coffee in line behind you",
    "Share your umbrella with someone in the rain",
    "Mow your neighbor's lawn",
    "Let someone go ahead of you in line",
    "Send a care package to a loved one",
    "Offer to pick up groceries for a friend",
    "Create a playlist for a friend",
    "Offer to babysit for a friend or family member",
    "Encourage someone who's going through a tough time",
    "Help a friend organize their space",
    "Write a positive message on social media about something you love",
    "Give someone a hand with their homework",
    "Invite someone to lunch or coffee",
    "Send a surprise thank you card to someone",
    "Give away something you no longer need",
    "Offer to teach someone a skill you know",
    "Buy a gift for someone just because",
    "Compliment someone's outfit",
]

# Function to display a random good deed
def show_good_deed():
    deed = random.choice(good_deeds)
    deed_label.config(text=deed)
    count_deeds()

# Function to count and display how many deeds have been shown
deed_count = 0
def count_deeds():
    global deed_count
    deed_count += 1
    count_label.config(text=f"Deeds Displayed: {deed_count}")

# Function to reset the deed and count
def reset():
    global deed_count
    deed_count = 0
    count_label.config(text="Deeds Displayed: 0")
    deed_label.config(text="")

# Function to change background color
def change_bg_color():
    color = color_entry.get()
    root.config(bg=color)
    deed_label.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Good Deed of the Day")

# Create a button and label
button = tk.Button(root, text="Get Good Deed", command=show_good_deed)
button.pack(pady=20)

# Label to display the good deed
deed_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=300)
deed_label.pack(pady=20)

# Label to display deed count
count_label = tk.Label(root, text="Deeds Displayed: 0", font=("Helvetica", 12))
count_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

# Entry to input background color
color_label = tk.Label(root, text="Enter background color (e.g., 'lightblue'):")
color_label.pack()

color_entry = tk.Entry(root)
color_entry.pack(pady=10)

# Button to change background color
color_button = tk.Button(root, text="Change Background Color", command=change_bg_color)
color_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()