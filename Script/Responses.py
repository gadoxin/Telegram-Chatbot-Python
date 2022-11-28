from datetime import datetime

# "This Bot was created by Gad Kalu Obioma #Please support
# 0795559208
# Access bank
# Gad Obioma kalu"

import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config

def sample_response(input_text):
    user_message = str(input_text).lower()
    if user_message in ("1", ):
        return "t_mobile Entered SuccesFully \n\n click /t_mobile"


    if user_message in ("James", "Philip", "John", "john", "philip", "james",):
        return "/confirm_name\n\n" \


    if user_message in ("07012346735",):
        return "/confirm_old_number\n\n" \


    if user_message in ("08163767615",):
        return "/Confirm_New_Number\n\n" \

    if user_message in ("United States", "unitedstates", "united states",):
        return "/confirm_address"

    if user_message in ("2", ):
        return "AT&T Entered SuccesFully \n\n click /ATnT"


    if user_message in ("3",):
        return "Sprint Entered SuccesFully \n\n click /Sprint"


    if user_message in ("4",):
        return "USCelluller Entered SuccesFully \n\n click /USCelluller"


    if user_message in ("5",):
        return "Cricketwireless Entered SuccesFully \n\n click /Cricketwireless"


    if user_message in ("6",):
        return "Ting Entered SuccesFully \n\n click /Ting"


    if user_message in ("am new",):
        return "wecome mate!"



    if user_message in ("time", "time?"):
        now = datetime.now()

        date_time = now.strftime("%d/%m/%y, %H:%H%S")


        return str(date_time)

# "This Bot was created by #Gad Kalu Obioma"



