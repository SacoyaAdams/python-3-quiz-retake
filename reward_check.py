
def find_best_user(file_path):
    # pass #TODO
    string = ""
    with open(file_path, 'r') as file:
        next(file) # skip the 1st row
        for line in file:
            info = line.strip().split(', ')
            # if user have the highest points print their name 
            if string == 21:
                print(string)

            


def test():
    result = find_best_user("users.txt")
    print(result)

test()