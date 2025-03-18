# Map GMDN codes to EMDN Hierarchy
## General Information:
bash script for easy use coming soon

better instructions will also come soon
>needs tensorflow to be installed to run

first time run will take longer, since the AI models will need to be downloaded


### How to use:
in root dir run /PreProcessing/EMDNpreproc.py with EMDNV2[.xslx](https://webgate.ec.europa.eu/dyna2/emdn/) file in /Input directory to create EMDN hierarchy in text format

repeat with /PreProcessing/EMDNgetLeafs.py and /PreProcessing/EMDNget2ndLayer.py

run /PreProcessing/xmlExtract.py with a subdirectory called "20250304" in /Input with all the [extracted gmdn codes](https://accessgudid.nlm.nih.gov/download) in directory to get GMDN data in text format

run Main.py to get (current crude) output of translation from GMDN code to EMDN code

### still a work-in-progress