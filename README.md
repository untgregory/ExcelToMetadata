# ExcelToMetadata

This script takes an Excel workbook containing 3 sheets (IPTC, MODS, and DC) and turns those sheets into a MODS.csv, a DC.csv, and an
IPTC.txt files and places them in a new folder.  The IPTC.txt file can be used with the Adobe Bridge Cultural Heritage Panel to attach
metadata directly to files.  The two csvs can be loaded into OpenRefine and altered in templating with the 2 templates provided in order
to create xml metadata files for each .tif or .jpg needed.
