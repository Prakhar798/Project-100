class Atm:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def check_balance(self):
        print("Balance : 50,000 Rs")

    def withdrawl(self, amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount : " + str(amount))
        print("Remaning Balance  = " + str(new_amount))


def main():
    card_number = input("Enter your card number : ")
    pin = input("Enter your pin : ")
    new_user = Atm(card_number, pin)
    print("Choose your activity")
    print("1. Balance Enquiry 2. Withdrawl")
    activity = int(input("Enter your activity number: "))
    if activity == 1:
        new_user.check_balance()
    elif activity == 2:
        amount = int(input("Enter amount you want to withdraw: "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number.")


main()
