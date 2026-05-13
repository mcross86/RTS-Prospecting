"""
Seed 10 leads per industry under company-os/03-prospects/new-leads/<industry>/<slug>/
Sources: public web listings and company sites. Verify on live site / Maps before dialing.
Run from anywhere: python seed_cedar_rapids_leads.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "03-prospects" / "new-leads"

Row = dict[str, str | None]

LEADS: dict[str, list[Row]] = {
    "hvac": [
        {"slug": "colony-plumbing-heating-air", "name": "Colony Plumbing, Heating & Air Conditioning", "phone": "(319) 364-4328", "address": "2224 16th Ave SW, Cedar Rapids, IA 52404", "website": "https://colonyheating.com/", "note": "Large local HVAC/plumbing; 24/7 positioning; commercial + residential."},
        {"slug": "master-plumbing-heating-cooling", "name": "Master Plumbing, Heating & Cooling", "phone": "(319) 318-1388", "address": "3111 1st Ave SE, Cedar Rapids, IA 52402", "website": "https://www.masterphc.com/", "note": "Full-service HVAC; dispatch + maintenance agreements."},
        {"slug": "novak-heating-air-duct-cleaning", "name": "Novak Heating, Air & Duct Cleaning", "phone": "(319) 364-4626", "address": "820 N 15th Ave, Hiawatha, IA 52233", "website": "https://www.novakheating.com/", "note": "CR corridor; Carrier dealer; duct + IAQ upsell."},
        {"slug": "schaal-plumbing-heating-cooling", "name": "Schaal Plumbing, Heating and Cooling", "phone": "(319) 209-5120", "address": "6115 7th St SW, Cedar Rapids, IA 52404", "website": "https://www.schaalhvac.com/", "note": "Plumbing + HVAC bundle; multi-truck scheduling."},
        {"slug": "iltens-incorporated", "name": "Ilten's Incorporated", "phone": "(319) 208-3295", "address": "919 14th Ave SW, Cedar Rapids, IA 52404", "website": "https://www.iltens.com/", "note": "Established CR contractor; zoning + replacement workflows."},
        {"slug": "cmr-heating-and-cooling", "name": "CMR Heating & Cooling", "phone": "(319) 447-2123", "address": "4806 Mary Green Ct, Cedar Rapids, IA 52411", "website": "http://www.cmrheating.com/", "note": "Since 1979; residential + commercial retrofits."},
        {"slug": "cedar-rapids-plumbing-heating-cooling", "name": "Cedar Rapids Plumbing, Heating & Cooling", "phone": None, "address": "Cedar Rapids, IA (verify street on site)", "website": "https://cedarrapidsphc.com/", "note": "Long-running local PHC; confirm main line on website."},
        {"slug": "air-comfort", "name": "Air Comfort", "phone": None, "address": "Cedar Rapids, IA metro", "website": "https://myaircomfort.com/", "note": "HVAC + geothermal + commercial; verify HQ/contact."},
        {"slug": "lins-heating-and-air-conditioning", "name": "LINS Heating & Air Conditioning", "phone": None, "address": "Eastern Iowa (verify)", "website": "https://linsheatingandair.com/", "note": "Regional HVAC; financing messaging on site."},
        {"slug": "legacy-cooling-and-heating", "name": "Legacy Cooling & Heating", "phone": None, "address": "Cedar Rapids, IA metro", "website": "https://legacycoolingandheating.com/", "note": "Local CR marketing; emergency repair positioning."},
    ],
    "auto-shops": [
        {"slug": "rpm-automotive", "name": "RPM Automotive", "phone": "(319) 393-1640", "address": "Cedar Rapids / Hiawatha area (verify)", "website": "https://rpmautomotiverepair.com/", "note": "Diagnostics; reviews cite honest pricing."},
        {"slug": "johns-automotive-service", "name": "John's Automotive Service", "phone": None, "address": "Cedar Rapids, IA", "website": "https://johnsautomotiveservice.com/", "note": "Since 1985; warranty/shuttle/loaner messaging — ops-heavy."},
        {"slug": "albert-auto-service", "name": "Albert Auto Service Inc", "phone": "(319) 297-7391", "address": "Cedar Rapids, IA (multi-location)", "website": "https://www.albertautoservice.com/", "note": "Family-owned since 1999; multi-location coordination."},
        {"slug": "cedar-automotive", "name": "Cedar Automotive", "phone": "(319) 450-7584", "address": "Near CID / Cedar Rapids, IA", "website": "https://www.cedar-automotive.com/", "note": "European + domestic; same-day positioning."},
        {"slug": "christian-brothers-automotive-cedar-rapids", "name": "Christian Brothers Automotive Cedar Rapids", "phone": "(319) 254-5424", "address": "Westdale Pkwy SW, Cedar Rapids, IA (verify suite)", "website": "https://cbac.com/cedar-rapids/", "note": "Franchise; multi-bay throughput + inspections."},
        {"slug": "havliks-auto-service", "name": "Havlik's Auto Service", "phone": "(319) 365-7257", "address": "1815 16th Ave SW, Cedar Rapids, IA", "website": "https://havlikauto.com/", "note": "Engine/transmission + diagnostics."},
        {"slug": "mefferds-auto-service", "name": "Mefferd's Auto Service", "phone": None, "address": "4580 Mt Vernon Rd SE, Cedar Rapids, IA 52403", "website": "https://www.mefferds.com/", "note": "Family-owned since 1968."},
        {"slug": "dennys-automotive-muffler-center", "name": "Denny's Automotive & Muffler Center", "phone": "(319) 363-5245", "address": "Cedar Rapids, IA (verify)", "website": "https://dennysmuffler.net/", "note": "Fleet discount advertised."},
        {"slug": "mcgrath-chevyland-service", "name": "McGrath Chevyland (Service Center)", "phone": "(319) 774-5816", "address": "1616 51st St NE, Cedar Rapids, IA 52402", "website": "https://www.patmcgrathchevyland.com/service-center.htm", "note": "Dealer service — larger org; different software motion than indie shops."},
        {"slug": "franks-country-auto", "name": "Frank's Country Auto, LLC", "phone": "(319) 364-0517", "address": "1100 Center Point Rd NE, Cedar Rapids, IA 52402", "website": "https://www.frankscountryauto.com/", "note": "40+ years local; shuttle + same-day messaging."},
    ],
    "dental": [
        {"slug": "ne-family-dentistry", "name": "Northeast Family Dentistry", "phone": "(319) 364-0472", "address": "203 29th St NE, Cedar Rapids, IA", "website": "https://www.nefamilydentistry.com/", "note": "Multi-provider family practice; recall + scheduling."},
        {"slug": "river-ridge-dental", "name": "River Ridge Dental", "phone": "(319) 832-2000", "address": "Cedar Rapids, IA (verify)", "website": "https://riverridgedental.com/", "note": "Broad services (ortho, implants, sleep); multi-location ops possible."},
        {"slug": "dental-arts-deb-cassill", "name": "Dental Arts (Dr. Deb Cassill)", "phone": None, "address": "Cedar Rapids, IA", "website": "https://cedarrapidsdentalarts.com/", "note": "Family + cosmetic; digital imaging messaging."},
        {"slug": "dental-health-partners", "name": "Dental Health Partners", "phone": "(319) 365-4997", "address": "Near I-380, Cedar Rapids, IA (verify)", "website": "https://www.dentalhealthpartners.com/", "note": "Multi-doctor; pediatrics amenities."},
        {"slug": "prairie-creek-dental", "name": "Prairie Creek Dental (PCD Iowa)", "phone": "(319) 540-8626", "address": "Cedar Rapids, IA 52404 area", "website": "https://www.pcdiowa.com/", "note": "Cosmetic + family; emergency access messaging."},
        {"slug": "lindale-dental-care", "name": "Lindale Dental Care", "phone": "(319) 362-2313", "address": "3730 1st Ave NE, Cedar Rapids, IA 52402", "website": "https://www.lindaledentalcare.com/", "note": "Since 1986; hygiene block scheduling."},
        {"slug": "the-dental-center", "name": "The Dental Center (Cedar Rapids / Hiawatha)", "phone": "(319) 365-0534", "address": "Cedar Rapids, IA (verify)", "website": "https://www.crdentalcenter.com/", "note": "In-house lab messaging — case tracking angle."},
        {"slug": "spring-valley-dental-care", "name": "Spring Valley Dental Care", "phone": None, "address": "Cedar Rapids, IA", "website": "https://www.springvalleydentalcare.com/", "note": "Restorative + pediatrics + aligners."},
        {"slug": "cedar-dental", "name": "Cedar Dental", "phone": "(319) 364-7108", "address": "4201 1st Ave SE, Cedar Rapids, IA", "website": "https://cedar-dental.com/", "note": "Cosmetic focus; consult tracking."},
        {"slug": "midwest-dental-cedar-rapids", "name": "Midwest Dental (Cedar Rapids)", "phone": "(319) 362-1262", "address": "1935 1st Ave SE, Cedar Rapids, IA", "website": "https://midwest-dental.com/dental-office/cedar-rapids", "note": "Corporate dental; still local ops friction possible."},
    ],
    "trucking": [
        {"slug": "bolton-logistics", "name": "Bolton Logistics", "phone": "(319) 624-2086", "address": "733 58th Ave Ct SW, Cedar Rapids, IA (verify)", "website": "https://boltonlogistics.com/", "note": "LTL + warehousing + final mile; dispatch + POD."},
        {"slug": "mid-iowa-truck-dispatch", "name": "Mid-Iowa Truck Dispatch, Inc.", "phone": None, "address": "Cedar Rapids, IA", "website": "https://www.midiowatruckdispatch.com/", "note": "Landstar agency; capacity sourcing workflows."},
        {"slug": "apex-logistics-services", "name": "Apex Logistics Services, LLC", "phone": None, "address": "Cedar Rapids, IA", "website": "https://www.goapexlogistics.com/", "note": "Regional trucking; customer tracking portal angle."},
        {"slug": "lti-delivers", "name": "LTI Delivers, Inc.", "phone": None, "address": "505 33rd Ave SW, Cedar Rapids, IA", "website": "https://ltidelivers.com/", "note": "Truckload + intermodal drayage."},
        {"slug": "philipps-trucking", "name": "Philipp's Trucking", "phone": "(319) 329-9136", "address": "Cedar Rapids, IA area", "website": "https://www.philippstrucking.com/", "note": "Large local fleet; construction hauling."},
        {"slug": "crst", "name": "CRST The Transportation Solution, Inc.", "phone": None, "address": "Cedar Rapids, IA HQ (enterprise)", "website": "https://crst.com/", "note": "Enterprise — only if you target integrations; long cycle."},
        {"slug": "stewart-transport-marion", "name": "Stewart Transport, Inc.", "phone": None, "address": "2110 County Home Rd, Marion, IA (verify via FMCSA/site)", "website": None, "note": "Small fleet Marion; high fit for lightweight ops tools."},
        {"slug": "quality-inc-marion", "name": "Quality Inc (carrier)", "phone": "(319) 373-5900", "address": "3675 Industrial Ave, Marion, IA (verify)", "website": None, "note": "General freight; confirm active DOT/MC."},
        {"slug": "smb-trucking-marion", "name": "SMB Trucking", "phone": "(319) 350-1803", "address": "Marion, IA (verify)", "website": None, "note": "Small carrier from corridor listings — verify before outreach."},
        {"slug": "ra-williams-and-sons", "name": "R A Williams & Sons", "phone": "(319) 377-7934", "address": "Marion / Linn County area (verify)", "website": None, "note": "Small fleet; confirm identity and authority status."},
    ],
    "home-cleaning": [
        {"slug": "the-cleaning-authority-cedar-rapids", "name": "The Cleaning Authority - Cedar Rapids", "phone": None, "address": "Cedar Rapids, IA metro", "website": "https://www.thecleaningauthority.com/cedarrapids/", "note": "Franchise; crew routing + QA checklists."},
        {"slug": "molly-maid-cedar-rapids", "name": "Molly Maid of Cedar Rapids", "phone": None, "address": "Cedar Rapids, IA", "website": "https://mollymaid.com/locations/iowa/cedar-rapids/", "note": "Franchise; recurring schedule density."},
        {"slug": "merry-maids-cedar-rapids", "name": "Merry Maids of Cedar Rapids", "phone": None, "address": "Cedar Rapids, IA", "website": "https://www.merrymaids.com/cedar-rapids", "note": "Neighbly brand; local owner ops."},
        {"slug": "cr-house-cleaners", "name": "CR House Cleaners", "phone": "(319) 261-9670", "address": "Cedar Rapids, IA metro", "website": "https://www.crhousecleaners.com/", "note": "Airbnb turnover + eco positioning."},
        {"slug": "brookes-cleaning-llc", "name": "Brooke's Cleaning LLC", "phone": None, "address": "Cedar Rapids, IA", "website": "https://brookescleaning.com/", "note": "Since 2007; construction cleanup add-on."},
        {"slug": "maidpro-cedar-rapids", "name": "MaidPro Cedar Rapids", "phone": "(319) 249-0797", "address": "805 Wright Brothers Blvd W SW #4A, Cedar Rapids, IA 52404", "website": "https://www.maidpro.com/", "note": "Franchise; crew app + QA photos common ask."},
        {"slug": "cleanhomes-iowa", "name": "CleanHomes", "phone": None, "address": "Cedar Rapids / IC corridor", "website": "https://cleanhomesiowa.com/", "note": "Family-owned; 15+ yrs messaging on site."},
        {"slug": "gms-residential-cleaning", "name": "GMS Residential Cleaning", "phone": None, "address": "Cedar Rapids, IA metro", "website": "https://www.gmsresidentialcleaning.com/", "note": "Since 2000; commercial + construction cleanup."},
        {"slug": "easy-clean-homes", "name": "Easy Clean Homes", "phone": None, "address": "Cedar Rapids, IA", "website": "https://easycleanhomes.com/", "note": "Online booking — lead routing + reminders."},
        {"slug": "stratus-building-solutions-iowa", "name": "Stratus Building Solutions (Iowa / CR coverage)", "phone": "(515) 222-3135", "address": "Iowa regional office (verify Cedar Rapids territory)", "website": "https://www.stratusclean.com/", "note": "Commercial janitorial franchise; verify local franchisee for CR territory."},
    ],
    "roofing": [
        {"slug": "river-city-roofing", "name": "River City Roofing Co.", "phone": "(309) 697-9999", "address": "5400 Center Point Rd NE, Cedar Rapids, IA 52402", "website": "https://www.rivercityroofs.com/", "note": "Residential + commercial + solar messaging; storm response."},
        {"slug": "five-star-home-improvement", "name": "Five Star Home Improvement", "phone": "(319) 450-1018", "address": "Cedar Rapids, IA metro", "website": "https://www.fivestarhic.com/cedarrapids/", "note": "Roofing + windows/gutters; multi-trade scheduling."},
        {"slug": "garcia-roofing-and-exteriors", "name": "Garcia Roofing & Exteriors", "phone": None, "address": "Cedar Rapids / Corridor", "website": "https://www.garciaroofingandexteriors.com/", "note": "Storm restoration + manufacturer warranties messaging."},
        {"slug": "kuyoc-roofing", "name": "Kuyoc Roofing", "phone": "1-877-478-8886", "address": "Serves Cedar Rapids, IA", "website": "https://kuyocroofing.com/ia/cedar-rapids", "note": "24/7 emergency + inspections; confirm local crew base."},
        {"slug": "hawkeye-roofing-llc", "name": "Hawkeye Roofing LLC", "phone": None, "address": "Cedar Rapids, IA metro", "website": "https://hawkeye-roofing-llc.com/", "note": "Local roofing + siding positioning."},
        {"slug": "ameripro-roofing-cedar-rapids", "name": "AmeriPro Roofing (Cedar Rapids)", "phone": "800-200-8151", "address": "Serves Cedar Rapids, IA", "website": "https://www.ameriproroofing.com/locations/cedar-rapids-ia/", "note": "National brand with local storm teams — still outbound target if you sell lead/job tracking."},
        {"slug": "apple-roofing-cedar-rapids", "name": "Apple Roofing (serves Cedar Rapids)", "phone": None, "address": "IA office (Urbandale HQ — verify)", "website": "https://appleroof.com/cedar-rapids-ia/", "note": "Regional player; 24hr repair messaging."},
        {"slug": "a-plus-roofing-and-gutters", "name": "A Plus Roofing and Gutters", "phone": None, "address": "Cedar Rapids, IA metro", "website": "https://aplusroofinggutters.com/", "note": "Storm + financing messaging."},
        {"slug": "evans-construction-and-roofing", "name": "Evans Construction and Roofing", "phone": "(319) 241-5592", "address": "Cedar Rapids, IA area", "website": "https://www.evansconstructionandroofingia.com/", "note": "30+ yrs; steep + low slope commercial/residential."},
        {"slug": "heyn-brothers-roofing-iowa", "name": "Heyn Brothers Roofing (Iowa office)", "phone": "(319) 984-1680", "address": "Serves Eastern Iowa including CR corridor", "website": "https://heynbrothers.com/", "note": "Regional roofer; verify CR territory and local project manager."},
    ],
    "daycare": [
        {"slug": "kidspoint-childcare", "name": "KidsPoint", "phone": None, "address": "Downtown + C St locations, Cedar Rapids, IA", "website": "https://www.kidspointchildcare.org/", "note": "Large nonprofit-style childcare; multi-site scheduling + family comms."},
        {"slug": "kindercare-cedar-rapids-day-school", "name": "KinderCare / Cedar Rapids Day School", "phone": None, "address": "615 1st Ave SE, Cedar Rapids, IA (verify)", "website": "https://crdayschool.com/", "note": "Downtown center; national SOPs with local staffing friction."},
        {"slug": "trinity-early-childhood-academy", "name": "Trinity Early Childhood Academy (TECA)", "phone": None, "address": "Trinity Lutheran, Cedar Rapids, IA (verify)", "website": "https://www.trinitycr.org/childcare/", "note": "Licensed childcare + preschool; compliance paperwork angle."},
        {"slug": "apple-kids-childcare", "name": "Apple Kids Childcare", "phone": None, "address": "Marion + Cedar Rapids, IA", "website": "https://www.applekidschildcare.com/", "note": "Multi-location; transportation + summer camp messaging."},
        {"slug": "excel-daycare", "name": "Excel Daycare", "phone": None, "address": "Cedar Rapids, IA", "website": "https://exceldaycare.com/", "note": "Scholarship/partnership messaging — grant + enrollment tracking."},
        {"slug": "hand-in-hand-early-care", "name": "Hand In Hand Early Care & Education", "phone": None, "address": "Marion / Cedar Rapids / Hiawatha locations", "website": "https://handinhandinc.com/", "note": "Multi-site; tours + waitlist workflows."},
        {"slug": "la-petite-academy-cedar-rapids", "name": "La Petite Academy of Cedar Rapids", "phone": None, "address": "Cedar Rapids, IA (verify)", "website": "https://lapetite.com/area/cedar-rapids/", "note": "Franchise network; local director owns ops pain."},
        {"slug": "collins-aerospace-day-academy", "name": "Collins Aerospace Day Academy", "phone": None, "address": "Cedar Rapids, IA (verify)", "website": "https://collinsdayacademy.com/", "note": "Employer-sponsored center; waitlist + shift-care scheduling."},
        {"slug": "castles-daycare-academy", "name": "Castles Daycare Academy", "phone": None, "address": "Cedar Rapids, IA (verify on site)", "website": "https://castlesdaycareacademy.com/", "note": "Independent; literacy-focused curriculum messaging."},
        {"slug": "noahs-ark-preschool", "name": "Noah's Ark Preschool (Cedar Hills ministry)", "phone": "(319) 396-3125", "address": "6455 E Ave NW, Cedar Rapids, IA 52405", "website": "https://noahsarkcr.org/", "note": "Half-day preschool; enrollment + tuition tracking."},
    ],
    "manufacturing": [
        {"slug": "midwest-metal-products", "name": "Midwest Metal Products", "phone": None, "address": "Cedar Rapids, IA (verify)", "website": "https://www.mwestmp.com/", "note": "Precision fab since 1964; aerospace/medical customers — job tracking."},
        {"slug": "sadler-machine-company", "name": "Sadler Machine Company", "phone": None, "address": "Cedar Rapids, IA (verify)", "website": "https://www.sadlermachine.com/", "note": "CNC job shop ISO 9001; paper travelers to digital."},
        {"slug": "gk-systems", "name": "GK Systems", "phone": None, "address": "Cedar Rapids, IA (large facility)", "website": "https://www.gksystems.com/", "note": "Heavy fab + expansions; production scheduling."},
        {"slug": "dw-products", "name": "DW Products", "phone": None, "address": "Cedar Rapids, IA", "website": "https://www.dwproducts.com/", "note": "Swiss CNC since 1951; automotive/filtration — quality records."},
        {"slug": "cedar-rapids-tool-and-die", "name": "Cedar Rapids Tool & Die", "phone": None, "address": "Cedar Rapids, IA", "website": "https://cedarrapidstool.com/", "note": "Tool/die + machinery repair — job costing angle."},
        {"slug": "pmx-industries", "name": "PMX Industries, Inc.", "phone": "(319) 368-7700", "address": "5300 Willow Creek Dr SW, Cedar Rapids, IA 52404", "website": "https://www.ipmx.com/", "note": "~100+ employees; copper processing — compliance + production data."},
        {"slug": "world-class-industries", "name": "World Class Industries", "phone": None, "address": "925 N 15th Ave, Hiawatha, IA 52233 (HQ)", "website": "https://worldclassind.com/", "note": "Assembly/kitting for OEMs; inventory + supplier portals."},
        {"slug": "crystal-group", "name": "Crystal Group, Inc.", "phone": None, "address": "855 Metzger Dr, Hiawatha, IA 52233", "website": "https://www.crystalrugged.com/", "note": "Rugged servers; defense/aerospace — AS9100 traceability workflows."},
        {"slug": "bensons-cnc", "name": "BensonsCNC", "phone": "(319) 389-6346", "address": "Marion, IA (Cedar Rapids metro)", "website": "https://www.bensonscnc.com/", "note": "Family CNC shop; quoting + traveler digitization."},
        {"slug": "mid-america-manufacturing", "name": "Mid-America Manufacturing (MAM)", "phone": None, "address": "Marion, IA (verify)", "website": "https://midamericamfg.com/", "note": "ISO job shop; inspection documentation."},
    ],
    "nonprofits": [
        {"slug": "greater-cedar-rapids-community-foundation", "name": "Greater Cedar Rapids Community Foundation", "phone": None, "address": "324 3rd St SE, Ste 200, Cedar Rapids, IA 52401", "website": "https://www.gcrcf.org/", "note": "Grantmaking + donor advised funds — CRM + grant workflows."},
        {"slug": "newbo-city-market", "name": "NewBo City Market", "phone": "(319) 200-4050", "address": "1100 3rd St SE, Cedar Rapids, IA 52401", "website": "http://www.newbocitymarket.org/", "note": "Events + vendors; market ops + vendor applications."},
        {"slug": "kids-first-law-center", "name": "Kids First Law Center", "phone": "(319) 365-5437", "address": "420 6th St SE, Ste 160, Cedar Rapids, IA 52401", "website": "https://www.kidsfirstiowa.org/", "note": "Legal services for families; case management + intake."},
        {"slug": "foundation-2", "name": "Foundation 2", "phone": "(319) 362-1170", "address": "305 2nd Ave SE, Cedar Rapids, IA 52401", "website": "http://www.foundation2.org/", "note": "Crisis + youth services; shift scheduling + compliance."},
        {"slug": "indian-creek-nature-center", "name": "Indian Creek Nature Center", "phone": "(319) 362-0664", "address": "5300 Otis Rd SE, Cedar Rapids, IA 52403", "website": "http://www.indiancreeknaturecenter.org/", "note": "Programs + memberships; events + education scheduling."},
        {"slug": "boys-and-girls-clubs-corridor", "name": "Boys & Girls Clubs of the Corridor", "phone": "(319) 363-5766", "address": "420 6th St SE, Ste 240, Cedar Rapids, IA 52401", "website": "http://www.inmyclub.org/", "note": "Youth programs; busing + site staffing rotations."},
        {"slug": "big-brothers-big-sisters-eci", "name": "Big Brothers Big Sisters of Cedar Rapids & East Central Iowa", "phone": "(319) 377-8993", "address": "3150 E Ave NW, Ste 103, Cedar Rapids, IA 52405", "website": "http://www.bigcr.org/", "note": "Volunteer matching + case notes; HIPAA-style privacy not dental but PII-heavy."},
        {"slug": "cedar-rapids-parks-foundation", "name": "Cedar Rapids Parks Foundation", "phone": "(319) 360-3898", "address": "PO Box 2641, Cedar Rapids, IA 52406", "website": "https://www.crparkfoundation.org/", "note": "Donor stewardship + park project fundraising."},
        {"slug": "hawkeye-area-council-bsa", "name": "Hawkeye Area Council, BSA", "phone": "(319) 862-0541", "address": "660 32nd Ave SW, Cedar Rapids, IA 52404", "website": "https://hawkeyebsa.org/", "note": "Councils run camps + districts; volunteer + event registration stacks."},
        {"slug": "eastern-iowa-arts-academy", "name": "Eastern Iowa Arts Academy", "phone": "(319) 350-1805", "address": "1841 E Ave NE, Cedar Rapids, IA 52402 (verify)", "website": "https://www.easterniowaartsacademy.org/", "note": "Arts education nonprofit; class enrollment + financial aid + Amilia registration stack."},
    ],
}


def write_lead(industry: str, row: Row) -> None:
    slug = row["slug"]
    assert isinstance(slug, str)
    out = ROOT / industry / slug
    out.mkdir(parents=True, exist_ok=True)

    name = row.get("name") or slug.replace("-", " ").title()
    phone = row.get("phone") or "— verify on website or Google Maps"
    address = row.get("address") or "— verify"
    website = row.get("website") or "— none found in quick research"
    note = row.get("note") or ""

    profile = f"""# {name}

## Lead snapshot

| Field | Value |
|-------|--------|
| **Industry vertical** | `{industry}` |
| **Primary location** | {address} |
| **Phone** | {phone} |
| **Website** | {website} |
| **Stage** | `new-leads` (not contacted) |

## Angle for outreach

{note}

## Next actions for sales

1. Verify phone/address on official site or Google Business Profile.
2. Identify owner or GM (LinkedIn / state LLC / About page).
3. Log first dial outcome in `meeting-notes.md` (create on first touch).

## Internal links

- Industry playbook: `../../../02-industries/{industry}/`
- Move when qualified: `../../qualified/{slug}/` (copy folder)

---
*Generated from public web research — not affiliated with the business.*
"""
    (out / "company-profile.md").write_text(profile, encoding="utf-8")

    research = f"""# Lead research — {name}

## Sources consulted

- Company website (if any): {website}
- General web search / directory listings (Chamber-style, maps, industry lists)

## Data quality

- **Confidence:** Medium — always re-verify before quoting anything to the prospect.
- **Do-not-assume:** Authority contacts, private emails, tech stack, revenue.

## Suggested discovery questions

1. How do you take service calls today (phone only, answering service, software)?
2. Where do job or case details live (paper, spreadsheets, QuickBooks, industry app)?
3. What breaks when you are busiest (seasonal spike, storm week, Monday mornings)?

"""
    (out / "lead-research.md").write_text(research, encoding="utf-8")

    (out / "meeting-notes.md").write_text(
        "# Meeting notes\n\n_No contact yet._\n\n## First call\n\n- Date:\n- Who answered:\n- Notes:\n",
        encoding="utf-8",
    )


def main() -> None:
    gitkeep = ROOT / ".gitkeep"
    if gitkeep.exists():
        gitkeep.unlink()

    total = 0
    for industry, rows in LEADS.items():
        assert len(rows) == 10, f"{industry} must have 10 leads, got {len(rows)}"
        for row in rows:
            write_lead(industry, row)
            total += 1
    print(f"Wrote {total} leads under {ROOT}")


if __name__ == "__main__":
    main()
