#!/usr/bin/python3
from models import storage
from models.user import User
from models.create_post import Post


def create_post_for_user(user_id, platform, message, schedule_time):
    # Check if the user exists
    all_users = storage.all(User)
    """print("Existing User IDs:")"""
    """for user in all_users.values():
        print(user.id)"""

    # Convert user_id to string and add 'User.' prefix for comparison
    user_id_str = "User." + str(user_id)
    # print("User ID Type:", type(user_id_str))
    # print("All Users:", all_users)
    # Check if the user ID exists in the stored users
    if user_id_str in all_users:
        user = all_users[user_id_str]

        # Create a new post for the user
        new_post = Post()
        new_post.user_id = user_id_str
        new_post.platform = platform
        new_post.message = message
        new_post.schedule_time = schedule_time
        new_post.save()
        print(f"Post created for user {user_id_str} on platform {platform}")
    else:
        print(f"Invalid user ID: {user_id_str}")

if __name__ == "__main__":
    # Get all existing user IDs from storage
    all_users = storage.all(User)
    existing_user_ids = [user.id for user in all_users.values()]

    # Define posts for each user
    user_posts = {
        "facebook": "Sample post for Facebook",
        "twitter": "Sample post for Twitter",
        "linkedin": "Sample post for LinkedIn"
    }

    # If there are existing users, create posts for them
    if existing_user_ids:
        for user_id in existing_user_ids:
            for platform, post_content in user_posts.items():
                create_post_for_user(user_id, platform, post_content, "2024-03-25T12:00:00")
    else:
        print("No existing users found.")
