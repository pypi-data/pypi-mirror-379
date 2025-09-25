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
