from datetime import datetime
from RNGhaiku import tweet_haiku
from the_animal_bands import talent_scout
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every 3 hours
sched.add_job(tweet_haiku, 'interval', hours=3)
sched.add_job(talent_scout, 'interval', hours=3)

sched.start()
