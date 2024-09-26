# 🪄 Stylus CSS Inline (SugarSS Inline)

Experiment based on [css-scope-inline](https://github.com/gnat/css-scope-inline). Made to work like [Stylus](https://github.com/stylus/stylus) CSS originally concieved by [
TJ Holowaychuk](https://github.com/tj) of Express.js (or like [sugarss](https://github.com/postcss/sugarss))

With new [CSS Nesting](https://developer.chrome.com/articles/css-nesting/), `hsl()` syntax differences and true CSS variables: **classic Stylus is beginning to diverge too greatly with vanilla CSS. It's time to leave!** -- This project may be an option for you.

## 🐍 Python Version (stylus.py)
* Most reliable version since it generates `main.styl` for you to load normally.
* This version is a bit more complete and robust than the Javascript one.

## ☕ Javascript Version (stylus.html)
* Runs in the browser automatically!
* Works inside inline scoped `<styl>`!
* Syntax highlighting in Sublime works!
* 🟠 External styl implementation pitfalls:
  * Browser removes invalid CSS from `<link>` and `@import()` making those paths invalid for processing.
  * Requires Javascript magic.
* 🟢 Working method ...

**main.styl**
```html
document.currentScript.outerHTML = `
<styl>
html
	background: green
</styl>`
```
**index.html**
```html
<script src="main.styl"></script>
```
**BONUS: Ability to include `.styl` within `.styl`**
* 🟠 Warning: May cause undesirable loading times as parent `.styl` must load *first*!
  * You're probably best off avoiding `.styl` within other `.styl` for loading performance.
```html
document.currentScript.outerHTML = `
<styl>
html
	background: green
</styl>
<styl src="component.styl"></styl>
`; document.querySelectorAll('styl[src]').forEach(s => { let ns = document.createElement('script'); ns.src = s.getAttribute('src'); s.replaceWith(ns) })
```


## 👀 Before you adopt.

I realise Stylus is amazing but.. you lose the ability to inline styles in a single line (tailwind-like). Sure, you save `{` and `}` but you gain verbosity elsewhere (unless of course you **always** add a new line for each style anyway!) May not be worthwhile to use this code depending on what patterns you currently enjoy using.

**A good highlighter can help a lot.**

![image](https://github.com/user-attachments/assets/0fb41d75-6df2-46e5-9496-251eb84fd0b7)


![image](https://github.com/user-attachments/assets/f659fc31-e473-449a-8377-f3539a07fb0c)
