# TOC regex

## V1

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(Top|\d+(?:\.\d+)*)\", \"(Navigation|[^\"]+)\", (?:tocLink|\"content\/([^\"]+)\")\); \/\/(.*)$", re.MULTILINE)

```

## V2

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(Top|\d+(?:\.\d+)*)\", \"(Navigation|((Frau|Herr|Präsident|Präsidentin) ([^\(]+?) \(([^\)]+)\))|[^\"]+)\", (?:tocLink|\"content\/([^\"]+)\")\); \/\/(0|(\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*)$", re.MULTILINE)
```

## V3

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<salutation>Frau|Herr|Präsident|Präsidentin) (?P<name>[^\(]+?) \((?P<party>[^\)]+)\))|[^\"]+)\", (?:tocLink|\"content\/([^\"]+)\")\); \/\/(0|(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*)$", re.MULTILINE)
```

## V4

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<salutation>Frau|Herr|Präsident|Präsidentin) (?P<name>[^\(]+?) \((?P<party>[^\)]+)\))|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>[^\"]+))|[^\"]+)\", (?:tocLink|\"(?P<href>content\/[^\"]+)\")\); \/\/(0|(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*)$", re.MULTILINE)
```

## V5

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>[^\"]+))|(?:(?:(?P<salutation>Frau|Herr|Präsident|Präsidentin|Ratspräsidentin|Ratspräsident) )?(?P<name>[^\(]+?) \((?P<party>[^\)]+)\))|[^\"]+)\", (?:tocLink|\"(?P<href>content\/[^\"]+)\")\); \/\/(0|(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*)$", re.MULTILINE)
```

## V6

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>.+))|(?:(?:(?P<salutation>Frau|Herr|Präsident|Präsidentin|Ratspräsidentin|Ratspräsident) )?(?P<name>[^\(]+?) \((?P<party>[^\)]+)\))|[^\"]+)\", (?:tocLink|\"(?P<href>content\/[^\"]+)\")\); \/\/(0|(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*)$", re.MULTILINE)
```

## V7

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?:(?P<salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<name>.+?) \((?P<party>[^\)]+)\))|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>[^\"]+))|[^\"]+)\", (?:tocLink|\"(?P<href>content\/[^\"]+)\")\); \/\/(0|(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*)$", re.MULTILINE)
```

## V8

```python
import re

e = re.compile(r"^(tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>.+?))|(?:Sitzung (?P<meet_id>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<name>.+?) \((?P<party>[^\)]+)\))|[^\"]+)\", (?:tocLink|\"(?P<href>content\/[^\"]+)\")\); \/\/(0|null|(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+).*))$", re.MULTILINE)
```

## V9

```python
import re

e = re.compile(r"^(tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>.+?))|(?:Sitzung (?P<meet_id>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<name>.+?) \((?P<party>[^\)]+)\))|(?:(?P<meet_misc_type>Revision Reglement|Altlastensanierung),? +(?P<meet_misc_title>.+?))|[^\"]+)\", (?:tocLink|\"(?P<href>content\/[^\"]+)\")\); \/\/(?:(?P<time>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*))$", re.MULTILINE)
```

## V10

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<gr_number>\d{4}\/\d+) (?P<title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<name>.+?) \((?P<party>[^\)]+)\))|(?:(?P<meet_misc_type>Revision Reglement|Altlastensanierung),? +(?P<meet_misc_title>.+?))|[^\"]+)\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$", re.MULTILINE)
```

## V11

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<level>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<name>.+?) \((?P<party>[^\)]+)\))|(?:(?P<meet_misc_type>Revision Reglement|Altlastensanierung),? +(?P<meet_misc_title>.+?))|[^\"]+)\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$", re.MULTILINE)
```

## V12

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<id>Top|\d+(?:\.\d+)*)\", \"(Navigation|Mitteilungen|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<item_title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<speaker_salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<speaker_name>.+?) \((?P<speaker_party>[^\)]+)\))|(?:(?P<meet_misc_type>Revision Reglement|Altlastensanierung),? +(?P<meet_misc_title>.+?))|[^\"]+)\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$", re.MULTILINE)
```

## V13

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<id>Top|\d+(?:\.\d+)*)\", \"(Navigation|(?P<item_announcements>Mitteilungen)|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<item_title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<speaker_salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<speaker_name>.+?) \((?P<speaker_party>[^\)]+)\))|(?:(?P<meet_misc_type>Revision Reglement|Altlastensanierung),? +(?P<meet_misc_title>.+?))|[^\"]+)\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$", re.MULTILINE)
```

## V14

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<id>Top|\d+(?:\.\d+)*)\", \"(Navigation|(?P<item_announcements>Mitteilungen)|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<item_title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<speaker_salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<speaker_name>.+?) \((?P<speaker_party>[^\)]+)\))|(?:(?P<item_misc_type>Revision Reglement|Altlastensanierung),? +(?P<item_misc_title>.+?))|[^\"]+)\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$", re.MULTILINE)
```

## V15

```python
import re

e = re.compile(r"^tocTab\[ir\+\+\] = new Array \(\"(?P<id>Top|\d+(?:\.\d+)*)\", \"(Navigation|(?P<item_announcements>Mitteilungen)|(?:(?P<item_id>(?P<item_year>\d{4})\/(?P<item_number>\d+)) (?P<item_title>.+?))|(?:Sitzung (?P<meet_nr>\d+) vom (?P<meet_date>\d{2}\.\d{2}\.\d{4}))|(?:(?:(?P<speaker_salutation>Frau|Herr|(?:(?:Rats|P)räsident(?:in)?)) )?(?P<speaker_name>.+?) \((?P<speaker_party>[^\)]+)\))|(?P<item_misc>[^\"]+))\", (?:tocLink|\"(?P<url>content\/[^\"]+)\")\); \/\/(?:(?P<updated_at>\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}:\d+)|.*)$", re.MULTILINE)
```

## V

```python
import re

e = re.compile(r"", re.MULTILINE)
```

## V

```python
import re

e = re.compile(r"", re.MULTILINE)
```

## V

```python
import re

e = re.compile(r"", re.MULTILINE)
```

## V

```python
import re

e = re.compile(r"", re.MULTILINE)
```

## V

```python
import re

e = re.compile(r"", re.MULTILINE)
```