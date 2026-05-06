import tkinter as tk
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.cleanliness = 80
    
    def feed(self, points):
        self.hunger = min(self.hunger + points, 100)
    
    def play(self):
        self.energy = max(0, self.energy - 5)
        self.hunger = max(0, self.hunger - 5)

    def sleep(self):
        while self.energy < 100:
            self.energy += 2
            time.sleep(2)
        return True
    
    def clean(self):
        time.sleep(10)
        self.cleanliness = 100
    
    def mood(self):
        if self.hunger >= 80 and self.energy >= 80:
            return "Happy"
        elif self.hunger < 25 and self.energy >= 25:
            return "Hungry"
        elif self.hunger >= 25 and self.energy < 25:
            return "Tired"
        elif self.hunger < 25 and self.energy < 25:
            return "Grumpy"
        else:
            return "Okay"
        
class petGUI:
    def __init__(self, root):
        self.root = root
        self.pet = None
        self.root.title = ("Tamagotchi")
        self.root.minsize(200, 200)

        self.create_frames()
        self.create_pet("Jack")
        self.create_widgets()
        self.state = "normal"

    def create_frames(self):
        self.mainFrame = tk.Frame(root, width="200", height="200", background="beige")
        self.petInfo = tk.Frame(self.mainFrame, width="80", height="80").grid(row=1, column=0)
        self.petButtons = tk.Frame(self.mainFrame, width="80", height="80").grid(row=1, column=1)

    def create_pet(self, name):
        self.pet = Pet(name)

    def create_widgets(self):
        self.hunger_stat = tk.Label(self.petInfo, text=f"Hunger: {self.pet.hunger}")
        self.hunger_stat.pack()

        self.energy_stat = tk.Label(self.petInfo, text=f"Energy: {self.pet.energy}")
        self.energy_stat.pack()

        self.cleanliness_stat = tk.Label(self.petInfo, text=f"Cleanliness: {self.pet.cleanliness}")
        self.cleanliness_stat.pack()

        self.mood_label = tk.Label(self.petInfo, text=f"{self.pet.name} is {self.pet.mood()}")
        self.mood_label.pack()

        self.feedBtn = tk.Button(self.petButtons, text="Feed", command=self.feed_pet)
        self.feedBtn.pack() 

        self.sleepBtn = tk.Button(self.petButtons, text="Sleep", command=self.sleep_pet)
        self.sleepBtn.pack()

        self.cleanBtn = tk.Button(self.petButtons, text="Clean", command=self.clean_pet)
        self.cleanBtn.pack()

        self.playBtn = tk.Button(self.petButtons, text="Play", command=self.play_pet)
        self.playBtn.pack()

    def feed_pet(self):
        if self.state is "normal":
            self.pet.feed(5)
            self.update_display()

    def sleep_pet(self):
        if self.state is "normal":
            self.state = "sleeping"
            self.pet.sleep()
            self.state = "normal"

    def clean_pet(self):
        if self.state is "normal":
            self.state = "cleaning"
            self.pet.clean()
            self.update_display()
    
    def play_pet(self):
        if self.state is "normal":
            self.pet.play()
            self.update_display()
    
    def update_display(self):
        self.hunger_stat.config(text=f"Hunger: {self.pet.hunger}")
        self.energy_stat.config(text=f"Energy: {self.pet.energy}")
        self.cleanliness_stat.config(text=f"Cleanliness: {self.pet.cleanliness}")
        self.mood_label.config(self.petInfo, text=f"{self.pet.name} is {self.pet.mood()}")


        

root = tk.Tk()
app = petGUI(root)
root.mainloop()