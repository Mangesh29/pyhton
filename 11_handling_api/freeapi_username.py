import requests

def fectch_random_user_freeapi():
    url="https://freeapi.hashnode.space/api-guide/apireference/getARandomUser"

    response= requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
         user_data=data["data"]
         username=user_data["login"]["uername"]
         country = user_data["location"]["countey"]
         return username, country
    else:
         raise Exception("Failed to fectch  user data ")
    

def main():
     
      try:
          username,country= fectch_random_user_freeapi()
          print(f"Username: {username} \nCountry:{country}")
      except Exception as e:
           print(str(e))
           
           

if __name__=="__main__":
     main()
