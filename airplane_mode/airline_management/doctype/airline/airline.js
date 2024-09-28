// Copyright (c) 2024, David Maina and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field has a value
        if (frm.doc.website) {
            // Add a web link instead of a custom button
            frm.add_web_link(__('Visit Website'), frm.doc.website);
        }
    }
});

