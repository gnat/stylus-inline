# 🌘 Stylus CSS Inline

## 🐍 Python Version (stylus.py)
* Most reliable version since it compiles to main.css

## ☕ Javascript Version (stylus.html)
* Works for inline scoped `<script>` (or `<stylus>`) !
* Syntax highlighting in Sublime works!
* 🟠 External stylus in real time: Browser removes invalid CSS from `<link>` and `@import()` making those paths invalid for processing.
  * Requires loading via custom JS function to work. Might or might not be worth it?
    * Could load via `stylus('/css/main.css')` and inline `<script>` at top? Meh.


## 👀 Before you adopt.
* I realise Stylus is amazing but.. you lose the ability to inline a ton of styles at once in a single line. Sure, you save `{` and `}` but you gain verbosity elsewhere (unless of course you always add a new line for each style! May not be worthwhile to use this code depending on what patterns you currently enjoy using.

![image](https://github.com/gnat/stylus-inline/assets/24665/3a306fe7-26da-44f9-bc14-5e1a9559cf7e)

