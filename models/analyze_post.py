#!/usr/bin/python3
"""
Analytic Data
"""
from models.socialmedia_post import SocialMediaPost


def analyze_posts_for_user(user_id, platform=None):
    """
    Analyze posts for a given user.
    Args:
        user_id (str): The ID of the user whose posts to analyze.
    Returns:
        dict: A dictionary containing analysis results.
    """
    # Retrieve posts for the given user on a particular platform
    user_posts = get_user_posts(user_id, platform)
    print("Retrieved posts:", user_posts)
    # Count the occurrences of the 'message' attribute as total_posts
    total_posts = count_attribute_occurrences(user_posts, 'message')
    print("Total posts count:", total_posts)
    # Perform analysis on the retrieved posts
    analysis_results = {
        'total_posts': total_posts,
        'total_likes': sum(post.likes for post in user_posts),
        'total_comments': sum(post.comments for post in user_posts),
        'total_views': sum(post.views for post in user_posts)
        # Add more analysis metrics when needed
    }

    return analysis_results

def count_attribute_occurrences(posts, attribute):
    """
    Count the occurrences of a specific attribute in a list of posts.
    Args:
        posts (list): A list of SocialMediaPost objects.
        attribute (str): The attribute to count occurrences of.
    Returns:
        int: The total number of occurrences of the attribute.
    """
    count = 0
    for post in posts:
        if hasattr(post, attribute) and getattr(post, attribute):
            count += 1
    return count

def get_user_posts(user_id, platform=None):
    """
    Retrieve posts for a given user.
    Args:
        user_id (str): The ID of the user whose posts to retrieve.
    Returns:
        list: A list of SocialMediaPost objects belonging to the user.
    """
    from models import storage
    user_posts = []
    print("All posts in the system:", storage.all(SocialMediaPost).values())
    print("Retrieving posts for user:", user_id)
    for post in storage.all(SocialMediaPost).values():
        print("Post user ID:", post.user_id)
        # Strip the 'User.' prefix from post.user_id for comparison
        post_user_id = post.user_id.split('.')[-1]
        if post.user_id == user_id and (platform is None or post.platform == platform):
            user_posts.append(post)
    print("Retrieved posts:", user_posts)
    return user_posts
