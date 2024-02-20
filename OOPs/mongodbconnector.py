import pymongo

client = pymongo.MongoClient('mongodb+srv://youtubepy:youtubepy@cluster0.vqafvne.mongodb.net/?retryWrites=true&w=majority')
db = client["ytmanager"]
collection = db["videos"]
print(collection)


def insert():
    title = input("Enter title: ")
    link = input("Enter link: ")
    collection.insert_one({"title": title, "link": link})
    print("Video inserted successfully")

def read():
    for video in collection.find():
        print(video)

def update():
    title = input("Enter title: ")
    link = input("Enter link: ")
    collection.update_one({"title": title}, {"$set": {"link": link}})
    print("Video updated successfully")

def delete():
    title = input("Enter title: ")
    collection.delete_one({"title": title})
    print("Video deleted successfully")


def main():
    while True:
        print("Youtube Video Manager")
        print("1. Insert")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            insert()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()