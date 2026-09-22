# 07 · Spring Security and JWT 🟠
**Time needed: 45 minutes**

Your resume lists Spring Security with role-based access control, and JWT in your
microservices project. Expect a few questions, especially in a banking context.

---

## First, the context: authentication vs authorisation

- **Authentication** — *who are you?* Checking credentials.
- **Authorisation** — *what are you allowed to do?* Checking permissions.

You authenticate once; you authorise on every request. In your Business Card system,
authentication proved the user was a bank employee; authorisation decided whether that
employee was a **requester**, an **approver** or an **admin**.

---

## Q1. How does Spring Security work?
It sits in front of your application as a **chain of servlet filters**. Every request
passes through the chain before reaching a controller.

```
Request → [ filters: authenticate, authorise, CSRF, CORS ] → DispatcherServlet → Controller
```

The key filter for a token-based API is one that reads the token, validates it, and
places an `Authentication` object into the `SecurityContext`. Everything downstream then
knows who the caller is.

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    SecurityFilterChain chain(HttpSecurity http) throws Exception {
        http
          .csrf(csrf -> csrf.disable())                       // stateless API - see Q5
          .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
          .authorizeHttpRequests(auth -> auth
              .requestMatchers("/api/auth/**").permitAll()
              .requestMatchers("/api/cards/approve/**").hasRole("APPROVER")
              .requestMatchers("/api/admin/**").hasRole("ADMIN")
              .anyRequest().authenticated())
          .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }
}
```


**Say this.**
> "Spring Security is a chain of servlet filters that runs before the request reaches a
> controller. For a token-based API the key filter reads the `Authorization` header,
> validates the token, and puts an `Authentication` object into the `SecurityContext` —
> after which everything downstream knows who the caller is and what roles they hold.
>
> The important point is that it runs **before** my code, so an unauthenticated request
> never reaches business logic at all. I do not have to remember to check in each method."

## Q2. 🔴 Role-based access control — your story
Two ways to enforce it. Know both.

**At the URL level**, as above with `hasRole(...)`.

**At the method level**, which is more precise:
```java
@PreAuthorize("hasRole('APPROVER')")
public CardDto approve(Long id) { ... }

@PreAuthorize("hasRole('ADMIN') or #userId == authentication.principal.id")
public UserDto getUser(Long userId) { ... }     // admins, or the user themselves
```
Requires `@EnableMethodSecurity`.

**Your version:**
> "In the Business Card system there were three roles — requester, approver and admin —
> and the rule that mattered was that a requester must never be able to approve. I
> enforced it at the API layer with Spring Security rather than in the UI, because a UI
> check only hides the button. Anyone can call the endpoint directly with a REST client,
> so the authorisation has to be server side."

That last sentence is the point. In a banking interview it lands well.

⚠️ **`hasRole` vs `hasAuthority`:** `hasRole("ADMIN")` looks for the authority
`ROLE_ADMIN` — Spring adds the prefix for you. `hasAuthority("ROLE_ADMIN")` is the
literal form. Mismatched prefixes are a very common bug.

## Q3. 🔴 JWT — how it works

A JWT is three base64 sections separated by dots:

```
header.payload.signature

header    { "alg": "HS256", "typ": "JWT" }
payload   { "sub": "neelima", "roles": ["APPROVER"], "exp": 1735689600 }
signature HMACSHA256(base64(header) + "." + base64(payload), secret)
```

### The flow
```
1. POST /login with credentials
2. Server verifies, signs a JWT, returns it
3. Client sends it on every request:  Authorization: Bearer <token>
4. Server verifies the SIGNATURE and expiry - no database lookup needed
5. Request proceeds with the user's identity and roles
```

### 🔴 Why use a JWT instead of a session?
> "A session means the server stores state and every request looks it up, which is fine
> for one server but awkward when you scale — you need sticky sessions or a shared store
> like Redis. A JWT is **self-contained**: the user and roles are inside it, and the
> signature proves it has not been tampered with. So any instance of any service can
> validate it independently, with no shared session store. In a microservices setup that
> is the deciding factor."

### 🔴 The two things people get wrong
**1. A JWT is signed, not encrypted.** Anyone can base64-decode the payload and read it.
The signature only proves it has not been *altered*. **Never put anything sensitive in
the payload** — no passwords, no account numbers.

**2. You cannot easily revoke one.** It is valid until it expires, so if a token is
stolen it works until then. The usual answers: keep access tokens **short-lived**
(15 minutes) with a longer-lived **refresh token**, and keep a small **blocklist** of
revoked token IDs for logout. Say the trade-off rather than pretending it is solved.

## Q4. Where should the token be stored on the client?
> "An `httpOnly` cookie is safer than `localStorage`, because JavaScript cannot read an
> httpOnly cookie, so an injected script cannot steal it. Anything in localStorage is
> readable by any script on the page. The trade-off is that cookies need CSRF protection,
> whereas an `Authorization` header does not."

## Q5. CSRF, and why it is disabled for APIs
**CSRF** is when another site makes the user's browser send a request to yours, relying
on the browser automatically attaching the session cookie.

> "It is disabled for a stateless API because the attack depends on the browser
> attaching credentials automatically. If the client sends an explicit `Authorization`
> header, another site cannot make the browser add it. If I were using cookie-based auth,
> CSRF protection would need to stay on."

Do not just say "we disable CSRF" — say *why*, or it looks like copied configuration.

## Q6. Password storage
```java
@Bean PasswordEncoder passwordEncoder() { return new BCryptPasswordEncoder(); }
```
Never store plain text, and never a plain hash like MD5 or SHA-256. BCrypt is
deliberately **slow** and **salts** each password automatically, which defeats rainbow
tables and makes brute force expensive.


**Say this.**
> "Passwords are stored as a BCrypt hash, never plain text and never a plain SHA or MD5
> hash. Two properties matter. BCrypt salts each password automatically, so two users with
> the same password get different hashes and a precomputed rainbow table is useless. And it
> is deliberately **slow** with a tunable work factor, so brute forcing is expensive —
> which is the opposite of what you want from a general-purpose hash. That slowness is the
> feature."

## Q7. Other things worth a sentence
- **OAuth2 vs JWT** — not alternatives. OAuth2 is the authorisation *framework*; a JWT
  is a token *format* often used within it.
- **CORS vs CSRF** — CORS is a browser rule about which origins may read a response.
  CSRF is an attack. They get confused constantly.
- **Method security vs URL security** — URL rules are coarse and can be bypassed if
  another entry point reaches the same service method. Method-level annotations protect
  the method itself.


**Say this if they probe the distinctions.**
> "OAuth2 and JWT are not alternatives — OAuth2 is an authorisation framework describing
> how a token is obtained, and JWT is a token format often used inside it. CORS and CSRF
> also get confused: CORS is a browser rule about which origins may read a response, and
> CSRF is an attack where another site makes the browser send an authenticated request.
> And URL-level security is coarse — if another entry point reaches the same service
> method it is unprotected, so for anything sensitive I put `@PreAuthorize` on the method
> itself."

---

## ✅ Check yourself before moving on
1. Explain the JWT structure and the full request flow.
2. Explain why a JWT suits microservices better than server-side sessions.
3. Explain why a JWT is not secret, and what that means for what you put in it.
4. Explain why CSRF is disabled for a stateless API.
5. Tell your RBAC story, ending on why authorisation must be server side.
