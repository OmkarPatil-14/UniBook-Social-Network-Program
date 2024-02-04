class Main:
    # global variable for storing the file name
    global file_name
    file_name = input("Enter a file name for the network :")
    def create_SocialNetwork(self):
        global file_name
        with open(file_name) as input_file:
            global social_NW
            social_NW = {}
            # read each line of the file and add connections to the social network
            for line in input_file:
                if " " not in line:
                    social_member_count = line
                else:
                    main_friend, friend1 = line.split()
                    if line.split() == 0:
                        pass
                    if main_friend in social_NW:
                        social_NW[main_friend].append(friend1)
                    if main_friend not in social_NW:
                        social_NW[main_friend] = [friend1]
                    if friend1 in social_NW:
                        social_NW[friend1].append(main_friend)
                    if friend1 not in social_NW:
                        social_NW[friend1] = [main_friend]


    def display_SocialNetwork(self):
        global social_NW
        print("##########################################")
        print("The Social Network for given file is :")
        # print each member and their connections
        for key, val in social_NW.items():
            print(f"{key} -> {val}")

    def display_CommonFriends(self):
        global social_NW
        common_friends = {}
        for main_friend, common_friend in social_NW.items():
            friends_lists = [[] for _ in range(len(common_friend))]
            for key, val in social_NW.items():
                for i, friend in enumerate(common_friend):
                    if friend in val:
                        friends_lists[i].append(1)
                    else:
                        friends_lists[i].append(0)
            common_friends[main_friend] = [sum(l) for l in zip(*friends_lists)]
        print("##########################################")
        print("The common friends in the social network are :")
        for key, value in common_friends.items():
            print(f"{key} -> {value}")

    def recommendFriend(self):
        global social_NW
        keys = list(social_NW.keys())
        print(f"Enter a name from {keys}")
        main_friend = (input("Enter Member Name to recommend friend for:"))
        main_direct_friends = social_NW[main_friend]
        for f in main_direct_friends:
            if f not in social_NW:
                pass
            else:
                indirect_friends = social_NW[f]
                indirect_friends.remove(main_friend)  # removes the person itself
                friends = (social_NW[main_friend])
                z = [item for item in indirect_friends if item not in friends]
                if len(z) != 0:
                    print(f"The Recommended friend for {main_friend} are {z}")
                    break
                elif len(z) == 0:
                    print(f"{main_friend} has no friend recommendation")

class feature3():
    def display_numFriends(self):
        global social_NW
        keys = list(social_NW.keys())
        print(f"Enter a name from {keys}")
        key = input("Enter the Member name :")
        numoffriend = (len((social_NW[key])))
        if numoffriend == 1:
            print(f">>> {key} has {numoffriend} friend")
        else:
            print(f">>> {key} has {numoffriend} friends")

    def mostFriends(self):
        # Display the member with the most number of friends
        global social_NW
        friend_count_dict = {}
        for key, value in social_NW.items():
            f_count = len([item for item in value if item])
            friend_count_dict[key] = f_count
        max_value = max(friend_count_dict, key=friend_count_dict.get)
        print(f">>> {max_value} has the most number of friends")

    def leastFriends(self):
        # Display the member(s) with the least number of friends
        global social_NW
        friend_count_dict = {}
        for key, value in social_NW.items():
            f_count = len([item for item in value if item])
            friend_count_dict[key] = f_count
        min_value = min(friend_count_dict.values())
        key_w_min = [key for key in friend_count_dict if friend_count_dict[key] == min_value]
        print(">>> The members with least friends are " + str(key_w_min))

    def showRelation(self):
        global social_NW
        keys = list(social_NW.keys())
        print(f"Enter a name from {keys}")
        key_input = input("Enter the Member name :")
        friends = social_NW[key_input]
        print(f">>> {key_input} is friends with {friends}")

    def showIndirectRelationship(self):
        global social_NW
        # Get the list of all members in the social network
        keys = list(social_NW.keys())
        print(f"Enter a name from {keys}")
        main_friend = (input("Enter Member Name :"))
        main_direct_friends = social_NW[main_friend]
        indirect_list = []
        for f in main_direct_friends:
            if f not in social_NW:
                pass
            else:
                indirect_friends = social_NW[f]
                indirect_friends.remove(main_friend)
                indirect_list.append(indirect_friends)
        name_list = []
        for i in indirect_list:
            for name in i:
                if name in name_list:
                    pass
                else:
                    name_list.append(name)

        main_direct_friends = social_NW[main_friend]
        for n in main_direct_friends:
            if n in name_list:
                name_list.remove(n)
        print(f">>> The Indirect relationships for {main_friend} are {name_list}")

    def validateNetwork(self):
        global social_NW
        num_of_connections = len(social_NW)
        inconsistent_count = 0
        consistent_count = 0
        for key, val in social_NW.items():
            main_direct_friends = social_NW[key]
            for f in main_direct_friends:
                if f not in social_NW:
                    pass
                else:
                    indirect_friends = social_NW[f]
                    if f not in indirect_friends:
                        inconsistent_count = inconsistent_count + 1

                    else:
                        consistent_count = consistent_count + 1

        if inconsistent_count > consistent_count:
            print("The network is inconsistent")
        elif inconsistent_count < consistent_count:
            print("The network is consistent")
        else:
            print("The network is consistent")


    def f3main(self):
        global social_NW
        while True:
            bar = ("===============================================================")
            space = ("                                                             ")
            print(bar)
            print("Network Statistics:")
            print("1. Display how many friends a given member has")
            print("2. Show the member with the most number of friends")
            print("3. Show the members with the least number of friends")
            print("4. Show the relationships for a given member")
            print("5. Show the indirect relationships for a given member")
            print("6. Validate the network to check if it is consistent")
            print(space)
            user_input = input("Enter your option :")

            if user_input == "1":
                f.display_numFriends()
            if user_input == "2":
                f.mostFriends()
            if user_input == "3":
                f.leastFriends()
            if user_input == "4":
                f.showRelation()
            if user_input == "5":
                f.showIndirectRelationship()
            if user_input == "6":
                f.validateNetwork()





s = Main()
f = feature3()
s.create_SocialNetwork()

while True:
    print("##########################################")
    print("Choose an option to continue:")
    print("1. Display the Social Network")
    print("2. Display the Common friends")
    print("3. Recommend a friend")
    print("4. Check Social Network Stats")
    user_input = input("Enter an option :")


    if user_input == "1":
        s.display_SocialNetwork()
    if user_input == "2":
        s.display_CommonFriends()
    if user_input == "3":
        s.recommendFriend()
    if user_input == "4":
        break

f.f3main()

