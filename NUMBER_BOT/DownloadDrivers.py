#!/usr/bin/python3
from pathlib import Path
import pandas as pd
import logging
from datetime import datetime
import os

logging.basicConfig(filename='/home/pi/DOWNLOAD_DRIVERS_INFO.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
filepath = Path('Drivers.csv')
now=datetime.now()
current_time=now.strftime("%D-%H:%M:S")
# just appending is not an option because people can leave the championship
# in case the webpage can't be reach
# also because crontab all print will be appended to a file
try:
    df=pd.read_html('https://www.rallysimfans.hu/rbr/bajnoksag2.php?b=reszletek&bajnoksag_id=251&nevezes_lista')
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        file = open(filepath, 'w')
        file.close()
    filepath.parent.mkdir(parents=True, exist_ok=True)
    if len(df[20])>2:
        df[20].to_csv(filepath)
        print("Written to file "+current_time)
except Exception as e:
    logger.error(e)
    print(str(e)+" "+current_time)
