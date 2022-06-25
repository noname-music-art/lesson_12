import json


def load_posts() -> list[dict]:
    """Load posts from JSON file"""
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    """Search post by keyword"""
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post: dict) -> dict:
    """Add new post to JSON file"""
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
