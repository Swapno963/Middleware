## Key Feature
1. The middleware  skips processing for login, logout, and admin paths by explicitly checking request.path.

2. Each role has a predefined home path stored in a dictionary (role_home_paths).

3. The middleware fetches the expected path for the user's role and compares it with the current path.

4. The middleware checks if the current path starts with the expected home path for the role.

5. If the path is already correct, no redirection occurs, breaking the infinite loop.