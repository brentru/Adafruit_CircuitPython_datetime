# SPDX-FileCopyrightText: 2001-2021 Python Software Foundation.All rights reserved.
# SPDX-FileCopyrightText: 2000 BeOpen.com. All rights reserved.
# SPDX-FileCopyrightText: 1995-2001 Corporation for National Research Initiatives.
#                         All rights reserved.
# SPDX-FileCopyrightText: 1995-2001 Corporation for National Research Initiatives.
#                         All rights reserved.
# SPDX-FileCopyrightText: 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
# SPDX-FileCopyrightText: 2021 Brent Rubell for Adafruit Industries
# SPDX-License-Identifier: GPL-2.0-or-later

# Example of working with a `time` object
# from https://docs.python.org/3/library/datetime.html#examples-of-usage-time
from adafruit_datetime import time, timezone

# Create a new time object
t = time(12, 10, 30, tzinfo=timezone.utc)

# ISO 8601 formatted string
iso_time = t.isoformat()
print("ISO8601-Formatted Time:", iso_time)

# Timezone name
print("Timezone Name:", t.tzname())

# Return a string representing the time, controlled by an explicit format string
strf_time = t.strftime("%H:%M:%S %Z")
print("Formatted time string:", strf_time)

# Specifies a format string in formatted string literals
print("The time is {:%H:%M}.".format(t))
