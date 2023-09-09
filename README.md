# 🌘 Stylus CSS Inline


* Works for inline scoped `<script>` !
* Browser removes invalid CSS from `<link>` and `@import()` making those paths invalid for processing.
  * Requires loading via custom JS function to work. Might or might not be worth it?
    * Could load via `stylus('/css/main.css')` and inline `<script>` at top?
* Or, can use python version for easy "build" Stylus.
