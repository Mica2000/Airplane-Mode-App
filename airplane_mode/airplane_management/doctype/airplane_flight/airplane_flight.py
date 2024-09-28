# Copyright (c) 2024, MIT and contributors
# For license information, please see license.txt
import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def before_submit(self):
        # Fetch all related airplane tickets and populate them in the child table
        self.populate_airplane_tickets()
        
    def on_submit(self):
        self.status = "Completed"
        self.db_Set('status','Completed',update_modified=False)  # Save the updated status


    def populate_airplane_tickets(self):
        if self.name:
            tickets = frappe.get_all("Airplane Ticket", filters={"flight": self.name}, fields=["name", "passenger", "seat", "flight_price"])
            self.set("airplane_tickets", [])
            for ticket in tickets:
                row = self.append("airplane_tickets", {})
                row.ticket_name = ticket.name
                row.passenger = ticket.passenger
                row.seat = ticket.seat
                row.flight_price = ticket.flight_price

def get_context(context):
    flights = frappe.get_all(
        'Airplane Flight',
        fields=['name', 'source_airport_code', 'destination_airport_code', 
                'departure_date', 'departure_time', 'flight_duration', 'route'],distinct=True)
    



