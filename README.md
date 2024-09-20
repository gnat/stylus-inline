# 🪄 Stylus CSS Inline

Experiment based on [css-scope-inline](https://github.com/gnat/css-scope-inline). Made to work like [Stylus](https://github.com/stylus/stylus) CSS originally concieved by [
TJ Holowaychuk](https://github.com/tj) of Express.js

With new [CSS Nesting](https://developer.chrome.com/articles/css-nesting/), `hsl()` syntax differences and true CSS variables: **classic Stylus is beginning to diverge too greatly with vanilla CSS. It's time to leave!** -- This project may be an option for you.

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

I realise Stylus is amazing but.. you lose the ability to inline styles in a single line (tailwind-like). Sure, you save `{` and `}` but you gain verbosity elsewhere (unless of course you **always** add a new line for each style anyway!) May not be worthwhile to use this code depending on what patterns you currently enjoy using.

**A good highlighter can help a lot.**

![image](https://github.com/user-attachments/assets/0fb41d75-6df2-46e5-9496-251eb84fd0b7)


![image](https://github.com/user-attachments/assets/f659fc31-e473-449a-8377-f3539a07fb0c)
