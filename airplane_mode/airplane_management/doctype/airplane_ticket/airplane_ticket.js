// Copyright (c) 2024, David Maina and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add a custom button to open the seat assignment dialog
        frm.add_custom_button(__('Assign Seat'), function() {
            // Create a new dialog
            const dialog = new frappe.ui.Dialog({
                title: 'Assign Seat',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1 // make it mandatory
                    }
                ],
                primary_action_label: 'Assign',
                primary_action: function(data) {
                    // If a seat number is provided, assign it to the Seat field
                    if (data.seat_number) {
                        frm.set_value('seat', data.seat_number);
                        frm.save(); // save the form to persist the data
                        dialog.hide(); // hide the dialog after setting the value
                        frappe.show_alert({message: __('Seat Assigned Successfully!'), indicator: 'green'});
                    }
                }
            });

            // Show the dialog
            dialog.show();
        });
    }
});

