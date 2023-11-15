# 🌘 Stylus CSS Inline

### 🟠 Beware!
* CSS nesting made Stylus somewhat obsolete.
* The ability to "stack" many styles inline makes Stylus somewhat obsolete.
  
## 🐍 Python Version (stylus.py)
* Most reliable version since it compiles to main.css

## ☕ Javascript Version (stylus.py)
* Works for inline scoped `<script>` (or `<stylus>`) !
* Syntax highlighting in Sublime works!
* 🟠 External stylus in real time: Browser removes invalid CSS from `<link>` and `@import()` making those paths invalid for processing.
  * Requires loading via custom JS function to work. Might or might not be worth it?
    * Could load via `stylus('/css/main.css')` and inline `<script>` at top?
