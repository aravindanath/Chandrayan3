import time
import datetime
from datetime import datetime

print(datetime.now())

date = str(datetime.now())
st =date.replace("-","_").replace(" ","_").replace(":","_")
print(st.split(".")[0])
print(time.time())
print(str(round(time.time())))





