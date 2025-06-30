from Person import Person
from UDGraph import Graph


class SocialMediaApp:
    def __init__(self):
        self.graph = Graph()
        self.people = []

    def add_profile(self, name, gender='', privacy='public', biography=''):
        if len(self.people) >= 10:
            return None

        person = Person(name, gender, privacy, biography)
        self.graph.add_vertex(person)
        self.people.append(person)
        return person

    def follow(self, follower, following):
        self.graph.add_edge(follower, following)

    def unfollow(self, follower, following):
        self.graph.remove_edge(follower, following)

    def display_all_profiles(self):
        for i, person in enumerate(self.people, 1):
            print(f"{i}. {person.get_name()}")

    def display_profile_details(self, person, show_full_details=False):
        print("\n" + "=" * 55)
        print(f"Name: {person.get_name()}")
        print(f"Privacy: {person.get_privacy().capitalize()}")

        if show_full_details or person.get_privacy() == 'public':
            print(f"Gender: {person.get_gender()}")
            print(f"Biography: {person.get_biography()}")

            # Show followers
            followers = self.graph.get_incoming_adjacent(person)
            print("\nFollowers:")
            if followers:
                for follower in followers:
                    print(f"- {follower.get_name()}")
            else:
                print("No followers")

            # Show following
            following = self.graph.get_outgoing_adjacent(person)
            print("\nFollowing:")
            if following:
                for follower in following:
                    print(f"- {follower.get_name()}")
            else:
                print("Not following anyone")

    def display_followers(self, person):
        followers = self.graph.get_incoming_adjacent(person)
        print(f"\n{person} Follower List:")
        if followers:
            for follower in followers:
                print(f"- {follower.get_name()}")
        else:
            print("No followers")

    def display_following(self, person):
        following = self.graph.get_outgoing_adjacent(person)
        print(f"\n{person} Following List:")
        if following:
            for follower in following:
                print(f"- {follower.get_name()}")
        else:
            print("Not following anyone")

    def edit_profile_menu(self, person):
        while True:
            self.display_profile_details(person, show_full_details=True)

            print("\n" + "=" * 55)
            print("Edit Options:")
            print("1. Edit name")
            print("2. Edit gender")
            print("3. Edit biography")
            print("4. Edit privacy")
            print("5. Remove follower")
            print("6. Remove following")
            print("7. Follow someone")
            print("8. Back to main menu")

            print("*" * 55)
            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                new_name = input("\nEnter new name: ")
                person.set_name(new_name)
                print("Name updated successfully!")
            elif choice == '2':
                new_gender = input("\nEnter new gender (f/m): ").lower()
                while new_gender not in ['f', 'm']:
                    print("Invalid gender. Please enter 'f' for female or 'm' for male.")
                    new_gender = input("Enter new gender (f/m): ").lower()

                gender = 'Female' if new_gender == 'f' else 'Male'
                person.set_gender(gender)
                print("Gender updated successfully!")
                    # new_gender = input("Enter new gender (f/m): ").lower()
                    # if new_gender in ['f', 'm']:
                    #     gender = 'Female' if new_gender == 'f' else 'Male'
                    #     person.set_gender(gender)
                    #     print("Gender updated successfully!")
                    #     break
                    # print("Invalid gender. Please enter 'f' for female or 'm' for male.")
            elif choice == '3':
                new_biography = input("\nEnter new biography: ")
                person.set_biography(new_biography)
                print("Biography updated successfully!")
            elif choice == '4':
                new_privacy = input("\nEnter privacy (public/private): ").lower()
                while new_privacy not in ['public', 'private']:
                    print("Invalid privacy setting. Please enter 'public' or 'private'.")
                    new_privacy = input("\nEnter privacy (public/private): ").lower()
                person.set_privacy(new_privacy)
                print("Privacy updated successfully!")
            elif choice == '5':
                followers = self.graph.get_incoming_adjacent(person)
                if followers:
                    print("\nSelect follower to remove:")
                    for i, follower in enumerate(followers, 1):
                        print(f"{i}. {follower.get_name()}")
                    try:
                        selection = int(input("\nEnter choice (0 to cancel): "))
                        if 1 <= selection <= len(followers):
                            self.unfollow(followers[selection - 1], person)
                            print("Follower removed successfully!")
                        elif selection == 0:
                            print("Operation cancelled.")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number")
                else:
                    print("No followers to remove")
            elif choice == '6':
                following = self.graph.get_outgoing_adjacent(person)
                if following:
                    print("\nSelect following to remove:")
                    for i, follower in enumerate(following, 1):
                        print(f"{i}. {follower.get_name()}")
                    try:
                        selection = int(input("\nEnter choice (0 to cancel): "))
                        if 1 <= selection <= len(following):
                            self.unfollow(person, following[selection - 1])
                            print("Following removed successfully!")
                        elif selection == 0:
                            print("Operation cancelled.")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number")
                else:
                    print("Not following anyone")
            elif choice == '7':
                available_to_follow = [p for p in self.people if
                                       p != person and p not in self.graph.get_outgoing_adjacent(person)]
                if available_to_follow:
                    print("\nAvailable to follow:")
                    for i, p in enumerate(available_to_follow, 1):
                        print(f"{i}. {p.get_name()}")
                    try:
                        selection = int(input("\nEnter choice (0 to cancel): "))
                        if 1 <= selection <= len(available_to_follow):
                            self.follow(person, available_to_follow[selection - 1])
                            print("Followed successfully!")
                        elif selection == 0:
                            print("Operation cancelled.")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number")
                else:
                    print("No one available to follow")
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    app = SocialMediaApp()

    # Create sample profiles
    karen = app.add_profile("Karen", "Female", "public", "Just a normal person")
    susy = app.add_profile("Susy", "Female", "public", "Loves cats")
    brian = app.add_profile("Brian", "Male", "private", "Software developer")
    calvin = app.add_profile("Calvin", "Male", "public", "Photography enthusiast")
    elon = app.add_profile("Elon", "Male", "private", "Tech entrepreneur")

    # Create follow relationships
    app.follow(karen, susy)
    app.follow(karen, brian)
    app.follow(karen, elon)
    app.follow(elon, karen)
    app.follow(elon, calvin)
    app.follow(brian, karen)

    print("*" * 55)
    print("\n\t\tWelcome to Your New Social Media App:")

    while True:
        print("\n" + "*" * 55)
        print("1. View all profile names")
        print("2. View details for any profile")
        print("3. View followers for any profile")
        print("4. View followed accounts for any profile")
        if len(app.people) < 10:
            print("5. Add new user")
        print("6. Edit user profile")
        print("7. Exit")
        print("" + "*" * 55)

        try:
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                while True:
                    print("\n" + "=" * 55)
                    print(f"{'View All Profile Names:':^55}")
                    print("=" * 55)
                    app.display_all_profiles()
                    try:
                        selection = input(
                            "\nSelect user to view details (1-{}) or 'b' to go back: ".format(len(app.people)))
                        if selection.lower() == 'b':
                            break
                        selection = int(selection)
                        if 1 <= selection <= len(app.people):
                            app.display_profile_details(app.people[selection - 1], show_full_details=True)
                            input("\nPress Enter to continue...")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number or 'b' to go back")

            elif choice == '2':
                while True:
                    print("\n" + "=" * 55)
                    print(f"{'View Details for Any Profile:':^55}")
                    print("=" * 55)
                    app.display_all_profiles()
                    try:
                        selection = input(
                            "\nSelect whose profile to view (1-{}) or 'b' to go back: ".format(len(app.people)))
                        if selection.lower() == 'b':
                            break
                        selection = int(selection)
                        if 1 <= selection <= len(app.people):
                            app.display_profile_details(app.people[selection - 1])
                            input("\nPress Enter to continue...")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number or 'b' to go back")

            elif choice == '3':
                while True:
                    print("\n" + "=" * 55)
                    print(f"{'View Followers for Any Profile:':^55}")
                    print("=" * 55)
                    app.display_all_profiles()
                    try:
                        selection = input(
                            "\nSelect whose profile to view followers (1-{}) or 'b' to go back: ".format(len(app.people)))
                        if selection.lower() == 'b':
                            break
                        selection = int(selection)
                        if 1 <= selection <= len(app.people):
                            app.display_followers(app.people[selection - 1])
                            input("\nPress Enter to continue...")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number or 'b' to go back")

            elif choice == '4':
                while True:
                    print("\n" + "=" * 55)
                    print(f"{'View Followed Accounts for Any Profile:':^55}")
                    print("=" * 55)
                    app.display_all_profiles()
                    try:
                        selection = input(
                            "\nSelect whose profile to view following (1-{}) or 'b' to go back: ".format(len(app.people)))
                        if selection.lower() == 'b':
                            break
                        selection = int(selection)
                        if 1 <= selection <= len(app.people):
                            app.display_following(app.people[selection - 1])
                            input("\nPress Enter to continue...")
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number or 'b' to go back")

            elif choice == '5' and len(app.people) < 10:
                print("\n" + "=" * 55)
                print(f"{'Add New User:':^55}")
                print("=" * 55)
                name = input("Enter name: ")

                while True:
                    gender_input = input("Enter gender (f/m): ").lower()
                    if gender_input == 'f':
                        gender = "Female"
                        break
                    elif gender_input == 'm':
                        gender = "Male"
                        break
                    else:
                        print("Invalid input. Please enter 'f' for female or 'm' for male.")

                privacy = input("Enter privacy (public/private): ").lower()
                while privacy not in ['public', 'private']:
                    print("Invalid privacy setting. Please enter 'public' or 'private'.")
                    privacy = input("Enter privacy (public/private): ").lower()

                biography = input("Enter biography: ")
                person = app.add_profile(name, gender, privacy, biography)

                if person:
                    print(f"\nProfile for {name} created successfully!")
                else:
                    print("\nCannot add more users (maximum limit reached)")
                input("\nPress Enter to continue...")

            elif choice == '6':
                while True:
                    print("\n" + "=" * 55)
                    print(f"{'Edit Any Profile:':^55}")
                    print("=" * 55)
                    app.display_all_profiles()
                    try:
                        selection = input("\nSelect user to edit (1-{}) or 'b' to go back: ".format(len(app.people)))
                        if selection.lower() == 'b':
                            break
                        selection = int(selection)
                        if 1 <= selection <= len(app.people):
                            app.edit_profile_menu(app.people[selection - 1])
                        else:
                            print(f"Invalid selection! Please enter a number between 1 and {len(app.people)}")
                    except ValueError:
                        print("Please enter a valid number or 'b' to go back")

            elif choice == '7':
                break

            else:
                # Determine valid range for the error message
                valid_range = "1-5,7" if len(app.people) >= 10 else "1-7"
                print(f"Invalid choice! Please enter a number between {valid_range}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
