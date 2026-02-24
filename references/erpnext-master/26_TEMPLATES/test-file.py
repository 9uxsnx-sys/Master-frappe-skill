# ERPNext Test Template
# Place in: custom_app/tests/test_[doctype].py

import frappe
from frappe.tests.utils import FrappeTestCase


class TestCustomDocType(FrappeTestCase):
    """Test cases for Custom DocType"""
    
    def setUp(self):
        """Set up test data"""
        self.test_customer = "TEST-CUSTOMER-001"
        self.create_test_customer()
    
    def tearDown(self):
        """Clean up test data"""
        frappe.db.rollback()
    
    def create_test_customer(self):
        """Create test customer if not exists"""
        if not frappe.db.exists("Customer", self.test_customer):
            frappe.get_doc({
                "doctype": "Customer",
                "customer_name": self.test_customer,
                "customer_type": "Company",
                "customer_group": "All Customer Groups",
                "territory": "All Territories"
            }).insert()
    
    def test_create_document(self):
        """Test document creation"""
        doc = frappe.get_doc({
            "doctype": "Custom DocType",
            "custo
