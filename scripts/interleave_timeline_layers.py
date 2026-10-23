#!/usr/bin/env python3
"""
Interleave Multi-Track Research Layers into Municipal Communications Timeline.
Enriches timeline.html with comprehensive forensic research entries across 6 dimensions:
1. Foreclosure & Title History (12054 Chapin Court certified foreclosure record, ORCP 71 packet)
2. Turning Leaf & ZBS Network (TLH entity portfolio, Tracey Baron research, ZBS Law network, fellow homeowners Layne, Dysinger, Nguyen)
3. Vetted Comparators (Kelvin & Dunlap, Burgard ADA, Nicita fee waiver, McLoughlin Promenade, Clackamas Community College sewer relief, $1k fine hike)
4. Municipal Code & Penalty Architecture (OCMC amendments, Bancroft lien monetization, Title 1 code stacking)
5. Public Intelligence & ADA Hypocrisy (Webb admissions, Disability Pride proclamations vs shutoff, FOIA zero-policy audit)
6. Environmental Microclimate & RAC Rulemaking (Landsat +12°F heat island, Platting root conflicts, DLCD OAR 660-047 public comments)

Maintains the pristine 98 lived communications as 'Lived Communications (98)'.
NO HORIZONTAL RULE DIVIDERS (---) PER USER FORMATTING PREFERENCE.
"""

import os
import re
import json

TIMELINE_PATH = '/home/annika/ExecutiveFunctionOS_Web/timeline.html'
BACKUP_PATH = '/home/annika/ExecutiveFunctionOS_Web/timeline.html.bak'

NEW_ENTRIES = [
    # ==========================================
    # PHASE 0: HISTORICAL FOUNDATION (1994-2022)
    # ==========================================
    {
        "id": "hist-0-1",
        "item_num": "0.1",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "1994 – October 2000",
        "date_sort": "1994-01-01",
        "title": "Tower Vista Subdivision Platting & Mandated Street Trees",
        "medium": "Municipal Planning Record & Plat Map",
        "medium_cat": "Other",
        "from": "City of Oregon City Planning Commission",
        "to": "Subdivision Developer / Future Grantees",
        "actor_cat": "City Leadership",
        "subject": "Tower Vista Subdivision Approval Conditions",
        "summary": "Oregon City approves subdivision plat for Tower Vista / Chapin Court. City development conditions require narrow 4-foot planter strips with mandated deciduous street trees between curb and sidewalk, creating an engineered structural conflict between expanding root networks and thin 4-inch concrete panels that the City later weaponizes against homeowners.",
        "summary_html": "<p>Oregon City approves subdivision plat for Tower Vista / Chapin Court. City development conditions require narrow 4-foot planter strips with mandated deciduous street trees between curb and sidewalk, creating an engineered structural conflict between expanding root networks and thin 4-inch concrete panels that the City later weaponizes against homeowners.</p>",
        "record_source": "Oregon City Planning Commission Plat Files; forensic-microclimate.html (Slide 10); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Plat Map &amp; Planning Files</span>; <a href=\"forensic-microclimate.html#slide-10\">forensic-microclimate.html (Slide 10)</a>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "hist-0-2",
        "item_num": "0.2",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "October 2006",
        "date_sort": "2006-10-01",
        "title": "NINA Combo Loan & Inflated Darren Harper Appraisal ($352,000)",
        "medium": "Loan Origination Appraisal & Promissory Note",
        "medium_cat": "Other",
        "from": "Darren Harper (Appraiser) / Ace Mortgage Funding / Decision One",
        "to": "Elbert & Sherry Garboden",
        "actor_cat": "Other / Unknown",
        "subject": "Predatory Subprime 80/20 NINA Financing Origination",
        "summary": "Appraiser Darren Harper produces inflated $352,000 valuation for Ace Mortgage Funding and Decision One Mortgage Co (HSBC subprime wholesale). Funds 100% leveraged NINA combo (80% 1st $281,600 / 20% 2nd $70,400 CitiMortgage), setting the underwater structural baseline that later collapsed into foreclosure.",
        "summary_html": "<p>Appraiser Darren Harper produces inflated $352,000 valuation for Ace Mortgage Funding and Decision One Mortgage Co (HSBC subprime wholesale). Funds 100% leveraged NINA combo (80% 1st $281,600 / 20% 2nd $70,400 CitiMortgage), setting the underwater structural baseline that later collapsed into foreclosure.</p>",
        "record_source": "Origination Loan Packet (Loan 0579478143); Decision One Closing Disclosure; GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Decision One Loan File</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "hist-0-3",
        "item_num": "0.3",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "2009 – 2018",
        "date_sort": "2009-01-01",
        "title": "OCMC 12.04.030 Sidewalk Liability Shift & 167 Tree Culling Permits",
        "medium": "Municipal Code Records & Forestry Audit",
        "medium_cat": "Other",
        "from": "City of Oregon City Commission",
        "to": "Oregon City Property Owners",
        "actor_cat": "City Leadership",
        "subject": "Privatization of Public Infrastructure Repairs & Canopy Loss",
        "summary": "Oregon City amends OCMC 12.04.030 to shift 100% of financial and legal liability for sidewalk maintenance caused by mandated street trees onto adjacent homeowners. Over the next decade, City issues permits resulting in the culling of over 167 mature shade trees, initiating massive canopy loss and escalating urban heat vulnerability in South End neighborhoods.",
        "summary_html": "<p>Oregon City amends OCMC 12.04.030 to shift 100% of financial and legal liability for sidewalk maintenance caused by mandated street trees onto adjacent homeowners. Over the next decade, City issues permits resulting in the culling of over 167 mature shade trees, initiating massive canopy loss and escalating urban heat vulnerability in South End neighborhoods.</p>",
        "record_source": "OCMC 12.04.030; City Forestry Department Permit Registers 2009-2018; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">OCMC 12.04.030</span>; <span class=\"file-source-tag\">City Forestry Records</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "fc-2011-07",
        "item_num": "0.3b",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "June 21, 2012 (Recorded August 8, 2012)",
        "date_sort": "2012-08-08",
        "title": "Recorded Assignment Conveys Beneficial Interest to CWALT 2006-OC11",
        "medium": "County Deed Records (Instr. No. 2012-052957 / Doc No. 2012-050620)",
        "medium_cat": "Court Filing / Order",
        "from": "Mortgage Electronic Registration Systems, Inc. (MERS)",
        "to": "The Bank of New York Mellon as Trustee for CWALT 2006-OC11",
        "actor_cat": "Other / Unknown",
        "subject": "Chain of Title Securitization Assignment Discrepancy",
        "summary": "MERS executes Assignment of Deed of Trust on June 21, 2012 (recorded August 8, 2012 in Clackamas County Official Records as Instrument No. 2012-052957 / Doc No. 2012-050620, Ex. B-1), conveying beneficial interest exclusively to CWALT, Inc., Alternative Loan Trust 2006-OC11. When BONYM files foreclosure five years later, it sues under CWALT 2006-OC10—a legally separate trust with different SEC filings and distinct certificateholders—creating a permanent standing defect.",
        "summary_html": "<p>MERS executes Assignment of Deed of Trust on June 21, 2012 (recorded August 8, 2012 in Clackamas County Official Records as Instrument No. 2012-052957 / Doc No. 2012-050620, Ex. B-1), conveying beneficial interest exclusively to CWALT, Inc., Alternative Loan Trust 2006-OC11. When BONYM files foreclosure five years later, it sues under CWALT 2006-OC10—a legally separate trust with different SEC filings and distinct certificateholders—creating a permanent standing defect.</p>",
        "record_source": "Clackamas County Official Records Instrument No. 2012-052957 (Doc No. 2012-050620, Ex. B-1); WFG Title Report File 22-359102 (Ex. B-6); ORCP 71 Motion.",
        "record_source_html": "<p><span class=\"file-source-tag\">Clackamas Instr. No. 2012-052957 (Ex. B-1)</span>; <span class=\"file-source-tag\">WFG Title Report (Ex. B-6)</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "tlh-2014-01",
        "item_num": "0.3c",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "January 10, 2014",
        "date_sort": "2014-01-10",
        "title": "Turning Leaf Homes Operating Agreement & Distressed Portfolio Acquisition",
        "medium": "Corporate Operating Agreement & Operating Records",
        "medium_cat": "Other",
        "from": "Turning Leaf Homes, LLC (Tracey Baron / Managers)",
        "to": "LLC Members / Operating Entities",
        "actor_cat": "Other / Unknown",
        "subject": "TLH Entity Structure & Distressed Residential Rental Assets",
        "summary": "Second Amended and Restated Turning Leaf Homes Operating Agreement executed. TLH establishes portfolio of distressed residential rental properties across Clackamas, Multnomah, and Washington counties. The portfolio later becomes target of predatory foreclosure actions by institutional servicers represented by ZBS Law and Robinson Tait.",
        "summary_html": "<p>Second Amended and Restated Turning Leaf Homes Operating Agreement executed. TLH establishes portfolio of distressed residential rental properties across Clackamas, Multnomah, and Washington counties. The portfolio later becomes target of predatory foreclosure actions by institutional servicers represented by ZBS Law and Robinson Tait.</p>",
        "record_source": "Turning Leaf Homes Operating Agreement (Jan 10, 2014); Corporate filings and legal docs.txt; Tracey Baron Research Archives.",
        "record_source_html": "<p><span class=\"file-source-tag\">TLH Operating Agreement</span>; <span class=\"file-source-tag\">Corporate filings and legal docs.txt</span>.</p>"
    },
    {
        "id": "tlh-2015-02",
        "item_num": "0.3d",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "February 2015",
        "date_sort": "2015-02-01",
        "title": "Wilmington Trust v. Brian Kincaid & Turning Leaf Homes (CV15020527)",
        "medium": "Circuit Court Docket (Clackamas County)",
        "medium_cat": "Court Filing / Order",
        "from": "Wilmington Trust / Zieve, Brodnax & Steele (ZBS Law)",
        "to": "Estate of Brian C. Kincaid; Turning Leaf Homes, LLC",
        "actor_cat": "Municipal Court",
        "subject": "Foreclosure on 934 Haley Ct & Robinson Tait Law Firm Collapse",
        "summary": "Foreclosure action initiated on 934 Haley Ct, Oregon City. Note executed 2006 for $246,500; primary borrower died and property deeded to Turning Leaf Homes LLC. ZBS Law participates; law firm Robinson Tait abruptly closes in 15 minutes, losing the Certificate of Sale and requiring emergency court motions to issue replacement instruments.",
        "summary_html": "<p>Foreclosure action initiated on 934 Haley Ct, Oregon City. Note executed 2006 for $246,500; primary borrower died and property deeded to Turning Leaf Homes LLC. ZBS Law participates; law firm Robinson Tait abruptly closes in 15 minutes, losing the Certificate of Sale and requiring emergency court motions to issue replacement instruments.</p>",
        "record_source": "Clackamas County Case No. CV15020527; Foreclosure Case Procedural and Financial Data Comparison.xlsx; Tracey Baron Research.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. CV15020527</span>; <span class=\"file-source-tag\">Tracey Baron Research Spreadsheets</span>.</p>"
    },
    {
        "id": "tlh-2015-04",
        "item_num": "0.3e",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "April 23, 2015",
        "date_sort": "2015-04-23",
        "title": "Bowles Fernandez Law Retained to Defend TLH Oregon Properties",
        "medium": "Legal Engagement Agreement",
        "medium_cat": "Other",
        "from": "Turning Leaf Homes, LLC (Tracey Baron)",
        "to": "Bowles Fernandez Law LLC",
        "actor_cat": "Other / Unknown",
        "subject": "Systemic Defense of Distressed Rental Real Estate Portfolio",
        "summary": "Bowles Fernandez Law LLC executes formal litigation engagement letter with Turning Leaf Homes LLC to defend its distressed residential rental portfolio against predatory judicial foreclosures across Oregon circuit courts, challenging securitization chain defects and lack of real-party-in-interest standing.",
        "summary_html": "<p>Bowles Fernandez Law LLC executes formal litigation engagement letter with Turning Leaf Homes LLC to defend its distressed residential rental portfolio against predatory judicial foreclosures across Oregon circuit courts, challenging securitization chain defects and lack of real-party-in-interest standing.</p>",
        "record_source": "Bowles Fernandez Law Engagement Letter (April 23, 2015); Corporate filings and legal docs.txt.",
        "record_source_html": "<p><span class=\"file-source-tag\">Bowles Fernandez Engagement Letter</span>; <span class=\"file-source-tag\">Corporate filings and legal docs.txt</span>.</p>"
    },
    {
        "id": "comp-2015",
        "item_num": "0.3f",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "comparator",
        "layer_title": "Vetted Comparators",
        "date_time": "May 2015",
        "date_sort": "2015-05-01",
        "title": "Comparator: Kelvin & Dunlap v. City of Oregon City (CV15050082)",
        "medium": "Circuit Court Complaint (Clackamas County)",
        "medium_cat": "Court Filing / Order",
        "from": "Kelvin & Dunlap",
        "to": "City of Oregon City / Code Enforcement Officers",
        "actor_cat": "City Leadership",
        "subject": "Warrantless Entry, Dangerous Building Placard & Water Disconnection",
        "summary": "Oregon City code enforcement and police officers conduct warrantless inspection, post backdated 'dangerous building' placard without pre-deprivation notice, and shut off municipal water service to displace a disabled and medically vulnerable resident. Demonstrates a ten-year operational playbook of weaponized code enforcement identical to that later deployed against 12054 Chapin Court.",
        "summary_html": "<p>Oregon City code enforcement and police officers conduct warrantless inspection, post backdated 'dangerous building' placard without pre-deprivation notice, and shut off municipal water service to displace a disabled and medically vulnerable resident. Demonstrates a ten-year operational playbook of weaponized code enforcement identical to that later deployed against 12054 Chapin Court.</p>",
        "record_source": "Clackamas County Circuit Court Case No. CV15050082; Julius AI Gleaning Digest; Case Ground Truth and Evidence Map.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. CV15050082</span>; <span class=\"file-source-tag\">00_JULIUS_AI_GLEANING_DIGEST.md</span>.</p>"
    },
    {
        "id": "tlh-2015-06",
        "item_num": "0.3g",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "June 2015",
        "date_sort": "2015-06-01",
        "title": "Turning Leaf Homes v. Specialized Loan Servicing LLC (6:15-cv-01295)",
        "medium": "Federal District Court Docket (D. Or.)",
        "medium_cat": "Court Filing / Order",
        "from": "Turning Leaf Homes, LLC",
        "to": "Specialized Loan Servicing LLC (SLS)",
        "actor_cat": "Other / Unknown",
        "subject": "Federal Challenge to Loan Servicer Securitization Standing Defects",
        "summary": "TLH files affirmative federal litigation against servicer Specialized Loan Servicing LLC, challenging unlawful foreclosure attempts, defective promissory note chain of title, and failure of securitization trust to prove legal holding of mortgage assets.",
        "summary_html": "<p>TLH files affirmative federal litigation against servicer Specialized Loan Servicing LLC, challenging unlawful foreclosure attempts, defective promissory note chain of title, and failure of securitization trust to prove legal holding of mortgage assets.</p>",
        "record_source": "U.S. District Court for the District of Oregon Case No. 6:15-cv-01295; Motion to Set Aside Void Judgment Ex. G-4.",
        "record_source_html": "<p><span class=\"file-source-tag\">U.S. District Court Case 6:15-cv-01295</span>; <span class=\"file-source-tag\">ORCP 71 Motion Ex. G-4</span>.</p>"
    },
    {
        "id": "tlh-2015-07",
        "item_num": "0.3h",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "July 2015",
        "date_sort": "2015-07-01",
        "title": "Wells Fargo v. Todd Tomlinson & Turning Leaf Homes (CV15070620)",
        "medium": "Circuit Court Docket (Clackamas County)",
        "medium_cat": "Court Filing / Order",
        "from": "Wells Fargo Bank, N.A.",
        "to": "Todd Leon Tomlinson; Turning Leaf Homes, LLC",
        "actor_cat": "Municipal Court",
        "subject": "Foreclosure on 18238 Tamaway Dr & Myers Representation of TLH Affiliates",
        "summary": "Foreclosure on Lake Oswego property. Attorney Jeffrey A. Myers appears and files pleadings representing Turning Leaf Homes LLC and RenX Group LLC, asserting defenses of lack of real-party-in-interest standing, defect in service, and failure to join necessary parties—the exact defenses Myers later argued were improper when he switched sides to represent foreclosing banks against TLH.",
        "summary_html": "<p>Foreclosure on Lake Oswego property. Attorney Jeffrey A. Myers appears and files pleadings representing Turning Leaf Homes LLC and RenX Group LLC, asserting defenses of lack of real-party-in-interest standing, defect in service, and failure to join necessary parties—the exact defenses Myers later argued were improper when he switched sides to represent foreclosing banks against TLH.</p>",
        "record_source": "Clackamas County Case No. CV15070620; Washington County Case C151603CV; ORCP 71 Motion Ex. G-2, G-3, G-5.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. CV15070620</span>; <span class=\"file-source-tag\">ORCP 71 Motion Ex. G-5</span>.</p>"
    },
    {
        "id": "tlh-2015-08",
        "item_num": "0.3i",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "August 2015",
        "date_sort": "2015-08-01",
        "title": "TLH Residential Leases Designate Jeffrey A. Myers as 'Company Attorney'",
        "medium": "Standard Residential Rental Agreement",
        "medium_cat": "Other",
        "from": "Turning Leaf Homes, LLC",
        "to": "Tenants / Property Managers",
        "actor_cat": "Other / Unknown",
        "subject": "Confidential Attorney-Client Privity with Jeffrey A. Myers",
        "summary": "Standard residential lease agreements used across Turning Leaf Homes portfolio explicitly list Jeffrey A. Myers as 'Company Attorney.' This establishes Myers possessed confidential business records, operational knowledge, and litigation strategies of TLH, which he later unethically exploited when representing foreclosing lenders against TLH in Case 17CV38591 without conflict disclosure or waiver.",
        "summary_html": "<p>Standard residential lease agreements used across Turning Leaf Homes portfolio explicitly list Jeffrey A. Myers as 'Company Attorney.' This establishes Myers possessed confidential business records, operational knowledge, and litigation strategies of TLH, which he later unethically exploited when representing foreclosing lenders against TLH in Case 17CV38591 without conflict disclosure or waiver.</p>",
        "record_source": "TLH Residential Lease Form (August 2015); ORCP 71 Motion Ex. G-1; GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">TLH Standard Lease</span>; <span class=\"file-source-tag\">ORCP 71 Motion Ex. G-1</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "hist-0-4",
        "item_num": "0.4",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "November 2015",
        "date_sort": "2015-11-01",
        "title": "Garboden Chapter 7: CitiMortgage Negative Equity & Jesse Baker Appearance",
        "medium": "Bankruptcy Court Docket (D. Or. Case No. 15-35133-rld7)",
        "medium_cat": "Court Filing / Order",
        "from": "CitiMortgage, Inc. / Jesse A.P. Baker (Aldridge Pite, LLP)",
        "to": "U.S. Bankruptcy Court / Amy Mitchell (Trustee)",
        "actor_cat": "Other / Unknown",
        "subject": "Junior Mortgage Negative Equity Proved in Federal Court",
        "summary": "In prior borrower Garboden's Chapter 7 proceeding, Jesse A.P. Baker (Aldridge Pite, LLP) appears representing 2nd mortgage holder CitiMortgage, Inc. CitiMortgage Doc 18 proves negative equity (-$26,628.58) with total secured debt ($324,722.38) exceeding property value ($324,015.00), demonstrating junior note valuelessness and senior loan balance of $264,674.24.",
        "summary_html": "<p>In prior borrower Garboden's Chapter 7 proceeding, Jesse A.P. Baker (Aldridge Pite, LLP) appears representing 2nd mortgage holder CitiMortgage, Inc. CitiMortgage Doc 18 proves negative equity (-$26,628.58) with total secured debt ($324,722.38) exceeding property value ($324,015.00), demonstrating junior note valuelessness and senior loan balance of $264,674.24.</p>",
        "record_source": "U.S. Bankruptcy Court (D. Or. Case No. 15-35133-rld7, Doc 18); GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">U.S. Bankruptcy Court Doc 18</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "fc-2016-01",
        "item_num": "0.4b",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "January 28, 2016",
        "date_sort": "2016-01-28",
        "title": "Bankruptcy Trustee Amy Mitchell Settlement with Turning Leaf Homes III",
        "medium": "Bankruptcy Settlement Agreement (Case No. 15-35133-rld7)",
        "medium_cat": "Court Filing / Order",
        "from": "Amy Mitchell (Chapter 7 Trustee)",
        "to": "Turning Leaf Homes III, LLC / Tracey Baron",
        "actor_cat": "Other / Unknown",
        "subject": "Settlement of Estate Interest in 12054 Chapin Court",
        "summary": "Chapter 7 Trustee Amy Mitchell executes formal settlement and compromise with Turning Leaf Homes III, LLC regarding 12054 Chapin Court. Agreement provides for bankruptcy estate to convey title to TLH via Trustee's Deed upon approval by U.S. Bankruptcy Court, establishing lawful title chain from the bankruptcy estate.",
        "summary_html": "<p>Chapter 7 Trustee Amy Mitchell executes formal settlement and compromise with Turning Leaf Homes III, LLC regarding 12054 Chapin Court. Agreement provides for bankruptcy estate to convey title to TLH via Trustee's Deed upon approval by U.S. Bankruptcy Court, establishing lawful title chain from the bankruptcy estate.</p>",
        "record_source": "U.S. Bankruptcy Court Case 15-35133-rld7 Doc 21; Settlement Agreement (Jan 28, 2016); Corporate filings and legal docs.txt Section 5.",
        "record_source_html": "<p><span class=\"file-source-tag\">Settlement Agreement (Jan 28, 2016)</span>; <span class=\"file-source-tag\">Bankruptcy Doc 21</span>.</p>"
    },
    {
        "id": "fc-2016-04",
        "item_num": "0.4c",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "April 14–27, 2016 (Recorded May 16, 2016)",
        "date_sort": "2016-04-14",
        "title": "Bankruptcy Order Approves Compromise; Trustee's Deed to TLH (Instr. No. 2016-031273)",
        "medium": "Bankruptcy Order (Doc 39) & Recorded Trustee's Deed (Instr. No. 2016-031273)",
        "medium_cat": "Court Filing / Order",
        "from": "Hon. Randall L. Dunn (U.S. Bankruptcy Judge) / Amy Mitchell (Trustee)",
        "to": "Turning Leaf Homes, LLC",
        "actor_cat": "Municipal Court",
        "subject": "Conveyance of Fee Title for 12054 Chapin Court to Turning Leaf Homes",
        "summary": "Judge Dunn enters Order Approving Motion to Settle and Compromise (Doc 39) on April 14, 2016. Chapter 7 Trustee Amy Mitchell executes Trustee's Deed on April 27, 2016 (recorded May 16, 2016 as Instrument No. 2016-031273, Ex. A-2), conveying all right, title, and interest in 12054 Chapin Court to Turning Leaf Homes, LLC and vesting fee simple ownership in TLH.",
        "summary_html": "<p>Judge Dunn enters Order Approving Motion to Settle and Compromise (Doc 39) on April 14, 2016. Chapter 7 Trustee Amy Mitchell executes Trustee's Deed on April 27, 2016 (recorded May 16, 2016 as Instrument No. 2016-031273, Ex. A-2), conveying all right, title, and interest in 12054 Chapin Court to Turning Leaf Homes, LLC and vesting fee simple ownership in TLH.</p>",
        "record_source": "U.S. Bankruptcy Court Case 15-35133-rld7 Doc 39; Clackamas County Official Records Instrument No. 2016-031273 (Ex. A-2); Corporate filings and legal docs.txt Section 6.",
        "record_source_html": "<p><span class=\"file-source-tag\">Bankruptcy Doc 39</span>; <span class=\"file-source-tag\">Instr. No. 2016-031273 (Ex. A-2)</span>.</p>"
    },
    {
        "id": "tlh-2017-02",
        "item_num": "0.4d",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "February 6, 2017",
        "date_sort": "2017-02-06",
        "title": "In re Turning Leaf Homes IV, LLC Chapter 11 Reorganization (17-30353-tmb11)",
        "medium": "U.S. Bankruptcy Court Petition (Bankr. D. Or.)",
        "medium_cat": "Court Filing / Order",
        "from": "Turning Leaf Homes IV, LLC (Tracey Baron, Manager)",
        "to": "U.S. Bankruptcy Court / Secured Creditors",
        "actor_cat": "Other / Unknown",
        "subject": "Chapter 11 Reorganization Petition for Portfolio Properties",
        "summary": "Turning Leaf Homes IV, LLC, managed by Tracey Baron, files Chapter 11 voluntary bankruptcy petition (Case No. 17-30353-tmb11) before Judge Trish M. Brown to restructure mortgage debt and resist aggressive foreclosure actions across rental properties held in Oregon.",
        "summary_html": "<p>Turning Leaf Homes IV, LLC, managed by Tracey Baron, files Chapter 11 voluntary bankruptcy petition (Case No. 17-30353-tmb11) before Judge Trish M. Brown to restructure mortgage debt and resist aggressive foreclosure actions across rental properties held in Oregon.</p>",
        "record_source": "U.S. Bankruptcy Court Case No. 17-30353-tmb11; Foreclosure Case Procedural and Financial Data Comparison.xlsx.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 17-30353-tmb11</span>; <span class=\"file-source-tag\">Tracey Baron Research Spreadsheets</span>.</p>"
    },
    {
        "id": "tlh-2017-09",
        "item_num": "0.4d2",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "September 21, 2017",
        "date_sort": "2017-09-21",
        "title": "Bank Counsel Sworn Admission in Fannie Mae v. Fitch: TLH IV and TLH Are 'Completely Separate' Business Entities",
        "medium": "Circuit Court Sworn Declaration (Clackamas County Case 15CV34832)",
        "medium_cat": "Court Filing / Order",
        "from": "Brady Godbout (Attorney for Fannie Mae / McCarthy & Holthus, LLP)",
        "to": "Clackamas County Circuit Court",
        "actor_cat": "Other / Unknown",
        "subject": "Sworn Admission of Independent Legal Existence Across Turning Leaf Numbered Entities",
        "summary": "In Fannie Mae v. Fitch (Clackamas County Case No. 15CV34832), bank counsel Brady Godbout of McCarthy & Holthus LLP files a sworn declaration addressing a suggestion of bankruptcy stay filed under Turning Leaf Homes IV, LLC (Case No. 17-30353-tmb11). Godbout attests under penalty of perjury that the bankruptcy stay of TLH IV does not halt foreclosure because title is held by Turning Leaf Homes, LLC, which is 'a completely separate business entity.' This certified declaration (Exhibit L in 17CV38591) establishes institutional and judicial recognition that each Turning Leaf numbered entity was legally distinct, refuting Jeffrey Myers's later pretext that TLH somehow 'merged into' or was synonymous with other entities.",
        "summary_html": "<p>In <em>Fannie Mae v. Fitch</em> (Clackamas County Case No. 15CV34832), bank counsel Brady Godbout of McCarthy &amp; Holthus LLP files a sworn declaration addressing a suggestion of bankruptcy stay filed under Turning Leaf Homes IV, LLC (Case No. 17-30353-tmb11). Godbout attests under penalty of perjury that the bankruptcy stay of TLH IV does not halt foreclosure because title is held by Turning Leaf Homes, LLC, which is <strong>\"a completely separate business entity.\"</strong> This certified declaration (Exhibit L in 17CV38591) establishes institutional and judicial recognition that each Turning Leaf numbered entity was legally distinct, refuting Jeffrey Myers's later pretext that TLH somehow \"merged into\" or was synonymous with other entities.</p>",
        "record_source": "Clackamas County Circuit Court Case No. 15CV34832 (Godbout Decl. filed 09/21/2017); Case 17CV38591 Motion to Set Aside Void Judgment Exhibit L; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 15CV34832 (Godbout Decl.)</span>; <span class=\"file-source-tag\">17CV38591 Motion Ex. L</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "fc-2017-10",
        "item_num": "0.4e",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "October 26, 2017",
        "date_sort": "2017-10-26",
        "title": "ZBS Law Records Defective Multnomah Lis Pendens for Clackamas Property",
        "medium": "Notice of Pendency of Action (Rec. No. 2017-073187)",
        "medium_cat": "Court Filing / Order",
        "from": "Zieve, Brodnax & Steele, LLP (ZBS Law)",
        "to": "Clackamas County Clerk / Public Records",
        "actor_cat": "Other / Unknown",
        "subject": "Facial Jurisdictional Defect in Recorded Lis Pendens",
        "summary": "ZBS Law records Notice of Pendency of Action in Clackamas County Official Records (Instr. No. 2017-073187). On its face, the instrument certifies under penalty of law that the foreclosure action is pending 'in the Circuit Court of the State of Oregon, in and for the County of Multnomah'—not Clackamas County. The instrument fails to give lawful constructive notice and does not appear in subsequent title searches.",
        "summary_html": "<p>ZBS Law records Notice of Pendency of Action in Clackamas County Official Records (Instr. No. 2017-073187). On its face, the instrument certifies under penalty of law that the foreclosure action is pending 'in the Circuit Court of the State of Oregon, in and for the County of Multnomah'—not Clackamas County. The instrument fails to give lawful constructive notice and does not appear in subsequent title searches.</p>",
        "record_source": "Clackamas County Official Records Fee No. 2017-073187; WFG Title Report 22-359102; ORCP 71 Motion Eriksson Decl. ¶ 15.",
        "record_source_html": "<p><span class=\"file-source-tag\">Clackamas Rec. No. 2017-073187</span>; <span class=\"file-source-tag\">WFG Title Report</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "tlh-2018-01",
        "item_num": "0.4e2",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "January 5, 2018",
        "date_sort": "2018-01-05",
        "title": "FITE, LLC Chapter 11 Bankruptcy (18-30038-tmb11) & Exclusion of Chapin Court from Asset Schedules",
        "medium": "U.S. Bankruptcy Court Petition & Schedules (Bankr. D. Or.)",
        "medium_cat": "Court Filing / Order",
        "from": "FITE, LLC (Tracey Baron, Manager)",
        "to": "U.S. Bankruptcy Court / Secured Creditors",
        "actor_cat": "Other / Unknown",
        "subject": "FITE Chapter 11 Filing Follows TLH IV/V Merger Only; Chapin Court Omitted",
        "summary": "FITE, LLC files Chapter 11 voluntary bankruptcy (Case No. 18-30038-tmb11, Bankr. D. Or.) following a January 3, 2018 merger of only Turning Leaf Homes IV, LLC and Turning Leaf Homes V, LLC. Turning Leaf Homes, LLC was NOT a party to the merger and remained an independent active Oregon LLC. In the sworn bankruptcy schedules (Doc 13), FITE, LLC lists its real estate assets; crucially, the combined asset schedules of TLH IV, TLH V, and FITE, LLC all together do not include 12054 Chapin Court (Exhibit E-5 to ORCP 71 motion), proving FITE never held, claimed, or scheduled any interest in the Chapin Court property.",
        "summary_html": "<p>FITE, LLC files Chapter 11 voluntary bankruptcy (Case No. 18-30038-tmb11, Bankr. D. Or.) following a January 3, 2018 merger of only Turning Leaf Homes IV, LLC and Turning Leaf Homes V, LLC. Turning Leaf Homes, LLC was <strong>NOT</strong> a party to the merger and remained an independent active Oregon LLC. In the sworn bankruptcy schedules (Doc 13), FITE, LLC lists its real estate assets; crucially, the combined asset schedules of TLH IV, TLH V, and FITE, LLC all together <strong>do not include 12054 Chapin Court</strong> (Exhibit E-5 to ORCP 71 motion), proving FITE never held, claimed, or scheduled any interest in the Chapin Court property.</p>",
        "record_source": "U.S. Bankruptcy Court Case No. 18-30038-tmb11 Petition & Schedule A/B; Oregon Secretary of State Articles of Merger (Jan 3, 2018); Case 17CV38591 Motion to Set Aside Void Judgment Exhibit E-5.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 18-30038-tmb11 Doc 13</span>; <span class=\"file-source-tag\">17CV38591 Motion Ex. E-5</span>; <span class=\"file-source-tag\">Articles of Merger (01/03/2018)</span>.</p>"
    },
    {
        "id": "tlh-2018-05",
        "item_num": "0.4f",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "May 2018",
        "date_sort": "2018-05-01",
        "title": "BONYM v. Brad Hiday & Turning Leaf Homes (18CV51697 - Rose Lane)",
        "medium": "Circuit Court Docket (Clackamas County)",
        "medium_cat": "Court Filing / Order",
        "from": "Jeffrey A. Myers / BONYM CWALT 2007-OA4",
        "to": "Brad K. Hiday; Turning Leaf Homes, LLC",
        "actor_cat": "Municipal Court",
        "subject": "Foreclosure on 30620 SW Rose Lane & Myers Conflict of Interest",
        "summary": "Judicial foreclosure filed on 30620 SW Rose Lane, Wilsonville. Turning Leaf Homes acquired interest via 2015 deed. Attorney substitution from Janaya L. Carter to Jeffrey A. Myers. In this contemporaneous filing, Myers correctly captions Turning Leaf Homes LLC as a standalone active defendant without any 'now known as FITE' designation—proving Myers knew TLH was an independent active entity when he misled the court in 17CV38591.",
        "summary_html": "<p>Judicial foreclosure filed on 30620 SW Rose Lane, Wilsonville. Turning Leaf Homes acquired interest via 2015 deed. Attorney substitution from Janaya L. Carter to Jeffrey A. Myers. In this contemporaneous filing, Myers correctly captions Turning Leaf Homes LLC as a standalone active defendant without any 'now known as FITE' designation—proving Myers knew TLH was an independent active entity when he misled the court in 17CV38591.</p>",
        "record_source": "Clackamas County Case No. 18CV51697; ORCP 71 Motion Ex. F-1; Tracey Baron Research Spreadsheets.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 18CV51697</span>; <span class=\"file-source-tag\">ORCP 71 Motion Ex. F-1</span>.</p>"
    },
    {
        "id": "tlh-2018-05b",
        "item_num": "0.4f2",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "May 8, 2018 (Dissolved October 11, 2018)",
        "date_sort": "2018-05-08",
        "title": "Dismissal of FITE, LLC Chapter 11 Bankruptcy (18-30038-tmb11) & Administrative Dissolution",
        "medium": "U.S. Bankruptcy Court Order of Dismissal & Oregon SOS Records",
        "medium_cat": "Court Filing / Order",
        "from": "Hon. Trish M. Brown (U.S. Bankruptcy Judge)",
        "to": "FITE, LLC / Secured Creditors",
        "actor_cat": "Municipal Court",
        "subject": "Termination of FITE Bankruptcy & Public Record Ignored by Jeffrey Myers",
        "summary": "Judge Trish M. Brown enters an Order dismissing FITE, LLC's Chapter 11 bankruptcy proceeding (Case No. 18-30038-tmb11). Five months later, on October 11, 2018, FITE, LLC is administratively dissolved by the Oregon Secretary of State. This public dismissal and dissolution occurred well before Jeffrey A. Myers falsely claimed on the record in 17CV38591 that Turning Leaf Homes LLC 'merged into or became FITE, LLC.' Given the formal federal dismissal and state dissolution, Myers could not have missed that FITE was a dead, unmerged entity that never held title to Chapin Court, making his later representations to Senior Judge Breithaupt particularly egregious.",
        "summary_html": "<p>Judge Trish M. Brown enters an Order dismissing FITE, LLC's Chapter 11 bankruptcy proceeding (Case No. 18-30038-tmb11). Five months later, on October 11, 2018, FITE, LLC is administratively dissolved by the Oregon Secretary of State. This public dismissal and dissolution occurred well before Jeffrey A. Myers falsely claimed on the record in 17CV38591 that Turning Leaf Homes LLC 'merged into or became FITE, LLC.' Given the formal federal dismissal and state dissolution, Myers could not have missed that FITE was a dead, unmerged entity that never held title to Chapin Court, making his later representations to Senior Judge Breithaupt particularly egregious.</p>",
        "record_source": "U.S. Bankruptcy Court Case No. 18-30038-tmb11 Order of Dismissal (May 8, 2018); Oregon Secretary of State Business Registry for FITE, LLC (Registry # 1391799-97); Case 17CV38591 ORCP 71 Motion Grounds Three & Four.",
        "record_source_html": "<p><span class=\"file-source-tag\">Bankruptcy Dismissal Order (05/08/2018)</span>; <span class=\"file-source-tag\">Oregon SOS Registry # 1391799-97</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "tlh-2018-06",
        "item_num": "0.4f3",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "June 21, 2018 (Schedules Filed July 5, 2018)",
        "date_sort": "2018-06-21",
        "title": "Michelle Baron Chapter 7 Bankruptcy (18-32159-tmb7) Lists 12054 Chapin Court Under 50% TLH Ownership",
        "medium": "U.S. Bankruptcy Court Petition & Schedule A/B (Bankr. D. Or.)",
        "medium_cat": "Court Filing / Order",
        "from": "Michelle Baron (Debtor / 50% Member of Turning Leaf Homes, LLC)",
        "to": "U.S. Bankruptcy Court / Chapter 7 Trustee",
        "actor_cat": "Other / Unknown",
        "subject": "Debtor Member's Sworn Schedules Attest to TLH Fee Ownership of 12054 Chapin Court",
        "summary": "Michelle Baron, holding a 50% managing ownership interest in Turning Leaf Homes, LLC alongside Tracey Baron, files Chapter 7 voluntary bankruptcy (Case No. 18-32159-tmb7, Bankr. D. Or.). In her sworn Schedule A/B (Doc 10, filed July 5, 2018), Michelle Baron explicitly schedules 12054 Chapin Court, Oregon City, OR 97045 as real property asset owned through her 50% equity in Turning Leaf Homes, LLC. This federal court filing proves that fee ownership of Chapin Court was actively claimed and scheduled by TLH's members in 2018, directly contradicting ZBS Law's false assertions and demonstrating that TLH was an active, operating entity with substantive assets during the exact window ZBS Law procured an improper default.",
        "summary_html": "<p>Michelle Baron, holding a 50% managing ownership interest in Turning Leaf Homes, LLC alongside Tracey Baron, files Chapter 7 voluntary bankruptcy (Case No. 18-32159-tmb7, Bankr. D. Or.). In her sworn Schedule A/B (Doc 10, filed July 5, 2018), Michelle Baron explicitly schedules <strong>12054 Chapin Court, Oregon City, OR 97045</strong> as real property asset owned through her 50% equity in Turning Leaf Homes, LLC. This federal court filing proves that fee ownership of Chapin Court was actively claimed and scheduled by TLH's members in 2018, directly contradicting ZBS Law's false assertions and demonstrating that TLH was an active, operating entity with substantive assets during the exact window ZBS Law procured an improper default.</p>",
        "record_source": "U.S. Bankruptcy Court Case No. 18-32159-tmb7 Petition (Doc 1) & Schedule A/B (Doc 10); Case 17CV38591 Motion to Set Aside Void Judgment Eriksson Decl. ¶ 21; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 18-32159-tmb7 Doc 10</span>; <span class=\"file-source-tag\">17CV38591 Eriksson Decl. ¶ 21</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "fc-2018-09",
        "item_num": "0.4g",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "September 20, 2018",
        "date_sort": "2018-09-20",
        "title": "ZBS Law Files Defective Return of Service on Tracey Baron (17CV38591)",
        "medium": "Affidavit of Service (Clackamas County Circuit Court)",
        "medium_cat": "Court Filing / Order",
        "from": "Janaya L. Carter / ZBS Law / Process Server",
        "to": "Turning Leaf Homes LLC now known as FITE LLC",
        "actor_cat": "Municipal Court",
        "subject": "Defective Corporate Service on 'Clerk on Duty'",
        "summary": "ZBS Law files Return of Service claiming corporate service on 'TURNING LEAF HOMES, LLC, A LIMITED LIABILITY COMPANY, NOW KNOWN AS FITE, LLC' by leaving documents with 'Tracey Barron, clerk/Clerk on Duty' at 1701 SE Oak Shore Lane. Service fails under ORCP 7 D(3) because Baron was not a designated clerk, FITE was a distinct unmerged entity, and TLH's registered agent address was ignored.",
        "summary_html": "<p>ZBS Law files Return of Service claiming corporate service on 'TURNING LEAF HOMES, LLC, A LIMITED LIABILITY COMPANY, NOW KNOWN AS FITE, LLC' by leaving documents with 'Tracey Barron, clerk/Clerk on Duty' at 1701 SE Oak Shore Lane. Service fails under ORCP 7 D(3) because Baron was not a designated clerk, FITE was a distinct unmerged entity, and TLH's registered agent address was ignored.</p>",
        "record_source": "Case No. 17CV38591 Docket (10/01/2018 Filing); Defendant Service Methods and Descriptions in Bank Filings.xlsx; ORCP 71 Motion.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case 17CV38591 Service Return</span>; <span class=\"file-source-tag\">Bank Filings Spreadsheet</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "fc-2019-01",
        "item_num": "0.4h",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "January 11, 2019",
        "date_sort": "2019-01-11",
        "title": "ZBS Law Mails Motion for Summary Judgment to Withdrawn Counsel",
        "medium": "Motion for Summary Judgment & Certificate of Service",
        "medium_cat": "Court Filing / Order",
        "from": "Jeffrey A. Myers / ZBS Law",
        "to": "Andrew D. Glascock (Withdrawn Attorney)",
        "actor_cat": "Municipal Court",
        "subject": "Unlawful Service Destroying Personal Jurisdiction Under Wells Fargo v. Jasper",
        "summary": "Plaintiff's counsel Jeffrey A. Myers files Motion for Summary Judgment and mails service copies exclusively to attorney Andrew Glascock, who had formally withdrawn over a year earlier, despite actual court-docketed notice that mailings to that address were returned as undeliverable. Under Wells Fargo Bank v. Jasper, 289 Or App 610 (2018), resuming service to a known failed address is objectively unreasonable and voids personal jurisdiction.",
        "summary_html": "<p>Plaintiff's counsel Jeffrey A. Myers files Motion for Summary Judgment and mails service copies exclusively to attorney Andrew Glascock, who had formally withdrawn over a year earlier, despite actual court-docketed notice that mailings to that address were returned as undeliverable. Under Wells Fargo Bank v. Jasper, 289 Or App 610 (2018), resuming service to a known failed address is objectively unreasonable and voids personal jurisdiction.</p>",
        "record_source": "Case 17CV38591 Docket; Dispositive Motions and Service Records for Case 17CV38591.xlsx; ORCP 71 Motion Ground One.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case 17CV38591 Docket</span>; <span class=\"file-source-tag\">Dispositive Motions Spreadsheet</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "fc-2019-02",
        "item_num": "0.4i",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "February 27, 2019",
        "date_sort": "2019-02-27",
        "title": "Jeffrey Myers Misrepresents TLH as Dissolved 'FITE LLC' to Procure Default",
        "medium": "Circuit Court Hearing Transcript (Case 17CV38591)",
        "medium_cat": "Court Filing / Order",
        "from": "Jeffrey A. Myers (ZBS Law)",
        "to": "Senior Judge Henry C. Breithaupt (Clackamas County Circuit Court)",
        "actor_cat": "Municipal Court",
        "subject": "Fraud on the Court & Procedural Impossibility Under ORCP 69 A(1)",
        "summary": "At the February 27, 2019 summary judgment hearing before Senior Judge Henry C. Breithaupt, Jeffrey Myers falsely represents on the record that Turning Leaf Homes LLC is 'now known as FITE, LLC.' Myers makes this representation despite the public docketed record that FITE, LLC's Chapter 11 bankruptcy (18-30038-tmb11) had already been dismissed on May 8, 2018 by Judge Trish M. Brown, that FITE was administratively dissolved on October 11, 2018, and that FITE never held title to Chapin Court—facts impossible for Myers to miss. Myers nonetheless continues lying about Turning Leaf's existence to procure an improper order for default against phantom FITE while TLH had a live Answer and Counterclaims pending, creating a fatal procedural violation under ORCP 69 A(1).",
        "summary_html": "<p>At the February 27, 2019 summary judgment hearing before Senior Judge Henry C. Breithaupt, Jeffrey Myers falsely represents on the record that Turning Leaf Homes LLC is 'now known as FITE, LLC.' Myers makes this representation despite the public docketed record that FITE, LLC's Chapter 11 bankruptcy (18-30038-tmb11) had already been dismissed on May 8, 2018 by Judge Trish M. Brown, that FITE was administratively dissolved on October 11, 2018, and that FITE never held title to Chapin Court—facts impossible for Myers to miss. Myers nonetheless continues lying about Turning Leaf's existence to procure an improper order for default against phantom FITE while TLH had a live Answer and Counterclaims pending, creating a fatal procedural violation under ORCP 69 A(1).</p>",
        "record_source": "Case 17CV38591 Hearing Transcript (Feb 27, 2019, Ex. U-3); Case No. 18-30038-tmb11 Dismissal Order; Oregon SOS FITE Dissolution Records; ORCP 71 Motion Ground Three & Four.",
        "record_source_html": "<p><span class=\"file-source-tag\">Feb 27 2019 Transcript (Ex. U-3)</span>; <span class=\"file-source-tag\">Bankruptcy Dismissal (05/08/2018)</span>; <span class=\"file-source-tag\">Oregon SOS Records</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "fc-2019-03",
        "item_num": "0.4j",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "March 19 – August 7, 2019",
        "date_sort": "2019-08-07",
        "title": "Turning Leaf Homes LLC 12-Person Jury Trial Canceled Upon Docketing of Void Foreclosure Judgment",
        "medium": "Circuit Court Docket & Trial Calendar (Case 17CV38591)",
        "medium_cat": "Court Filing / Order",
        "from": "Clackamas County Circuit Court / Hon. Michael C. Wetzel",
        "to": "Turning Leaf Homes, LLC / The Bank of New York Mellon",
        "actor_cat": "Municipal Court",
        "subject": "Extinguishment of Jury Trial Right & Improper Judgment Docketing",
        "summary": "On March 19, 2019, the court entered a UTCR 7.020 Limited Judgment of Dismissal as to other defendants and formally calendared a Twelve-Person Jury Trial for Turning Leaf Homes, LLC on August 7, 2019 at 9:00 AM (Ex. O-4). Judge Wetzel's conditional reinstatement expired June 3, 2019, and Presiding Judge Kathie Steele entered a General Judgment of Dismissal on July 26, 2019 (Ex. K-2). On July 30, 2019, Judge Wetzel signed a foreclosure judgment against phantom FITE LLC. That judgment sat undocketed until August 7, 2019 at 2:27 PM—the very afternoon of the scheduled jury trial—at which time the clerk docketed the judgment and marked TLH's jury trial as 'CANCELED Trial - Twelve Person Jury (9:00 AM) — Judgment', extinguishing TLH's right to trial over its live Answer and Counterclaims.",
        "summary_html": "<p>On March 19, 2019, the court entered a UTCR 7.020 Limited Judgment of Dismissal as to other defendants and formally calendared a <strong>Twelve-Person Jury Trial for Turning Leaf Homes, LLC on August 7, 2019 at 9:00 AM</strong> (Ex. O-4). Judge Wetzel's conditional reinstatement expired June 3, 2019, and Presiding Judge Kathie Steele entered a General Judgment of Dismissal on July 26, 2019 (Ex. K-2). On July 30, 2019, Judge Wetzel signed a foreclosure judgment against phantom FITE LLC. That judgment sat undocketed until August 7, 2019 at 2:27 PM—the very afternoon of the scheduled jury trial—at which time the clerk docketed the judgment and marked TLH's jury trial as <em>\"CANCELED Trial - Twelve Person Jury (9:00 AM) — Judgment\"</em>, extinguishing TLH's right to trial over its live Answer and Counterclaims.</p>",
        "record_source": "Case 17CV38591 Register of Actions (Ex. O-4); General Judgment of Dismissal (Ex. K-2); General Judgment of Foreclosure (July 30/Aug 7, 2019, Ex. 26).",
        "record_source_html": "<p><span class=\"file-source-tag\">Case 17CV38591 Register of Actions (Ex. O-4)</span>; <span class=\"file-source-tag\">Judgment of Dismissal (Ex. K-2)</span>; <span class=\"file-source-tag\">Foreclosure Judgment (Ex. 26)</span>.</p>"
    },
    {
        "id": "hist-0-5",
        "item_num": "0.5",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "June 3 – July 26, 2019",
        "date_sort": "2019-06-03",
        "title": "UTCR 7.020 Reinstatement Expiration (June 3, 2019) & General Judgment of Dismissal (July 26, 2019)",
        "medium": "Circuit Court Order & General Judgment of Dismissal (Case 17CV38591)",
        "medium_cat": "Court Filing / Order",
        "from": "Hon. Michael C. Wetzel / Presiding Judge Kathie F. Steele",
        "to": "The Bank of New York Mellon / Case 17CV38591",
        "actor_cat": "Municipal Court",
        "subject": "Automatic Expiration of Conditional Reinstatement & Entry of General Judgment of Dismissal",
        "summary": "Following the March 19, 2019 UTCR 7.020 dismissal for want of prosecution, Judge Wetzel's April 1, 2019 Order conditionally reinstated Case 17CV38591 only until June 3, 2019. When Plaintiff failed to obtain a signed general judgment by the June 3, 2019 deadline, the conditional reinstatement automatically expired, and Presiding Judge Kathie F. Steele entered a General Judgment of Dismissal on July 26, 2019 (Ex. K-2)—four days before the July 30, 2019 foreclosure judgment was signed.",
        "summary_html": "<p>Following the March 19, 2019 UTCR 7.020 dismissal for want of prosecution, Judge Wetzel's April 1, 2019 Order conditionally reinstated Case 17CV38591 only until June 3, 2019. When Plaintiff failed to obtain a signed general judgment by the June 3, 2019 deadline, the conditional reinstatement automatically expired, and Presiding Judge Kathie F. Steele entered a General Judgment of Dismissal on July 26, 2019 (Ex. K-2)—four days before the July 30, 2019 foreclosure judgment was signed.</p>",
        "record_source": "Clackamas County Circuit Court Case No. 17CV38591 (Ex. K-1, Ex. K-2); Declaration of Annika Eriksson ¶¶ 37, 40; ORCP 71 Motion.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 17CV38591 (Ex. K-1, Ex. K-2)</span>; <span class=\"file-source-tag\">Eriksson Decl. ¶¶ 37, 40</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "hist-0-6",
        "item_num": "0.6",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "Summer 2019",
        "date_sort": "2019-07-01",
        "title": "Turning Leaf Homes Default & $72,026 Municipal Lien (CE-000520-19)",
        "medium": "Municipal Court Judgment & County Lien Docket",
        "medium_cat": "Court Filing / Order",
        "from": "City of Oregon City Municipal Court",
        "to": "Turning Leaf Homes LLC (Fee No. 2019-079244)",
        "actor_cat": "Municipal Court",
        "subject": "Case CE-000520-19 Default Judgment & Lien",
        "summary": "City cites prior owner Turning Leaf Homes LLC for yard maintenance (CE-000520-19). Baron arrives late; default entered. Municipal Court dockets massive $72,026.00 civil lien (Fee No. 2019-079244). City later utilizes this prior owner penalty to deny sidewalk grant assistance and justify aggressive administrative pressure against Eriksson.",
        "summary_html": "<p>City cites prior owner Turning Leaf Homes LLC for yard maintenance (CE-000520-19). Baron arrives late; default entered. Municipal Court dockets massive $72,026.00 civil lien (Fee No. 2019-079244). City later utilizes this prior owner penalty to deny sidewalk grant assistance and justify aggressive administrative pressure against Eriksson.</p>",
        "record_source": "Case CE-000520-19; Fee No. 2019-079244; Officer Knudson Affidavit; Ex. 33; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case CE-000520-19</span>; <span class=\"file-source-tag\">Fee No. 2019-079244</span>; [Ex. 33]; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "hist-0-7",
        "item_num": "0.7",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "July 30, 2019",
        "date_sort": "2019-07-30",
        "title": "Entry of Void Default Foreclosure Judgment & CWALT Trust Mismatch",
        "medium": "Circuit Court General Judgment",
        "medium_cat": "Court Filing / Order",
        "from": "Clackamas County Circuit Court",
        "to": "BONYM / CWALT 2006-OC10",
        "actor_cat": "Municipal Court",
        "subject": "Case 17CV38591 Foreclosure General Judgment Entry",
        "summary": "General Judgment of Foreclosure signed by Judge Wetzel on July 30, 2019 (entered Aug 7, 2019) naming CWALT 2006-OC10. Recorded chain of title shows beneficial interest was assigned to CWALT 2006-OC11. Judgment entered by default against FITE, LLC, while TLH's Answer and live Counterclaims remained pending and unadjudicated, rendering judgment void.",
        "summary_html": "<p>General Judgment of Foreclosure signed by Judge Wetzel on July 30, 2019 (entered Aug 7, 2019) naming CWALT 2006-OC10. Recorded chain of title shows beneficial interest was assigned to CWALT 2006-OC11. Judgment entered by default against FITE, LLC, while TLH's Answer and live Counterclaims remained pending and unadjudicated, rendering judgment void.</p>",
        "record_source": "Case 17CV38591 Docket (General Judgment of Foreclosure, July 30, 2019); Document Execution and Filing Dates for Foreclosure Proceedings.xlsx; ORCP 71 Motion.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case 17CV38591 General Judgment</span>; <span class=\"file-source-tag\">Foreclosure Proceedings Dates Spreadsheet</span>; <span class=\"file-source-tag\">ORCP 71 Motion</span>.</p>"
    },
    {
        "id": "fc-2019-2023-writs",
        "item_num": "0.7d",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "October 2019 – August 2023",
        "date_sort": "2019-10-03",
        "title": "Chain of Authority & the July 30 / July 31 / August 7 Judgment Date Dichotomy Across Three Writs",
        "medium": "Circuit Court Writs of Execution & Praecipes (Case 17CV38591)",
        "medium_cat": "Court Filing / Order",
        "from": "ZBS Law, LLP (Jeffrey A. Myers / Amber L. Labrecque)",
        "to": "Clackamas County Clerk / Clackamas County Sheriff",
        "actor_cat": "Municipal Court",
        "subject": "Contradictory Judgment Dates in Writs #30586, #36119, and #17120597",
        "summary": "Foreclosure judgment in 17CV38591 is internally contradicted across all three Praecipes and Writs: (1) Praecipe #1 (Sept 26/30, 2019, Ex. P-1) & Writ #1 (#30586, Oct 3, 2019, Ex. Q-1) commanded execution of a nonexistent July 31, 2019 judgment; (2) Praecipe #2 (Nov 30/Dec 9, 2022, Ex. P-2) & Writ #2 (#36119, Dec 16, 2022, Ex. Q-2) claimed the judgment was entered and executed on August 7, 2019 and double-counted Aug 7 in interest calculations; (3) Praecipe #3 (Aug 23/31, 2023, Ex. P-3) cited August 7, 2019, while Writ #3 (Aug 31, 2023, #17120597, Ex. Q-3) split the dates, certifying execution on July 30, 2019 and docketing on August 7, 2019; and the unrecorded May 9, 2024 Sheriff's Deed cited August 7, 2019, while ZBS briefs reverted to July 31, 2019.",
        "summary_html": "<p>Foreclosure judgment in 17CV38591 is internally contradicted across all three Praecipes and Writs: (1) <strong>Praecipe #1 (Sept 26/30, 2019, Ex. P-1) &amp; Writ #1 (#30586, Oct 3, 2019, Ex. Q-1)</strong> commanded execution of a nonexistent <strong>July 31, 2019</strong> judgment; (2) <strong>Praecipe #2 (Nov 30/Dec 9, 2022, Ex. P-2) &amp; Writ #2 (#36119, Dec 16, 2022, Ex. Q-2)</strong> claimed the judgment was entered and executed on <strong>August 7, 2019</strong> and double-counted Aug 7 in interest calculations; (3) <strong>Praecipe #3 (Aug 23/31, 2023, Ex. P-3)</strong> cited August 7, 2019, while <strong>Writ #3 (Aug 31, 2023, #17120597, Ex. Q-3)</strong> split the dates, certifying execution on <strong>July 30, 2019</strong> and docketing on <strong>August 7, 2019</strong>; and the unrecorded May 9, 2024 Sheriff's Deed cited August 7, 2019, while ZBS briefs reverted to July 31, 2019.</p>",
        "record_source": "Case 17CV38591 Praecipes (Exs. P-1–P-3); Writs of Execution (Exs. Q-1–Q-3); Sheriff's Case No. 23-20024; ORCP 71 Motion.",
        "record_source_html": "<p><span class=\"file-source-tag\">Praecipes (Exs. P-1–P-3)</span>; <span class=\"file-source-tag\">Writs of Execution (Exs. Q-1–Q-3)</span>; <span class=\"file-source-tag\">Sheriff's File 23-20024</span>.</p>"
    },
    {
        "id": "comp-2019",
        "item_num": "0.7b",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "comparator",
        "layer_title": "Vetted Comparators",
        "date_time": "November 2019",
        "date_sort": "2019-11-01",
        "title": "Comparator: Nicita v. Holladay & City of Oregon City (3:19-cv-01960-YY)",
        "medium": "U.S. District Court Complaint & Findings (D. Or.)",
        "medium_cat": "Court Filing / Order",
        "from": "Michael Nicita",
        "to": "City of Oregon City / City Recorder Holladay",
        "actor_cat": "City Leadership",
        "subject": "Retaliatory Denial of Discretionary Appeal Fee Waiver",
        "summary": "Federal § 1983 civil rights lawsuit establishing City of Oregon City practice of retaliatorily denying discretionary fee waivers to indigent citizens attempting to appeal municipal citations, creating an unlawful financial barrier to administrative and judicial review.",
        "summary_html": "<p>Federal § 1983 civil rights lawsuit establishing City of Oregon City practice of retaliatorily denying discretionary fee waivers to indigent citizens attempting to appeal municipal citations, creating an unlawful financial barrier to administrative and judicial review.</p>",
        "record_source": "U.S. District Court (D. Or. Case No. 3:19-cv-01960-YY); Julius AI Investigation Digest; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 3:19-cv-01960-YY</span>; <span class=\"file-source-tag\">00_JULIUS_AI_GLEANING_DIGEST.md</span>.</p>"
    },
    {
        "id": "fc-2021-12",
        "item_num": "0.7c",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "December 8, 2021",
        "date_sort": "2021-12-08",
        "title": "Baron Marriage Dissolution Awards 12054 Chapin Court to Michelle Anne Baron (21DR19354)",
        "medium": "General Judgment of Dissolution of Marriage (Ex. A-5)",
        "medium_cat": "Court Filing / Order",
        "from": "Clackamas County Circuit Court",
        "to": "Michelle Anne Baron / Tracey Stewart Baron",
        "actor_cat": "Municipal Court",
        "subject": "Judicial Division of Real Property in Baron Divorce",
        "summary": "Clackamas County Circuit Court enters General Judgment of Dissolution of Marriage in Case No. 21DR19354 (Ex. A-5). Under the division of real properties, Michelle Anne Baron is specifically awarded all right, title, and interest in 12054 Chapin Court, Oregon City, OR 97045, confirming her authority as sole managing member of Turning Leaf Homes, LLC to convey fee-simple title to Annika Eriksson.",
        "summary_html": "<p>Clackamas County Circuit Court enters General Judgment of Dissolution of Marriage in Case No. 21DR19354 (Ex. A-5). Under the division of real properties, Michelle Anne Baron is specifically awarded all right, title, and interest in 12054 Chapin Court, Oregon City, OR 97045, confirming her authority as sole managing member of Turning Leaf Homes, LLC to convey fee-simple title to Annika Eriksson.</p>",
        "record_source": "Case No. 21DR19354 General Judgment (Dec 8, 2021, Ex. A-5); Declaration of Annika Eriksson ¶ 46; Corporate filings and legal docs.txt Section 7.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case 21DR19354 Divorce Judgment (Ex. A-5)</span>; <span class=\"file-source-tag\">Eriksson Decl. ¶ 46</span>.</p>"
    },
    {
        "id": "hist-0-8",
        "item_num": "0.8",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "December 14–21, 2021",
        "date_sort": "2021-12-21",
        "title": "Bargain & Sale Deed Conveys Fee-Simple Title to Annika Eriksson (Instr. No. 2021-109930)",
        "medium": "County Deed Records (Instr. No. 2021-109930)",
        "medium_cat": "Court Filing / Order",
        "from": "Turning Leaf Homes LLC (Michelle Baron, Managing Member)",
        "to": "Annika Eriksson",
        "actor_cat": "Other / Unknown",
        "subject": "Deed Conveyance & Vesting of Fee Simple Title",
        "summary": "Turning Leaf Homes LLC (by sole managing member Michelle Baron) conveys 12054 Chapin Court to Annika Eriksson via Statutory Bargain and Sale Deed executed December 14, 2021 and recorded December 21, 2021 in Clackamas County Official Records as Instrument No. 2021-109930 (Ex. A-1 / Ex. 1). Eriksson vests record fee-simple legal and equitable title.",
        "summary_html": "<p>Turning Leaf Homes LLC (by sole managing member Michelle Baron) conveys 12054 Chapin Court to Annika Eriksson via Statutory Bargain and Sale Deed executed December 14, 2021 and recorded December 21, 2021 in Clackamas County Official Records as Instrument No. 2021-109930 (Ex. A-1 / Ex. 1). Eriksson vests record fee-simple legal and equitable title.</p>",
        "record_source": "Clackamas County Official Records Instrument No. 2021-109930 (Ex. A-1 / Ex. 1); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Clackamas Instr. No. 2021-109930 (Ex. A-1 / Ex. 1)</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "tlh-2021-11",
        "item_num": "0.8b",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "November 1–6, 2021",
        "date_sort": "2021-11-01",
        "title": "Settlement & Release: Annika & Don and Turning Leaf Homes / Brilliant Homes",
        "medium": "Property Settlement and Mutual Release Agreements",
        "medium_cat": "Other",
        "from": "Annika Eriksson & Donald Buckhout",
        "to": "Turning Leaf Homes, LLC / Brilliant Homes, LLC",
        "actor_cat": "Other / Unknown",
        "subject": "Resolution of Prior Tenancy & Transition of Real Property Interests",
        "summary": "Formal Settlement and Release Agreements executed regarding 515 NW 112th Ave, Portland between tenants Annika & Don and property owners Turning Leaf Homes LLC and Brilliant Homes LLC, settling prior tenancy matters and establishing mutual covenants that preceded the conveyance of 12054 Chapin Court.",
        "summary_html": "<p>Formal Settlement and Release Agreements executed regarding 515 NW 112th Ave, Portland between tenants Annika & Don and property owners Turning Leaf Homes LLC and Brilliant Homes LLC, settling prior tenancy matters and establishing mutual covenants that preceded the conveyance of 12054 Chapin Court.</p>",
        "record_source": "Settlement and Release Agreements (Nov 1 & Nov 6, 2021); Corporate filings and legal docs.txt Section 8.",
        "record_source_html": "<p><span class=\"file-source-tag\">Settlement Agreements (Nov 2021)</span>; <span class=\"file-source-tag\">Corporate filings and legal docs.txt</span>.</p>"
    },
    {
        "id": "fc-2022-03",
        "item_num": "0.8c",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "March 23, 2022",
        "date_sort": "2022-03-23",
        "title": "WFG National Title Report Discloses Trust Mismatch & Defective Lis Pendens",
        "medium": "Property Information Report (File No. 22-359102)",
        "medium_cat": "Other",
        "from": "WFG National Title Insurance Company",
        "to": "Annika Eriksson",
        "actor_cat": "Other / Unknown",
        "subject": "Title Examination Confirms OC11 Assignment & Lack of Multnomah Action",
        "summary": "WFG National Title Insurance Company issues Title Report File No. 22-359102. Examination reveals the 2012 assignment (Instr. No. 2012-052957) runs to CWALT 2006-OC11 (not OC10) and ZBS Law's 2017 Notice of Pendency of Action was recorded for Multnomah County rather than Clackamas, creating no valid encumbrance against TLH or subsequent grantees.",
        "summary_html": "<p>WFG National Title Insurance Company issues Title Report File No. 22-359102. Examination reveals the 2012 assignment (Instr. No. 2012-052957) runs to CWALT 2006-OC11 (not OC10) and ZBS Law's 2017 Notice of Pendency of Action was recorded for Multnomah County rather than Clackamas, creating no valid encumbrance against TLH or subsequent grantees.</p>",
        "record_source": "WFG National Title Insurance Company Report File No. 22-359102; ORCP 71 Motion Ex. B-6.",
        "record_source_html": "<p><span class=\"file-source-tag\">WFG Title Report 22-359102</span>; <span class=\"file-source-tag\">ORCP 71 Motion Ex. B-6</span>.</p>"
    },
    {
        "id": "hist-0-9",
        "item_num": "0.9",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "August 2022",
        "date_sort": "2022-08-01",
        "title": "Jesse Baker Senior Servicer Flip & Dual-Property Chapter 13 Pincer",
        "medium": "U.S. Bankruptcy Court Docket (Case No. 22-31175-thp13)",
        "medium_cat": "Court Filing / Order",
        "from": "Jesse A.P. Baker / Aldridge Pite, LLP",
        "to": "U.S. Bankruptcy Court / Annika Eriksson",
        "actor_cat": "Other / Unknown",
        "subject": "Coordinated Objection to Confirmation & Beaverton Cross-Attack",
        "summary": "In Annika's Chapter 13 bankruptcy, Jesse Baker flips from representing junior lender CitiMortgage to senior servicer Shellpoint (BNY Mellon / CWALT), attacking Eriksson's deed as 'unauthorized' and filing massive $205,746.40 arrears claim. Baker simultaneously files identical objection for Deutsche Bank on Annika's Beaverton home (1730 SW 203rd Ave), engineering unfeasible stacked demands to torpedo confirmation and force dismissal.",
        "summary_html": "<p>In Annika's Chapter 13 bankruptcy, Jesse Baker flips from representing junior lender CitiMortgage to senior servicer Shellpoint (BNY Mellon / CWALT), attacking Eriksson's deed as 'unauthorized' and filing massive $205,746.40 arrears claim. Baker simultaneously files identical objection for Deutsche Bank on Annika's Beaverton home (1730 SW 203rd Ave), engineering unfeasible stacked demands to torpedo confirmation and force dismissal.</p>",
        "record_source": "U.S. Bankruptcy Court Case No. 22-31175-thp13 Docket; Proof of Claim 4-1; GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 22-31175-thp13</span>; <span class=\"file-source-tag\">Proof of Claim 4-1</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "hist-0-10",
        "item_num": "0.10",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "October 2022",
        "date_sort": "2022-10-01",
        "title": "City Enacts OCMC Chapter 15.11 (Distressed Residential Property Ordinance)",
        "medium": "Municipal Ordinance Enactment",
        "medium_cat": "Other",
        "from": "City of Oregon City Commission",
        "to": "City Code Enforcement Division / Property Servicers",
        "actor_cat": "City Leadership",
        "subject": "Servicer Accountability Framework & Regulatory Gaps Exploited at Chapin Court",
        "summary": "Oregon City adopts OCMC Chapter 15.11 with the purported legislative intent to place affirmative maintenance and security responsibilities on mortgage servicers and foreclosing entities for abandoned or distressed properties. However, because the City failed to enforce the ordinance against major servicers, failed to account for multi-year contested foreclosures where ownership is actively disputed in court, and failed to address pre-existing foreclosures initiated years earlier, it engineered a massive regulatory gap. This enforcement void was subsequently exploited against 12054 Chapin Court: while corporate servicer Shellpoint was never held accountable for property maintenance or compliance, the City concentrated administrative liens, escalating daily fines, and prolonged water shutoff enforcement entirely against the disabled resident homeowner.",
        "summary_html": "<p>Oregon City adopts OCMC Chapter 15.11 with the purported legislative intent to place affirmative maintenance and security responsibilities on mortgage servicers and foreclosing entities for abandoned or distressed properties. However, because the City failed to enforce the ordinance against major servicers, failed to account for multi-year contested foreclosures where ownership is actively disputed in court, and failed to address pre-existing foreclosures initiated years earlier, it engineered a massive regulatory gap. This enforcement void was subsequently exploited against 12054 Chapin Court: while corporate servicer Shellpoint was never held accountable for property maintenance or compliance, the City concentrated administrative liens, escalating daily fines, and prolonged water shutoff enforcement entirely against the disabled resident homeowner.</p>",
        "record_source": "OCMC Chapter 15.11; Oregon City Ordinance No. 22-1008; City Commission Records; First Amended Complaint (3:26-cv-01885-IM).",
        "record_source_html": "<p><span class=\"file-source-tag\">OCMC 15.11</span>; <span class=\"file-source-tag\">Ordinance No. 22-1008</span>; <span class=\"file-source-tag\">First Amended Complaint (3:26-cv-01885-IM)</span>.</p>"
    },
    {
        "id": "tlh-homeowner-layne",
        "item_num": "0.11",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "2022 – 2025",
        "date_sort": "2022-11-01",
        "title": "Homeowner Defense: Nancy Kay Layne v. BONYM & ZBS Law Foreclosure Fight",
        "medium": "Circuit Court Pleadings & Quiet Title Challenge",
        "medium_cat": "Court Filing / Order",
        "from": "Nancy Kay Layne (Homeowner)",
        "to": "The Bank of New York Mellon / ZBS Law",
        "actor_cat": "Other / Unknown",
        "subject": "Contesting Securitization Assignment Defects & Robosigned Notes",
        "summary": "Oregon homeowner Nancy Kay Layne prosecutes quiet title action ('Layne QT') and wrongful foreclosure challenge contesting standing defects, missing promissory notes, and robo-signed MERS mortgage assignments executed by ZBS Law. Demonstrates identical pattern of foreclosing entities prosecuting actions without legal privity.",
        "summary_html": "<p>Oregon homeowner Nancy Kay Layne prosecutes quiet title action ('Layne QT') and wrongful foreclosure challenge contesting standing defects, missing promissory notes, and robo-signed MERS mortgage assignments executed by ZBS Law. Demonstrates identical pattern of foreclosing entities prosecuting actions without legal privity.</p>",
        "record_source": "Layne QT Pleading Files; google_drive_intake/review-cycles/2026-08-18/findings.md; Retrospective Justice Engine Research.",
        "record_source_html": "<p><span class=\"file-source-tag\">Layne QT.pdf</span>; <span class=\"file-source-tag\">findings.md</span>; Retrospective Justice Engine.</p>"
    },
    {
        "id": "tlh-homeowner-dysinger",
        "item_num": "0.12",
        "phase_num": 0,
        "phase_title": "0. Phase 0: Historical Foundation & Structural Architecture (1994–2022)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "2023 – 2026",
        "date_sort": "2023-01-01",
        "title": "Homeowner Defense: Janice Dysinger & Tarlecki Foreclosure Challenge & Washington County Quiet Title (23CV50085)",
        "medium": "Circuit Court Foreclosure & Quiet Title Pleadings",
        "medium_cat": "Court Filing / Order",
        "from": "Janice Dysinger, Tarlecki & Annika Eriksson (Homeowners)",
        "to": "Foreclosure Servicers / Mortgage Trustees",
        "actor_cat": "Municipal Court",
        "subject": "Retrospective Justice Benchmark: Predatory Servicing & Void Judgment Challenges",
        "summary": "Oregon homeowners Janice Dysinger and Tarlecki challenge predatory mortgage servicing and defective securitization assignments in parallel with Annika Eriksson's Washington County quiet title action (Case No. 23CV50085) and Clackamas County proceedings (Case Nos. 17CV38591 & 24CV21417), forming the multi-case validation dataset for the Retrospective Justice Engine.",
        "summary_html": "<p>Oregon homeowners Janice Dysinger and Tarlecki challenge predatory mortgage servicing and defective securitization assignments in parallel with Annika Eriksson's Washington County quiet title action (Case No. 23CV50085) and Clackamas County proceedings (Case Nos. 17CV38591 &amp; 24CV21417), forming the multi-case validation dataset for the Retrospective Justice Engine.</p>",
        "record_source": "Washington County Case No. 23CV50085; Dysinger & Tarlecki Foreclosure Files; Retrospective Justice Grant Proposal (proposal.pdf).",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 23CV50085</span>; <span class=\"file-source-tag\">Dysinger &amp; Tarlecki Files</span>; <span class=\"file-source-tag\">Retrospective Justice Proposal</span>.</p>"
    },

    # ==========================================
    # PHASE 1: DISCOVERY & CRISIS ONSET (OCT 2023 - MAY 2024)
    # ==========================================
    {
        "id": "comm-1-4b",
        "item_num": "1.5b",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "January 11, 2024",
        "date_sort": "2024-01-11",
        "title": "City Utility Internal Log Discloses Directive to Demand $867.62 Combining Prior Tenant Arrears",
        "medium": "Internal Utility Billing Account Notes (Fraijo Decl. Ex. 1)",
        "medium_cat": "Notice / Letter (City)",
        "from": "Ashley Flues (City of Oregon City Utility Billing)",
        "to": "Internal Utility Billing Records / Code Enforcement",
        "actor_cat": "City Staff",
        "subject": "Internal Directive to Combine Prior Tenant Stephanie Jones's $606.60 Arrears with New Resident Account",
        "summary": "City Utility Billing staffer Ashley Flues logs an internal account note stating: 'This address was shut off back on 10/3 and then someone turned it back on. Code confirmed it is Annika in the house - D/H for the full amount of Stephanie Jones account and this account + $25.00 to equal $867.62.' This internal note—later produced by the City as Exhibit 1 to Ashley Fraijo's federal court declaration—reveals that City utility staff internally directed a door hanger combining prior tenant Stephanie Jones's unpaid $606.60 debt (Account 01-466348-04) with Eriksson's first two water bills ($236.02 on Account 01-466348-05). While the accounts were never formally merged in the online customer portal (where Jones's account remained separate), Fraijo's filing revealed the City's internal posture of seeking to hold the incoming occupant responsible for the prior tenant's debt.",
        "summary_html": "<p>City Utility Billing staffer Ashley Flues logs an internal account note stating: <em>\"This address was shut off back on 10/3 and then someone turned it back on. Code confirmed it is Annika in the house - D/H for the full amount of Stephanie Jones account and this account + $25.00 to equal $867.62.\"</em> This internal note—later produced by the City as Exhibit 1 to Ashley Fraijo's federal court declaration—reveals that City utility staff internally directed a door hanger combining prior tenant Stephanie Jones's unpaid $606.60 debt (Account 01-466348-04) with Eriksson's first two water bills ($236.02 on Account 01-466348-05). While the accounts were never formally merged in the online customer portal (where Jones's account remained separate), Fraijo's filing revealed the City's internal posture of seeking to hold the incoming occupant responsible for the prior tenant's debt.</p>",
        "record_source": "Fraijo Decl. Exs. 1–4 (Internal City Utility Billing Notes & Account Ledgers 01-466348-04 & 01-466348-05); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Fraijo Decl. Exs. 1–4</span>; <span class=\"file-source-tag\">Account 01-466348-05 Ledger</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "fc-2023-09-sheriff",
        "item_num": "1.4b",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "September 7–19, 2023",
        "date_sort": "2023-09-19",
        "title": "Sheriff Pre-Sale Certified Mailings Omit Recorded Owner Annika Eriksson; 5 Envelopes Returned (23-20024)",
        "medium": "Sheriff's Pre-Sale File, Instructions & USPS Certified Mail Strips (23-20024)",
        "medium_cat": "Court Filing / Order",
        "from": "ZBS Law, LLP (Jeffrey A. Myers) / Clackamas County Sheriff",
        "to": "9 Notice Recipients (Omitting Annika Eriksson)",
        "actor_cat": "Municipal Court",
        "subject": "Pre-Sale Certified Mailings Under ORS 18.888/18.918 & Total Omission of Fee Owner",
        "summary": "On September 7, 2023, ZBS Law (Jeffrey A. Myers) issued Instructions to Sheriff directing Certified and First-Class Mail notice to 9 recipients while completely omitting recorded fee-simple owner Annika Eriksson (whose Bargain & Sale Deed, Instr. No. 2021-109930, had been recorded Dec 20, 2021) and asserting under ORS 18.904(2) that 'a copy of the Judgment is not required to be attached.' On Sept 19, 2023, the Sheriff mailed 9 Certified Mail packets (7020 3160 0000 0262 5640 through 5725): Sherry Garboden (5640), Elbert Garboden (5657), and All Other Unknown Parties at 12054 Chapin Ct (5718) were returned UNCLAIMED; Turning Leaf Homes LLC (5671) and dissolved Fite LLC (5688) at Oak Shore Lane were returned NOT DELIVERABLE AS ADDRESSED / UTF; TLH (5664) and Fite LLC (5695) were sent to withdrawn counsel Andrew Glascock; only Citimortgage (5701) and Oregon Dept of Revenue (5725) were delivered.",
        "summary_html": "<p>On September 7, 2023, ZBS Law (Jeffrey A. Myers) issued Instructions to Sheriff directing Certified and First-Class Mail notice to 9 recipients while <strong>completely omitting recorded fee-simple owner Annika Eriksson</strong> (whose Bargain &amp; Sale Deed, Instr. No. 2021-109930, had been recorded Dec 20, 2021) and asserting under ORS 18.904(2) that <em>\"a copy of the Judgment is not required to be attached.\"</em> On Sept 19, 2023, the Sheriff mailed 9 Certified Mail packets (7020 3160 0000 0262 5640 through 5725): Sherry Garboden (5640), Elbert Garboden (5657), and All Other Unknown Parties at 12054 Chapin Ct (5718) were <strong>returned UNCLAIMED</strong>; Turning Leaf Homes LLC (5671) and dissolved Fite LLC (5688) at Oak Shore Lane were <strong>returned NOT DELIVERABLE AS ADDRESSED / UTF</strong>; TLH (5664) and Fite LLC (5695) were sent to <strong>withdrawn counsel Andrew Glascock</strong>; only Citimortgage (5701) and Oregon Dept of Revenue (5725) were delivered.</p>",
        "record_source": "Sheriff's Case No. 23-20024 File (Sale_File.pdf pp. 1–7; 23-24_returned_mail_20231121102023.pdf); USPS Tracking & Green Cards; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Sheriff's File 23-20024</span>; <span class=\"file-source-tag\">Sale_File.pdf pp. 1–7</span>; <span class=\"file-source-tag\">Returned Mail Scans</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "fc-2023-11",
        "item_num": "1.4c",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "October 27 – November 1, 2023",
        "date_sort": "2023-11-01",
        "title": "Sheriff Execution Sale: Labrecque Written Credit Bid ($465,396.39) & Sole Bidder Rain City Capital",
        "medium": "Written Credit Bid Letter, Auction Script & Bidder Registration Sheet (23-20024)",
        "medium_cat": "Court Filing / Order",
        "from": "Amber L. Labrecque (ZBS Law) / Adrianna Ramirez (Sheriff Management Analyst)",
        "to": "Clackamas County Sheriff Civil Division / Public Auction Attendees",
        "actor_cat": "Municipal Court",
        "subject": "Execution Sale of 12054 Chapin Court, Electronic Credit Bid & Bidder Registration",
        "summary": "On October 27, 2023, Amber L. Labrecque of ZBS Law submitted a written credit bid letter via electronic service instructing the Sheriff: 'Please bid in the amount of $465,396.39' on behalf of BNYM-OC10. At the November 1, 2023 (10:00 AM) auction at 9101 SE Sunnybrook Blvd., Clackamas, OR, Senior Management Analyst Adrianna Ramirez conducted the sale. Neither BNYM nor ZBS Law appeared in person. Only one prospective bidder signed the Bidder Registration Sheet: #1) Rain City Capital of Oregon (12131 113th Ave NE #201, Kirkland, WA 98037). Rain City Capital placed no bid, and lines #2–#6 were blank. Annika Eriksson filed a formal objection to the sale on December 19, 2023.",
        "summary_html": "<p>On October 27, 2023, <strong>Amber L. Labrecque</strong> of ZBS Law submitted a written credit bid letter via electronic service instructing the Sheriff: <strong>\"Please bid in the amount of $465,396.39\"</strong> on behalf of BNYM-OC10. At the November 1, 2023 (10:00 AM) auction at 9101 SE Sunnybrook Blvd., Senior Management Analyst Adrianna Ramirez conducted the sale. Neither BNYM nor ZBS Law appeared in person. Only <strong>one single prospective bidder</strong> signed the Bidder Registration Sheet: <strong>#1) Rain City Capital of Oregon</strong>. Rain City Capital placed no bid, and lines #2–#6 were blank. Annika Eriksson filed a formal objection to the sale on December 19, 2023.</p>",
        "record_source": "Sheriff's Case No. 23-20024 File (Sale_File.pdf pp. 8–10); Bidder Registration Sheet; ZBS Credit Bid Letter dated 10/27/2023; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Sheriff's File 23-20024</span>; <span class=\"file-source-tag\">Sale_File.pdf pp. 8–10</span>; <span class=\"file-source-tag\">ZBS Credit Bid Letter</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-1-5b",
        "item_num": "1.6b",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "January 22–23 & April 1–9, 2024",
        "date_sort": "2024-01-22",
        "title": "Mid-Winter Water Shutoff & Project Access NOW Assistance Payments ($311.02 & $266.22)",
        "medium": "Disconnection Order, Charitable Payments & City Billing Logs",
        "medium_cat": "Billing Statement",
        "from": "Jonathan (Project Access NOW) / City of Oregon City Utility Billing",
        "to": "Account 01-466348-05 (Annika Eriksson)",
        "actor_cat": "City Staff",
        "subject": "January 22 Shutoff, $311.02 Project Access NOW Reconnection Payment & April $266.22 Payment",
        "summary": "On January 22, 2024, Oregon City physically shuts off residential water service and adds a $50.00 shutoff fee, bringing Eriksson's Account 01-466348-05 balance to $311.02 ($236.02 usage + $25.00 door hanger + $50.00 shutoff fee). On January 23, 2024 (Batch B00015794, Receipt R00738478), Jonathan from Project Access NOW pays $311.02 on Eriksson's behalf to restore water service, while John Oreskovich assesses another $50.00 meter tampering fee (paid Feb 22, 2024). Subsequently, per Oreskovich's April 1, 2024 account log ('Project Access: PA will be paying the full amount'), Project Access NOW remits a second assistance payment of $266.22 on April 9, 2024 (Batch B00016405, Receipt R00763703), covering the January ($128.93) and February ($137.29) statements.",
        "summary_html": "<p>On January 22, 2024, Oregon City physically shuts off residential water service and adds a $50.00 shutoff fee, bringing Eriksson's Account 01-466348-05 balance to <strong>$311.02</strong> ($236.02 usage + $25.00 door hanger + $50.00 shutoff fee). On January 23, 2024 (Batch B00015794, Receipt R00738478), <strong>Jonathan from Project Access NOW</strong> pays <strong>$311.02</strong> on Eriksson's behalf to restore water service, while John Oreskovich assesses another $50.00 meter tampering fee (paid Feb 22, 2024). Subsequently, per Oreskovich's April 1, 2024 account log (<em>\"Project Access: PA will be paying the full amount\"</em>), Project Access NOW remits a second assistance payment of <strong>$266.22</strong> on April 9, 2024 (Batch B00016405, Receipt R00763703), covering the January ($128.93) and February ($137.29) statements.</p>",
        "record_source": "Fraijo Decl. Exs. 1–3 (Utility Account 01-466348-05 Ledger & Internal Notes); Receipts R00738478 & R00763703; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Fraijo Decl. Exs. 1–3</span>; <span class=\"file-source-tag\">Receipts R00738478 &amp; R00763703</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "fc-2024-01",
        "item_num": "1.5c",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "January 25, 2024",
        "date_sort": "2024-01-25",
        "title": "Sheriff Certificate of Sale Recorded; No Sheriff Deed Ever Executed",
        "medium": "County Deed Records (Instr. No. 2024-002834)",
        "medium_cat": "Court Filing / Order",
        "from": "Clackamas County Sheriff",
        "to": "The Bank of New York Mellon",
        "actor_cat": "Municipal Court",
        "subject": "Absence of Conveyance Deed Leaves Fee Title in Eriksson",
        "summary": "Clackamas County Sheriff records Certificate of Sale as Instrument No. 2024-002834. Crucially, as certified by official deed searches in 2026, no Sheriff's Deed was ever executed or recorded. Under Oregon law (ORS 18.942), fee legal title remains vested in record owner Annika Eriksson.",
        "summary_html": "<p>Clackamas County Sheriff records Certificate of Sale as Instrument No. 2024-002834. Crucially, as certified by official deed searches in 2026, no Sheriff's Deed was ever executed or recorded. Under Oregon law (ORS 18.942), fee legal title remains vested in record owner Annika Eriksson.</p>",
        "record_source": "Clackamas County Deed Records Instr. No. 2024-002834; Title Search Verification; ORCP 71 Motion Eriksson Decl. ¶ 15.",
        "record_source_html": "<p><span class=\"file-source-tag\">Clackamas Rec. No. 2024-002834</span>; <span class=\"file-source-tag\">ORCP 71 Motion Ex. I-1</span>.</p>"
    },
    {
        "id": "fc-2024-04-posthearing",
        "item_num": "1.5d",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "December 19, 2023 – April 8, 2024",
        "date_sort": "2024-01-25",
        "title": "Post-Objection Motions, Jan 22 Non-Oral Hearing, Myers Email Objection & Contested Denial Order",
        "medium": "Circuit Court Motions, Email Correspondence & Judicial Denial Order (17CV38591)",
        "medium_cat": "Court Filing / Order",
        "from": "Annika Eriksson / Jeffrey A. Myers (ZBS Law) / Hon. Michael C. Wetzel",
        "to": "Clackamas County Circuit Court",
        "actor_cat": "Municipal Court",
        "subject": "Denial of Post-Hearing Motions as Moot & Email Objection That Judge Wetzel Did Not Rule on Vacatur",
        "summary": "Following the Dec 19, 2023 objection hearing where Judge Wetzel orally rejected Eriksson's objection to the sale as untimely, Eriksson filed a post-hearing Motion to Set Aside Void Sheriff's Sale and Dismiss Case on Dec 19, 2023 (Ex. O-4), calendared for a Non-Oral Hearing on Jan 22, 2024 at 8:45 AM before Judge Eric James Tait (canceled ... other). Myers's Jan 12, 2024 proposed order was marked 'Unsigned. Moot.' on Jan 23, 2024 (Ex. W-1). On Jan 25, 2024 at 4:30 PM, Eriksson emailed Myers (Ex. Z-1) objecting that Judge Wetzel never ruled on her motion to vacate the judgment; Myers refused to remove the denial language (Ex. Z-2, 5:25 PM) and filed the order with emails attached (rejected Jan 26 as 'UNSIGNED: Needs to be filed without exhibits attached', Ex. W-2). On April 2, 2024 (entered April 8), Judge Wetzel entered Myers's order denying both the objection to sale and motion to set aside the judgment (Ex. T-1). On April 30, 2024, Amber Labrecque requested the Sheriff's Deed, executed May 9, 2024 and never recorded.",
        "summary_html": "<p>Following the Dec 19, 2023 objection hearing where Judge Wetzel orally rejected Eriksson's objection to the sale as untimely, Eriksson filed a post-hearing <strong>Motion to Set Aside Void Sheriff's Sale and Dismiss Case</strong> on Dec 19, 2023 (Ex. O-4), calendared for a <strong>Non-Oral Hearing on Jan 22, 2024 at 8:45 AM before Judge Eric James Tait</strong> (canceled ... other). Myers's Jan 12, 2024 proposed order was marked <em>\"Unsigned. Moot.\"</em> on Jan 23, 2024 (Ex. W-1). On Jan 25, 2024 at 4:30 PM, Eriksson emailed Myers (Ex. Z-1) objecting that Judge Wetzel never ruled on her motion to vacate the judgment; Myers refused to remove the denial language (Ex. Z-2, 5:25 PM) and filed the order with emails attached (rejected Jan 26 as <em>\"UNSIGNED: Needs to be filed without exhibits attached\"</em>, Ex. W-2). On April 2, 2024 (entered April 8), Judge Wetzel entered Myers's order denying both the objection to sale and motion to set aside the judgment (Ex. T-1). On April 30, 2024, Amber Labrecque requested the Sheriff's Deed, executed May 9, 2024 and never recorded.</p>",
        "record_source": "Case 17CV38591 Register of Actions (Ex. O-4); Order - Denial (Ex. T-1); Proposed Orders (Exs. W-1, W-2); Eriksson-Myers Emails (Exs. Z-1, Z-2); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Register of Actions (Ex. O-4)</span>; <span class=\"file-source-tag\">Order - Denial (Ex. T-1)</span>; <span class=\"file-source-tag\">Proposed Orders (Exs. W-1, W-2)</span>; <span class=\"file-source-tag\">Emails (Exs. Z-1, Z-2)</span>.</p>"
    },
    {
        "id": "fc-2024-05",
        "item_num": "1.10d",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "May 2, 2024",
        "date_sort": "2024-05-02",
        "title": "Annika Eriksson Files Quiet Title Action & Records Lis Pendens (24CV21417)",
        "medium": "Circuit Court Complaint & Notice of Pendency (Instr. No. 2024-015436)",
        "medium_cat": "Court Filing / Order",
        "from": "Annika Eriksson",
        "to": "BONYM / Shellpoint / City of Oregon City / Security Title Guarantee",
        "actor_cat": "Municipal Court",
        "subject": "Affirmative Title Challenge & Statutory Notice to Encumbrancers",
        "summary": "Annika Eriksson files Complaint for Quiet Title in Clackamas County Circuit Court (Case No. 24CV21417) and records formal Notice of Pendency of Action in Official Records (Instr. No. 2024-015436). Action challenges void 2019 judgment, trust mismatch, lack of note holder standing, and municipal utility liens.",
        "summary_html": "<p>Annika Eriksson files Complaint for Quiet Title in Clackamas County Circuit Court (Case No. 24CV21417) and records formal Notice of Pendency of Action in Official Records (Instr. No. 2024-015436). Action challenges void 2019 judgment, trust mismatch, lack of note holder standing, and municipal utility liens.</p>",
        "record_source": "Clackamas County Case No. 24CV21417 Docket; Clackamas County Official Records Fee No. 2024-015436; Legal case compilation.txt.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 24CV21417</span>; <span class=\"file-source-tag\">Clackamas Rec. No. 2024-015436</span>.</p>"
    },
    {
        "id": "comm-1-10b",
        "item_num": "1.10b",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "May 2024",
        "date_sort": "2024-05-15",
        "title": "Landsat Thermal Telemetry Confirms +12°F Chapin Court Heat Island",
        "medium": "Satellite Thermal Radiometry & GIS Analysis",
        "medium_cat": "Other",
        "from": "USGS / Landsat 8-9 Thermal Infrared Sensor (TIRS)",
        "to": "Forensic Microclimate Research Workspace",
        "actor_cat": "Other / Unknown",
        "subject": "Empirical Surface Temperature & Canopy Deficit Telemetry",
        "summary": "Satellite radiometric telemetry analyzed across South End neighborhood confirms Chapin Court cul-de-sac registers 10°F to 12°F hotter than surrounding tree-canopied zones. Empirical verification that City-mandated canopy removal directly caused dangerous localized extreme heat conditions for disabled resident suffering from heat-vulnerable hyperthyroidism.",
        "summary_html": "<p>Satellite radiometric telemetry analyzed across South End neighborhood confirms Chapin Court cul-de-sac registers 10°F to 12°F hotter than surrounding tree-canopied zones. Empirical verification that City-mandated canopy removal directly caused dangerous localized extreme heat conditions for disabled resident suffering from heat-vulnerable hyperthyroidism.</p>",
        "record_source": "Landsat 8/9 Band 10 Thermal Infrared Radiometry; forensic-microclimate.html (Slide 3); Case Ground Truth and Evidence Map.",
        "record_source_html": "<p><a href=\"forensic-microclimate.html#slide-3\">forensic-microclimate.html (Slide 3)</a>; <span class=\"file-source-tag\">Landsat Telemetry Analysis</span>.</p>"
    },
    {
        "id": "comp-2024-05",
        "item_num": "1.10c",
        "phase_num": 1,
        "phase_title": "1. Phase 1: Discovery & Crisis Onset (Oct 2023 – May 2024)",
        "layer": "comparator",
        "layer_title": "Vetted Comparators",
        "date_time": "May 1, 2024",
        "date_sort": "2024-05-01",
        "title": "Comparator: Resolution 24-16 — Clackamas Community College Sewer Relief",
        "medium": "City Commission Resolution & Staff Report",
        "medium_cat": "Other",
        "from": "City of Oregon City Commission",
        "to": "Clackamas Community College (Public Institution)",
        "actor_cat": "City Leadership",
        "subject": "Institutional Debt Forgiveness vs Residential Shutoff Disparity",
        "summary": "City Commission passes Resolution 24-16 granting ~$36,900 per year in sewer billing relief and debt forbearance to Clackamas Community College. While providing institutional relief, the City strictly refused administrative review, lifeline payment plans, or health forbearance to residential water customers, cutting off Annika Eriksson 54 days later.",
        "summary_html": "<p>City Commission passes Resolution 24-16 granting ~$36,900 per year in sewer billing relief and debt forbearance to Clackamas Community College. While providing institutional relief, the City strictly refused administrative review, lifeline payment plans, or health forbearance to residential water customers, cutting off Annika Eriksson 54 days later.</p>",
        "record_source": "Oregon City Resolution 24-16; Commission Meeting Minutes May 1, 2024; Julius AI Investigation Digest.",
        "record_source_html": "<p><span class=\"file-source-tag\">Resolution 24-16</span>; <span class=\"file-source-tag\">00_JULIUS_AI_GLEANING_DIGEST.md</span>.</p>"
    },

    # ==========================================
    # PHASE 2: INITIAL DISCONNECTION & RETALIATION SPIKE (JUN 2024 - SEP 2024)
    # ==========================================
    {
        "id": "comm-2-3b",
        "item_num": "2.3b",
        "phase_num": 2,
        "phase_title": "2. Phase 2: Initial Disconnection & Retaliation Spike (Jun 2024 – Sep 2024)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "July 3, 2024",
        "date_sort": "2024-07-03",
        "title": "City Proclaims Disability Pride Month Amid Simultaneous Water Disconnection",
        "medium": "Mayoral Proclamation & Public Video Archive",
        "medium_cat": "Public Meeting / Testimony",
        "from": "Mayor Denyse McGriff / Oregon City Commission",
        "to": "Oregon City Public",
        "actor_cat": "City Leadership",
        "subject": "Disability Pride Proclamation During Active Deprivation",
        "summary": "Mayor McGriff reads formal proclamation declaring July 2024 'Disability Pride Month,' affirming City's dedication to accessibility and inclusion. Concurrently, eight days earlier, City crews severed municipal water to disabled resident Annika Eriksson, enforcing catastrophic hygiene and hydration deprivation on Day 9 of what became a 510-day shutoff.",
        "summary_html": "<p>Mayor McGriff reads formal proclamation declaring July 2024 'Disability Pride Month,' affirming City's dedication to accessibility and inclusion. Concurrently, eight days earlier, City crews severed municipal water to disabled resident Annika Eriksson, enforcing catastrophic hygiene and hydration deprivation on Day 9 of what became a 510-day shutoff.</p>",
        "record_source": "Oregon City Commission Regular Meeting Minutes & Video Archive (July 3, 2024); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Commission Minutes July 3, 2024</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-2-6b",
        "item_num": "2.6b",
        "phase_num": 2,
        "phase_title": "2. Phase 2: Initial Disconnection & Retaliation Spike (Jun 2024 – Sep 2024)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "July 8, 2024",
        "date_sort": "2024-07-08",
        "title": "OCMC 8.20 Monopoly: Rapid Solid Waste Cutoff Without Lifeline Protections",
        "medium": "Utility Inter-Departmental Notice",
        "medium_cat": "Notice / Letter (City)",
        "from": "Oregon City Code Compliance / Clackamas Garbage",
        "to": "Annika Eriksson (12054 Chapin Court)",
        "actor_cat": "City Staff",
        "subject": "Mandatory Solid Waste Franchise Termination",
        "summary": "Under OCMC 8.20 franchise monopoly rules, City utility triggers immediate suspension of mandatory solid waste disposal following water disconnection. City weaponizes lack of trash pickup within weeks by initiating code enforcement citations for yard debris and accumulated bins, engineering compounded code violations.",
        "summary_html": "<p>Under OCMC 8.20 franchise monopoly rules, City utility triggers immediate suspension of mandatory solid waste disposal following water disconnection. City weaponizes lack of trash pickup within weeks by initiating code enforcement citations for yard debris and accumulated bins, engineering compounded code violations.</p>",
        "record_source": "OCMC Chapter 8.20; Utility Billing Records; Case Ground Truth and Evidence Map.",
        "record_source_html": "<p><span class=\"file-source-tag\">OCMC Chapter 8.20</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-2-14b",
        "item_num": "2.14b",
        "phase_num": 2,
        "phase_title": "2. Phase 2: Initial Disconnection & Retaliation Spike (Jun 2024 – Sep 2024)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "September 4, 2024 (Morning)",
        "date_sort": "2024-09-04",
        "title": "Post-Acquittal Red Placard Backdated to August 4, 2024 (Kennedy + 5 Officers)",
        "medium": "Dangerous Building Placard & Police Dispatch Log",
        "medium_cat": "Notice / Letter (City)",
        "from": "Building Official James Sayers / Code Officer Todd Kennedy / OCPD",
        "to": "12054 Chapin Court Occupants",
        "actor_cat": "Police / Code Enforcement",
        "subject": "Retaliatory Vacate Order Following Municipal Court Trial",
        "summary": "Immediately following Municipal Court hearing resulting in recusal, Code Compliance Officer Kennedy, Building Official Sayers, and five armed police officers appear at 12054 Chapin Court, order occupants to vacate, and affix an UNSAFE / DANGEROUS BUILDING red placard backdated by exactly 31 days to August 4, 2024. Backdating fabricates expired appeal timelines to bypass pre-deprivation due process.",
        "summary_html": "<p>Immediately following Municipal Court hearing resulting in recusal, Code Compliance Officer Kennedy, Building Official Sayers, and five armed police officers appear at 12054 Chapin Court, order occupants to vacate, and affix an UNSAFE / DANGEROUS BUILDING red placard backdated by exactly 31 days to August 4, 2024. Backdating fabricates expired appeal timelines to bypass pre-deprivation due process.</p>",
        "record_source": "Red Placard (Backdated 08/04/2024); OCPD Incident Log 24-018224; Sayers Deposition Exhibit; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Placard Photo (09/04/2024)</span>; <span class=\"file-source-tag\">OCPD CAD Log</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "tlh-homeowner-nguyen",
        "item_num": "2.15b",
        "phase_num": 2,
        "phase_title": "2. Phase 2: Initial Disconnection & Retaliation Spike (Jun 2024 – Sep 2024)",
        "layer": "tlh-zbs",
        "layer_title": "Turning Leaf & ZBS Network",
        "date_time": "September 2024",
        "date_sort": "2024-09-15",
        "title": "Homeowner Defense: Thanh Nguyen Resists Foreclosure & Duplicate Liens",
        "medium": "County Records & Business Property Defense",
        "medium_cat": "Other",
        "from": "Thanh Nguyen (Homeowner / Builder)",
        "to": "Loan Servicing Entities / Clackamas County",
        "actor_cat": "Other / Unknown",
        "subject": "Systemic Resistance to Servicer Overcharges & Disputed Liens",
        "summary": "Homeowner and builder Thanh Nguyen resists predatory foreclosure maneuvers, duplicate lien docketing, and servicing misrepresentations across Clackamas and Multnomah properties, representing another parallel node of Oregon property owners fighting against institutional foreclosure abuses.",
        "summary_html": "<p>Homeowner and builder Thanh Nguyen resists predatory foreclosure maneuvers, duplicate lien docketing, and servicing misrepresentations across Clackamas and Multnomah properties, representing another parallel node of Oregon property owners fighting against institutional foreclosure abuses.</p>",
        "record_source": "Corporate and Property Filings (Happy Valley / Clackamas); Retrospective Justice Engine Homeowner Network; intake/Court files/new_view.csv.",
        "record_source_html": "<p><span class=\"file-source-tag\">new_view.csv</span>; Retrospective Justice Homeowner Network.</p>"
    },

    # ==========================================
    # PHASE 4: WINTER FREEZE & ENTRENCHMENT (NOV 2024 - MAR 2025)
    # ==========================================
    {
        "id": "comm-4-2b",
        "item_num": "4.2b",
        "phase_num": 4,
        "phase_title": "4. Phase 4: Winter Freeze & Entrenchment (Nov 2024 – Mar 2025)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "November 1, 2024",
        "date_sort": "2024-11-01",
        "title": "Building Official Sayers Written Admission: Water Cutoff Causes Sewer Gas Influx",
        "medium": "Official Building Division Notice Letter (Ex. 14)",
        "medium_cat": "Notice / Letter (City)",
        "from": "James Sayers (Building Official)",
        "to": "Annika Eriksson",
        "actor_cat": "City Staff",
        "subject": "Plumbing Trap Evaporation & Structural Health Hazards",
        "summary": "Building Official James Sayers issues a formal letter to Annika Eriksson (Ex. 14) admitting in writing: 'Without running water, the sewer gases come up through the drainpipes and contaminate the living areas... Because of this, the home is considered a Dangerous Building.' Establishes the City knowingly manufactured the exact hazardous biological condition it cited to declare the residence dangerous and uninhabitable.",
        "summary_html": "<p>Building Official James Sayers issues a formal letter to Annika Eriksson (Ex. 14) admitting in writing: <em>\"Without running water, the sewer gases come up through the drainpipes and contaminate the living areas... Because of this, the home is considered a Dangerous Building.\"</em> Establishes the City knowingly manufactured the exact hazardous biological condition it cited to declare the residence dangerous and uninhabitable.</p>",
        "record_source": "Building Official Sayers Letter (Nov 1, 2024, Ex. 14); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Sayers Letter (Nov 1, 2024, Ex. 14)</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-4-3b",
        "item_num": "4.3b",
        "phase_num": 4,
        "phase_title": "4. Phase 4: Winter Freeze & Entrenchment (Nov 2024 – Mar 2025)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "November 5, 2024 – March 2025",
        "date_sort": "2024-11-05",
        "title": "Shellpoint Disburses $2,863.77 Curing Check; Fraijo Holds Check 4 Months & Returns It Unapplied",
        "medium": "Servicer Escrow Disbursement Check & City Billing Records (Exs. 21–23)",
        "medium_cat": "Billing Statement",
        "from": "NewRez LLC d/b/a Shellpoint Mortgage Servicing / Ashley Fraijo",
        "to": "City of Oregon City Utility Billing",
        "actor_cat": "City Staff",
        "subject": "4-Month Suppression of $2,863.77 Curing Check & Return Without Application",
        "summary": "Shellpoint disburses a $2,863.77 check (dated November 5, 2024) to Oregon City to satisfy municipal utility charges on 12054 Chapin Court. Customer Accounting Coordinator Ashley Fraijo holds the check for four months without applying it or notifying Plaintiffs while communicating with private real estate broker Damien Pogue, before returning the check unapplied to Shellpoint in March 2025 to preserve the physical water shutoff.",
        "summary_html": "<p>Shellpoint disburses a $2,863.77 check (dated November 5, 2024) to Oregon City to satisfy municipal utility charges on 12054 Chapin Court. Customer Accounting Coordinator Ashley Fraijo holds the check for four months without applying it or notifying Plaintiffs while communicating with private real estate broker Damien Pogue, before returning the check unapplied to Shellpoint in March 2025 to preserve the physical water shutoff.</p>",
        "record_source": "Exs. 21–23; Fraijo Decl. ¶ 28; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Exs. 21–23</span>; <span class=\"file-source-tag\">Fraijo Decl. ¶ 28</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-4-4b",
        "item_num": "4.4b",
        "phase_num": 4,
        "phase_title": "4. Phase 4: Winter Freeze & Entrenchment (Nov 2024 – Mar 2025)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "December 2024",
        "date_sort": "2024-12-01",
        "title": "Bancroft Bonding Act & Municipal Lien Monetization ($3.1M Receivables)",
        "medium": "City Annual Financial Report & Audit Statements",
        "medium_cat": "Other",
        "from": "City of Oregon City Finance Department",
        "to": "Oregon City Commission / Municipal Auditors",
        "actor_cat": "City Staff",
        "subject": "Securitization of Civil Code Enforcement Liens via Bancroft Act",
        "summary": "City Comprehensive Annual Financial Report details active monetization of civil code enforcement and sidewalk repair liens under Oregon Bancroft Bonding Act (ORS 223.205). City maintains $3.1M in lien receivables, revealing structural financial incentive to levy aggressive liens against homeowners rather than offering repair grants.",
        "summary_html": "<p>City Comprehensive Annual Financial Report details active monetization of civil code enforcement and sidewalk repair liens under Oregon Bancroft Bonding Act (ORS 223.205). City maintains $3.1M in lien receivables, revealing structural financial incentive to levy aggressive liens against homeowners rather than offering repair grants.</p>",
        "record_source": "City of Oregon City ACFR FY 2024 (Note 7: Assessment Liens); ORS 223.205 et seq.; Case Ground Truth and Evidence Map.",
        "record_source_html": "<p><span class=\"file-source-tag\">City ACFR FY 2024</span>; <span class=\"file-source-tag\">ORS 223.205</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },

    # ==========================================
    # PHASE 5: PROLONGED ISOLATION & FEDERAL INITIATION (APR 2025 - NOV 2025)
    # ==========================================
    {
        "id": "comp-2025-06",
        "item_num": "4.6b",
        "phase_num": 4,
        "phase_title": "4. Phase IV: Winter Freeze, Check Suppression & Tort Claims (November 2024 – August 2025)",
        "layer": "comparator",
        "layer_title": "Vetted Comparators",
        "date_time": "June 10, 2025",
        "date_sort": "2025-06-10",
        "title": "Comparator: McLoughlin Promenade Right-of-Way Forbearance",
        "medium": "City Commission Work Session Minutes & Video",
        "medium_cat": "Public Meeting / Testimony",
        "from": "City Commission / City Manager Anthony Konkol",
        "to": "Promenade Bluff Property Owners",
        "actor_cat": "City Leadership",
        "subject": "Selective Forbearance for Wealthy Bluff Owners vs Yard Fines",
        "summary": "City Commission formal work session directs staff to allow private encroachments (decks, stairways, landscaped patios) to remain indefinitely in public right-of-way for affluent McLoughlin Promenade homeowners. Sharp contrast with ruthless $300-$1,000/day fines and criminal citations against disabled fixed-income residents for natural tree root heaves.",
        "summary_html": "<p>City Commission formal work session directs staff to allow private encroachments (decks, stairways, landscaped patios) to remain indefinitely in public right-of-way for affluent McLoughlin Promenade homeowners. Sharp contrast with ruthless $300-$1,000/day fines and criminal citations against disabled fixed-income residents for natural tree root heaves.</p>",
        "record_source": "City Commission Work Session Minutes (June 10, 2025); Video Archive; Julius AI Investigation Digest; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Work Session Minutes (06/10/2025)</span>; <span class=\"file-source-tag\">00_JULIUS_AI_GLEANING_DIGEST.md</span>.</p>"
    },
    {
        "id": "comm-5-3b",
        "item_num": "4.8b",
        "phase_num": 4,
        "phase_title": "4. Phase IV: Winter Freeze, Check Suppression & Tort Claims (November 2024 – August 2025)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "July 2, 2025",
        "date_sort": "2025-07-02",
        "title": "Second Annual Disability Pride Proclamation on Day 372 of Water Disconnection",
        "medium": "Mayoral Proclamation & Public Video Archive",
        "medium_cat": "Public Meeting / Testimony",
        "from": "Mayor Denyse McGriff / Oregon City Commission",
        "to": "Oregon City Public",
        "actor_cat": "City Leadership",
        "subject": "Second Civic Pride Proclamation During Ongoing Human Rights Violation",
        "summary": "Mayor McGriff re-issues Disability Pride Month Proclamation, lauding city commitment to disabled dignity. At that precise hour, Annika Eriksson was enduring Day 372 without running tap water, forced to haul survival water by hand in sub-tropical summer temperatures exceeding 95°F.",
        "summary_html": "<p>Mayor McGriff re-issues Disability Pride Month Proclamation, lauding city commitment to disabled dignity. At that precise hour, Annika Eriksson was enduring Day 372 without running tap water, forced to haul survival water by hand in sub-tropical summer temperatures exceeding 95°F.</p>",
        "record_source": "Oregon City Commission Meeting Minutes (July 2, 2025); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Commission Minutes July 2, 2025</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comp-2025-07",
        "item_num": "4.8c",
        "phase_num": 4,
        "phase_title": "4. Phase IV: Winter Freeze, Check Suppression & Tort Claims (November 2024 – August 2025)",
        "layer": "comparator",
        "layer_title": "Vetted Comparators",
        "date_time": "July 2025",
        "date_sort": "2025-07-15",
        "title": "Comparator: Burgard v. City of Oregon City (3:25-cv-01198-AR)",
        "medium": "Federal Civil Rights Complaint & City Answer (ECF 17)",
        "medium_cat": "Court Filing / Order",
        "from": "Burgard (Plaintiff)",
        "to": "City of Oregon City (Defendant)",
        "actor_cat": "City Leadership",
        "subject": "Systemic ADA Title II & Section 504 Failure to Accommodate",
        "summary": "Active federal ADA Title II and Rehabilitation Act lawsuit against Oregon City. City Answer (ECF 17) formally admits receiving federal financial assistance and receiving repeated accommodation requests from disabled citizens, while denying legal liability for refusing interactive process.",
        "summary_html": "<p>Active federal ADA Title II and Rehabilitation Act lawsuit against Oregon City. City Answer (ECF 17) formally admits receiving federal financial assistance and receiving repeated accommodation requests from disabled citizens, while denying legal liability for refusing interactive process.</p>",
        "record_source": "U.S. District Court (D. Or. Case No. 3:25-cv-01198-AR, ECF 17); Julius AI Investigation Digest; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case No. 3:25-cv-01198-AR (ECF 17)</span>; <span class=\"file-source-tag\">00_JULIUS_AI_GLEANING_DIGEST.md</span>.</p>"
    },
    {
        "id": "comm-5-5b",
        "item_num": "5.1b",
        "phase_num": 5,
        "phase_title": "5. Phase 5: Prolonged Isolation & Federal Initiation (Apr 2025 – Nov 2025)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "September 29 – October 24, 2025",
        "date_sort": "2025-09-29",
        "title": "Jacob Burgard Public Records Disclosure: Zero Written ADA Policies or Staff Training Materials (Plus Eriksson PRR R001174-102425)",
        "medium": "Official Oregon Public Records Responses (GovQA / Ex. 35)",
        "medium_cat": "Notice / Letter (City)",
        "from": "Office of the City Recorder (Evan Lee)",
        "to": "Jacob Burgard (Sept 29, 2025 ADA Records Request) & Annika Eriksson (Oct 24, 2025 PRR R001174-102425)",
        "actor_cat": "City Staff",
        "subject": "Absence of Written ADA Title II Policies, SOPs, or Staff Training Materials for Preceding 5 Years",
        "summary": "In response to public records requests placed by Jacob Burgard (plaintiff in Burgard v. City of Oregon City, 3:25-cv-01198-AR) asking for the City's written ADA accommodation policies, ADA training materials for City staff, and attempts to designate or hire an ADA Coordinator, the City Recorder formally confirms on September 29, 2025 that Oregon City maintains zero written policies, Standard Operating Procedures (SOPs), directives, or staff training materials regarding ADA accommodations or an ADA Coordinator for the preceding five years (shared by Burgard with Eriksson, Ex. 35). On October 24, 2025, Eriksson submits Public Records Request R001174-102425 seeking OCMC 15.11 distressed property records and Shellpoint communications.",
        "summary_html": "<p>In response to public records requests placed by <strong>Jacob Burgard</strong> (plaintiff in <em>Burgard v. City of Oregon City</em>, <code>3:25-cv-01198-AR</code>) asking for the City's written ADA accommodation policies, ADA training materials for City staff, and attempts to designate or hire an ADA Coordinator, the City Recorder formally confirms on September 29, 2025 that Oregon City maintains zero written policies, Standard Operating Procedures (SOPs), directives, or staff training materials regarding ADA accommodations or an ADA Coordinator for the preceding five years (shared by Burgard with Eriksson, Ex. 35). On October 24, 2025, Eriksson submits Public Records Request <code>R001174-102425</code> seeking OCMC 15.11 distressed property records and Shellpoint communications.</p>",
        "record_source": "City Public Records Response to Jacob Burgard (Sept 29, 2025, Ex. 35); Eriksson PRR R001174-102425 (Oct 24, 2025); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Burgard PRR Response (09/29/2025, Ex. 35)</span>; <span class=\"file-source-tag\">PRR R001174-102425</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-5-3c",
        "item_num": "5.3c",
        "phase_num": 5,
        "phase_title": "5. Phase 5: Prolonged Isolation & Federal Initiation (Apr 2025 – Nov 2025)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "October 26 – November 10, 2025",
        "date_sort": "2025-10-26",
        "title": "Discovery & Webarchive Capture of Hastily Assembled Draft ADA Webpage; Republication Cutting Window to 30 Days",
        "medium": "Webarchive Capture (OC_ADA Grievance.webarchive) & City Webpages",
        "medium_cat": "Records Request",
        "from": "Jacob Burgard & Annika Eriksson / City of Oregon City Web Admin",
        "to": "Public / Evidentiary Record",
        "actor_cat": "City Staff",
        "subject": "Discovery of Live Unedited ADA Grievance Page & Republication Halving Grievance Window",
        "summary": "Following Assistant City Manager Alexandra Troutman's assertion that ADA policies applied only to employees and Burgard's Oct 1 rebuttal citing 28 C.F.R. § 35.107, Annika Eriksson and Jacob Burgard discover Oregon City hastily publishing an unedited draft ADA Grievance page attempting to create retroactive Title II compliance. Burgard inspects and captures the page (OC_ADA Grievance | Oregon City, OR.webarchive, 5.3 MB; ADA grievance website archive.txt), emailing Eriksson: 'Oh this is definitely new… It's being created now. The pages have filler content. The coordinator position is being filled in by Alex Troutman... 100% because of me.' The archived page contains unedited placeholders: [ADA Coordinator Name], ada@oregoncity.gov, (XXX) XXX-XXXX, [ADA Coordinator Office Address], and a 60 calendar day grievance deadline. The City then takes down the page and quietly republishes it around Nov 10, 2025, inserting Alexandra Troutman's contact details and cutting the grievance window in half from 60 days to 30 days.",
        "summary_html": "<p>Following Assistant City Manager Alexandra Troutman's assertion that ADA policies applied only to employees and Burgard's Oct 1 rebuttal citing 28 C.F.R. § 35.107, Annika Eriksson and Jacob Burgard discover Oregon City hastily publishing an unedited draft ADA Grievance page attempting to create retroactive Title II compliance. Burgard inspects and captures the page (<code>OC_ADA Grievance | Oregon City, OR.webarchive</code>, 5.3 MB; <span class=\"file-source-tag\">ADA grievance website archive.txt</span>), emailing Eriksson: <em>\"Oh this is definitely new… It's being created now. The pages have filler content. The coordinator position is being filled in by Alex Troutman... 100% because of me.\"</em> The archived page contains unedited placeholders: <code>[ADA Coordinator Name]</code>, <code>ada@oregoncity.gov</code>, <code>(XXX) XXX-XXXX</code>, <code>[ADA Coordinator Office Address]</code>, and a <strong>60 calendar day</strong> grievance deadline. The City then takes down the page and quietly republishes it around Nov 10, 2025, inserting Alexandra Troutman's contact details and <strong>cutting the grievance window in half from 60 days to 30 days</strong>.</p>",
        "record_source": "OC_ADA Grievance | Oregon City, OR.webarchive (Oct 26, 2025); Emails with Burgard.txt; ADA grievance website archive.txt; Ex. 35; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">OC_ADA Grievance.webarchive</span>; <span class=\"file-source-tag\">Emails with Burgard.txt</span>; <span class=\"file-source-tag\">ADA grievance archive.txt</span>; <span class=\"file-source-tag\">Ex. 35</span>.</p>"
    },
    {
        "id": "comm-5-7b",
        "item_num": "5.7b",
        "phase_num": 5,
        "phase_title": "5. Phase 5: Prolonged Isolation & Federal Initiation (Apr 2025 – Nov 2025)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "November 16, 2025",
        "date_sort": "2025-11-16",
        "title": "Doorstep TRO Standoff: Retained Counsel Ramon Henderson 'Not Happening Today' (510-Day Shutoff Ends)",
        "medium": "Cell Phone Audio Recording & Field Incident Transcript",
        "medium_cat": "Audio Recording / Transcript",
        "from": "Ramon Henderson (Retained City Defense Counsel) / City Utility Crew",
        "to": "Annika Eriksson & Donald Buckhout",
        "actor_cat": "City Legal / Retained Counsel",
        "subject": "Doorstep Liability-Waiver Demand Under Circuit Court TRO & Manual Valve Restoration",
        "summary": "Following the November 14, 2025 Temporary Restraining Order issued by Clackamas County Circuit Court (Case No. 24CV21417) commanding the City to restore potable water by November 16, 2025, City utility personnel arrive accompanied by retained defense attorney Ramon Henderson (Hodgkinson Street Mepham). Henderson blocks the crew from turning the valve and declares on cell phone audio recording that restoration is 'not happening today' unless Plaintiffs sign an un-drafted liability waiver. After Henderson steps away, Donald Buckhout manually turns the curb-stop valve himself, restoring running water and ending the 510-day physical shutoff.",
        "summary_html": "<p>Following the November 14, 2025 Temporary Restraining Order issued by Clackamas County Circuit Court (Case No. 24CV21417) commanding the City to restore potable water by November 16, 2025, City utility personnel arrive accompanied by retained defense attorney Ramon Henderson (Hodgkinson Street Mepham). Henderson blocks the crew from turning the valve and declares on cell phone audio recording that restoration is <em>\"not happening today\"</em> unless Plaintiffs sign an un-drafted liability waiver. After Henderson steps away, Donald Buckhout manually turns the curb-stop valve himself, restoring running water and ending the 510-day physical shutoff.</p>",
        "record_source": "Field Audio Recording & Transcript (11/16/2025); Clackamas County Case No. 24CV21417 TRO; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Audio Recording (11/16/2025)</span>; <span class=\"file-source-tag\">Case 24CV21417 TRO</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },

    # ==========================================
    # PHASE 6: UTILITY RESTORATION & DUAL-TRACK ESCALATION (DEC 2025 - MAY 2026)
    # ==========================================
    {
        "id": "fc-2026-01",
        "item_num": "6.1b",
        "phase_num": 6,
        "phase_title": "6. Phase 6: Utility Restoration & Dual-Track Escalation (Dec 2025 – May 2026)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "January 26, 2026",
        "date_sort": "2026-01-26",
        "title": "Shellpoint Payoff Statement Demands $552,450 ($75k Corporate Advances)",
        "medium": "Formal Payoff Demand (Loan 0579478143)",
        "medium_cat": "Billing Statement",
        "from": "NewRez LLC d/b/a Shellpoint Mortgage Servicing",
        "to": "Annika Eriksson",
        "actor_cat": "Other / Unknown",
        "subject": "Exorbitant Corporate Advance & Interest Accumulation Breakdown",
        "summary": "Shellpoint issues formal payoff quote totaling $552,450.22 on $264,151.04 principal, demanding $200,655.53 in accrued interest (back to Nov 2015), $75,238.82 in unexplained corporate/escrow advances, and $66.94/day per diem, revealing abusive servicer fee stacking.",
        "summary_html": "<p>Shellpoint issues formal payoff quote totaling $552,450.22 on $264,151.04 principal, demanding $200,655.53 in accrued interest (back to Nov 2015), $75,238.82 in unexplained corporate/escrow advances, and $66.94/day per diem, revealing abusive servicer fee stacking.</p>",
        "record_source": "Shellpoint Payoff Statement dated 01/26/2026; Loan 0579478143; GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Shellpoint Payoff Statement</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "comm-6-2b",
        "item_num": "6.2b",
        "phase_num": 6,
        "phase_title": "6. Phase 6: Utility Restoration & Dual-Track Escalation (Dec 2025 – May 2026)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "February 10, 2026",
        "date_sort": "2026-02-10",
        "title": "Public Works Director Dayna Webb Admission: No Administrative Appeal Procedure",
        "medium": "Recorded Public City Commission Work Session",
        "medium_cat": "Public Meeting / Testimony",
        "from": "Dayna Webb (Public Works Director)",
        "to": "Oregon City Commission",
        "actor_cat": "City Leadership",
        "subject": "Systemic Lack of Due Process for Disconnected Customers",
        "summary": "In recorded work session, Public Works Director Dayna Webb explicitly admits to City Commission that Oregon City provides no formal administrative hearing, dispute mechanism, or due process appeal route for residents facing municipal utility termination or disputed municipal billings.",
        "summary_html": "<p>In recorded work session, Public Works Director Dayna Webb explicitly admits to City Commission that Oregon City provides no formal administrative hearing, dispute mechanism, or due process appeal route for residents facing municipal utility termination or disputed municipal billings.</p>",
        "record_source": "City Commission Work Session Video & Minutes (Feb 10, 2026); Federal Civil Rights Action ECF 1; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Commission Work Session Video (02/10/2026)</span>; <span class=\"file-source-tag\">Federal Action ECF 1</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-6-6b",
        "item_num": "6.6b",
        "phase_num": 6,
        "phase_title": "6. Phase 6: Utility Restoration & Dual-Track Escalation (Dec 2025 – May 2026)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "May 20, 2026",
        "date_sort": "2026-05-20",
        "title": "Annika Eriksson Appointed to State DLCD MHOR RAC (OAR 660-047)",
        "medium": "Official State Appointment Notice",
        "medium_cat": "Other",
        "from": "Oregon Department of Land Conservation and Development (DLCD)",
        "to": "Annika Eriksson",
        "actor_cat": "Other / Unknown",
        "subject": "State Rulemaking Advisory Committee Appointment for Housing & Climate",
        "summary": "DLCD appoints Annika Eriksson as official member of the Rulemaking Advisory Committee (RAC) for Mandatory Housing Output Rulemaking (MHOR) under OAR 660-047. Position enables state-level regulatory review of municipal climate resilience, infrastructure liability dumping, and involuntary displacement.",
        "summary_html": "<p>DLCD appoints Annika Eriksson as official member of the Rulemaking Advisory Committee (RAC) for Mandatory Housing Output Rulemaking (MHOR) under OAR 660-047. Position enables state-level regulatory review of municipal climate resilience, infrastructure liability dumping, and involuntary displacement.</p>",
        "record_source": "DLCD Appointment Confirmation; OAR 660-047 Administrative Record; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">DLCD RAC Appointment Letter</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },

    # ==========================================
    # PHASE 7: RETALIATORY ENFORCEMENT & RULEMAKING (JUN 2026 - AUG 2026)
    # ==========================================
    {
        "id": "comm-7-1b",
        "item_num": "7.1b",
        "phase_num": 7,
        "phase_title": "7. Phase 7: Retaliatory Enforcement & Rulemaking (Jun 2026 – Aug 2026)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "June 12, 2026",
        "date_sort": "2026-06-12",
        "title": "Eriksson Testimony to DLCD on Municipal Involuntary Vacancy Traps",
        "medium": "Formal Regulatory Testimony & Policy Submission",
        "medium_cat": "Public Meeting / Testimony",
        "from": "Annika Eriksson (RAC Member)",
        "to": "DLCD RAC & Department Leadership",
        "actor_cat": "Annika Eriksson",
        "subject": "Anti-Displacement Protections in Climate-Stressed Neighborhoods",
        "summary": "Eriksson presents forensic analysis to State RAC demonstrating how local cities weaponize utility shutoffs and sidewalk liability mandates to engineer constructive evictions and cloud property titles, advocating for explicit state anti-displacement protections in OAR 660-047.",
        "summary_html": "<p>Eriksson presents forensic analysis to State RAC demonstrating how local cities weaponize utility shutoffs and sidewalk liability mandates to engineer constructive evictions and cloud property titles, advocating for explicit state anti-displacement protections in OAR 660-047.</p>",
        "record_source": "DLCD RAC Meeting Minutes & Written Submission (June 12, 2026); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">DLCD Submission June 12, 2026</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-7-3b",
        "item_num": "7.3b",
        "phase_num": 7,
        "phase_title": "7. Phase 7: Retaliatory Enforcement & Rulemaking (Jun 2026 – Aug 2026)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "June 23, 2026",
        "date_sort": "2026-06-23",
        "title": "Troutman Categorical ADA Denial: 'ADA Does Not Excuse Code Compliance'",
        "medium": "Official Written ADA Determination (Ex. 20)",
        "medium_cat": "Notice / Letter (City)",
        "from": "Alexandra Troutman (Assistant City Manager & ADA Coordinator)",
        "to": "Annika Eriksson",
        "actor_cat": "City Leadership",
        "subject": "Categorical Rejection of Disability Accommodation for Code Enforcement",
        "summary": "Assistant City Manager and ADA Coordinator Alexandra Troutman issues a written determination within 24 hours declaring: 'The ADA does not excuse compliance with municipal code requirements.' Rejection establishes the City's formal policy of refusing reasonable modifications in code enforcement under Title II of the ADA.",
        "summary_html": "<p>Assistant City Manager and ADA Coordinator Alexandra Troutman issues a written determination within 24 hours declaring: <em>\"The ADA does not excuse compliance with municipal code requirements.\"</em> Rejection establishes the City's formal policy of refusing reasonable modifications in code enforcement under Title II of the ADA.</p>",
        "record_source": "Troutman Written Denial (June 23, 2026, Ex. 20); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Troutman Denial (06/23/2026, Ex. 20)</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-7-5b",
        "item_num": "7.5b",
        "phase_num": 7,
        "phase_title": "7. Phase 7: Retaliatory Enforcement & Rulemaking (Jun 2026 – Aug 2026)",
        "layer": "public-ada",
        "layer_title": "Public Intel & ADA",
        "date_time": "July 1, 2026",
        "date_sort": "2026-07-01",
        "title": "Third Disability Pride Month Proclamation Amid $300/Day Yard Citations",
        "medium": "Mayoral Proclamation & Public Video Archive",
        "medium_cat": "Public Meeting / Testimony",
        "from": "Mayor Denyse McGriff / Oregon City Commission",
        "to": "Oregon City Public",
        "actor_cat": "City Leadership",
        "subject": "Third Annual Mayoral Proclamation",
        "summary": "For third consecutive year, Oregon City Commission passes Disability Pride Month Proclamation while code compliance division prosecutes compounding $300/day fines against disabled resident Eriksson for unpruned shrubbery in extreme summer heat.",
        "summary_html": "<p>For third consecutive year, Oregon City Commission passes Disability Pride Month Proclamation while code compliance division prosecutes compounding $300/day fines against disabled resident Eriksson for unpruned shrubbery in extreme summer heat.</p>",
        "record_source": "City Commission Regular Meeting Minutes (July 1, 2026); CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Commission Minutes July 1, 2026</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-7-6b",
        "item_num": "7.6b",
        "phase_num": 7,
        "phase_title": "7. Phase 7: Retaliatory Enforcement & Rulemaking (Jun 2026 – Aug 2026)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "August 14, 2026",
        "date_sort": "2026-08-14",
        "title": "DLCD Record: Oregon City Opposes State Anti-Displacement Rules",
        "medium": "Official Municipal Regulatory Comment Letter",
        "medium_cat": "Other",
        "from": "City of Oregon City Planning Department",
        "to": "Oregon DLCD Commission",
        "actor_cat": "City Staff",
        "subject": "Opposition to State Mandatory Infrastructure Assistance Rules",
        "summary": "Oregon City submits formal regulatory comments opposing state housing rules requiring municipalities to provide direct sidewalk repair subsidies or climate hardship exemptions, arguing state mandates interfere with local municipal lien authority.",
        "summary_html": "<p>Oregon City submits formal regulatory comments opposing state housing rules requiring municipalities to provide direct sidewalk repair subsidies or climate hardship exemptions, arguing state mandates interfere with local municipal lien authority.</p>",
        "record_source": "DLCD Public Comment Registry (OAR 660-047); City Comment Letter dated 08/14/2026; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">DLCD Registry 08/14/2026</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comm-7-10b",
        "item_num": "7.10b",
        "phase_num": 7,
        "phase_title": "7. Phase 7: Retaliatory Enforcement & Rulemaking (Jun 2026 – Aug 2026)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "August 25, 2026",
        "date_sort": "2026-08-25",
        "title": "$54,600 Municipal Default Judgment: $300/Day Stacking (Timbs Excessive Fine)",
        "medium": "Municipal Court Judgment (Case CE-014675-26)",
        "medium_cat": "Court Filing / Order",
        "from": "Judge Pro Tem Lindgren / Oregon City Municipal Court",
        "to": "Annika Eriksson",
        "actor_cat": "Municipal Court",
        "subject": "Excessive Fines & Default Judgment Following Denied Appearance",
        "summary": "Municipal Court enters staggering $54,600 default judgment against Annika Eriksson by stacking daily penalties of $300/day for tall grass and sidewalk tree roots. Grossly disproportionate penalty violates Eighth Amendment excessive fines clause under Timbs v. Indiana.",
        "summary_html": "<p>Municipal Court enters staggering $54,600 default judgment against Annika Eriksson by stacking daily penalties of $300/day for tall grass and sidewalk tree roots. Grossly disproportionate penalty violates Eighth Amendment excessive fines clause under Timbs v. Indiana.</p>",
        "record_source": "Case No. CE-014675-26 Judgment; Timbs v. Indiana, 139 S. Ct. 682; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case CE-014675-26 Judgment</span>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },

    # ==========================================
    # PHASE 8: SANCTIONS COLLISION & SOVEREIGN RECKONING (SEP 2026 - OCT 2026)
    # ==========================================
    {
        "id": "comm-8-8",
        "item_num": "8.8",
        "phase_num": 8,
        "phase_title": "8. Phase 8: Sanctions Collision & Sovereign Reckoning (Sep 2026 – Oct 2026)",
        "layer": "microclimate-rac",
        "layer_title": "Microclimate & RAC",
        "date_time": "October 3, 2026",
        "date_sort": "2026-10-03",
        "title": "Eriksson Formal Memorandum to LCDC Chair Allan Lazo & Commission",
        "medium": "Formal Regulatory Policy Memorandum & Corpus Link",
        "medium_cat": "Other",
        "from": "Annika Eriksson (MHOR RAC Member)",
        "to": "Allan Lazo (Chair) & Land Conservation and Development Commission",
        "actor_cat": "Annika Eriksson",
        "subject": "Public Comment on Division 047 Infrastructure & Displacement Gaps",
        "summary": "Eriksson transmits detailed policy memorandum to LCDC Chair Allan Lazo and Commissioners, documenting the uncoupling of tree planting mandates from maintenance funding, extreme heat island impacts (+12°F), and recommending state rules requiring municipal safe harbor funds before code enforcement actions.",
        "summary_html": "<p>Eriksson transmits detailed policy memorandum to LCDC Chair Allan Lazo and Commissioners, documenting the uncoupling of tree planting mandates from maintenance funding, extreme heat island impacts (+12°F), and recommending state rules requiring municipal safe harbor funds before code enforcement actions.</p>",
        "record_source": "LCDC Division 047 Docket; OAR_660_047_V5_Public_Comment_Eriksson.md; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">LCDC Docket 10/03/2026</span>; <a href=\"forensic-microclimate.html\">forensic-microclimate.html</a>; <span class=\"file-source-tag\">CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md</span>.</p>"
    },
    {
        "id": "comp-2026-10",
        "item_num": "8.8b",
        "phase_num": 8,
        "phase_title": "8. Phase 8: Sanctions Collision & Sovereign Reckoning (Sep 2026 – Oct 2026)",
        "layer": "comparator",
        "layer_title": "Vetted Comparators",
        "date_time": "October 7, 2026",
        "date_sort": "2026-10-07",
        "title": "Ordinance No. 26-1007: City Moves to Triple Code Fines ($300 to $1,000/Day)",
        "medium": "City Commission First Reading & Staff Report",
        "medium_cat": "Other",
        "from": "City of Oregon City Commission",
        "to": "Oregon City Residents",
        "actor_cat": "City Leadership",
        "subject": "Drastic Escalation of Compounding Municipal Penalties",
        "summary": "City Commission conducts first reading of Ordinance No. 26-1007, voting to increase municipal code violation maximum fines from $300/day to $1,000/day. Escalates punitive extraction apparatus against vulnerable property owners while ongoing federal civil rights challenge is actively pending.",
        "summary_html": "<p>City Commission conducts first reading of Ordinance No. 26-1007, voting to increase municipal code violation maximum fines from $300/day to $1,000/day. Escalates punitive extraction apparatus against vulnerable property owners while ongoing federal civil rights challenge is actively pending.</p>",
        "record_source": "City Commission Ordinance No. 26-1007 Agenda Packet (Oct 7, 2026); Julius AI Investigation Digest; CASE_GROUND_TRUTH_AND_EVIDENCE_MAP.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Ordinance No. 26-1007</span>; <span class=\"file-source-tag\">00_JULIUS_AI_GLEANING_DIGEST.md</span>.</p>"
    },
    {
        "id": "comm-8-9",
        "item_num": "8.9",
        "phase_num": 8,
        "phase_title": "8. Phase 8: Sanctions Collision & Sovereign Reckoning (Sep 2026 – Oct 2026)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "October 9, 2026",
        "date_sort": "2026-10-09",
        "title": "Shellpoint Secret Escrow Disbursal of $4,629.79 to City of Oregon City",
        "medium": "Servicer Escrow Disbursement Ledger & Bank Notice",
        "medium_cat": "Billing Statement",
        "from": "NewRez LLC d/b/a Shellpoint Mortgage Servicing",
        "to": "City of Oregon City Utility / Lien Division",
        "actor_cat": "Other / Unknown",
        "subject": "Concealed Escrow Payment to Satisfy Municipal Liens Behind Borrower's Back",
        "summary": "Shellpoint disburses $4,629.79 from escrow directly to 'City of Oregon' to satisfy municipal utility and code liens without notice to record title holder Annika Eriksson, padding mortgage arrears by another $4.6k while colluding with the City to monetize disputed code penalties.",
        "summary_html": "<p>Shellpoint disburses $4,629.79 from escrow directly to 'City of Oregon' to satisfy municipal utility and code liens without notice to record title holder Annika Eriksson, padding mortgage arrears by another $4.6k while colluding with the City to monetize disputed code penalties.</p>",
        "record_source": "Shellpoint Transaction History Ledger (10/09/2026); Case 24CV21417 Docket; GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">Shellpoint Ledger 10/09/2026</span>; <span class=\"file-source-tag\">Case 24CV21417</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "comm-8-10",
        "item_num": "8.10",
        "phase_num": 8,
        "phase_title": "8. Phase 8: Sanctions Collision & Sovereign Reckoning (Sep 2026 – Oct 2026)",
        "layer": "code",
        "layer_title": "Municipal Code",
        "date_time": "October 13, 2026",
        "date_sort": "2026-10-13",
        "title": "Clackamas County Sheriff Vehicle Tow Contest (Miranda v. Cornelius)",
        "medium": "Formal Hearing Request & Administrative Notice",
        "medium_cat": "Court Filing / Order",
        "from": "Annika Eriksson",
        "to": "Clackamas County Sheriff's Office / Andy's Towing LLC",
        "actor_cat": "Police / Code Enforcement",
        "subject": "CCC § 7.01.160 & ORS 809.716 Vehicle Tow Contest (Plate 755 LEN)",
        "summary": "Deputy Eagle stops Annika's 1995 Mazda pickup (755 LEN) safely parked off travel lanes and orders tow by Andy's Towing, handing Annika a defective blank-backed notice omitting citation number and inventory report. Eriksson files emergency hearing request under Miranda v. Cornelius (unlawful non-caretaking punitive seizure).",
        "summary_html": "<p>Deputy Eagle stops Annika's 1995 Mazda pickup (755 LEN) safely parked off travel lanes and orders tow by Andy's Towing, handing Annika a defective blank-backed notice omitting citation number and inventory report. Eriksson files emergency hearing request under Miranda v. Cornelius (unlawful non-caretaking punitive seizure).</p>",
        "record_source": "CCSO Notice of Towed Vehicle (10/13/2026); Synthesized CCSO Hearing Request; GEMINI.md.",
        "record_source_html": "<p><span class=\"file-source-tag\">CCSO Tow Notice</span>; <span class=\"file-source-tag\">Hearing Request Packet</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    },
    {
        "id": "fc-2026-10b",
        "item_num": "8.11",
        "phase_num": 8,
        "phase_title": "8. Phase 8: Sanctions Collision & Sovereign Reckoning (Sep 2026 – Oct 2026)",
        "layer": "foreclosure",
        "layer_title": "Foreclosure & Title",
        "date_time": "October 20, 2026",
        "date_sort": "2026-10-20",
        "title": "ORCP 71 Motion Set for Hearing: Attack on Void Foreclosure Judgment",
        "medium": "Circuit Court Motion & Supporting Declarations (17CV38591)",
        "medium_cat": "Court Filing / Order",
        "from": "Annika Eriksson (Record Title Holder)",
        "to": "Hon. Michael C. Wetzel (Clackamas County Circuit Court)",
        "actor_cat": "Municipal Court",
        "subject": "Motion to Vacate 2019 Foreclosure Judgment Under ORCP 71 B(1)(d) & 71 C",
        "summary": "Hearing scheduled before Judge Wetzel for November 30, 2026 on Eriksson's Motion to Set Aside Void 2019 Foreclosure Judgment. Motion establishes 4 independent dispositive grounds: service on withdrawn counsel under Jasper, CWALT 2006-OC10 vs OC11 trust mismatch, phantom FITE entity fraud, and default entered over TLH's live Answer.",
        "summary_html": "<p>Hearing scheduled before Judge Wetzel for November 30, 2026 on Eriksson's Motion to Set Aside Void 2019 Foreclosure Judgment. Motion establishes 4 independent dispositive grounds: service on withdrawn counsel under Jasper, CWALT 2006-OC10 vs OC11 trust mismatch, phantom FITE entity fraud, and default entered over TLH's live Answer.</p>",
        "record_source": "Clackamas County Case No. 17CV38591 Motion to Set Aside Void Judgment; GEMINI.md; Complete Foreclosure and Servicing Narrative.",
        "record_source_html": "<p><span class=\"file-source-tag\">Case 17CV38591 ORCP 71 Motion</span>; <span class=\"file-source-tag\">GEMINI.md</span>.</p>"
    }
]

def render_card_html(entry):
    item_num = entry['item_num']
    date_time = entry['date_time']
    medium = entry['medium']
    actor = entry['actor_cat']
    layer = entry['layer']
    layer_title = entry['layer_title']
    title = entry['title']
    from_p = entry['from']
    to_p = entry['to']
    snippet = entry['summary']
    if len(snippet) > 220:
        snippet = snippet[:217] + '...'
    snippet_escaped = snippet.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

    participants_html = ''
    if from_p or to_p:
        participants_html = f'<div class="card-participants"><strong>From:</strong> {from_p} &bull; <strong>To:</strong> {to_p}</div>'

    return f"""            <article class="event-card" id="{entry['id']}"
                     data-id="{entry['id']}"
                     data-phase="{entry['phase_num']}"
                     data-actor-cat="{entry['actor_cat']}"
                     data-medium-cat="{entry['medium_cat']}"
                     data-layer="{layer}"
                     onclick="openEventDrawer('{entry['id']}')">
              <div class="card-meta-line">
                <span class="badge-item">Item {item_num}</span>
                <span class="badge-date">{date_time}</span>
                <span class="badge-layer badge-layer-{layer}">{layer_title}</span>
                <span class="badge-medium">{medium}</span>
                <span class="badge-actor">{actor}</span>
              </div>
              <h3 class="card-title">{title}</h3>
              {participants_html}
              <div class="card-summary-snippet">{snippet_escaped}</div>
              <div class="card-footer">
                <span class="view-record-trigger">View full record &rarr;</span>
                <button type="button" class="copy-link-btn" onclick="copyCardLink(event, '{entry['id']}')" title="Copy permanent link to this entry">
                  &sect; Copy Anchor
                </button>
              </div>
            </article>"""

def main():
    # 1. Read the base template from BACKUP_PATH if available to ensure pristine 98 lived communications
    if os.path.exists(BACKUP_PATH):
        print(f"Reading pristine base from {BACKUP_PATH}...")
        with open(BACKUP_PATH, 'r', encoding='utf-8') as f:
            base_html = f.read()
    else:
        print(f"Reading base from {TIMELINE_PATH}...")
        with open(TIMELINE_PATH, 'r', encoding='utf-8') as f:
            base_html = f.read()

    # Extract original 98 entries
    start_tag = 'const ENTRIES_DATA = '
    end_tag = ';\n    const entriesMap'
    start_idx = base_html.find(start_tag)
    if start_idx == -1:
        raise ValueError("Could not find start of ENTRIES_DATA")
    end_idx = base_html.find(end_tag, start_idx)
    if end_idx == -1:
        raise ValueError("Could not find end of ENTRIES_DATA")

    json_blob = base_html[start_idx + len(start_tag):end_idx].strip()
    raw_entries = json.loads(json_blob)

    # Filter to only original lived entries (either starting with p1-p8 or layer=='lived')
    new_ids = set(e['id'] for e in NEW_ENTRIES)
    lived_entries = [e for e in raw_entries if e['id'] not in new_ids]
    for item in lived_entries:
        item['layer'] = 'lived'
        item['layer_title'] = 'Lived Experience'
        if item['id'] == 'comm-1-6':
            item['title'] = 'First Physical Water Shutoff & Project Access NOW Restoration Payment ($311.02)'
            item['summary'] = "On January 22, 2024, the City physically shuts off water service to 12054 Chapin Court. City utility staffer John Oreskovich logs an internal alert: 'SHUT OFF 1/22/2024 $311.02 TO RESTORE'—reflecting Eriksson's actual utility balance of $236.02 plus a $25.00 door hanger fee and a $50.00 shutoff fee (excluding prior tenant Stephanie Jones's separate $606.60 account). Eriksson immediately coordinates with Project Access NOW, and on January 23, 2024 (credited January 24, Batch B00015794, Receipt R00738478), Jonathan from Project Access NOW pays $311.02 via VISA card (*4447, Auth 613634) on Eriksson's behalf to restore water service. Oreskovich logs: 'Jonathan, from Project Access (via health care provider) made the full payment to restore service,' but simultaneously assesses an additional $50.00 meter tampering fee (paid Feb 22, 2024), bringing January municipal fees alone to $125.00."
            item['summary_html'] = "<p>On January 22, 2024, the City physically shuts off water service to 12054 Chapin Court. City utility staffer John Oreskovich logs an internal alert: <em>\"SHUT OFF 1/22/2024 $311.02 TO RESTORE\"</em>—reflecting Eriksson's actual utility balance of $236.02 plus a $25.00 door hanger fee and a $50.00 shutoff fee (excluding prior tenant Stephanie Jones's separate $606.60 account). Eriksson immediately coordinates with Project Access NOW, and on January 23, 2024 (credited January 24, Batch B00015794, Receipt R00738478), <strong>Jonathan from Project Access NOW</strong> pays <strong>$311.02</strong> via VISA card (*4447, Auth 613634) on Eriksson's behalf to restore water service. Oreskovich logs: <em>\"Jonathan, from Project Access (via health care provider) made the full payment to restore service,\"</em> but simultaneously assesses an additional $50.00 meter tampering fee (paid Feb 22, 2024), bringing January municipal fees alone to $125.00.</p>"
        
        # Sanitize any legacy horizontal rule dividers from lived entries
        for field in ['summary', 'summary_html', 'record_source', 'record_source_html']:
            if field in item and item[field]:
                item[field] = item[field].replace('\n\n---', '').replace('<p>---</p>', '').replace('---', '')

    print(f"Loaded {len(lived_entries)} pristine lived communications.")

    # Combine lived + new research entries
    all_entries = list(lived_entries) + list(NEW_ENTRIES)
    total_count = len(all_entries)
    print(f"Total entries combined: {total_count}")

    # Count by layer
    counts_by_layer = {}
    for e in all_entries:
        l = e['layer']
        counts_by_layer[l] = counts_by_layer.get(l, 0) + 1

    print("Counts by layer:", counts_by_layer)

    # Group entries by phase_num
    phases = {}
    for entry in all_entries:
        p_num = entry['phase_num']
        if p_num not in phases:
            phases[p_num] = {
                'phase_num': p_num,
                'phase_title': entry['phase_title'],
                'entries': []
            }
        phases[p_num]['entries'].append(entry)

    # Sort entries inside each phase
    def entry_sort_key(e):
        ds = e.get('date_sort', '')
        item_parts = re.split(r'(\d+)', str(e['item_num']))
        parsed_parts = []
        for part in item_parts:
            if part.isdigit():
                parsed_parts.append(int(part))
            elif part:
                parsed_parts.append(part.lower())
        if e.get('phase_num', 0) == 0:
            return (ds, parsed_parts)
        return (parsed_parts, ds)

    for p_num in sorted(phases.keys()):
        phases[p_num]['entries'].sort(key=entry_sort_key)

    # Flatten back to a single sorted list
    flattened_entries = []
    for p_num in sorted(phases.keys()):
        flattened_entries.extend(phases[p_num]['entries'])

    # Build the HTML timeline-stream section
    stream_blocks = []
    for p_num in sorted(phases.keys()):
        p_data = phases[p_num]
        p_entries = p_data['entries']
        cards_html = "\n\n".join(render_card_html(e) for e in p_entries)
        block_html = f"""        <section class="phase-block" data-phase-num="{p_num}">
          <div class="phase-header">
            <h2 class="phase-title">{p_data['phase_title']}</h2>
            <span class="phase-count">{len(p_entries)} records</span>
          </div>
          <div class="phase-entries">
{cards_html}
          </div>
        </section>"""
        stream_blocks.append(block_html)

    new_timeline_stream_html = "\n\n".join(stream_blocks)

    # 1. Replace ENTRIES_DATA JSON in <script> first using base_html coordinates
    new_json_str = json.dumps(flattened_entries, indent=4, ensure_ascii=False)
    html = base_html[:start_idx + len(start_tag)] + new_json_str + base_html[end_idx:]

    # 2. Replace the contents of <div class="timeline-stream" id="timelineStream"> ... </div>
    pattern_stream = r'(<div class="timeline-stream" id="timelineStream">)(.*?)(</div>\s*</main>)'
    replacement_stream = r'\g<1>\n' + new_timeline_stream_html + r'\n        \g<3>'
    html = re.sub(pattern_stream, replacement_stream, html, flags=re.DOTALL)

    # Update counts and headers in HTML
    for old_n in (97, 98, 104, len(lived_entries)):
        html = html.replace(f'index and verbatim evidentiary record of {old_n} communications', f'index and verbatim evidentiary record of {total_count} multi-track records')
        html = html.replace(f'<a href="timeline.html" class="active">Timeline ({old_n})</a>', f'<a href="timeline.html" class="active">Timeline ({total_count})</a>')
        html = html.replace(f'Point-and-click repository indexing {old_n} documented communications', f'Point-and-click repository indexing {total_count} documented multi-track records')
        html = html.replace(f'<div class="stat-number">{old_n}</div>', f'<div class="stat-number">{total_count}</div>')
        html = html.replace(f'placeholder="Search {old_n} records (person, date, topic, exhibit)..."', f'placeholder="Search {total_count} records across 7 tracks (person, date, topic, exhibit)..."')
        html = html.replace(f'Timeline ({old_n} Events)', f'Timeline ({total_count} Records)')
        html = html.replace(f'{old_n} item forensic dossier', f'{total_count} record multi-track dossier')
        html = html.replace(f'{old_n}-Item Forensic Timeline', f'{total_count}-Record Multi-Track Forensic Timeline')
        html = html.replace(f'The {old_n} Municipal Communications', f'Multi-Track Forensic Timeline ({total_count} Records)')
        html = html.replace(f'{old_n} Communications Recorded', f'{total_count} Multi-Track Records')
        html = html.replace(f'{old_n} chronological communications', f'{total_count} multi-track forensic records')
        html = html.replace(f'{old_n} Communications Logged', f'{total_count} Multi-Track Records Logged')
        html = html.replace(f'Showing {old_n} of {old_n} communications', f'Showing {total_count} of {total_count} multi-track records')
    html = html.replace('130 Multi-Track Records Logged', f'{total_count} Multi-Track Records Logged')
    html = html.replace('Showing 130 of 130 multi-track records', f'Showing {total_count} of {total_count} multi-track records')

    # Add / Update Badge CSS for all layers
    layer_css = """
    .badge-layer {
      display: inline-block;
      padding: 0.15rem 0.45rem;
      border-radius: 3px;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.7rem;
      letter-spacing: 0.04em;
    }
    .badge-layer-lived {
      background: rgba(31, 95, 88, 0.12);
      color: var(--paladin-teal);
      border: 1px solid rgba(31, 95, 88, 0.3);
    }
    .badge-layer-foreclosure {
      background: rgba(15, 23, 42, 0.08);
      color: #0F172A;
      border: 1px solid rgba(15, 23, 42, 0.25);
    }
    .badge-layer-tlh-zbs {
      background: rgba(67, 56, 202, 0.10);
      color: #4338CA;
      border: 1px solid rgba(67, 56, 202, 0.3);
    }
    .badge-layer-comparator {
      background: rgba(2, 132, 199, 0.10);
      color: #0284C7;
      border: 1px solid rgba(2, 132, 199, 0.3);
    }
    .badge-layer-code {
      background: rgba(217, 119, 6, 0.12);
      color: #B45309;
      border: 1px solid rgba(217, 119, 6, 0.3);
    }
    .badge-layer-public-ada {
      background: rgba(196, 92, 62, 0.12);
      color: #C45C3E;
      border: 1px solid rgba(196, 92, 62, 0.3);
    }
    .badge-layer-microclimate-rac {
      background: rgba(13, 148, 136, 0.12);
      color: #0D9488;
      border: 1px solid rgba(13, 148, 136, 0.3);
    }

    .layer-pills-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.4rem 0.6rem;
      margin-top: 0.65rem;
      width: 100%;
      border-top: 1px dashed rgba(31, 95, 88, 0.2);
      padding-top: 0.65rem;
    }
    .layer-pill-label {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.72rem;
      color: var(--paladin-ink-muted);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-right: 0.25rem;
    }
    .layer-pill {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.74rem;
      padding: 0.25rem 0.65rem;
      border-radius: 4px;
      border: 1px solid var(--paladin-rule-strong);
      background: #FFFFFF;
      color: var(--paladin-ink);
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .layer-pill:hover {
      border-color: var(--paladin-teal);
      background: var(--paladin-paper-subtle);
    }
    .layer-pill.active {
      background: var(--paladin-teal);
      color: #FFFFFF;
      border-color: var(--paladin-teal);
      font-weight: 700;
    }
    .layer-pill[data-layer-val="lived"].active { background: var(--paladin-teal); }
    .layer-pill[data-layer-val="foreclosure"].active { background: #0F172A; }
    .layer-pill[data-layer-val="tlh-zbs"].active { background: #4338CA; }
    .layer-pill[data-layer-val="comparator"].active { background: #0284C7; }
    .layer-pill[data-layer-val="code"].active { background: #B45309; }
    .layer-pill[data-layer-val="public-ada"].active { background: #C45C3E; }
    .layer-pill[data-layer-val="microclimate-rac"].active { background: #0D9488; }
"""
    if '.badge-layer {' not in html:
        html = html.replace('.badge-actor {', layer_css + '\n    .badge-actor {')
    else:
        # replace existing badge-layer CSS block
        css_start = html.find('.badge-layer {')
        css_end = html.find('.badge-actor {', css_start)
        if css_start != -1 and css_end != -1:
            html = html[:css_start] + layer_css.strip() + '\n\n    ' + html[css_end:]

    # Remove any existing layerFilter or layer-pills-bar to re-generate cleanly
    html = re.sub(r'<select id="layerFilter".*?</select>\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="layer-pills-bar">.*?</div>\s*', '', html, flags=re.DOTALL)

    # Insert fresh layer controls
    n_all = total_count
    n_lived = counts_by_layer.get('lived', 0)
    n_fc = counts_by_layer.get('foreclosure', 0)
    n_tlh = counts_by_layer.get('tlh-zbs', 0)
    n_comp = counts_by_layer.get('comparator', 0)
    n_code = counts_by_layer.get('code', 0)
    n_ada = counts_by_layer.get('public-ada', 0)
    n_rac = counts_by_layer.get('microclimate-rac', 0)

    layer_controls = f"""
        <select id="layerFilter" class="filter-select" aria-label="Filter by Research Track">
          <option value="all">All Tracks (Expanded Index: {n_all})</option>
          <option value="lived">Lived Communications ({n_lived})</option>
          <option value="foreclosure">Foreclosure &amp; Title History ({n_fc})</option>
          <option value="tlh-zbs">Turning Leaf &amp; ZBS Network ({n_tlh})</option>
          <option value="comparator">Vetted Comparators ({n_comp})</option>
          <option value="code">Municipal Code &amp; Penalties ({n_code})</option>
          <option value="public-ada">Public Intel &amp; ADA Hypocrisy ({n_ada})</option>
          <option value="microclimate-rac">Microclimate &amp; RAC ({n_rac})</option>
        </select>
"""
    html = html.replace('<select id="phaseFilter"', layer_controls + '        <select id="phaseFilter"')

    # Ensure Phase 0 is in phaseFilter
    if '<option value="0">' not in html:
        html = html.replace('<option value="all">All Phases (1–8)</option>',
                            '<option value="all">All Phases (0–8)</option>\n          <option value="0">0. Phase 0: Historical Foundation &amp; Structural Architecture (1994–2022)</option>')
        html = html.replace('<option value="all">All Phases (0–8)</option>',
                            '<option value="all">All Phases (0–8)</option>\n          <option value="0">0. Phase 0: Historical Foundation &amp; Structural Architecture (1994–2022)</option>')

    # Add layer pills row below the filter controls
    layer_pills_html = f"""
        <div class="layer-pills-bar">
          <span class="layer-pill-label">Track Filter:</span>
          <button type="button" class="layer-pill active" data-layer-val="all">All ({n_all})</button>
          <button type="button" class="layer-pill" data-layer-val="lived">Lived ({n_lived})</button>
          <button type="button" class="layer-pill" data-layer-val="foreclosure">Foreclosure &amp; Title ({n_fc})</button>
          <button type="button" class="layer-pill" data-layer-val="tlh-zbs">TLH &amp; ZBS ({n_tlh})</button>
          <button type="button" class="layer-pill" data-layer-val="comparator">Comparators ({n_comp})</button>
          <button type="button" class="layer-pill" data-layer-val="code">Code ({n_code})</button>
          <button type="button" class="layer-pill" data-layer-val="public-ada">Public Intel &amp; ADA ({n_ada})</button>
          <button type="button" class="layer-pill" data-layer-val="microclimate-rac">Microclimate &amp; RAC ({n_rac})</button>
        </div>"""

    # Insert layer_pills_html right before <button type="button" id="resetFiltersBtn"
    html = html.replace('<button type="button" id="resetFiltersBtn"', layer_pills_html + '\n        <button type="button" id="resetFiltersBtn"')

    # Wire up JavaScript filtering
    if 'let matchesLayer =' not in html:
        old_apply_vars = "const query = searchInput.value.toLowerCase().trim();\n      const phaseVal = phaseFilter.value;\n      const actorVal = actorFilter.value;\n      const mediumVal = mediumFilter.value;"
        new_apply_vars = "const query = searchInput.value.toLowerCase().trim();\n      const layerFilter = document.getElementById('layerFilter');\n      const layerVal = layerFilter ? layerFilter.value : 'all';\n      const phaseVal = phaseFilter.value;\n      const actorVal = actorFilter.value;\n      const mediumVal = mediumFilter.value;"
        html = html.replace(old_apply_vars, new_apply_vars)

        old_match = "let matchesPhase = (phaseVal === 'all' || entry.phase_num.toString() === phaseVal);\n        let matchesActor = (actorVal === 'all' || entry.actor_cat === actorVal);\n        let matchesMedium = (mediumVal === 'all' || entry.medium_cat === mediumVal);\n\n        if (matchesSearch && matchesPhase && matchesActor && matchesMedium) {"
        new_match = "let matchesLayer = (layerVal === 'all' || entry.layer === layerVal);\n        let matchesPhase = (phaseVal === 'all' || entry.phase_num.toString() === phaseVal);\n        let matchesActor = (actorVal === 'all' || entry.actor_cat === actorVal);\n        let matchesMedium = (mediumVal === 'all' || entry.medium_cat === mediumVal);\n\n        if (matchesSearch && matchesLayer && matchesPhase && matchesActor && matchesMedium) {"
        html = html.replace(old_match, new_match)

        # In resetAllFilters()
        html = html.replace("searchInput.value = '';\n      phaseFilter.value = 'all';",
                            "searchInput.value = '';\n      const layerFilter = document.getElementById('layerFilter');\n      if (layerFilter) layerFilter.value = 'all';\n      if (typeof syncLayerPills === 'function') syncLayerPills('all');\n      phaseFilter.value = 'all';")

        # In resultsCounter
        html = html.replace("resultsCounter.textContent = 'Showing ' + visibleCount + ' of ' + ENTRIES_DATA.length + ' communications';",
                            "resultsCounter.textContent = 'Showing ' + visibleCount + ' of ' + ENTRIES_DATA.length + ' multi-track records';")

        # Sync layer pills function and event listeners
        pills_js = """
    function syncLayerPills(val) {
      document.querySelectorAll('.layer-pill').forEach(pill => {
        if (pill.dataset.layerVal === val) {
          pill.classList.add('active');
        } else {
          pill.classList.remove('active');
        }
      });
    }

    document.querySelectorAll('.layer-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        const val = pill.dataset.layerVal;
        const layerFilter = document.getElementById('layerFilter');
        if (layerFilter) layerFilter.value = val;
        syncLayerPills(val);
        applyFilters();
      });
    });

    const layerFilterEl = document.getElementById('layerFilter');
    if (layerFilterEl) {
      layerFilterEl.addEventListener('change', () => {
        syncLayerPills(layerFilterEl.value);
        applyFilters();
      });
    }
"""
        html = html.replace("mediumFilter.addEventListener('change', applyFilters);",
                            "mediumFilter.addEventListener('change', applyFilters);" + pills_js)

    # In Drawer: add drawerLayerBadge and Drawer table row for Research Layer
    if 'id="drawerLayerBadge"' not in html:
        html = html.replace('<span id="drawerItemBadge" class="badge-item">Item 1.1</span>',
                            '<span id="drawerItemBadge" class="badge-item">Item 1.1</span>\n          <span id="drawerLayerBadge" class="badge-layer badge-layer-lived">Lived Experience</span>')
        
        table_layer_row = """          <tr>
            <td>Research Track</td>
            <td id="drawerLayer">—</td>
          </tr>
"""
        html = html.replace('<tr>\n            <td>Medium</td>', table_layer_row + '          <tr>\n            <td>Medium</td>')

        # In openEventDrawer(id): fill drawerLayerBadge & drawerLayer
        drawer_js_old = "drawerItemBadge.textContent = 'Item ' + entry.item_num;\n      drawerPhaseBadge.textContent = 'Phase ' + entry.phase_num;\n      drawerMediumBadge.textContent = entry.medium;"
        drawer_js_new = """drawerItemBadge.textContent = 'Item ' + entry.item_num;
      const drawerLayerBadge = document.getElementById('drawerLayerBadge');
      if (drawerLayerBadge) {
        drawerLayerBadge.textContent = entry.layer_title || 'Lived Experience';
        drawerLayerBadge.className = 'badge-layer badge-layer-' + (entry.layer || 'lived');
      }
      const drawerLayer = document.getElementById('drawerLayer');
      if (drawerLayer) drawerLayer.textContent = entry.layer_title || 'Lived Experience';
      drawerPhaseBadge.textContent = 'Phase ' + entry.phase_num;
      drawerMediumBadge.textContent = entry.medium;"""
        html = html.replace(drawer_js_old, drawer_js_new)

    # Darken drawer summary & source text boxes for optimal contrast and legibility
    drawer_css_old_start = html.find('.drawer-summary-box {')
    drawer_css_old_end = html.find('.drawer-footer {', drawer_css_old_start)
    if drawer_css_old_start != -1 and drawer_css_old_end != -1:
        drawer_css_darkened = """.drawer-summary-box {
      background: #0F172A;
      border: 1px solid rgba(13, 148, 136, 0.4);
      border-left: 4px solid var(--paladin-teal);
      padding: 1.25rem;
      border-radius: 6px;
      font-size: 1rem;
      line-height: 1.7;
      color: #F8FAFC;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.35);
    }

    .drawer-summary-box p {
      margin-bottom: 0.85rem;
      color: #F8FAFC;
    }

    .drawer-summary-box p:last-child {
      margin-bottom: 0;
    }

    .drawer-summary-box strong {
      color: #FFFFFF;
      font-weight: 700;
    }

    .drawer-summary-box em {
      color: #E2E8F0;
    }

    .drawer-summary-box a {
      color: #38BDF8;
      text-decoration: underline;
    }

    .drawer-summary-box a:hover {
      color: #7DD3FC;
    }

    .drawer-summary-box blockquote {
      border-left: 3px solid var(--paladin-amber);
      background: rgba(217, 119, 6, 0.15);
      padding: 0.65rem 0.85rem;
      margin: 0.85rem 0;
      font-style: italic;
      color: #FEF3C7;
      border-radius: 0 4px 4px 0;
    }

    .drawer-summary-box code {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.85em;
      background: rgba(255, 255, 255, 0.12);
      color: #38BDF8;
      padding: 0.1rem 0.35rem;
      border-radius: 3px;
    }

    .drawer-source-box {
      background: #141D30;
      border: 1px solid rgba(217, 119, 6, 0.4);
      border-left: 4px solid var(--paladin-amber);
      padding: 0.95rem 1.15rem;
      border-radius: 6px;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.82rem;
      color: #E2E8F0;
      line-height: 1.55;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.35);
    }

    .drawer-source-box a {
      color: #38BDF8;
      text-decoration: underline;
    }

    .drawer-source-box a:hover {
      color: #7DD3FC;
    }

    .file-source-tag {
      display: inline-block;
      background: rgba(13, 148, 136, 0.2);
      border: 1px solid rgba(13, 148, 136, 0.4);
      color: #2DD4BF;
      padding: 0.1rem 0.4rem;
      border-radius: 3px;
      margin: 0.15rem 0;
      word-break: break-all;
    }

    """
        html = html[:drawer_css_old_start] + drawer_css_darkened + html[drawer_css_old_end:]

    print(f"Writing updated HTML to {TIMELINE_PATH}...")
    with open(TIMELINE_PATH, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Success! Multi-track timeline enriched with {total_count} records.")

if __name__ == '__main__':
    main()
