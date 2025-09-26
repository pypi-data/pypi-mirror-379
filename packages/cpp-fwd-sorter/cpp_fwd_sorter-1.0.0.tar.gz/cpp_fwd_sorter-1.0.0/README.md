# cpp-fwd-sorter

A tiny helper that **alphabetically sorts C++ forward declarations** in your headers/sources — and plays nicely with `clang-format`. Think of it as a breezy little cleanup crew for your `class Foo;` and `struct Bar;` lines.

The project ships with:
* **Sorter**: reads from stdin, writes to stdout; sorts contiguous forward-declaration blocks.
* **Wrapper**: runs `clang-format` first, then the sorter (perfect for editor integration).
> Supports `class`, `struct`, and `enum class` declarations, keeps end-of-line comments with their lines, and preserves indentation. Selection formatting is supported via `--offset` / `--length` (like `clang-format`).

---

## Install

```bash
pip install cpp-fwd-sorter
```

Pip will install **platform-specific launchers** for both tools so you can call them directly from your shell and from VSCode.

---

## Quick start

### Sort a file (after clang-format)

```bash
clang-format -style=file my_header.hpp | cpp-fwd-sorter > my_header.hpp.sorted
```

### Sort in place (using a temp file)

```bash
cpp-fwd-sorter < my_header.hpp > /tmp/sorted && mv /tmp/sorted my_header.hpp
```

### Example

Before:

```cpp
#include "Foo.h"
#include "Bar.h"

class Zeta;
class Alpha;
struct Beta;
enum class Gamma;

class Widget { };
```

After:

```cpp
#include "Foo.h"
#include "Bar.h"

class Alpha;
class Zeta;
struct Beta;
enum class Gamma;

class Widget { };
```

(Classes first, then structs, then enum classes — each group alphabetized.)

---

## VSCode: use the bundled wrapper

If you want VSCode’s **Format Document / Format Selection** to include sorting:

1. Install the package:

   ```bash
   pip install cpp-fwd-sorter
   ```

2. In VSCode settings, point the **clang-format path** to the wrapper launcher (pip created it for you). For the Microsoft C/C++ extension:

   ```jsonc
   // settings.json
   {
     "C_Cpp.clang_format_path": "cpp-fwd-format",  // the wrapper launcher
     "editor.defaultFormatter": "ms-vscode.cpptools",
     "editor.formatOnSave": true
   }
   ```

   > If your system needs a full path, use `which cpp-fwd-format` (Unix) or find it under your Python “Scripts” directory on Windows.

That’s it. VSCode will call the wrapper, which runs `clang-format` and then the sorter on the result.

---

## What gets sorted (and how)

* Detects **contiguous** blocks of simple forward declarations:

  * `class Name;`
  * `struct ns::Name;`
  * `enum class Name;`
* Sorts by kind (class → struct → enum class), then **alphabetically** (case-insensitive).
* **Keeps comments** on the same line as the declaration.
* Leaves everything else untouched.
* When VSCode calls selection formatting, we honor `--offset` and `--length`, expanding to full lines to keep things tidy.

---

## Tips & extras

* Works great in **pre-commit hooks**: run your normal `clang-format`, then pipe to `cpp-fwd-sorter`.
* Not trying to be a parser — it’s a pragmatic formatter for common forward-decl patterns. If your codebase uses exotic declarations, open an issue and we can extend it.

---

Enjoy the alphabetical zen ✨
