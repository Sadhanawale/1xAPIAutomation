#add your constant here

class APIConstant(object):
   @staticmethod
   def base_url(self):
       return "https://restful-booker.herokuapp.com"
   @staticmethod
   def url_create_booking(self):
       return "https://restful-booker.herokuapp.com/booking"
   @staticmethod
   def  url_create_token():
       return"https://restful-booker.herokuapp.com/auth"


# update,put,patch,delete- booking id
   def url_patch_put_delete_booking(booking_id):
    return"https://restful-booker.herokuapp.com/booking/"+str(booking_id)
