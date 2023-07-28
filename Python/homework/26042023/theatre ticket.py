max_tickets = 1000
ticket_price = 50
sold_tickets = 0

while sold_tickets < max_tickets:

    print("There are", max_tickets - sold_tickets, "tickets available.")
    num_tickets = int(input("How many tickets do you want to buy? "))


    if num_tickets > max_tickets - sold_tickets:
        print("Sorry, there are not enough tickets available. Please try again.")
    else:
        total_price = num_tickets * ticket_price
        print("You have bought", num_tickets, "tickets for a total of $", total_price)
        sold_tickets += num_tickets
print("All tickets have been sold. Thank you for your business!")