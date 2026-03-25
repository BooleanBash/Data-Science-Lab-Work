import random

def load_category_words(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"⚠️ {filename} not found!")
        return []

# Word categories
word_bank = {
    "Programming": load_category_words("programming_words.txt"),
    "Sports": load_category_words("sports.txt"),
    "Countries": load_category_words("countries.txt")
}

# Hangman stages (visual lives)
stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |
     |
     |
     |
    --------
    """
]

def choose_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice (1/2/3): ")

    if choice in ["exit", "quit", "stop", "end", "Exit", "Quit", "Stop", "End", "EXIT", "QUIT", "STOP", "END"]:
        print("Exiting game.")
        return "exit"

    if choice == '1':
        return "Easy"
    elif choice == '2':
        return "Medium"
    elif choice == '3':
        return "Hard"
    else:
        print("Invalid choice, defaulting to Medium.")
        return "Medium"

def filter_by_difficulty(words, level):
    if level == "Easy":
        return [w for w in words if len(w) <= 5]
    elif level == "Medium":
        return [w for w in words if 6 <= len(w) <= 8]
    else:
        return [w for w in words if len(w) >= 9]

def choose_word(level):
    category = random.choice(list(word_bank.keys()))
    words = word_bank[category]

    filtered_words = filter_by_difficulty(words, level)

    if not filtered_words:
        filtered_words = words  # fallback

    word = random.choice(filtered_words)

    return word, category

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def give_hint(word, guessed_letters):
    remaining_letters = [letter for letter in word if letter not in guessed_letters]
    if remaining_letters:
        return random.choice(remaining_letters)
    return None

def play_game():
    show_rules()
    level = choose_difficulty()
    if level == "exit":
        return "exit"
    word, category = choose_word(level)
    guessed_letters = []
    attempts = 6
    hints_used = 0

    print(f"\n🎮 Hangman - {level} Mode")
    print("Type 'hint' for help or guess the full word.\n")

    while attempts > 0:
        print(stages[6 - attempts])
        
        print("Word:", display_word(word, guessed_letters))
        print(f"Category: {category}")
        print("Guessed:", " ".join(guessed_letters))
        print("Lives left:", attempts)
        print("Hints Left:", 3 - hints_used)

        guess = input("Enter a letter, full word, or 'hint': ").lower()

        #EXIT OPTION
        if guess in ["exit", "quit", "stop", "end", "Exit", "Quit", "Stop", "End", "EXIT", "QUIT", "STOP", "END"]:
            print("Exiting game. Thanks for playing!")
            return "exit"

        # HINT SYSTEM
        if guess == "hint":
            if hints_used >= 3:
                print(" 🟥 No More Hints Available! 🟥 ")
                continue

            hint_letter = give_hint(word, guessed_letters)

            if hint_letter:
                print(f"💡 Hint: The letter '{hint_letter}' is in the word!")
                guessed_letters.append(hint_letter)

                hints_used += 1
                print(f"Hint {hints_used}/3 used.")

                if hints_used == 0:
                    print("First hint is free!")
                else:
                    attempts -= 1
                    print("Hint cost: -1 life")

            continue

        # WORD GUESS SYSTEM
        if len(guess) > 1:
            if not guess.isalpha():
                print("❌ Enter a valid word.")
                continue

            if guess == word:
                print("\n🎉 You guessed the whole word correctly!")
                print("Word was:", word)
                return
            else:
                attempts -= 2
                print("❌ Wrong word guess! (-2 lives)")
                continue

        # LETTER VALIDATION
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print(" 🟥 Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong!")

        # WIN CONDITION
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You WON!")
            print("Word was:", word)
            return

    # FINAL STATE (LOSS)
    print(stages[0])
    print("\n💀 Game Over!")
    print("Word was:", word)


def show_rules():
    print("\n" + "="*50)
    print("📜 HANGMAN GAME RULES 📜")
    print("="*50)

    print("\nObjective:")
    print("Guess the hidden word before you run out of lives.")

    print("\nCategories & Difficulty:")
    print("- Choose a difficulty level (Easy / Medium / Hard)")
    print("- Words are selected from categories: Programming, Sports, Countries")
    print("- Category will be shown during the game")

    print("\nHow to Play:")
    print("- Guess one letter at a time")
    print("- Or guess the full word directly")
    print("- Type 'hint' to reveal a letter")
    print("- Type 'stop' or 'end' anytime to exit the game")

    print("\n💡Hint System:")
    print("- Maximum 2 hints allowed per game")
    print("- First hint is FREE")
    print("- Second hint costs 1 life")

    print("\nPenalties:")
    print("- Wrong letter: -1 life")
    print("- Wrong word guess: -2 lives")
    print("- Extra hints reduce lives")

    print("\n❤️  Lives:")
    print("- You start with 6 lives")
    print("- Game ends when lives reach 0")

    print("\nWinning:")
    print("- Guess all letters correctly OR")
    print("- Guess the full word correctly")

    print("\n" + "="*50)

def main():
    print("\n Welcome to Hangman ")

    while True:
        result = play_game()
        

        if result in ["exit", "quit", "stop", "end", "Exit", "Quit", "Stop", "End", "EXIT", "QUIT", "STOP", "END"]:
            print("Thanks for playing!")
            break

        again = input("\nPlay again? (yes/no): ").lower()

        if again in ["no", "stop", "end"]:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()