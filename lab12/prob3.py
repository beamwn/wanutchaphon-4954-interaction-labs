import re

def split_my_info(my_info):
    name =re.split(":", my_info)
    ID =re.split("My ID", name[1])
    findall = re.findall("\d+",ID[1])
    print("My name is",ID[0])
    print("My ID is",findall[0])
    


if __name__ == "__main__":
    my_info = "My name:Wanutchaphon Haema My ID is 6530404954"
    split_my_info(my_info)