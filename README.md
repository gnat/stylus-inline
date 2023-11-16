# 🌘 Stylus CSS Inline

## 🐍 Python Version (stylus.py)
* Most reliable version since it generates `main.css` locally for you to load normally in the browser.

## ☕ Javascript Version (stylus.html)
* Works for inline scoped `<stylus>`!
* Syntax highlighting in Sublime works!
* 🟠 External stylus in real time: Browser removes invalid CSS from `<link>` and `@import()` making those paths invalid for processing.
  * Requires loading via custom JS function to work. Might or might not be worth it?
    * Could load via `stylus('/css/main.css')` and inline `<script>` at top? Meh.


## 👀 Before you adopt.
* I realise Stylus is amazing but.. you lose the ability to inline a ton of styles at once in a single line. Sure, you save `{` and `}` but you gain verbosity elsewhere (unless of course you always add a new line for each style! May not be worthwhile to use this code depending on what patterns you currently enjoy using.
* With the new Nested syntax, hsl(), variables becoming common: classic Stylus is beginning to diverge greatly with vanilla CSS. It's time to leave. This may be an option, but a better option might be just [vanilla css](https://twitter.com/dhh/status/1719041666412347651)

![image](https://github.com/gnat/stylus-inline/assets/24665/3a306fe7-26da-44f9-bc14-5e1a9559cf7e)

