// Copyright (c) 2024, David Maina and contributors
// For license information, please see license.txt

// revenue_by_airline.js
frappe.query_reports["Revenue by Airline"] = {
    onload: function(report) {
        frappe.call({
            method: "frappe.desk.query_report.run",
            args: {
                report_name: "Revenue by Airline",
                filters: report.get_values()
            },
            callback: function(r) {
                if (r.message) {
                    const data = r.message;
                    let airlines = [];
                    let revenues = [];

                    data.result.forEach(row => {
                        airlines.push(row[0]);  // Airline
                        revenues.push(row[1]);  // Revenue
                    });

                    // Add the donut chart
                    report.page.add_chart({
                        data: {
                            labels: airlines,
                            datasets: [
                                {
                                    values: revenues
                                }
                            ]
                        },
                        type: 'donut',  // Set chart type to donut
                        height: 250
                    });
                }
            }
        });
    }
};