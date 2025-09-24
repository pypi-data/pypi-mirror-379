# Pararamio AIO

Async Python API client for [pararam.io](https://pararam.io) platform.

## Features

- ⚡ **Async/Await**: Modern asynchronous interface with aiohttp
- 🚀 **Explicit Loading**: Predictable API calls with explicit `load()` methods
- 🍪 **Cookie Persistence**: Automatic session management
- 🔐 **Two-Factor Authentication**: Built-in 2FA support
- 🐍 **Type Hints**: Full typing support for better IDE experience

## Installation

```bash
pip install pararamio-aio
```

## Quick Start

```python
import asyncio
from pararamio_aio import PararamioAIO, User, Chat, Post
from pararamio_aio import AsyncFileCookieManager

async def main():
    # Initialize cookie manager for persistent authentication
    cookie_manager = AsyncFileCookieManager("session.cookie")

    # Initialize client
    async with PararamioAIO(
        login="your_login",
        password="your_password",
        key="your_2fa_key",
        cookie_manager=cookie_manager
    ) as client:
        # Authenticate
        await client.authenticate()

        # Search for users - returns User objects (clean names!)
        users = await client.search_users("John")
        for user in users:
            print(f"{user.name}")

        # Get chat messages - returns Chat and Post objects
        chat = await client.get_chat_by_id(12345)
        posts = await chat.get_posts(limit=10)
        for post in posts:
            await post.load()  # Explicit loading
            print(f"{post.author.name}: {post.text}")

asyncio.run(main())
```

## Explicit Loading

Unlike the sync version, pararamio-aio uses explicit loading for predictable async behavior:

```python
# Get user object
user = await client.get_user_by_id(123)
print(user.name)  # Basic data is already loaded

# Load full profile data explicitly
await user.load()
print(user.bio)  # Now additional data is available

# Load specific relations
posts = await user.get_posts()
for post in posts:
    await post.load()  # Load each post's content
```

## Cookie Management

The async client supports multiple cookie storage options:

### Default (In-Memory)
```python
# By default, uses AsyncInMemoryCookieManager (no persistence)
async with PararamioAIO(
    login="user",
    password="pass",
    key="key"
) as client:
    await client.authenticate()
    # Cookies are stored in memory only during the session
```

### File-based Persistence
```python
from pararamio_aio import AsyncFileCookieManager

# Create a cookie manager for persistent storage
cookie_manager = AsyncFileCookieManager("session.cookie")

# First run - authenticates with credentials
async with PararamioAIO(
    login="user",
    password="pass",
    key="key",
    cookie_manager=cookie_manager
) as client:
    await client.authenticate()

# Later runs - uses saved cookie
cookie_manager2 = AsyncFileCookieManager("session.cookie")
async with PararamioAIO(cookie_manager=cookie_manager2) as client:
    # Already authenticated!
    profile = await client.get_profile()
```

## Concurrent Operations

Take advantage of async for concurrent operations:

```python
async def get_multiple_users(client, user_ids):
    # Fetch all users concurrently
    tasks = [client.get_user_by_id(uid) for uid in user_ids]
    users = await asyncio.gather(*tasks)

    # Load all profiles concurrently
    await asyncio.gather(*[user.load() for user in users])

    return users
```

## API Reference

### Client Methods

All methods are async and must be awaited:

- `authenticate()` - Authenticate with the API
- `search_users(query)` - Search for users
- `get_user_by_id(user_id)` - Get user by ID
- `get_users_by_ids(ids)` - Get multiple users
- `get_chat_by_id(chat_id)` - Get chat by ID
- `search_groups(query)` - Search for groups
- `create_chat(title, description)` - Create new chat

### Model Objects

All models have async methods:

- `User` - User profile
  - `load()` - Load full profile
  - `get_posts()` - Get user's posts
  - `get_groups()` - Get user's groups

- `Chat` - Chat/conversation
  - `load()` - Load chat details
  - `get_posts(limit, offset)` - Get messages
  - `send_message(text)` - Send message

- `Post` - Message/post
  - `load()` - Load post content
  - `delete()` - Delete post

- `Group` - Community group
  - `load()` - Load group details
  - `get_members()` - Get member list

## Error Handling

```python
from pararamio_aio import (
    PararamioAuthenticationException,
    PararamioHTTPRequestException
)

async with PararamioAIO(**credentials) as client:
    try:
        await client.authenticate()
    except PararamioAuthenticationException as e:
        print(f"Authentication failed: {e}")
    except PararamioHTTPRequestException as e:
        print(f"HTTP error {e.code}: {e.message}")
```

## Advanced Usage

### Custom Session

```python
import aiohttp

# Create custom session with specific timeout
timeout = aiohttp.ClientTimeout(total=60)
connector = aiohttp.TCPConnector(limit=100)
session = aiohttp.ClientSession(timeout=timeout, connector=connector)

async with PararamioAIO(session=session, **credentials) as client:
    # Client will use your custom session
    await client.authenticate()
```

### Rate Limiting

The client automatically handles rate limiting:

```python
client = PararamioAIO(
    wait_auth_limit=True,  # Wait instead of failing on rate limit
    **credentials
)
```

## Migration from Sync Version

If you're migrating from the synchronous `pararamio` package:

1. Add `async`/`await` keywords
2. Use async context manager (`async with`)
3. Call `load()` explicitly when needed
4. Use `asyncio.gather()` for concurrent operations

Example migration:

```python
# Sync version
client = Pararamio(**creds)
user = client.get_user_by_id(123)
print(user.bio)  # Lazy loaded

# Async version
async with PararamioAIO(**creds) as client:
    user = await client.get_user_by_id(123)
    await user.load()  # Explicit load
    print(user.bio)
```

## License

MIT License - see LICENSE file for details.
