class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True

    groups = group.get_groups()
    for sub_group in groups:
        if is_user_in_group(user, sub_group):
            return True
    return False

# test case 1 - user is in the group
parent1 = Group("parent1")
child1 = Group("child1")
sub_child1 = Group("subchild1")
sub_child2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child1.add_user(sub_child_user)

child1.add_group(sub_child1)
child1.add_group(sub_child2)
parent1.add_group(child1)

print(is_user_in_group(sub_child_user, parent1))
print(is_user_in_group(sub_child_user, child1))
print(is_user_in_group(sub_child_user, sub_child1))
print(is_user_in_group(sub_child_user, sub_child2))
print("")

# test case 2 - user is not in the group
parent2 = Group("parent2")
child2 = Group("child2")
sub_child3 = Group("subchild3")

child2.add_group(sub_child3)
parent2.add_group(child2)
print(is_user_in_group(sub_child_user, parent2))
print(is_user_in_group(sub_child_user, child2))
print(is_user_in_group(sub_child_user, sub_child3))
print("")

# test case 3 - empty group
parent3 = Group("parent3")
print(is_user_in_group(sub_child_user, parent3))
