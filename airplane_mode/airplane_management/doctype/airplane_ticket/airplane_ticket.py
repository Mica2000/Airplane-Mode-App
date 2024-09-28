# Copyright (c) 2024, MIT and contributors
# For license information, please see license.txt

# Copyright (c) 2024, David Maina and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
import string
import random
from frappe import _


class AirplaneTicket(Document):
    def validate(self):
        # Ensure add-ons are unique
        self.remove_duplicate_add_ons()
        # Calculate the total amount
        self.calculate_total_amount()

    def remove_duplicate_add_ons(self):
        """
        Removes duplicate add-ons by summing their amounts and keeping only unique add-on types.
        """
        if not self.get('add_ons'):
            return

        # Dictionary to keep track of unique add-on types and their total amounts
        unique_add_ons = {}

        # Iterate through the add-on items
        for addon in self.get('add_ons'):
            addon_type = addon.get('item')
            amount = addon.get('amount')

            if addon_type in unique_add_ons:
                # Update the existing amount for this add-on type
                unique_add_ons[addon_type] += amount
            else:
                # Add new add-on type to the unique dictionary
                unique_add_ons[addon_type] = amount

        # Clear existing add-ons and re-add unique ones
        self.set('add_ons', [])
        for addon_type, total_amount in unique_add_ons.items():
            self.append('add_ons', {
                'item': addon_type,
                'amount': total_amount
            })

    def calculate_total_amount(self):
        """
        Calculates the total amount by adding flight price and sum of all add-on amounts.
        """
        # Initialize total amount to the flight price
        total_amount = self.flight_price or 0

        # Add the amounts of all add-ons
        if self.get('add_ons'):
            for addon in self.get('add_ons'):
                total_amount += addon.get('amount') or 0

        # Set the total amount field
        self.total_amount = total_amount

    def before_save(self):
        # Automatically generate a seat number if not already assigned
        self.generate_seat_number()

    def generate_seat_number(self):
        """
        Generate a seat number if not already assigned.
        """
        if not self.seat:  # Check if the seat is not already assigned
            row = random.randint(1, 99)  # Generate a random row between 1 and 99
            column = random.choice(string.ascii_uppercase[:5])  # Choose a letter from A to E
            self.seat = f"{row}{column}"  # Assign the seat as a string like '12A'

    def before_submit(self):
        """
        Hook to prevent submission if the status is not "Boarded".
        """
        frappe.logger().debug(f"Ticket status before submit: {self.status}")
        if self.status != "Boarded":
            frappe.throw(_("Ticket cannot be submitted unless the status is 'Boarded'"), frappe.ValidationError)

# To check the remaining seats
class Ticket:
    def __init__(self):
        # Generate a random seat assignment during initialization
        row = random.randint(1, 99)  # Generate a random row between 1 and 99
        column = random.choice(string.ascii_uppercase[:5])  # Choose a letter from A to E
        self.seat = f"{row}{column}"  # Assign the seat as a string like '12A'

    def before_submit(self):
        """
        Hook to prevent submission if the status is not "Boarded".
        """
        frappe.logger().debug(f"Ticket status before submit: {self.status}")
        if self.status != "Boarded":
            frappe.throw(
                frappe._("Ticket cannot be submitted unless the status is 'Boarded'"),
                frappe.ValidationError
            )