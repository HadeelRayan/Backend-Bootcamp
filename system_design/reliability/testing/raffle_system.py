import random


class Raffle:
    def __init__(self, max_people, max_tickets, ticket_price):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.ticket_price = ticket_price
        self.total_earnings = 0
        self.participants = {}

    # to check if it really adds a person to the list
    def add_person(self, name):
        if len(self.participants) < self.max_people and name not in self.participants:
            self.participants[name] = 0

    # check if the ticket is sold
    # to check if the price is updated
    # check about more than one ticket
    def buy_ticket(self, name, number_of_tickets=1):
        # A person can buy one or more tickets.
        if name in self.participants and self.total_tickets_sold() + number_of_tickets <= self.max_tickets:
            self.participants[name] += number_of_tickets
            self.total_earnings += self.ticket_price * number_of_tickets

    # check is the sum is right
    # check the return value
    def total_tickets_sold(self):
        return sum(self.participants.values())

    # to check if the winner is in the list
    # to check if the winner name is legal
    def select_winner(self):
        # Select a winner taking into account the number of tickets each person bought.
        if not self.participants:
            return None
        tickets = []
        for name, ticket_count in self.participants.items():
            tickets.extend([name] * ticket_count)
        return random.choice(tickets)
