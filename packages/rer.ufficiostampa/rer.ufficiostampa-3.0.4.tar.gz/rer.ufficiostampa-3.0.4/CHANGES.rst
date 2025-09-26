Changelog
=========

3.0.4 (2025-09-25)
------------------

- Add endpoints to manage personal channel subscriptions.
  [cekk]


3.0.3 (2025-09-22)
------------------

- Cleanup data from subscriptions csv import.
  [cekk]
- Add endpoints to manage personal channel subscriptions.
  [cekk]

3.0.2 (2025-09-19)
------------------

- Do not return Invito in @search-comunicati results.
  [cekk]


3.0.1 (2025-09-19)
------------------

- Fix token encodings in vocabularies.
  [cekk]

3.0.0 (2025-09-17)
------------------

- Revert to RER functionalities.
  [cekk]
- Add restapi endpoints to search old comunicati.
  [cekk]
- Set logo in control panel.
  [cekk]
- Add management links in object actions to be used in Volto.
  [cekk]
- Create a new CartellaStampa inside every new Comunicato.
  [cekk]
- Editors can see list of subscribers but cannot edit them.
  [cekk]
- Fix legislature behavior.
  [cekk]
- Customize basic behaviors for Comunicato and Invito.
  [cekk]
- Remove not maintained old-style browser views. Now it works only with restapi.
  [cekk]
- Comunicato and Invito text is now managed with BlocksField and limited with only slate block.
  [cekk]
- Flag that allow to automatically select all attachments by default in email form.
  [cekk]
- Flag that allow to recursive publish/unpublish all contents inside a Comunicato/Invito.
  [cekk]
- Allow to set max attachments size in control panel.
  [cekk]
- Improved history and subscribers management.
  [cekk]
- Handle status messages in history.
  [cekk]
  
2.0.2 (2025-05-12)
------------------

- Add error_message field in history data.
  [cekk]


2.0.1 (2025-03-03)
------------------

- Re-enable async send.
  [cekk]


2.0.0 (2025-03-03)
------------------

- Plone 6 compatibility. For Plone <= 5.2 use 1.x releases.
  [mamico]


1.6.7 (2024-09-19)
------------------

- Change Twitter with X in email templates.
  [cekk]


1.6.6 (2023-03-14)
------------------

- Do not send duplicated emails lowering all addresses before send.
  [cekk]


1.6.5 (2023-01-05)
------------------

- Add querystring modifiers for keyword indexes to prevent utf-8 errors.
  [cekk]


1.6.4 (2023-01-03)
------------------

- Index also text from contents.
  [cekk]


1.6.3 (2022-11-23)
------------------

- Read value of slave form fields from the querystring.
  [cekk]


1.6.2 (2022-11-03)
------------------

- Fix field logic.
  [cekk]
- Set proper value in legislature field.
  [cekk]

1.6.1 (2022-10-27)
------------------

- Fix README indentation.
  [cekk]

1.6.0 (2022-10-27)
------------------

- Handle master/select logic for Legislature and Arguments in search form.
  [cekk]

- Additional validations for subscribers import, also new behavior if invalid email/channels passed
  [foxtrot-dfm1]

1.5.1 (2022-06-06)
------------------

- Pass query to export-csv endpoint to export only selected subscribers.
  [cekk]


1.5.0 (2022-03-10)
------------------

- Add versioning for Comunicato and Invito.
  [cekk]
- Add solrpush behavior for additional fields.
  [cekk]

1.4.0 (2022-01-20)
------------------

- New search endpoint for comunicati (@search-comunicati). This is needed because new rer.sitesearch overrides @search endpoint and always search on SOLR.
  [cekk]


1.3.0 (2022-01-20)
------------------

- Normalize title and description on save.
  [cekk]
- Add effective date in Comunicato view.
  [cekk]

1.2.2 (2021-11-04)
------------------

- Arguments field is now required.
  [cekk]


1.2.1 (2021-09-16)
------------------

- Cleanup subject string before send, to remove strange characters.
  [cekk]


1.2.0 (2021-09-02)
------------------

- Cleanup channels (remove duplicated ones).
  [cekk]
- Refactor how to perform queries (to handle also unicode problems).
  [cekk]
- Accessibility fixes: modal focus trap + select keyboard events
  [nzambello]


1.1.0 (2021-08-05)
------------------

- Disallow add new items in *arguments* field.
  [cekk]
- Export in csv also title and number.
  [cekk]
- Correctly wrap search terms with "*'*" in it.
  [cekk]
- Customize social viewlets to fix title and description meta tags (and also add a light dependency with rer.agidtheme.base).
  [cekk]
- Add dependency to ftfy to better encode csv exports.
  [cekk]

1.0.1 (2021-07-09)
------------------

- Fix import for python2 and sort indexes.
  [cekk]


1.0.0 (2021-05-26)
------------------

- Initial release.
  [cekk]
