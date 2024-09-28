# flight_detail.py
import frappe

@frappe.whitelist()
def get_flight_details(flight_name):
    try:
        flight = frappe.get_doc("Flight", flight_name)
        context = {
            "flight": flight
        }
        return frappe.render_template("flight_detail.html", context)
    except frappe.DoesNotExistError:
        return frappe.render_template("flight_detail.html", {"flight": None})
    
@frappe.whitelist()
def get_flight_details(flight_name):
    try:
        flight = frappe.get_doc("Flight", flight_name)
        context = {"flight": flight}
        frappe.logger().info(f"Flight data: {flight.as_dict()}")  # For debugging
        return frappe.render_template("flight_detail.html", context)
    except frappe.DoesNotExistError:
        frappe.logger().error(f"Flight not found: {flight_name}")  # For debugging
        return frappe.render_template("flight_detail.html", {"flight": None})