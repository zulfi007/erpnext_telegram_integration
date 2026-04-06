import frappe


def execute():
	doctypes_to_remove = (
		"Telegram Notification",
		"Telegram User Settings",
		"Telegram Settings",
		"Date Notification",
		"Date Fields",
		"Extra Notification Log",
	)

	for doctype in doctypes_to_remove:
		# Remove the DocType record from metadata
		frappe.delete_doc_if_exists("DocType", doctype)

		# Also drop the actual MySQL table directly as a safety measure
		if frappe.db.table_exists(doctype):
			frappe.db.sql(f"DROP TABLE IF EXISTS `tab{doctype}`")

	frappe.delete_doc_if_exists("Module Def", "Extra Notifications")
