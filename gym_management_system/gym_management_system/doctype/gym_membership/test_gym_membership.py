# Copyright (c) 2023, Xiaofei Li and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMembership(FrappeTestCase):
	
	def test_create_memebership(self):
		doc = frappe.get_doc({
			"doctype": "Gym Membership",
			"plan_name":"Test Membership Plan",
			"monthly_price":2.0,
			"annual_price":24.0

		}).insert()

	def test_delete_membership(self):
		frappe.delete_doc({
			"Gym Membership",
			"Test Membership Plan"
		})
