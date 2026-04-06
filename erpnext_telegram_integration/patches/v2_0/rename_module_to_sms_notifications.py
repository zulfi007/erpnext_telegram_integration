import frappe


def execute():
	if frappe.db.exists("Module Def", "Erpnext Telegram Integration"):
		frappe.rename_doc("Module Def", "Erpnext Telegram Integration", "SMS Notifications", force=True)
