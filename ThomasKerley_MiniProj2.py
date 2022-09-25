# Import Faker.
from faker import Faker
# Import the WifiESSID class from Faker Wi-Fi ESSID.
from faker_wifi_essid import WifiESSID

fake = Faker()                                                                                                      
fake.add_provider(WifiESSID)                                                                                        
for i in range(20):                                                                                                 
    fake.wifi_essid()  