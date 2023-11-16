# 🪄 Stylus CSS Inline

For fun prototype based on [css-scope-inline](https://github.com/gnat/css-scope-inline). Unsure if development will continue, but if anyone wants to borrow ideas or code.. here you go. Made to work like [Stylus](https://github.com/stylus/stylus) CSS originally concieved by [
TJ Holowaychuk](https://github.com/tj) of Express.js fame.

With new [CSS Nesting](https://developer.chrome.com/articles/css-nesting/), `hsl()` syntax differences, true CSS variables: classic Stylus is beginning to diverge too greatly with vanilla CSS. It's time to leave! This project may be an option for you.

2023 it may also be best to seriously consider [vanilla CSS](https://twitter.com/dhh/status/1719041666412347651).

## 🐍 Python Version (stylus.py)
* Most reliable version since it generates `main.css` for you to load normally.
* This version is a bit more complete and robust than the Javascript one.

## ☕ Javascript Version (stylus.html)
* Runs in the browser automatically!
* Works inside inline scoped `<stylus>`!
* Syntax highlighting in Sublime works!
* 🟠 Idea of external stylus in real time has issues.
  * Browser removes invalid CSS from `<link>` and `@import()` making those paths invalid for processing.
    * Requires loading via custom JS function to work. Might or might not be worth it?
      * Could load via `stylus('/css/main.css')` and inline `<script>` at top? Meh.


## 👀 Before you adopt.

I realise Stylus is amazing but.. you lose the ability to inline a ton of styles at once in a single line. Sure, you save `{` and `}` but you gain verbosity elsewhere (unless of course you **always** add a new line for each style anyway!) May not be worthwhile to use this code depending on what patterns you currently enjoy using.
