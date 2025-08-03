import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            result = json.load(file)
            # result type is list
            return result
    except FileNotFoundError:
        return []

load_data()        

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)        

        # using with open() syntax help us to automatically close the file

def list_all_videos(videos):
    print("\n")
    print("*" * 40)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 40)    

def add_video(videos):
    title = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({'title': title, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be update: "))

    if 1 <= index <= len(videos):
        title = input("Enter the new video title: ")
        time = input("Enter the new video length: ")
        videos[index-1] = {'title': title, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()
    while True:
        print("\n YOUTUBE VIDEOS MANAGER | Select your choice ")
        print("1. List all the videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

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
                print("Invalid Choice!!")
            
if __name__ == "__main__":
    main()            