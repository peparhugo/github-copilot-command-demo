"""
REST API Client Example - GitHub Copilot in PyCharm

This example demonstrates how Copilot can help generate API client code.
The example uses JSONPlaceholder, a free fake API for testing.
"""

import json
from typing import List, Dict, Optional
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


class JSONPlaceholderClient:
    """
    REST API client for JSONPlaceholder.
    
    Demonstrates Copilot's ability to generate:
    - HTTP methods (GET, POST, PUT, DELETE)
    - Error handling
    - Type hints
    - Documentation
    """
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        """Initialize the API client."""
        self.base_url = self.BASE_URL
    
    def _make_request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make HTTP request to the API.
        
        Args:
            endpoint: API endpoint path
            method: HTTP method (GET, POST, PUT, DELETE)
            data: Optional data for POST/PUT requests
            
        Returns:
            Response data as dictionary or None if error
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            headers = {"Content-Type": "application/json"}
            
            if data:
                data_bytes = json.dumps(data).encode('utf-8')
                request = Request(url, data=data_bytes, headers=headers, method=method)
            else:
                request = Request(url, headers=headers, method=method)
            
            with urlopen(request) as response:
                return json.loads(response.read().decode('utf-8'))
                
        except HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            return None
        except URLError as e:
            print(f"URL Error: {e.reason}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None
    
    # Posts endpoints
    def get_posts(self) -> Optional[List[Dict]]:
        """Get all posts from the API."""
        return self._make_request("posts")
    
    def get_post(self, post_id: int) -> Optional[Dict]:
        """
        Get a specific post by ID.
        
        Args:
            post_id: The ID of the post to retrieve
            
        Returns:
            Post data or None if not found
        """
        return self._make_request(f"posts/{post_id}")
    
    def create_post(self, title: str, body: str, user_id: int) -> Optional[Dict]:
        """
        Create a new post.
        
        Args:
            title: Post title
            body: Post content
            user_id: ID of the user creating the post
            
        Returns:
            Created post data or None if failed
        """
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self._make_request("posts", method="POST", data=data)
    
    def update_post(self, post_id: int, title: str, body: str, user_id: int) -> Optional[Dict]:
        """
        Update an existing post.
        
        Args:
            post_id: ID of the post to update
            title: New title
            body: New content
            user_id: User ID
            
        Returns:
            Updated post data or None if failed
        """
        data = {
            "id": post_id,
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self._make_request(f"posts/{post_id}", method="PUT", data=data)
    
    def delete_post(self, post_id: int) -> bool:
        """
        Delete a post by ID.
        
        Args:
            post_id: ID of the post to delete
            
        Returns:
            True if successful, False otherwise
        """
        result = self._make_request(f"posts/{post_id}", method="DELETE")
        return result is not None
    
    # Users endpoints
    def get_users(self) -> Optional[List[Dict]]:
        """Get all users from the API."""
        return self._make_request("users")
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """
        Get a specific user by ID.
        
        Args:
            user_id: The ID of the user to retrieve
            
        Returns:
            User data or None if not found
        """
        return self._make_request(f"users/{user_id}")
    
    def get_user_posts(self, user_id: int) -> Optional[List[Dict]]:
        """
        Get all posts by a specific user.
        
        Args:
            user_id: The ID of the user
            
        Returns:
            List of posts or None if error
        """
        return self._make_request(f"users/{user_id}/posts")
    
    # Comments endpoints
    def get_post_comments(self, post_id: int) -> Optional[List[Dict]]:
        """
        Get all comments for a specific post.
        
        Args:
            post_id: The ID of the post
            
        Returns:
            List of comments or None if error
        """
        return self._make_request(f"posts/{post_id}/comments")
    
    def get_comments(self) -> Optional[List[Dict]]:
        """Get all comments from the API."""
        return self._make_request("comments")


# Example usage and demonstration
def demonstrate_api_client():
    """Demonstrate various API client operations."""
    client = JSONPlaceholderClient()
    
    print("=" * 50)
    print("JSONPlaceholder API Client Demo")
    print("=" * 50)
    
    # Get all posts (limited to first 5 for brevity)
    print("\n1. Getting first 5 posts...")
    posts = client.get_posts()
    if posts:
        for post in posts[:5]:
            print(f"   - Post {post['id']}: {post['title'][:50]}...")
    
    # Get a specific post
    print("\n2. Getting post with ID 1...")
    post = client.get_post(1)
    if post:
        print(f"   Title: {post['title']}")
        print(f"   Body: {post['body'][:100]}...")
    
    # Create a new post
    print("\n3. Creating a new post...")
    new_post = client.create_post(
        title="Test Post from Copilot Demo",
        body="This post was created using the API client generated with GitHub Copilot!",
        user_id=1
    )
    if new_post:
        print(f"   Created post with ID: {new_post.get('id')}")
        print(f"   Title: {new_post.get('title')}")
    
    # Get user information
    print("\n4. Getting user with ID 1...")
    user = client.get_user(1)
    if user:
        print(f"   Name: {user['name']}")
        print(f"   Email: {user['email']}")
        print(f"   Company: {user['company']['name']}")
    
    # Get comments for a post
    print("\n5. Getting comments for post 1...")
    comments = client.get_post_comments(1)
    if comments:
        print(f"   Found {len(comments)} comments")
        print(f"   First comment by: {comments[0]['email']}")
    
    print("\n" + "=" * 50)
    print("Demo completed!")
    print("=" * 50)


if __name__ == "__main__":
    demonstrate_api_client()
