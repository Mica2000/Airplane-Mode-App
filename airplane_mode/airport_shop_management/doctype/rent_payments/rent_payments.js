// Copyright (c) 2024, David Maina and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rent Payments', {
    refresh: function(frm) {
        // Add a button to print the receipt
        frm.add_custom_button(__('Print Receipt'), function() {
            // Open the print format
            frappe.route_options = {
                "doctype": "Rent Payments",
                "name": frm.doc.name,
                "format": "Rent Payment", // 
                "no_letterhead": 1
            };
            // Redirect to the print view
            frappe.set_route("print", "Rent Payments", frm.doc.name);
        });
    }
});
