frappe.ready(function() {
    // Get the flight parameter from the URL
    var urlParams = new URLSearchParams(window.location.search);
    var flightName = urlParams.get('flight');

    if (flightName) {
        // Set the flight field value
        frappe.web_form.set_value('flight', flightName);
        
        // Optionally, you can fetch more details about the flight and pre-fill other fields
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: 'Airplane Flight',
                name: flightName
            },
            callback: function(response) {
                if (response.message) {
                    var flight = response.message;
                    // You can pre-fill more fields here if needed
                    // For example:
                    // frappe.web_form.set_value('booking_date', flight.departure_date);
                }
            }
        });
    }

    // Set today's date as the default booking date
    var today = frappe.datetime.get_today();
    frappe.web_form.set_value('booking_date', today);
});