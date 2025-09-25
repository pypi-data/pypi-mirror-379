# ERPNext Korean Localisation

This Frappe app bundles the official Korean translations for ERPNext and ensures
that Korean is enabled for new sites managed by the ERPNext MCP stack. The app
ships the upstream `ko.csv` message catalog so the site remains fully
functional offline and receives updates together with the repository.

## Updating translations

Translations are sourced from the `version-15` branch of the official ERPNext
repository. To refresh the catalog, run the helper script under
`tools/scripts/update_korean_translations.sh` or fetch the latest `ko.csv`
manually and replace `erpnext_ko/locales/ko.csv`.

## Deployment

To install the localisation from PyPI inside the ERPNext containers, set
`ERPNEXT_CUSTOM_APPS=erpnext_ko=erpnext-ko` in your `.env` (already the default
in this repository). The configurator will download the published package and
install it for the site during bootstrap.

For local development against the checked-out source, drop the `=erpnext-ko`
suffix so the configurator uses the bind-mounted app directory instead.

