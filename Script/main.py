import Constants as keys
from telegram.ext import *
import Responses as R
# start of online server proxy config

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


print ("Bot has started")

def start_command(update, context):
    update.message.reply_text("Greetings 👋 👋 \n\n\n"
                              "Menu\n\n"
                              "<SwapSim> 🔒 ✅ \n\n"
                              "<u1chips> 🔒 ✅ \n\n"
                              "<SwapHistory> 🔒 ✅ \n\n"
                              "<About> 🔒 ✅ \n\n"
                              "<Xtra> 🔒 ✅ \n\n"
                              "<Support> 🔒 ✅  \n\n\n"
                              "menu locked 🔒 ✅ \n\n"
                              "Botkey 🔑 required to access menu...\n\n"
                              "Get 🔑 /BotKey")

def t_mobile_command(update, context):
    update.message.reply_text("<Please select t_mobile Info!>\n\n"
                              "click /t_mobile_Info")

def ATnT_command(update, context):
    update.message.reply_text("<Please select AT&T Info!>\n\n"
                              "click /ATnT_Info")


def ATnT_Info_command(update, context):
    update.message.reply_text("<The information Below is required to process simswap>\n\n"
                              "1. old number\n\n"
                              "2. new number\n\n"
                              "3. plan\n\n"
                              "4. Address\n\n"
                              "click /ATnT_Form")

def ATnT_Form_command(update, context):
    update.message.reply_text("Enter info in this format\n\n"
                              "Enter your full name\n\n"
                              "Old number\n\n"
                              "Plan\n\n"
                              "Address\n\n"
                              "click --> /saveATnT ✅ to save after entering info")

def saveATnT_command(update, context):
    update.message.reply_text("<saved Successfully>\n\n"
                              "Click /Confirm_ATnT_swap")


def Confirm_ATnT_swap_command(update, context):
    update.message.reply_text("Verification code sent to AT&T, number takes approximately 2-5 mins to recieve\n"
                              "wait at least 2 mins \n\n click /Swapped_ATnT")


def Swapped_ATnT_command(update, context):
    update.message.reply_text("<The Sim card for oldnumber has been changed to AT&T>\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Congrats")


def Sprint_command(update, context):
    update.message.reply_text("<Please select Sprint Info!>\n\n"
                              "click /Sprint_Info")

def Sprint_Info_command(update, context):
    update.message.reply_text("<The information Below is required to process simswap>\n\n"
                              "1. old number\n\n"
                              "2. new number\n\n"
                              "3. plan\n\n"
                              "4. Address\n\n"
                              "click /Sprint_Form")

def Sprint_Form_command(update, context):
    update.message.reply_text("Enter info in this format\n\n"
                              "Enter your full name\n\n"
                              "Old number\n\n"
                              "Plan\n\n"
                              "Address\n\n"
                              "click --> /saveSprint ✅ to save after entering info")

def saveSprint_command(update, context):
     update.message.reply_text("<saved Successfully>\n\n"
                               "Click /Confirm_Sprint_swap")


def Confirm_Sprint_swap_command(update, context):
    update.message.reply_text("Verification code sent to Sprint, number takes approximately 2-5 mins to recieve\n"
                              "wait at least 2 mins \n\n afterwards click /Swapped_Sprint")


def Swapped_Sprint_command(update, context):
    update.message.reply_text("<The Sim card for oldnumber has been changed to Sprint>\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Congrats")


def USCelluller_command(update, context):
    update.message.reply_text("<Please select USCelluller Info!>\n\n"
                              "click /USCelluller_Info")

def USCelluller_Info_command(update, context):
    update.message.reply_text("<The information Below is required to process simswap>\n\n"
                              "1. old number\n\n"
                              "2. new number\n\n"
                              "3. plan\n\n"
                              "4. Address\n\n"
                              "click /USCelluller_Form")

def USCelluller_Form_command(update, context):
    update.message.reply_text("Enter info in this format\n\n"
                              "Enter your full name\n\n"
                              "Old number\n\n"
                              "Plan\n\n"
                              "Address\n\n"
                              "click --> /saveUSCelluller ✅ to save after entering info")


def saveUSCelluller_command(update, context):
    update.message.reply_text("<saved Successfully>\n\n"
                              "Click /Confirm_USCelluller_swap")

def Confirm_USCelluller_swap_command(update, context):
    update.message.reply_text("Verification code sent to USCelluller, number takes approximately 2-5 mins to recieve\n"
                              "wait at least 2 mins \n\n afterwards click /Swapped_USCelluller")

def Swapped_USCelluller_command(update, context):
    update.message.reply_text("<The Sim card for oldnumber has been changed to USCelluller>\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Congrats")


def Cricketwireless_command(update, context):
    update.message.reply_text("<Please select Cricketwireless Info!>\n\n"
                              "click /Cricketwireless_Info")

def Cricketwireless_Info_command(update, context):
    update.message.reply_text("<The information Below is required to process simswap>\n\n"
                              "1. old number\n\n"
                              "2. new number\n\n"
                              "3. plan\n\n"
                              "4. Address\n\n"
                              "click /Cricketwireless_Form")

def Cricketwireless_Form_command(update, context):
    update.message.reply_text("Enter info in this format\n\n"
                              "Enter your full name\n\n"
                              "Old number\n\n"
                              "Plan\n\n"
                              "Address\n\n"
                              "click --> /saveCricketwireless ✅ to save after entering info")

def saveCricketwireless_command(update, context):
    update.message.reply_text("<saved Successfully>\n\n"
                              "Click /Confirm_Cricketwireless_swap")

def Confirm_Cricketwireless_swap_command(update, context):
    update.message.reply_text("Verification code sent to tmobile, number takes approximately 2-5 mins to recieve\n"
                              "wait at least 2 mins \n\n afterwards click /Swapped_Cricketwireless")

def Swapped_Cricketwireless_command(update, context):
    update.message.reply_text("<The Sim card for oldnumber has been changed to Cricketwireless>\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Congrats")

def t_mobile_Info_command(update, context):
    update.message.reply_text("<The information Below is required to process simswap>\n\n"
                              "1. old number\n\n"
                              "2. new number\n\n"
                              "3. plan\n\n"
                              "4. Address\n\n"
                              "click /tmobile_Form")

def tmobile_Form_command(update, context):
    update.message.reply_text("Enter info in this format\n\n"
                              "Enter your full name\n\n"
                              "Old number\n\n"
                              "Plan\n\n"
                              "Address\n\n"
                              "click --> /savetmobile ✅ to save after entering info")

def savetmobile_command(update, context):
    update.message.reply_text("<saved Successfully>\n\n"
                              "Click /Confirm_tmobile_swap")

def Confirm_tmobile_swap_command(update, context):
    update.message.reply_text("Verification code sent to tmobile, number takes approximately 2-5 mins to recieve\n"
                              "wait at least 2 mins \n\n afterwards click /Swapped_tmobile")

def Swapped_tmobile_command(update, context):
    update.message.reply_text("<The Sim card for oldnumber has been changed to t_mobile>\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Congrats")


def Ting_command(update, context):
    update.message.reply_text("<Please select Ting Info!>\n\n"
                              "click /Ting_Info")


def Ting_Info_command(update, context):
    update.message.reply_text("<The information Below is required to process simswap>\n\n"
                              "1. old number\n\n"
                              "2. new number\n\n"
                              "3. plan\n\n"
                              "4. Address\n\n"
                              "click /Ting_Form")


def Ting_Form_command(update, context):
    update.message.reply_text("Enter info in this format\n\n"
                              "Enter your full name\n\n"
                              "Old number\n\n"
                              "Plan\n\n"
                              "Address\n\n"
                              "click --> /saveTing ✅ to save after entering info")


def saveTing_command(update, context):
    update.message.reply_text("<saved Successfully>\n\n"
                              "Click /Confirm_Ting_swap")


def Confirm_Ting_swap_command(update, context):
    update.message.reply_text("Verification code sent to Ting, number takes approximately 2-5 mins to recieve\n"
                              "wait at least 2 mins \n\n afterwards click /Swapped_Ting")


def Swapped_Ting_command(update, context):
    update.message.reply_text("<The Sim card for oldnumber has been changed to Ting>\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Congrats")





def u1chips_command(update, context):
    update.message.reply_text("u1chips🌑\n\n"
                              "<Hello>\n"
                              "u1chips balance: 5🌑\n\n"
                              "u1chips are used to process SIM Swap requests \n\n"
                              "1 Swap = 20🌑\n\n"
                              "click /SelectU1chipsPlan")

def SwapMenu_command(update, context):
    update.message.reply_text("u1Swap Menu\n\n"
                              "/SwapSim 💕\n\n"
                              "/u1chips 🌑\n\n"
                              "/History 🗒️\n\n"
                              "/About 🆕\n\n"
                              "/Xtra 👽")



def History_command(update, context):
    update.message.reply_text("u1Swap History 📖\n\n"
                              "Last 💕:\n"
                              "3/10/2022 - T-Mobile - +1(226)-12^***\n"
                              "Daneil benson\n"
                              "1667-8196-6188-81627\n\n"
                              "Total 💕:\n"
                              "14\n\n"
                              "Total 🌑:\n"
                              "280 u1chips\n\n"
                              "Claimed 🌑:\n"
                              "15 u1chips")

def About_command(update, context):
    update.message.reply_text("<ABOUT>\n\n"
                              "ℹ️U1\n"
                              "u1 is an automated network operator, also known as a wireless service provider.\n"
                              "u1 provide wireless communications service that controls all the elements necessary\n"
                              "to deliver services to an end user, including wireless network infrastructure\n"
                              "back haul infrastructure, billing and customer care.\n\n"
                              "click /Version to check u1 version\n\n"
                              "click /Update to check for recent update")

def Version_command(update, context):
    update.message.reply_text("<VERSION>\n\n"
                              "u1 Version 2.78")

def Update_command(update, context):
    update.message.reply_text("<UPDATE>\n\n"
                              "u1Swap vsersion is updated")


def Xtra_command(update, context):
    update.message.reply_text("Xtra 👽\n\n"
                              "Click on the options below for Xtra features\n\n"
                              "1. /CarrierLookup\n\n"
                              "2. /ActivateSIMCard\n\n"
                              "3. /DeactivateSIMcard\n\n"
                              "3. /ChangeSIMPin\n\n"
                              "4. /TransferContacts\n\n"
                              "5. /RestoreContacts")


def CarrierLookup_command(update, context):
    update.message.reply_text("Update to version 3.28")

def ActivateSIMCard_command(update, context):
    update.message.reply_text("Update to version 3.28")


def DeactivateSIMcard_command(update, context):
    update.message.reply_text("Update to version 3.28")


def ChangeSIMPin_command(update, context):
    update.message.reply_text("Update to version 3.28")

def TransferContacts_command(update, context):
    update.message.reply_text("Update to version 3.28")

def RestoreContacts_command(update, context):
    update.message.reply_text("Update to version 3.28")


def SelectU1chipsPlan_command(update, context):
    update.message.reply_text("u1chips Plan🗒️\n\n"
                              "++++++++++++++++++++++++\n"
                              "click /BEGINNER:\n\n"
                              "click /PRO:\n\n"
                              "click /MASTER:\n"
                              "++++++++++++++++++++++++++\n")

def BEGINNER_command(update, context):
    update.message.reply_text("++++++++++++++\n"
                              "Beginner Plan\n\n"
                              "25 Swapbit = 0.02892682 BTC\n\n"
                              "Click /PaymentMethod1\n"
                              "++++++++++++++")

def PRO_command(update, context):
    update.message.reply_text("++++++++++++++\n"
                              "Pro Plan\n\n"
                              "55 Swapbit = 0.06383849 BTC BTC\n\n"
                              "Click /PaymentMethod1\n"
                              "++++++++++++++")

def MASTER_command(update, context):
    update.message.reply_text("++++++++++++++\n"
                              "Pro Plan\n\n"
                              "110 Swapbit = 0.10473502 BTC\n\n"
                              "Click /PaymentMethod1\n"
                              "++++++++++++++")


def BotKey_command(update, context):
    update.message.reply_text("Bot Key is required to unlock bot features-below\n \n"
                              "1. Swapping US SIM Cards\n \n"
                              "2. Activate SIM Card\n \n"
                              "3. Deactivate SIM Card\n \n"
                              "4. Change SIM Pin\n \n"
                              "5. Transfer Contacts\n \n"
                              "6. Restore Contacts\n\n"
                              "Get /PurchaseKey 🔑")

def PurchaseKey_command(update, context):
    update.message.reply_text("Bot activation key 🔑\n\n"
                              "Key: SS^*****\n\n"
                              "Payment fee via btc: 0.000181 BTC\n \n"
                              "Payment fee via XRP: 8.25 XRP\n \n"
                              "Payment fee via ETH: 0.003347 ETH\n \n"
                              "Payment Fee via USDT: 3 USDT\n \n"
                              "Validity: Lifetime\n \n"
                              "Click /Email")

def Email_command(update, context):
    update.message.reply_text(" <Enter email to checkout.>\n\n"
                               "Afterwards click /savemail")

def savemail_command(update, context):
        update.message.reply_text("<mail saved Successfully>\n\n"
                                  "Click /PaymentMethod")

def PaymentMethod1_command(update, context):
    update.message.reply_text("<Select a Payment Method>\n\n"
                              "1.  /BTC1\n \n"
                              "2.  /USDT(ERC20)1\n \n"
                              "3.  /ETH1\n \n"
                              "4.  /XRP1\n \n")


def BTC1_command(update, context):
    update.message.reply_text("Payment via bitcoin should be made to this address\n \n"
                              "BTC Address: bc1qn39a4yqzlsqs0ykr83zpcp9ns874n4jaakv2eq \n \n"
                              "/ActivatePlan ✅")


def USDT1_command(update, context):
    update.message.reply_text("Payment via USDT should be made to this address\n \n"
                              "USDT Address:  0xBCb7877236fB4feb1E34C27dabeB4473B557799F\n \n"
                              "/ActivatePlan ✅")


def ETH1_command(update, context):
    update.message.reply_text("Payment via  should be made to this address\n \n"
                              "ETH Address:  0xBCb7877236fB4feb1E34C27dabeB4473B557799F \n \n"
                              "/ActivatePlan ✅")


def XRP1_command(update, context):
    update.message.reply_text("Payment via  should be made to this address\n \n"
                              "XRP Address: rhmrWCMDtEfjKRpyAWvJAKgj4pNLtQtutb \n \n"
                              "/ActivatePlan"
                              )


def PaymentMethod_command(update, context):
        update.message.reply_text("<Select a Payment Method>\n\n"
                                  "1.  /BTC\n \n"
                                  "2.  /USDT(ERC20)\n \n"
                                  "3.  /ETH\n \n"
                                  "4.  /XRP\n \n")

def BTC_command(update, context):
    update.message.reply_text("Payment via bitcoin should be made to this address\n \n"
                              "BTC Address:  bc1qn39a4yqzlsqs0ykr83zpcp9ns874n4jaakv2eq \n \n"
                              "/Next ✅\n\n")

def USDT_command(update, context):
    update.message.reply_text("Payment via USDT should be made to this address\n \n"
                              "USDT Address: 0x45cbB12214751A3A5889a82Be7e9E66113AF77AD \n \n"
                              "/Next ✅\n\n")

def ETH_command(update, context):
    update.message.reply_text("Payment via  should be made to this address\n \n"
                              "ETH Address: 0x45cbB12214751A3A5889a82Be7e9E66113AF77AD \n \n"
                              "/Next ✅\n\n")


def XRP_command(update, context):
    update.message.reply_text("Payment via  should be made to this address\n \n"
                              "XRP Address: rhmrWCMDtEfjKRpyAWvJAKgj4pNLtQtutb \n \n"
                              "/Next ✅\n\n")

def Next_command(update, context):
    update.message.reply_text("Payments will confirm within 1-3 mins\n \n"
                              "Bot activation key 🔑 will be sent to your mail shortly.\n\n"
                              "Unconfirmed payment will culminate in order termination\n\n"
                              "Thanks")


def ActivatePlan_command(update, context):
    update.message.reply_text("Payments will confirm within 1-3 mins\n \n"
                              "Unconfirmed payment will culminate in order termination\n\n")

def ss210_command(update, context):
    update.message.reply_text("Lets get started 🤩\n\n"
                              "click /SwapMenu fo more info")

def SwapSim_command(update, context):
    update.message.reply_text("Sim Swap 💕\n\n"
                              "<Please Enter SIM card Carrier \n\n"
                              "<Enter>  1  for t_mobile\n\n"
                              "<Enter>  2  for AT&T\n\n"
                              "<Enter>  3  for Sprint\n\n"
                              "<Enter>  4  for U.S.Celluller\n\n"
                              "<Enter>  5  for Cricket wireless\n\n"
                              "<Enter>  6  for Ting")

def confirm_name_command(update, context):
    update.message.reply_text("Name saved succesfully\n\n"
                              "enter old number")

def confirm_old_number_command(update, context):
    update.message.reply_text("Number saved succesfully\n\n"
                              "<enter the new number you want transfer>")

def confirm_new_number_command(update, context):
    update.message.reply_text("New number saved succesfully\n\n"
                              "<enter address>")

def confirm_address_command(update, context):
    update.message.reply_text("click to save in SIM card Carrier \n\n" 
                               "1. /savetmobile ✅ \n\n"
                               "2. /saveTing ✅\n\n"
                               "3. /saveCricketwireless ✅\n\n"
                               "4. /saveUSCelluller ✅\n\n"
                               "5. /saveSprint ✅\n\n"
                               "6. /saveATnT ✅")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("t_mobile", t_mobile_command))
    dp.add_handler(CommandHandler("ATnT",  ATnT_command))
    dp.add_handler(CommandHandler("ATnT_Info", ATnT_Info_command))
    dp.add_handler(CommandHandler("ATnT_Form", ATnT_Form_command))
    dp.add_handler(CommandHandler("saveATnT", saveATnT_command))
    dp.add_handler(CommandHandler("Confirm_ATnT_swap", Confirm_ATnT_swap_command))
    dp.add_handler(CommandHandler("Swapped_ATnT", Swapped_ATnT_command))
    dp.add_handler(CommandHandler("Sprint", Sprint_command))
    dp.add_handler(CommandHandler("Sprint_Info", Sprint_Info_command))
    dp.add_handler(CommandHandler("Sprint_Form", Sprint_Form_command))
    dp.add_handler(CommandHandler("saveSprint", saveSprint_command))
    dp.add_handler(CommandHandler("Confirm_Sprint_swap", Confirm_Sprint_swap_command))
    dp.add_handler(CommandHandler("Swapped_Sprint", Swapped_Sprint_command))
    dp.add_handler(CommandHandler("USCelluller", USCelluller_command))
    dp.add_handler(CommandHandler("USCelluller_Info", USCelluller_Info_command))
    dp.add_handler(CommandHandler("USCelluller_Form",USCelluller_Form_command))
    dp.add_handler(CommandHandler("saveUSCelluller", saveUSCelluller_command))
    dp.add_handler(CommandHandler("Confirm_USCelluller_swap",Confirm_USCelluller_swap_command))
    dp.add_handler(CommandHandler("Swapped_USCelluller",Swapped_USCelluller_command))
    dp.add_handler(CommandHandler("Cricketwireless",  Cricketwireless_command))
    dp.add_handler(CommandHandler("Cricketwireless_Info", Cricketwireless_Info_command))
    dp.add_handler(CommandHandler("Cricketwireless_Form", Cricketwireless_Form_command))
    dp.add_handler(CommandHandler("saveCricketwireless", saveCricketwireless_command))
    dp.add_handler(CommandHandler("Confirm_Cricketwireless_swap", Confirm_Cricketwireless_swap_command))
    dp.add_handler(CommandHandler("Swapped_Cricketwireless", Swapped_Cricketwireless_command))
    dp.add_handler(CommandHandler("t_mobile_Info", t_mobile_Info_command))
    dp.add_handler(CommandHandler("savetmobile", savetmobile_command))
    dp.add_handler(CommandHandler("Swapped_tmobile",Swapped_tmobile_command))
    dp.add_handler(CommandHandler("tmobile_Form", tmobile_Form_command))
    dp.add_handler(CommandHandler("Confirm_tmobile_swap", Confirm_tmobile_swap_command))
    dp.add_handler(CommandHandler("Ting", Ting_command))
    dp.add_handler(CommandHandler("Ting_Info", Ting_Info_command))
    dp.add_handler(CommandHandler("Ting_Form", Ting_Form_command))
    dp.add_handler(CommandHandler("Confirm_Ting_swap", Confirm_Ting_swap_command))
    dp.add_handler(CommandHandler("Swapped_Ting", Swapped_Ting_command))
    dp.add_handler(CommandHandler("saveTing", saveTing_command))
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("savemail", savemail_command))
    dp.add_handler(CommandHandler("Email", Email_command))
    dp.add_handler(CommandHandler("PaymentMethod", PaymentMethod_command))
    dp.add_handler(CommandHandler("PurchaseKey", PurchaseKey_command))
    dp.add_handler(CommandHandler("BotKey", BotKey_command))
    dp.add_handler(CommandHandler("ss210", ss210_command))
    dp.add_handler(CommandHandler("SwapSim", SwapSim_command))
    dp.add_handler(CommandHandler("BTC", BTC_command))
    dp.add_handler(CommandHandler("USDT", USDT_command))
    dp.add_handler(CommandHandler("ETH", ETH_command))
    dp.add_handler(CommandHandler("XRP", XRP_command))
    dp.add_handler(CommandHandler("Next", Next_command))
    dp.add_handler(CommandHandler("u1chips", u1chips_command))
    dp.add_handler(CommandHandler("SelectU1chipsPlan", SelectU1chipsPlan_command))
    dp.add_handler(CommandHandler("BEGINNER", BEGINNER_command))
    dp.add_handler(CommandHandler("PRO", PRO_command))
    dp.add_handler(CommandHandler("MASTER", MASTER_command))
    dp.add_handler(CommandHandler("ActivatePlan", ActivatePlan_command))
    dp.add_handler(CommandHandler("History", History_command))
    dp.add_handler(CommandHandler("About", About_command))
    dp.add_handler(CommandHandler("Version", Version_command))
    dp.add_handler(CommandHandler("Update", Update_command))
    dp.add_handler(CommandHandler("CarrierLookup", CarrierLookup_command))
    dp.add_handler(CommandHandler("ActivateSIMCard", ActivateSIMCard_command))
    dp.add_handler(CommandHandler("DeactivateSIMcard", DeactivateSIMcard_command))
    dp.add_handler(CommandHandler("ChangeSIMPin", ChangeSIMPin_command))
    dp.add_handler(CommandHandler("TransferContacts", TransferContacts_command))
    dp.add_handler(CommandHandler("RestoreContacts", RestoreContacts_command))
    dp.add_handler(CommandHandler("SwapMenu", SwapMenu_command))
    dp.add_handler(CommandHandler("Xtra", Xtra_command))
    dp.add_handler(CommandHandler("PaymentMethod1", PaymentMethod1_command))
    dp.add_handler(CommandHandler("BTC1", BTC1_command))
    dp.add_handler(CommandHandler("USDT1", USDT1_command))
    dp.add_handler(CommandHandler("ETH1", ETH1_command))
    dp.add_handler(CommandHandler("XRP1", XRP1_command))
    dp.add_handler(CommandHandler("confirm_name", confirm_name_command))
    dp.add_handler(CommandHandler("confirm_old_number", confirm_old_number_command))
    dp.add_handler(CommandHandler("confirm_new_number", confirm_new_number_command))
    dp.add_handler(CommandHandler("confirm_address", confirm_address_command))

    # "This Bot was created by #Gad Kalu Obioma"





    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()

main()