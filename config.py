# Import the necessary module
from datetime import datetime

# Define the value
url = "https://pengguna.merahputih.id/register"
utc_datetimenow = datetime.today().isoformat(timespec="minutes")
utc_datetimenow = utc_datetimenow.replace("-", "").replace(":", "")
nama = "Register Monitor"
username = nama.replace(" ", ".")
username = username + "." + utc_datetimenow
password = "ipnet2017"
cfmPassword = "ipnet2017"
dob = "17081945"
gender = "women"
handphone = "085221300832"
