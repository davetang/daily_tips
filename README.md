![Status](https://github.com/davetang/daily_tips/actions/workflows/daily-check.yml/badge.svg)

# Daily tips

One tip every day.

## 📡 RSS Feed

[Commits RSS](https://github.com/davetang/daily_tips/commits/main.atom)

# Tips

| Date | Tip | Explanation | Tags |
| --- | --- | --- | --- |
| 2025-04-14 | `mv oldname.txt newname.txt && cat $_` | $_ can be used to get the last argument of the previous command. | shell, productivity |
| 2025-04-15 | Just type the name of the directory to autocd into it | In Bash and Zsh autocd is on by default; use `shopt autocd` and `setopt \| grep autocd` to check. | shell, productivity |
| 2025-04-16 | Use `purrr::walk()` for side effects. | When you do not care about the return value, use `purrr::walk()` instead of `purrr::map()`. | r, functional programming |
| 2025-04-17 | Use `fc` to Fix Command. | Opens your last command with `$EDITOR` and after you edit and save, the command runs immediately. | shell, productivity |
| 2025-04-18 | `diff -y file1.txt file2.txt` | `diff -y` provides a side-by-side comparison to easily spot differences. | shell, productivity |
| 2025-04-19 | `script mysession.log` | `script` save entire shell session (incl. input/output) for logging; use `exit` to stop session. | shell, productivity |
| 2025-04-20 | Use `--containall` with Singularity for better isolation | Prevents container from reading or writing from the host; useful for testing in a minimal, clean environment. | singularity |
| 2025-04-21 | `pstree -p PID` | Show processes in a tree with PID | shell, system |
| 2025-04-22 | Good enough now beats perfect later. | A working solution now is more useful than a perfect one that never arrives. | project management |
| 2025-04-23 | Consider using `tryCatch()` over `stopifnot()`. | `tryCatch()` can handle and recover from errors, while `stopifnot()` halts execution. | r, defensive programming |
