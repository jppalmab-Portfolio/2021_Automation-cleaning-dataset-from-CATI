import pandas as pd
import re
import numpy as np
from datetime import datetime
import time
import os


start_instance_time = datetime.now()
current_time = start_instance_time.strftime("%H:%M")
print("The instance -Running.py- has started at", current_time)

time.sleep(5)
print("Processing...")


# Open

exec(open("01 open.py").read())

# Regex
print("We are fixing the <apellidos compuestos> problem!")
exec(open("02 regex.py").read())
time.sleep(5)

# Split

exec(open("03 split.py").read())

# Save

exec(open("04 save.py").read())

#### Finishing the app
end_instance_time = datetime.now()
finish_time = end_instance_time.strftime("%H:%M")
print("The whole instance of -Running.py- has finished taking", round((end_instance_time - start_instance_time).total_seconds()/60), "minutes approx")
print("You can find the final database in the -01 output- folder")
print("This app was coded by Juan Pablo Palma B.")