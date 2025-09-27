# dcnr-scheduler

Minimal example package. After installation:

```python

from dcnr_scheduler import ScheduledRun, ScheduledPlan
from datetime import datetime

@ScheduledRun("at * on mon-fri freq 30/hour")
def print_msg(plan:ScheduledPlan, curr_dt:datetime):
    print(curr_dt, 'Hello world')

```