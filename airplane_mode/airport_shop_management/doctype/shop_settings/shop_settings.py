# Copyright (c) 2024, David Maina and contributors
# For license information, please see license.txt

# import frappe


#Rent reminder enabled
import frappe

def send_rent_reminders():
    tenants = frappe.get_all('Rent Payments', filters={'due_date': ['>=', frappe.utils.nowdate()]})
    
    for tenant in tenants:
        tenant_email = frappe.db.get_value('Tenant', tenant.name, 'email')
        if tenant_email:
            message = f"Dear {tenant.tenant_name},\n\nThis is a friendly reminder that your rent for shop {tenant.shop_name} is due on {tenant.due_date}. Please make your payment."
            frappe.sendmail(
                recipients=[tenant_email],
                subject="Rent Payment Reminder",
                message=message
            )
