
def list_all_videos(videos):
     pass 

def add_video(videos):
     pass
def update_video(videros):
     pass
def delete_video(videos):
     pass


def main():
     
    videos = []
    while True:
    
        print("\n Youtube Manger |chose an option")
        print("1.list  a all youtube videos")
        print("2.upadate a youtube video details")
        print("3.delete a  youtube video")
        print("4.Exit the app")
        choice = input ("enter your choies")



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
