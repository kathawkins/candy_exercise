'''
DIRECTIONS
==========

1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

2. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the candy_name parameter.

4. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. Starting with nominal cases, write tests for each of the functions below then 
write tests to handle edge cases.
'''


friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

#1
def get_friends_favorite_candy_count(favorites):
    candy_count = {}
    for friend in favorites:
        # friend = ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
        faves = friend[1]
        for candy in faves:
            if not candy in candy_count:
                candy_count[candy] = 1
            else:
                candy_count[candy]+=1
    # print(candy_count)
    return candy_count

# get_friends_favorite_candy_count(friend_favorites)

#2
def create_new_candy_data_structure(data):
    friend_likes = {}
    for friend in data:
        name = friend[0]
        faves = friend[1]
        for candy in faves:
            if candy not in friend_likes:
                friend_likes[candy]=[name]
            else:
                friend_likes[candy].append(name)
    return friend_likes

# candy_data=create_new_candy_data_structure(friend_favorites)
# print("candy data",candy_data)

#3
def get_friends_who_like_specific_candy(data, candy_name):
    friend_likes_dict=create_new_candy_data_structure(data)
    for candy,names in friend_likes_dict.items():
        if candy == candy_name:
            tuple_of_friends=tuple(names)
    # print(tuple_of_friends)
    return tuple_of_friends

get_friends_who_like_specific_candy(friend_favorites,"lollipop")

#4
def create_candy_set(data):
    friend_likes_dict=create_new_candy_data_structure(data)
    set_of_candies=set()
    for candy in friend_likes_dict.keys():
        set_of_candies.add(candy)
    # print(set_of_candies)
    return set_of_candies

# create_candy_set(friend_favorites)
