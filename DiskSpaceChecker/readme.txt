DiskSpaceChecker
================
Simple C# console app which takes 1 argument: path name
Starting at given path, recursively reads contents of every folder and outputs a summary of
-Full path name
- No Files
- Total file size
- Earliest file
- Latest file
Output is in CSV format, so this can be opened in Excel and analysed eg sort by size etc

Intended to help with archiving from Unix share

Example Usage:
=============
DiskSpaceChecker.exe \\global.nomura.com\CORP\nfs\bis-ipvglobal
