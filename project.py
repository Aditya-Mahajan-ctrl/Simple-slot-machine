import random

# Define the slot machine symbols and their corresponding payouts
symbols = ['Cherry', 'Lemon', 'Orange', 'Bell', 'Diamond', 'Lucky']
payouts = {
    'Cherry': 2,
    'Lemon': 3,
    'Orange': 4,
    'Bell': 5,
    'Diamond': 10,
    'Lucky': 20
}

def spin():
    """Simulate spinning the slot machine."""
    return [random.choice(symbols) for _ in range(3)]

def calculate_payout(result):
    """Calculate payout based on the result of the spin."""
    if all(symbol == result[0] for symbol in result):
        return payouts[result[0]]  # Payout is determined from the first symbol
    return 0  # No payout for different symbols

def main():
    print("Welcome to the Simple Slot Machine!")

    while True:
        # Ask user if they want to play
        play = input("Press 'Enter' to spin or type 'quit' to exit: ")
        if play.lower() == 'quit':
            print("Thanks for playing!")
            break

        # Spin the slot machine
        result = spin()
        print("Spinning...")
        print(f"Result: {result}")

        # Calculate payout
        payout = calculate_payout(result)

        if payout:
            print(f"Congratulations! You won {payout} coins!")
        else:
            print("Sorry, no win this time. Better luck next time!")

if __name__ == "__main__":
    main()
