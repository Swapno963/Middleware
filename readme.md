## Top 10 problems that developers solve using custom middleware:
1. Role-Based Access Control (RBAC)
Problem: Restrict access to certain parts of the application based on user roles.
Solution: Middleware inspects request.user to verify the user’s role and redirects unauthorized users to appropriate pages or denies access.

2. Logging and Monitoring
Problem: Track requests for debugging, performance analysis, or compliance.
Solution: Middleware logs details like request paths, user agents, execution times, or IP addresses for each request.

3. Authentication and Authorization Enforcement
Problem: Ensure certain views or endpoints are accessible only to authenticated users.
Solution: Middleware checks if request.user.is_authenticated and redirects unauthenticated users to the login page.

4. Custom Request or Response Headers
Problem: Add or modify HTTP headers for specific security, caching, or compliance requirements.
Solution: Middleware adds custom headers like X-Content-Type-Options, Strict-Transport-Security, or Access-Control-Allow-Origin.

5. Maintenance Mode
Problem: Temporarily block access to the application during maintenance or updates.
Solution: Middleware intercepts all requests and serves a maintenance page, except for certain IPs or admin users.

6. IP-Based Access Control
Problem: Restrict access to the application based on IP address for security or region-specific policies.
Solution: Middleware checks the request.META['REMOTE_ADDR'] against an allowlist or blocklist of IPs and denies or allows access accordingly.

7. Language and Locale Detection
Problem: Serve content in the user's preferred language.
Solution: Middleware inspects headers like Accept-Language or cookies to detect the user’s locale and sets request.LANGUAGE_CODE.

8. Request Throttling or Rate Limiting
Problem: Prevent abuse by limiting the number of requests a user or IP can make within a specific time frame.
Solution: Middleware tracks requests using cache or database and enforces limits, returning a 429 (Too Many Requests) response if exceeded.

9. URL Redirection or Normalization
Problem: Redirect or normalize URLs for SEO or user experience.
Solution: Middleware ensures all URLs follow a consistent pattern, such as adding a trailing slash or redirecting HTTP to HTTPS.

10. Custom Error Handling
Problem: Serve user-friendly error pages (e.g., 404 or 500) or handle exceptions globally.
Solution: Middleware intercepts errors or unhandled exceptions and serves custom error responses.


## Key Feature
1. The middleware  skips processing for login, logout, and admin paths by explicitly checking request.path.

2. Each role has a predefined home path stored in a dictionary (role_home_paths).

3. The middleware fetches the expected path for the user's role and compares it with the current path.

4. The middleware checks if the current path starts with the expected home path for the role.

5. If the path is already correct, no redirection occurs, breaking the infinite loop.