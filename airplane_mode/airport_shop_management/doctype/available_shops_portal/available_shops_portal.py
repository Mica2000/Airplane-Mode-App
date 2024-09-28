# Copyright (c) 2024, David Maina and contributors
# For license information, please see license.txt

# fetch available shops

from frappe.website.website_generator import WebsiteGenerator

class AvailableShopsPortal(WebsiteGenerator):
    def __init__(self):
        self.website = {
            'condition_field': 'published'
        }