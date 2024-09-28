# Copyright (c) 2024, David Maina and contributors
# For license information, please see license.txt

import frappe
def get_data(filters=None):
    # Query the data from your Airplane Flight Doctype
    data = frappe.db.sql("""
        SELECT
            airline AS airlines,
            SUM(revenue) AS revenue
        FROM `tabAirplane Flight`
        GROUP BY airline
        ORDER BY revenue DESC
    """, as_dict=True)
    
    # Structure the chart data
    chart = {
        "data": {
            "labels": [row['airlines'] for row in data],
            "datasets": [{
                "name": "Revenue",
                "values": [row['revenue'] for row in data]
            }]
        },
        "type": "donut",
        "title": "Revenue by Airlines"
    }

    # Return the report data and chart
    return {
        "columns": [
            {"label": "Airlines", "fieldname": "airlines", "fieldtype": "Data"},
            {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency"}
        ],
        "data": data,
        "chart": chart,
        "summary": [{
            "label": "Total Revenue",
            "value": sum([row['revenue'] for row in data]),
            "indicator": "Green"
        }]
    }
