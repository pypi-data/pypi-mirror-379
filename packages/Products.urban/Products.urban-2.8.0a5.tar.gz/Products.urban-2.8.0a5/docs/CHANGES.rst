Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

2.8.0a5 (2025-09-23)
--------------------

New features:


- [WBoudabous]
  Add translation for the buildingType field in the housing procedure.
  Fix setuphandler to return the existing config folder instead of None. (URBBDC-3142)


2.8.0a4 (2025-09-22)
--------------------

New features:


- Use imio.pm.wsclient 2.x version (REST).
  [aduchene]
  Add `get_last_plonemeeting_date`, `get_last_college_date` and `get_last_college_date` to CODT_BaseBuildLicence.
  [aduchene]
  Refactor PloneMeeting WS methods to use imio.pm.wsclient 2.x version.
  [aduchene] (URB-3151)
- Add building procedure's
  [WBoudabous, aduchene] (URBBDC-3142)


2.8.0a3 (2025-08-27)
--------------------

New features:


- Added buildingType attribute to the housing procedure.
  [WBoudabous] (URBBDC-3221)
- Added buildingPart attribute to the housing procedure.
  [WBoudabous] (URBBDC-3222)
- Updated translations for workflow states in the housing procedure.
  [WBoudabous] (URBBDC-3229)


2.8.0a2 (2025-08-07)
--------------------

New features:


- Added a taxation field.
  [WBoudabous] (URBBDC-3223)


2.8.0a1 (2025-08-03)
--------------------

New features:


- Add translation for nonapplicable state in Division
  [jchandelle] (SUP-39760)
- Added merge fields for observation and Vocabulary events.
  Added merge fields for dimension.
  Deactivated the "Road Decree" licence type.
  [WBoudabous] (URBBDC-3218)
- Add nature of the building vocabulary.
  [WBoudabous] (URBBDC-3221)
- Add part of the building vocabulary.
  [WBoudabous] (URBBDC-3222)
- Remove the fields "usage", "policeTicketReference", and "referenceProsecution" from the Housing schema.
  [WBoudabous] (URBBDC-3224)
- Reorder fields description, use_bound_licence_infos in the housing shema.
  [WBoudabous] (URBBDC-3226)
- Updated the "inspection_context" field for the Housing procedure:
  Moved it to the "urban_inspection" schemata.
  Switched to a new dynamic vocabulary: "inspectioncontexts".
  [WBoudabous] (URBBDC-3227)
- Update housing workflow.
  [WBoudabous] (URBBDC-3229)


Bug fixes:


- Add RoadDecree to URBAN_TYPES to be able to use it in the tests.
  [aduchene] (URB-3293)


Internal:


- Black
  [mpeeters] (URBBDC-3142)


2.7.43 (2025-08-12)
-------------------

Bug fixes:


- Fix patrimony certificates interface
  [jchandelle] (SUP-46330)


2.7.42 (2025-07-08)
-------------------

New features:


- Add option to add complementary delay to task
  Add value for SPW cyberattack
  [jchandelle] (URB-3337)


Bug fixes:


- Revert: Add building procedure's
  [WBoudabous, aduchene] (URBBDC-3142)


2.7.41 (2025-06-18)
-------------------

New features:


- Add translation for nonapplicable state in Division
  [jchandelle] (SUP-39760)
- Add building procedure's
  [WBoudabous, aduchene] (URBBDC-3142)


2.7.40 (2025-06-10)
-------------------

Bug fixes:


- Revert "URB-3293 - Add RoadDecree to URBAN_TYPES (#340)"
  [mpeeters] (URB-3293)


2.7.39 (2025-06-07)
-------------------

New features:


- Add way to easily hide licence type
  [jchandelle] (SUP-33793)
- Change display of inquiry view
  [jchandelle] (SUP-44199)
- Add a message in case we can't link pod template
  [jchandelle] (SUP-44861)


Bug fixes:


- Fix history parcel view when missing capakey
  [jchandelle] (SUP-36370)
- Fix filename encoding in mail sending
  [jchandelle] (SUP-43946)
- Fix recipient import in inquiry event
  [jchandelle] (SUP-44583)
- Fix 220 viewlet house number encoding
  jchandelle (SUP-44642)
- Fix link pod template in import config
  [jchandelle] (SUP-44861)


2.7.38 (2025-05-27)
-------------------

New features:


- Add debug functionality for schedule task
  [mpeeters] (URB-3070)


Bug fixes:


- Add RoadDecree to URBAN_TYPES so it can be used in the tests.
  [aduchene] (URB-3293)


Internal:


- Move `urban.schedule.condition.deposit_past_20days` into urban.schedule package
  [mpeeters] (URB-3154)


2.7.37 (2025-04-29)
-------------------

Bug fixes:


- Fix encoding in mail send notification
  [jchandelle] (SUP-43917)


2.7.36 (2025-04-24)
-------------------

Bug fixes:


- Fix logging syntax error
  [jchandelle] (SUP-44123)
- Disable getProxy function behind a env var
  [jchandelle] (URB-3230)


2.7.35 (2025-04-03)
-------------------

New features:


- Add environment fieldset to every licence type
  Add habitation fieldset to `MiscDemand`, `PreliminaryNotice` and `ProjectMeeting`
  [daggelpop] (SUP-33774)
- Add message explaining how to format CSV for inquiry
  [jchandelle] (URB-2876)
- Move centrality in first position in the fieldset
  [daggelpop] (URB-3017)
- Add patrimony fieldset to multiple licence types
  [daggelpop] (URB-3121)
- Add stringinterp to get foldermanager email
  [jchandelle] (URB-3283)
- Add button to inquiry to get neighbors address
  [jchandelle] (URB-3286)


Bug fixes:


- Fix handling EnvironmentRubricTerm in import config
  [jchandelle] (URB-3296)


2.7.34 (2025-03-27)
-------------------

Bug fixes:


- Fix licence type condition in content rules
  [jchandelle] (SUP-43534)


2.7.33 (2025-03-27)
-------------------

Bug fixes:


- Fix event send mail notification title encoding
  [jchandelle] (SUP-43533)


2.7.32 (2025-03-24)
-------------------

Bug fixes:


- Fix view for fixing task uid and add possiblity to call on licence folder
  [jchandelle] (SUP-43189)


2.7.31 (2025-03-12)
-------------------

New features:


- Add possibility to get template merged when import
  [jchandelle] (SUP-39711)


Bug fixes:


- Ensure 'in_progress'state covers 'complete' and 'deposit' states in statistics calculation.
  [WBoudabous] (SUP-42045)
- Fix lost value in licence duplication
  [jchandelle] (SUP-42578)
- Clarify `Copy to claimant`
  [daggelpop] (SUP-42931)
- Add External method to fix annoncements tasks
  [jchandelle] (URB-2680)


Internal:


- Fix ViewPageTemplateFile import
  [jchandelle] (SUP-41619, URB-3237)


2.7.30 (2025-02-07)
-------------------

New features:


- Add utility view to fix task_config_UID on task
  [jchandelle] (SUP-41619)
- Add utils view to closed task depending filter
  [jchandelle] (URB-3237)
- Add reorder to event attachment
  [jchandelle] (URBBDC-1111)


Bug fixes:


- Fix external decision values
  [daggelpop]
  Handle default vocabulary values for a non-array field
  [daggelpop] (SUP-40288)
- Fix urban vocabularies following configuration order
  [WBoudabous] (SUP-41929)
- Add missing translation in schedule config
  [WBoudabous] (URB-3142)


2.7.29 (2025-02-04)
-------------------

Bug fixes:


- Fix encoding in error message for import csv from carto
  Fix logic and pattern for import csv from carto
  [jchandelle] (URB-3250)


2.7.28 (2025-02-02)
-------------------

Bug fixes:


- Fix missing indentation
  [jchandelle] (URB-3250)


2.7.27 (2025-01-31)
-------------------

New features:


- Add compatibility with csv from carto to inquiry event
  [jchandelle] (URB-3250)


Bug fixes:


- Fix sending zem document by mail
  [jchandelle] (SUP-40979)
- Revert "URB-3151 - imio.pm.wsclient 2.x + roaddecree (classic) (#258)"
  [daggelpop] (SUP-42300)


2.7.26 (2025-01-23)
-------------------

Bug fixes:


- Fix retrieval vocabulary in upgrade step
  [jchandelle] (URB-2680)


2.7.25 (2025-01-21)
-------------------

Bug fixes:


- Fix upgrade step
  [jchandelle] (URB-2680)


2.7.24 (2024-12-03)
-------------------

New features:


- Add merge field for rubric description
  [jchandelle] (SUP-38659)
- Create new trigger for decision date reindex
  [jchandelle] (URB-2366)
- Add bound licences field to patrimony certificates
  [daggelpop] (URB-3046)
- Add latest new vocabulary terms for form_composition
  [dmshd] (URB-3126)
- Use imio.pm.wsclient 2.x version (REST).
  [aduchene]
  Add `get_last_plonemeeting_date`, `get_last_college_date` and `get_last_college_date` to CODT_BaseBuildLicence.
  [aduchene] (URB-3151)
- Implement `.getSecondDeposit()`
  [dmshd] (URB-3152)
- Remove permission to create integrated licences
  [daggelpop] (URB-3165)


Bug fixes:


- Allow corporate tenant in inspections
  [daggelpop] (SUP-33621)
- Fix follup event creation in ticket
  [jchandelle] (SUP-36493)
- Fix missing getLastAcknowledgment for division
  [jchandelle] (SUP-37911)
- Add centrality to every licence & make it a multiselect
  [daggelpop] (URB-3017)
- Add patrimony fieldset to patrimony certificate
  [daggelpop]
  Migrate patrimony certificates to their correct object class (instead of misc demand)
  [daggelpop] (URB-3121)


2.7.23 (2024-11-15)
-------------------

Bug fixes:


- Fix frozen_suspension state
  [jchandelle] (SUP-39511)
- Fix Task config
  [jchandelle] (URB-2680)
- Fix existing c13 title upgrade
  [daggelpop] (URB-3090)
- Fix import pod templates
  [jchandelle] (URB-3190)


2.7.22 (2024-10-25)
-------------------

New features:


- Add new condition in content rules for licence type
  [jchandelle] (URB-3020)
- Add banner on top of event after mail send
  [jchandelle] (URB-3204)


Bug fixes:


- Fix comment retrieval in transition form
  [daggelpop] (SUP-35563)
- Fix address comparison in _areSameAdresses
  [dmshd] (SUP-39098)
- Fix an issue when there was too many connection open that raised a SQLAlchemy error
  [laulaz] (SUP-39919)
- Fix content rules for event type
  [jchandelle] (SUP-40117)
- Translate `suspension` terms in French
  [daggelpop] (URB-3007)
- Fix opinion condition text
  [jchandelle] (URB-3020)
- Fix missing function to have multiple inquiry on CODT commercial licence
  [jchandelle] (URB-3130)
- Fix export import des config
  [jchandelle] (URB-3190)


2.7.21 (2024-10-09)
-------------------

Bug fixes:


- Handle null value in `EventTypeConditionExecutor`
  [daggelpop] (SUP-39901)
- Translate `suspend` in French
  [daggelpop] (URB-3007)
- Update content rule title
  [dmshd] (URB-3198)


2.7.19 (2024-10-04)
-------------------

Bug fixes:


- Fix getInquiryRadius method
  [jchandelle] (URB-2983)


2.7.18 (2024-10-04)
-------------------

New features:


- Add translation and add contextual title to the form from send email action
  [jchandelle] (URB-3020)


Bug fixes:


- Fix missing extending validity date
  [jchandelle] (URB-3153)


Internal:


- Add a new field "additional reference" and configure faceteed navigation
  [fngaha] (URB-2595)
- improve the functionality of searching for owners within a defined radius.
  [fngaha] (URB-2983)


2.7.17 (2024-10-01)
-------------------

New features:


- Translate all untranslated & empty msgtr

  While working on URB-2503 and while I was there, I took the opportunity to translate all untranslated and empty msgtr in the urban.po file. [dmshd] (URB-2503-Fill_all_untranslated_msgtr)
- Replace None occurences by "Aucun(e)"

  I replaced all "None" occurences and set "Aucun(e)" as the default value for translations instead of None or "-" for improved readability / accessibility / ux.

  [dmshd] · URB-2503 (URB-2503-Replace_None_by_Aucun-e)
- Improve / translate "See more..." link text

  I had to translate "See more..." and decided that "Lire les textes" would be a better translation for better readability and accessibility.
  The context is a link that follows "Textes du point Délib: See more...".
  Now it reads "Textes du point Délib: Lire les textes".

  [dmshd] · URB-2503 (URB-2503-Replace_See_more_dotdotdot_link_by_Lire_les_textes)
- Improve truncated "Voir..." link text

  While I had to translate the untranslated "See more..." link. I spotted that truncated long text had "Voir..." as a link text. I replaced it with "Lire la suite" for better readability and accessibility.

  [dmshd] · URB-2503 (URB-2503-Replace_Voir_plus_dotdotdot_by_Lire_la_suite)
- Add centrality to commercial licence
  [daggelpop] (URB-3017)
- Add 3 surface fields to commercial licence
  [daggelpop] (URB-3117)
- Add field `D.67 CoPat` to patrimony fieldset
  daggelpop (URB-3167)


Bug fixes:


- Fix merge field getStreetAndNumber
  [jchandelle] (SUP-38082)
- Fix mail message encoding
  [jchandelle] (SUP-39227)
- Fix space causing bug
  [dmshd] (URB-2676)
- Fix typo in french translation

  This is a bugfix for URB-3128. "Cessastion" -> "Cessation".

  [dmshd] (URB-3128-Fix_typo_in_french_translation)
- Fix event_type condition for content rules
  [jchandelle] (URB-3182)


Internal:


- Set buildout cache directories.

  I had a network problem and I had to rerun from the beginning. Took a long time. I searched for a way to fasten and discovered that I could set the cache directories. I set the cache directories as the iA.Delib team does it at iMio.

  [dmshd] (URB-3135-define_buildout_cache_directories)
- Ignore .python-version (pyenv file) and sort lines in .gitignore file.
  [dmshd] (URB-3135-ignore-python-version-file-and-sort-lines)


2.7.16 (2024-07-25)
-------------------

Bug fixes:


- Fix faceted widget id collision
  [daggelpop] (URB-3090)


2.7.15 (2024-07-05)
-------------------

New features:


- Add rule action for sending mail with attachments
  Add rule condition for corresponding event type and opinion to ask
  Add action for sending mail from event context with document in attachement
  [jchandelle] (URB-3020)
- Change limit year of date widget to current year + 25
  [jchandelle] (URB-3153)


Bug fixes:


- Fix getValidityDate indexation
  [jchandelle]
  Fix validity filter title
  [jchandelle] (URB-3090)
- Give dynamic group reader roles for obsolete licences
  [daggelpop] (URB-3131)


2.7.14 (2024-06-27)
-------------------

New features:


- Adapt vocabulary default config values for 2024 CODT reform
  [daggelpop] (URB-3003)
- Add frozen state
  [jchandelle] (URB-3007)
- Allow linking to patrimony certificates
  [daggelpop] (URB-3063)
- Add validity date filter and index
  [jchandelle] (URB-3090)
- Add new terms to foldercategories vocabulary
  [daggelpop] (URB-3096)
- Rename Patrimony certificate
  [daggelpop] (URB-3116)
- Add `get_bound_licences` and `get_bound_patrimonies` to CODT_BaseBuildLicence
  [daggelpop] (URB-3125)


Bug fixes:


- Mark PatrimonyCertificate as allowed type for bound_licences field in CODT build licences
  [daggelpop] (URB-3046)


2.7.13 (2024-05-28)
-------------------

New features:


- Add external method to add back deleted licence folder
  [jchandelle] (URB-3086)


Bug fixes:


- Fix unicode error on street name merge field
  [fngaha] (SUP-34184)
- Avoid to display disabled vocabulary entries with no start or end validity date
  [mpeeters] (SUP-36742)
- Fix error at EnvClassBordering creation
  [jchandelle] (URB-3108)


2.7.12 (2024-04-25)
-------------------

Bug fixes:


- Fix wrong files export
  [jchandelle] (MURBMONA-48)


2.7.11 (2024-04-25)
-------------------

Bug fixes:


- Add event sub file in export content
  Add missing portal_type to export sub content
  [jchandelle] (MURBMONA-48)


Internal:


- Add `withtitle` parameter to the getApplicantsSignaletic method
  [fngaha] (SUP-33759)
- Improve merge fields
  Provide a merge field that only returns streets
  Adapt the getStreetAndNumber method field to be able to receive a separation parameter between the street and the number
  [fngaha] (SUP-34184)
- Update the translation of empty fields
  [fngaha] (URB-3079)


2.7.10 (2024-04-10)
-------------------

New features:


- Add view for import urban config
  [jchandelle] (SUP-36419)


2.7.9 (2024-04-07)
------------------

Bug fixes:


- Avoid an error if a vocabulary term was removed
  [mpeeters] (SUP-36403,SUP-36406)
- Fix logic on some methods to exclude invalid vocabulary entries
  [mpeeters] (URB-3002)


Internal:


- Add tests for new vocabulary logic (start and end validity)
  [mpeeters] (URB-3002)


2.7.8 (2024-04-02)
------------------

Bug fixes:


- Add `state` optional parameter to `getLastAcknowledgment` method to fix an issue with schedule start date
  [mpeeters] (SUP-36274)
- Avoid an error if an advice was not defined
  [mpeeters] (SUP-36276)


2.7.7 (2024-04-01)
------------------

Bug fixes:


- Fix an error in calculation of prorogated delays
  [mpeeters] (URB-3008)


Internal:


- Add tests for buildlicence and CU2 completion schedule
  [mpeeters] (URB-3005)


2.7.6 (2024-03-25)
------------------

Bug fixes:


- Fix an issue with upgrade step numbers
  [mpeeters] (URB-3002)


2.7.5 (2024-03-24)
------------------

New features:


- Add caduc workflow state
  [jchandelle] (URB-3007)
- Add `getIntentionToSubmitAmendedPlans` method for documents
  [mpeeters] (URB-3008)
- Add a link field on CODT build licences
  [mpeeters] (URB-3046)


Bug fixes:


- Move methods to be available for every events.
  Change `is_CODT2024` to be true if there is no deposit but current date is greater than 2024-03-31.
  [mpeeters] (URB-3008)


2.7.4 (2024-03-20)
------------------

Bug fixes:


- Invert Refer FD delay 30 <-> 40 days
  [mpeeters] (URB-3008)


2.7.3 (2024-03-20)
------------------

New features:


- Add `is_not_CODT2024` method that can be used in templates
  [mpeeters] (URB-3008)


Bug fixes:


- Fix update of vocabularies
  [mpeeters] (URB-3002)


2.7.2 (2024-03-18)
------------------

New features:


- Add `getCompletenessDelay`, `getReferFDDelay` and `getFDAdviceDelay` methods that can be used in templates
  [mpeeters] (URB-3008)


2.7.1 (2024-03-14)
------------------

Bug fixes:


- Fix delay vocabularies value order
  [mpeeters] (URB-3003)


2.7.0 (2024-03-14)
------------------

New features:


- Add `is_CODT2024` and `getProrogationDelay` methods that can be used in template
  [mpeeters] (URB-2956)
- Adapt vocabulary logic to include start and end validity dates
  [mpeeters] (URB-3002)
- Adapt vocabulary terms for 2024 CODT reform
  [daggelpop] (URB-3003)
- Add `urban.schedule` dependency
  [mpeeters] (URB-3005)
- Add event fields `videoConferenceDate`, `validityEndDate` & marker `IIntentionToSubmitAmendedPlans`
  [daggelpop] (URB-3006)


Bug fixes:


- Avoid an error if the closing state is not a valid transition
  [mpeeters] (SUP-35736)


Internal:


- Provided prorogation field for environment license
  [fngaha] (URB-2924)
- Update applicant mailing codes :
  Replace mailed_data.getPersonTitleValue(short=True), mailed_data.name1, mailed_data.name2 by mailed_data.getSignaletic()
  [fngaha] (URB-2947)


2.6.25 (2024-02-13)
-------------------

Bug fixes:


- Fix an issue with installation through collective.bigbang
  [mpeeters] (URB-3016)


2.6.24 (2024-02-13)
-------------------

Bug fixes:


- Add upgrade step to reindex uid catalog
  [jchandelle] (URB-3015)


2.6.23 (2024-02-09)
-------------------

Bug fixes:


- Fix reference validator for similar ref
  [jchandelle] (URB-3012)


2.6.22 (2024-02-05)
-------------------

New features:


- Add index for street code
  [jchandelle] (MURBFMAA-20)


2.6.21 (2023-12-26)
-------------------

New features:


- Add prosecution ref and ticket ref to Inspection
  [ndemonte] (SUP-27127)
- Underline close due dates
  [ndemonte] (URB-2515)
- Add stop worksite option to inspection report
  [jchandelle] (URB-2827)
- Remove reference FD field from preliminary notice
  [jchandelle] (URB-2831)


Bug fixes:


- Validate CSV before claimant import
  [daggelpop] (SUP-33538)
- Fix an issue with Postgis `ST_MemUnion` by using `ST_Union` instead that also improve performances
  [mpeeters] (SUP-34226)
- Fix integrated licence creation by using unicode for regional authorities vocabulary
  [jchandelle] (URB-2869)


2.6.20 (2023-12-12)
-------------------

Bug fixes:


- Fix street number with specia character in unicode
  [jchandelle] (URB-2948)


2.6.19 (2023-12-04)
-------------------

Bug fixes:


- Fix an issue with Products.ZCTextIndex that was interpreting `NOT` as token instead of a word for notary letter references
  [mpeeters] (MURBARLA-25)


2.6.18 (2023-11-23)
-------------------

Bug fixes:


- Add `fix_schedule_config` external method ta fix class of condition objects
  [mpeeters] (SUP-33739)


2.6.17 (2023-11-16)
-------------------

Bug fixes:


- Adapt opinion request worklflow to bypass guard check for managers
  [mpeeters] (SUP-33308)


Internal:


- Provide getFirstAcknowledgment method
  [fngaha] (SUP-32215)


2.6.16 (2023-11-06)
-------------------

Bug fixes:


- Fix serializer to include disable street in uid resolver
  [jchandelle] (MURBMSGA-37)
- Fix street search to include disable street
  [jchandelle] (URB-2696)


2.6.15 (2023-10-12)
-------------------

Internal:


- Fix tests
  [mpeeters] (URB-2855)
- Improve performances for add views
  [mpeeters] (URB-2903)


2.6.14 (2023-09-13)
-------------------

Bug fixes:


- Avoid an error if a vocabulary value was removed, instead log the removed value and display the key to the user
  [mpeeters] (SUP-32338)


Internal:


- Reduce logging for sql queries
  [mpeeters] (URB-2788)
- Fix tests
  [mpeeters] (URB-2855)


2.6.13 (2023-09-05)
-------------------

Bug fixes:


- Move catalog import in urban type profile
  [jchandelle] (URB-2868)
- Fix facet config xml
  [jchandelle] (URB-2870)


2.6.12 (2023-09-01)
-------------------

Bug fixes:


- Fix new urban instance install
  [jchandelle] (URB-2868)
- Fix facet xml configuration
  [jchandelle] (URB-2870)


2.6.11 (2023-08-29)
-------------------

Bug fixes:


- Fix icon tag in table
  [jchandelle] (SUP-31983)


2.6.10 (2023-08-28)
-------------------

Bug fixes:


- Avoid an error if a task was not correctly removed from catalog
  [mpeeters] (URB-2873)


2.6.9 (2023-08-27)
------------------

Bug fixes:


- Fix UnicodeDecodeError on getFolderManagersSignaletic(withGrade=True)
  [fngaha] (URB-2871)


2.6.8 (2023-08-24)
------------------

Bug fixes:


- fix select2 widget on folder manager
  [jchandelle] (SUP-31898)
- Fix opinion schedules assigned user column
  [mpeeters] (URB-2819)


2.6.7 (2023-08-14)
------------------

Bug fixes:


- Hide old document generation links viewlet
  [mpeeters] (URB-2864)


2.6.6 (2023-08-10)
------------------

Bug fixes:


- Fix an issue with autocomplete view results format that was generating javascript errors
  [mpeeters] (SUP-31682)


2.6.5 (2023-07-27)
------------------

Bug fixes:


- Avoid errors on inexpected values on licences and log them
  [mpeeters] (SUP-31554)
- Fix translation for road adaptation vocabulary values
  [mpeeters] (URB-2575)
- Avoid an error if a vocabulary does not exist, this can happen when multiple upgrade steps interract with vocabularies
  [mpeeters] (URB-2835)


2.6.4 (2023-07-24)
------------------

New features:


- Add parameter to autocomplete to search with exact match
  [jchandelle] (URB-2696)


Bug fixes:


- Fix an issue with some urban instances with lists that contains empty strings or `None`
  [mpeeters] (URB-2575)
- Fix inspection title
  [jchandelle] (URB-2830)
- Add an external method to set profile version for Products.urban
  [mpeeters] (URB-2835)


2.6.3 (2023-07-18)
------------------

- Add missing translations [URB-2823]
  [mpeeters, anagant]

- Fix different type of vocabulary [URB-2575]
  [jchandelle]

- Change NN field position [SUP-27165]
  [jchandelle]

- Add Couple to Preliminary Notice [URB-2824]
  [ndemonte]

- Fix Select2 view display [URB-2575]
  [jchandelle]

- Provide getLastAcknowledgment method for all urbancertificates [SUP-30852]
  [fngaha]

- Fix encoding error [URB-2805]
  [fngaha]

- Add a explicit dependency to collective.exportimport
  [mpeeters]

- Cadastral historic memory error [SUP-30310]
  [sdelcourt]

- Add option to POST endpoint when creating a licence to disable check ref format [SUP-31043]
  [jchandelle]


2.6.2 (2023-07-04)
------------------

- Explicitly include `urban.restapi` zcml dependency [URB-2790]
  [mpeeters]


2.6.1 (2023-07-04)
------------------

- Fix zcml for migrations
  [mpeeters]


2.6.0 (2023-07-03)
------------------

- Fix `hidealloption` and `hide_category` parameters for dashboard collections
  [mpeeters]

- Fix render of columns with escape parameter
  [mpeeters, sdelcourt]

- Avoid a traceback if an UID was not found for inquiry cron [URB-2721]
  [mpeeters]

- Migrate to the latest version of `imio.dashboard`
  [mpeeters]


2.5.4 (2023-07-03)
------------------

- Change collection column name [URB-1537]
  [jchandelle]

- Fix class name in external method fix_labruyere_envclassthrees [SUP-29587]
  [ndemonte]


2.5.3 (2023-06-23)
------------------

- Add parcel and applicants contents to export content [URB-2733]
  [jchandelle]


2.5.2 (2023-06-15)
------------------

- Fix tests and update package metadata
  [sdelcourt, mpeeters]

- Add CSV import of recipients to an inquiry [URB-2573]
  [ndemonte]

- Fix bound licence allowed type [SUP-27062]
  [jchandelle]

- Add vat field to notary [SUP-29450]
  [jchandelle]

- Change MultiSelectionWidget to MultiSelect2Widget [URB-2575]
  [jchandelle]

- Add fields to legal aspect of generic licence [SUP-22944]
  [jchandelle]

- Add national register number to corporation form [SUP-27165]
  [jchandelle]

- Add an external method to update task delay [SUP-28870]
  [jchandelle]

- Add external method to fix broken environmental declarations [SUP-29587]
  [ndemonte]

- Fix export data with c.exportimport [URB-2733]
  [jchandelle]


2.5.1 (2023-04-06)
------------------

- Added 'retired' transition to 'deposit' and 'incomplete' states for codt_buildlicence_workflow
  [fngaha]

- Manage the display of licences linked to several applicants
  [fngaha]

- Add an import step to activate 'announcementArticlesText' optional field
  [fngaha]

- Fix external method [SUP-28740]
  [jchandelle]

- Add external method for fixing corrupted description. [SUP-28740]
  [jchandelle]

- Allow to encode dates going back to 1930
  [fngaha]

- Update MailingPersistentDocumentGenerationView call with generated_doc_title param. [URB-1862]
  [jjaumotte]

- Fix 0 values Bis & Puissance format for get_parcels [SUP-16626]
  [jjaumotte]

- Fix 0 values Bis & Puissance format for getPortionOutText
  [jjaumotte]

- Remove 'provincial' in folderroadtypes vocabulary [URB-2129]
  [jjaumotte]

- Remove locality name in default text [URB-2124]
  [jjaumotte]

- Remove/disable natura2000 folderzone [URB-2052]
  [jjaumotte]

- Add notaries mailing [URB-2110]
  [jjaumotte]

- Add copy to claymant action for recipient_cadastre in inquiry event
  [sdelcourt / jjaumotte]

- Fix liste_220 title encoding error + translation [SUP-15084]
  [jjaumotte]

- provides organizations to consult based on external directions
  [fngaha]

- Add an Ultimate date field in the list of activatable fields
  [fngaha]

- provide the add company feature to the CU1 process
  [fngaha]

- Update documentation with cadastre downloading
  [fngaha]

- Translate liste_220 errors
  [fngaha]

- Provide the add company feature to the CU1 process
  [fngaha]

- Improve mailing. Add the possibility to delay mailing during the night [SUP-12289]
  [sdelcourt]

- Fix default schedule config for CODT Buildlicence [SUP-12344]
  [sdelcourt]

- Allow shortcut transition to 'inacceptable' state for CODT licence wofklow. [SUP-6385]
  [sdelcourt]

- Set default foldermanagers view to sort the folder with z3c.table on title [URB-1151]
  [jjaumotte]

- Add some applicants infos on urban_description schemata. [URB-1171]
  [jjaumotte]

- Improve default reference expression for licence references. [URB-2046]
  [sdelcourt]

- Add search filter on public config folders (geometricians, notaries, architects, parcellings). [SUP-10537]
  [sdelcourt]

- Migrate PortionOut (Archetype) type to Parcel (dexterity) type. [URB-2009]
  [sdelcourt]

- Fix add permissions for Inquiries. [SUP-13679]
  [sdelcourt]

- Add custom division 99999 for unreferenced parcels. [SUP-13835]
  [sdelcourt]

- Migrate ParcellingTerm (Archetype) type to Parcelling (dexterity) type.
  [sdelcourt]

- Pre-check all manageable licences for foldermanager creation. [URB-1935]
  [jjaumotte]

- Add field to define final states closing all the urban events on a licence. [URB-2082]
  [sdelcourt]

- Refactor key date display to include urban event custom titles. [SUP-13982]
  [sdelcourt]

- Add Basebuildlicence reference field reprensentativeContacts + tests [URB-2335]
  [jjaumotte]

- Licences can created as a copy of another licence (fields, applicants and parcels can be copied). [URB-1934]
  [sdelcourt]

- Add collective.quickupload to do multiple file upload on licences and events.
  [sdelcourt]

- Fix empty value display on select fields. [URB-2073]
  [sdelcourt]

- Add new value 'simple procedure' for CODT BuildLicence procedure choice. [SUP-6566]
  [sdelcourt]

- Allow multiple parcel add from the 'search parcel' view. [URB-2126]
  [sdelcourt]

- Complete codt buildlicence config with 'college repport' event. [URB-2074]
  [sdelcourt]

- Complete codt buildlicence schedule.
  [sdelcourt]

- Add default codt notary letters schedule.
  [sdelcourt]

- Add parking infos fields on road tab.
  [sdelcourt]

- Remove pod templates styles form urban. [URB-2080]
  [sdelcourt]

- Add authority default values to CODT_integrated_licence, CODT_unique_licence, EnvClassBordering. [URB-2269]
  [mdhyne]

- Add default person title when creating applicant from a parcel search. [URB-2227]
  [mdhyne]
  [sdelcourt]

- Update vocabularies CODT Build Licence (folder categories, missing parts)
  [lmertens]

- Add dashboard template 'listing permis'
  [lmertens]

- Add translations [URB-1997]
  [mdhyne]

-add boolean field 'isModificationParceloutLicence'. [URB-2250]
  [mdhyne]

- Add logo urban to the tab, overriding the favicon.ico viewlet. [URB-2209]
  [mdhyne]

- Add all applicants to licence title. [URB-2298]
  [mdhyne]

- Add mailing loop for geometricians. [URB-2327]
  [mdhyne]

- Add parcel address to parcel's identity card.[SUP-20438]
  [mdhyne]

- Adapt ComputeInquiryDelay for EnvClassOne licences and Announcements events.[SUP20443]
  [mdhyne]

- Include parcels owners partner in cadastral queries.[SUP-20092]
  [sdelcourt]

- Add fields trail, watercourse, trailDetails, watercourseCategory and add vocabulary in global config for the fields.[MURBECAA-51]
  [mdhyne]

- To use 50m radius in announcement : changes setLinkedInquiry getAllInquiries() call by getAllInquiriesAndAnnouncements() and changes condition in template urbaneventinquiryview.pt. [MURBWANAA-23]
  [mdhyne]

- add new 'other' tax vocabulary entry and new linked TextField taxDetails
  [jjaumotte]

- Add contact couples.
  [sdelcourt]

2.4 (2019-03-25)
----------------
- add tax field in GenericLicence
  [fngaha]

- add communalReference field in ParcellingTerm
  [fngaha]

- Fix format_date
  [fngaha]

- Update getLimitDate
  [fngaha]

- Fix translations
- Update the mailing merge fields in all the mailing templates
  [fngaha]

- Specify at installation the mailing source of the models that can be mailed via the context variable
  [fngaha]

- Select at the installation the mailing template in all models succeptible to be mailed
  [fngaha]

- Referencing the mailing template in the general templates configuration (urban and environment)
  [fngaha]

- Allow content type 'MailingLoopTemplate' in general templates
  [fngaha]

- added the mailing template
  [fngaha]

- add mailing_list method
  [fngaha]

- add a z3c.table column for mailing with his icon
  [fngaha]

- fix translations
  [fngaha]

- update signaletic for corporation's applicant
  [fngaha]

- fix the creation of an applicant from a parcel
  [fngaha]

- add generic "Permis Publics" templates and linked event configuration
  [jjaumotte]

- add generic "Notary Letters" template and linked event configuration
  [jjaumotte]

- fix advanced searching Applicant field for all licences, and not just 'all'
  [jjaumotte]

2.3.0
-----
- Add attributes SCT, sctDetails
  [fngaha]

- Add translations for SCT, sctDetails
  [fngaha]

- Add vocabularies configuration for SCT
  [fngaha]

- Add migration source code
  [fngaha]

2.3.x (unreleased)
-------------------
- Update MultipleContactCSV methods with an optional number_street_inverted (#17811)
  [jjaumotte]

1.11.1 (unknown release date)
-----------------------------
- add query_parcels_in_radius method to view
  [fngaha]

- add get_work_location method to view
  [fngaha]

- add gsm field in contact
  [fngaha]

- improve removeItems utils
  [fngaha]

- Refactor rename natura2000 field because of conflict name in thee
  [fngaha]

- Refactor getFirstAdministrativeSfolderManager to getFirstGradeIdSfolderManager
  The goal is to use one method to get any ids
  [fngaha]

- Add generic SEVESO optional fields
  [fngaha]

- Fix concentratedRunoffSRisk and details optional fields
  [fngaha]

- Add getFirstAdministrativeSfolderManager method
  [fngaha]

- Add removeItems utils and listSolicitOpinionsTo method
  [fngaha]

- Add getFirstDeposit and _getFirstEvent method
  [fngaha]

- remove the character 'à' in the address signaletic
  [fngaha]

- use RichWidget for 'missingPartsDetails', 'roadMissingPartsDetails', 'locationMissingPartsDetails'
  [fngaha]

- Fix local workday's method"
  [fngaha]

- Add a workday method from collective.delaycalculator
  refactor getUrbanEvents by adding UrbanEventOpinionRequest
  rename getUrbanEventOpinionRequest to getUrbanEvent
  rename containsUrbanEventOpinionRequest to containsUrbanEvent
  [fngaha]

- Add methods
  getUrbanEventOpinionRequests
  getUrbanEventOpinionRequest
  containsUrbanEventOpinionRequest
  [fngaha]

- Update askFD() method
  [fngaha]

- Add generic Natura2000 optional fields
  [fngaha]

- Fix codec in getMultipleClaimantsCSV (when use a claimant contat)
  [fngaha]

- Add generic concentratedRunoffSRisk and details optional fields
  [fngaha]

- Add generic karstConstraint field and details optional fields
  [fngaha]


1.11.0 (2015-10-01)
-------------------

- Nothing changed yet.


1.10.0 (2015-02-24)
-------------------

- Can add attachments directly on the licence (#10351).


1.9.0 (2015-02-17)
------------------

- Add environment licence class two.

- Use extra value for person title signaletic in mail address.


1.8.0 (2015-02-16)
------------------

- Add environment licence class one.

- Bug fix: config folder are not allowed anymore to be selected as values
  for the field 'additionalLegalConditions'.


1.7.0
-----

- Add optional field RGBSR.

- Add field "deposit type" for UrbanEvent (#10263).


1.6.0
-----

- Use sphinx to generate documentation

- Add field "Périmètre de Rénovation urbaine"

- Add field "Périmètre de Revitalisation urbaine"

- Add field "Zones de bruit de l'aéroport"


1.5.0
-----

- Update rubrics and integral/sectorial conditions vocabularies


1.4.0
-----

- Add schedule view


1.3.0
-----

- Use plonetheme.imioapps as theme rather than urbasnkin

- Add fields "pm Title" and "pm Description" on urban events to map the fields "Title"
  and "Description" on plonemeeting items (#7147).

- Add a richer context for python expression in urbanEvent default text.

- Factorise all licence views through a new generic, extendable and customisable view (#6942).
  The fields display order is now given by the licence class schemata and thus this order
  is always consistent between the edit form and the view form.


1.2.0
------

- Added search on parcel Historic and fixed search on old parcels (#6681).


1.1.9
-----

- Opinion request fields are now active for MiscDemand licences (#5933).

- Added custom view for urban config and licence configs (#5892).

- Fixed urban formtabbing for plone 4.2.5 (#6423).

- Python expression can now be used in urbanEvent default text (#6406).

- "Deliberation college" documents are now disabled when using pm.wsclient (#6407).

- Added configuration step for pm.wsclient (#6400).

- Added rubrics and conditions config values for environment procedures (#5027).

- Fixed search on parcel historic (#6681).

- Added popup to see all licences related to a parcel historic (#5858).

- Generate mailing lists from contacts folder (architects, notaries, geometrcicians) (#6378).

- Adds pm.wsclient dependency.


1.1.8
-----

- Converted all urban listings into z3c tables.

- Simplified the opinion request configuration system (#5711).

- Added more columns on search result listing (#5535).

- Vocabulary term now have a the possibility to have a custom numbering that will only be displayed in forms but
  not in generated documents (#5408).

- An alternative name of divisions can be configured for generated documents (#5507).

- Address names of mailing documents can now be inverted (#4763).

- [bugfix] Create the correct link for UrbanDoc in the urban events when the licence is not
  in 'edit' state anymore.


1.1.7
-----

- Added options bar to licences listing (#5476, #5250).

- Use events rather than archetype built-in default method system to fill licence fields with default values
  because of performance issues (#5423).

- Parcels can be added on ParcellingTerm objects. Now, parcellingterm objects can be found by parcel references (#5537).

- A helper popup is now available on specific features datagrid to edit related fields without navigating through the
  edit form (#5576).

- Default text can be defined for urban event text fields as well (#5508).

bugfixes:
- Folder search by parcel reference is now working with lowercase inputs.


1.1.6
-----

- Added field Transparence on class Layer (#5197).

- Added style 'UrbanAdress' used to customize style in the adress field of documents (#4764).

- Added beta version of licence type 'Environmental Declaration'.

- Use an autocomplete for the licence search by street (#5163).

- Text of the specificFeatures fields are now editable within a licence (CU1, CU2, notaryletter) (#5280).

- Added an optional field 'architects' on MiscDemand class (#5286).

- Added field 'represented by society' on applicant/proprietary (#5282).

- Now, the licence search works with old parcels references and also works with incomplete parcels references as well (#5099).

- Urban editors can now add parcels manually (#5285).

- Added validator on reference field to check that each reference is unique (#5430).

- Show historic of old parcels on licences "map" tab and allow to show the location of their "children" (#4754).

- Urban editors can now add parcel owner manually on inquiry events (#5289).

- Added search by "folder reference" in urban folder search (#4878).

- Licences tabs can be renamed and reordered (#5465).

bugfixes:
- UrbanEvent view doesnt crash anymore when a wrong TAL condition is defined on an UrbanDoc.
- corrected template "accuse de reception d'une reclamation" (#5168, #5198).
- corrected the display of the specificFeatures for notary letters.
- The "50m area" used in inquiries doesnt crash anymore when finding parcel owner without address (#5376).
- Added warning on inquiry event when parcel owners without adress are found (#5289).
