# SARAO Machine Learning Utils 

Machine Learning utils  is a library for a convenient experience. Its consists of helper functions for creating astronomy/machine leanrning tools.

## Installation 

```
pip install saraomlutils

```

## Example

```
from saraomlutils.ga import get_night_window
from datetime import datetime

 # Get the night window for the proposed date
nightwindow = get_night_window(datetime.datetime.now())

nightwindow
```

