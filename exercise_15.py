from colorama import init, Fore, Style
import os

class Dog:
    def __init__(self, name, breed, hobby):
        self.name = name
        self.breed = breed
        self.hobby = hobby

    def bark(self):
        print(f"{self.name} the {self.breed} loves {self.hobby} says Woof!")
        input("\nPress Enter to return...")

    def sit(self):
        print(f"{self.name} is now sitting.")
        input("\nPress Enter to return...")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")
        input("\nPress Enter to return...")

    def play_dead(self):
        print(f"{self.name} is playing dead. Such a good dog!")
        input("\nPress Enter to return...")

    def roll_over(self):
        print(f"{self.name} rolls over! What a good dog!")
        input("\nPress Enter to return...")

    def display_menu(self):
        while True:
            os.system('cls')
            print(Fore.LIGHTCYAN_EX + 
                  f"Interact with {self.name} using the options below:")
            print("\n========= MENU ==========")
            print("[1] Bark")
            print("[2] Sit")
            print("[3] Fetch")
            print("[4] Play Dead")
            print("[5] Roll Over")
            print("[6] Back to Main Menu")
            print("=========================")

            try:
                choice = int(input("Enter your choice: "))
                os.system('cls')
                if not self.display_choice(choice):
                    break 
            except ValueError:
                os.system('cls')
                print(Fore.RED + 
                    "Invalid input. Please enter a number between 1 and 6.")
                input("\nPress Enter to return...")
                os.system('cls')

    def display_choice(self, choice):
        match choice:
            case 1:
                self.bark()
            case 2:
                self.sit()
            case 3:
                self.fetch()
            case 4:
                self.play_dead()
            case 5:
                self.roll_over()
            case 6:
                print(Fore.GREEN + "Thank you for interacting! Goodbye!")
                input("\nPress Enter to exit...")
                return
            case _:
                print(Fore.RED + "Invalid choice. Please try again.")
                input("\nPress Enter to return...")
        return True

def ynion_mabeamae():
    os.system('cls')
    print(Fore.CYAN)
    dog_name = input("Enter the dog's name: ")
    dog_breed = input("Enter the dog's breed: ")
    dog_hobby = input("Enter the dog's hobby: ")

    dog = Dog(name=dog_name, breed=dog_breed, hobby=dog_hobby)
    dog.display_menu()


ynion_mabeamae()