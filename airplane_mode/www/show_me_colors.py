import frappe

def get_context(context):
    context.color = frappe.form_dict.get('color', 'black')
    return context

# Define a route function
def show_me():
    # No additional logic needed; we'll handle everything in the template
    pass
