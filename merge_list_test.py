
def merge_posts(list_of_posts: list):
    org_list = []

    for ls in list_of_posts:
        org_list += [*ls]

    return org_list


custom = [[1, 2, 3, 4, 5, 6, 7], [
    4, 5, 6, 7, 8, 8, 9], [5, 6, 5, 4, 5, 5, 5, ]]

print(merge_posts(custom))
