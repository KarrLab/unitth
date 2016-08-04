INSTALL
---
* unzip
* edit and move the unitth.properties file to the working directory or $HOME

unitth.properties
---
Make sure to get the paths correct in here, especially if running on Microsoft 
platforms. There should be enough examples in the provided properties file.

If preferring to use system properties instead feel free to do so. All properties
defined as system properties will override the default ones and those in the 
unitth.properties file.

USAGE
---
java -jar unitth.jar <folders containing JUnit XML test reports>[* N]

Example:
java -jar unitth.jar build02/junitreport build04/junitreport 
build04/junitreport

NOTES
---
The reports shall not be moved around after generation since all the links 
will be generated as relative paths.