from __future__ import annotations

import frappe
from frappe.translate import clear_cache

LANG_CODE = "ko"
LANG_NAME = "Korean"


def _ensure_language() -> None:
    language = frappe.db.exists("Language", {"code": LANG_CODE})
    if not language:
        doc = frappe.get_doc(
            {
                "doctype": "Language",
                "language_name": LANG_NAME,
                "code": LANG_CODE,
                "enabled": 1,
                "direction": "ltr",
            }
        )
        doc.insert(ignore_permissions=True)
    else:
        frappe.db.set_value("Language", language, "enabled", 1, update_modified=False)


def _sync_translations() -> None:
    clear_cache()


def after_install() -> None:
    _ensure_language()
    _sync_translations()


def after_migrate() -> None:
    _ensure_language()
    _sync_translations()
