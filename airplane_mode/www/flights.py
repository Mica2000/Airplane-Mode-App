# flights.py
import frappe

def get_context(context):
    try:
        flight_name = frappe.form_dict.flight
        context.flight = frappe.get_doc("Flight", flight_name)
    except Exception as e:
        frappe.log_error(f"Error fetching flight data: {str(e)}")
        context.flight = None