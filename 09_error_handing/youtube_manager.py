import json




def load_data():
     try:
          with open("youtube.txt",'r')as file:
                test= json.load(file)
                 #print(type(test))
                return test
     except FileNotFoundError:
          return []

def save_data_heler(videos):
     with open("youtube.txt",'w')as file:
          json.dump(videos,file)
         


def list_all_videos(videos):
    print("\n")
    print("*" *70)
    for index, video in enumerate (videos,start=1):
        print(f"{index}. {video['name']}, Duration:{video['time']} ")
      
    print("\n")
    print("*" *70)
    
def add_video(videos):
      name=input("Enter vedio name:"  )
      time=input("Enter vedio time:")
      videos.append({'name':name, 'time':time})
      save_data_heler(videos)
    
def update_video(videos) :
     list_all_videos(videos)
     index= int(input(" Enter the video number to update"))
     if 1<= index <= len(videos):
        name=input("Enter  the new vedio name:"  )
        time=input("Enter  the new vedio time:")
        videos[index-1]({'name':name, 'time':time})
        save_data_heler(videos)

     else:
          print("Invalid index slected")
def delete_video(videos):
     list_all_videos(videos)
     index = int(input("Enter the video number to be deleted"))

     if 1<= index <= len(videos):
          del videos[index-1]
          save_data_heler(videos)
     else:
          print("Invalid video index selected")




def main():
     
    videos = []
    while True:
    
        print("\n Youtube Manger |chose an option")
        print("1.List  a all youtube videos")
        print("2.Add youtube videos")
        print("3.Upadate a youtube video details")
        print("4.Delete a  youtube video")
        print("5.Exit the app")
        choice = input ("Enter your choies: ")
         #print(videos)


        match choice:
                case '1':
                    list_all_videos(videos)
                case '2':
                    add_video(videos)  
                case '3':
                    update_video(videos)
                case '4':
                    delete_video(videos)
                case '5':
                    break
                case _:
                    print("invalid choice, please try again")
             
    
if __name__ == "__main__":
     main()
