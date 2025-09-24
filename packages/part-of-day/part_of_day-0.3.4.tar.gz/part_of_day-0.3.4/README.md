# Part of Day

This is an astral package wrapper, that uses it's calculations to give the part of day, instead of giving time intervals for spesific parts.

Usage example:
```python
from part_of_day import PartOfDayCalculator

from datetime import datetime, timezone

pod = PartOfDayCalculator(latitude=15.33, longitude=-7)

# following methods gives results related to now, if a datetime is not given
pod.is_it_day()
# True
pod.is_it_night()
# False
pod.get_part_of_day()
# <PartOfDay.DAY: 'Day'>

# or they can be used with a datetime
dt = datetime(2025, 3, 12, 6, 13, 25, 0, timezone.utc)

pod.is_it_day(dt)
# False
pod.is_it_night(dt)
# True
pod.get_part_of_day(dt)
# <PartOfDay.NIGHT: 'Night'>
```