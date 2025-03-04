### **Intrinsically Safe Characters in URLs**

From RFC 3986 and ChatGPT

#### **1. Unreserved Characters (Always Safe)**
These characters **never need to be percent-encoded** in a URL:
- **Alphanumeric characters (A-Z, a-z, 0-9)**
- **Hyphen (`-`)**
- **Underscore (`_`)**
- **Period (`.`)**
- **Tilde (`~`)**

#### **2. Reserved Characters (Safe Only in Proper Context)**
Some reserved characters are safe in **specific contexts**:
- **Colon (`:`)** → Safe in scheme (`https:`), host (`user:pass@`), and port (`:8080`).
- **Slash (`/`)** → Safe in path (`/path/to/resource`).
- **Question Mark (`?`)** → Safe as query separator (`?key=value`).
- **Ampersand (`&`)** → Safe as query parameter separator (`?key1=value1&key2=value2`).
- **Equals (`=`)** → Safe in query strings (`?key=value`).
- **Hash (`#`)** → Safe for fragments (`#section`).
- **At (`@`)** → Safe in user info (`user:pass@example.com`).

### **Characters That Require Encoding**
Certain characters **must** be percent-encoded in some cases:
- **Space (` `)** → `%20` or `+` (in query parameters).
- **Double Quote (`"`)** → `%22`
- **Less than (`<`), Greater than (`>`)** → `%3C`, `%3E`
- **Backslash (`\`)** → `%5C`
- **Pipe (`|`)** → `%7C`
- **Curly Braces (`{ }`)** → `%7B`, `%7D`
- **Caret (`^`)** → `%5E`
- **Backtick (`` ` ``)** → `%60`

### Not included in ChatGPT's analysis
- **Single Quote/Apostrophe (`` ' ``)** → `%27`
