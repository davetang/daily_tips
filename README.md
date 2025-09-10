![Status](https://github.com/davetang/daily_tips/actions/workflows/daily-check.yml/badge.svg)

# Daily tips

One tip every day.

# Kaizen

Kaizen (改善) is a Japanese word made up of two characters:

* 改 (kai) — "change" or "correct"
* 善 (zen) — "good" or "better"

So literally, kaizen means "change for the better."

## 📡 RSS Feed

[Commits RSS](https://github.com/davetang/daily_tips/commits/main.atom)

# Tips

| Date | Tip | Explanation | Tags |
| --- | --- | --- | --- |
| 2025-04-14 | `mv oldname.txt newname.txt && cat $_` | $_ can be used to get the last argument of the previous command. | shell, productivity |
| 2025-04-15 | Just type the name of the directory to autocd into it. | In Bash and Zsh autocd is on by default; use `shopt autocd` and `setopt \| grep autocd` to check. | shell, productivity |
| 2025-04-16 | Use `purrr::walk()` for side effects. | When you do not care about the return value, use `purrr::walk()` instead of `purrr::map()`. | r, functional programming |
| 2025-04-17 | Use `fc` to Fix Command. | Opens your last command with `$EDITOR` and after you edit and save, the command runs immediately. | shell, productivity |
| 2025-04-18 | `diff -y --color=always file1.txt file2.txt` | `diff -y` provides a side-by-side comparison to easily spot differences with colour! | shell, productivity |
| 2025-04-19 | `script mysession.log` | `script` save entire shell session (incl. input/output) for logging; use `exit` to stop session. | shell, productivity |
| 2025-04-20 | Use `--containall` with Singularity for better isolation. | Prevents container from reading or writing from the host; useful for testing in a minimal, clean environment. | singularity |
| 2025-04-21 | `pstree -p PID` | Show processes in a tree with PID. | shell, system |
| 2025-04-22 | Good enough now beats perfect later. | A working solution now is more useful than a perfect one that never arrives. | project management |
| 2025-04-23 | Consider using `tryCatch()` over `stopifnot()`. | `tryCatch()` can handle and recover from errors, while `stopifnot()` halts execution. | r, defensive programming |
| 2025-04-24 | `apropos unzip` | If you know what a command does, but not the name use `apropos` to search the man pages! | shell, documentation |
| 2025-04-25 | Use `--cleanenv` with Singularity. | Using `--cleanenv` prevents the container from inheriting most of the environment variables from the host. | singularity |
| 2025-04-26 | `tar -cJf archive-name.tar.xz folder/` | xz typically compresses better than gz but is slower; use for long term backups. | shell, compression |
| 2025-04-27 | `watch vcgencmd measure_temp` | Measure the temperature every second. | raspberry pi |
| 2025-04-28 | Use the dot placeholder with {purrr}. | `purrr::map_int(1:5, ~ . + 1)` vs. `purrr::map_int(1:5, function(x) x + 1)`. | r, functional programming |
| 2025-04-29 | Use `date` and `bc` to measure elapsed time. | Use `$(date +%s.%N)` to get times then use `echo "${END} - ${START}" \| bc` to get elapsed time. | shell, benchmarking |
| 2025-04-30 | Apply the aggregation of marginal gains. | Follow the philosophy of searching for a tiny margin of improvement in everything you do. | self-help, habits |
| 2025-05-01 | `find ~ -type f -size +100M` | Find files in your home directory that are larger than 100M using `find`. | shell, reminder |
| 2025-05-02 | `purrr::discard(~ stringr::str_detect(., "old"))` | Use `purrr::discard` to discard elements based on their values. | r, functional programming |
| 2025-05-03 | `purrr::list_rbind(my_list, names_to = "id")` | Use `purrr::list_rbind()` to combine list elements into a single data structure. | r, functional programming |
| 2025-05-04 | `f <- purrr::compose(sqrt, abs)` | Use `purrr::compose()` to combine multiple functions into one, chaining them from right to left. | r, functional programming |
| 2025-05-05 | Use `shellcheck` to lint and find potential issues in your script. | ShellCheck is a static analysis and linting tool for sh/bash scripts. | shell, linting |
| 2025-05-06 | Use the {gt} package to make nice looking tables in R. | The gt philosophy: we can construct a wide variety of useful tables with a cohesive set of table parts. | r, visualisation |
| 2025-05-07 | `seq 10 \| datamash sum 1 mean 1` | GNU datamash can perform basic numeric, textual and statistical operations on input textual data files. | shell, productivity |
| 2025-05-08 | Use `rsync` over `scp`. | `rsync` only transfers differences, has better support for resuming transfers, and has more features. | shell, productivity |
| 2025-05-09 | `tmpfile=$(mktemp)` | Use `mktemp` for secure, race-free temp file creation. | shell, scripting |
| 2025-05-10 | `find . -maxdepth 1 -type f ! -name "*.sh" ! -name "*.md" -exec ls {} +` | Use `!` with `find` to exclude files. | shell, productivity |
| 2025-05-11 | `trap 'echo Caught a signal (EXIT, INT, or TERM).; exit' EXIT INT TERM` | `trap` is useful for cleaning up temporary files, restoring settings, or just handling interruptions gracefully. | shell, scripting |
| 2025-05-12 | `echo Done with task at line $LINENO` | `$LINENO` gives the line number of the current command within a script or function. | shell, scripting |
| 2025-05-13 | `du -h --max-depth=1 \| sort -h` | Get size of files and top directories, then sort by human-readable sizes. | shell, reminder |
| 2025-05-14 | `git config --global help.autocorrect 1` | Auto-correct typos in Git commands. | shell, reminder |
| 2025-05-15 | `readarray -t FILES < <(find .)` | Use `readarray` to read stuff into an array. | bash scripting |
| 2025-05-16 | `tidyr::separate(df, group, c("key", "value"), sep = "\\s", extra = "merge")` | Use `extra = "merge"` to force splitting to match length of third parameter (`into`). | tidyverse |
| 2025-05-17 | Use `tidyr::separate_wider_delim()` instead of `tidyr::separate()`. | `separate()` has been superseded in favour of `separate_wider_position()` and `separate_wider_delim()`. | tidyverse |
| 2025-05-18 | Set boundaries with intention, not guilt. | Treat your personal time with the same respect you would give to a work meeting. | self-help |
| 2025-05-19 | Use `/etc/hosts` to set DNS mappings. | Save yourself typing IP addresses by adding an entry in `/etc/hosts`. | reminder, networking |
| 2025-05-20 | Use the {targets} package to build workflows in R. | The {targets} package allows you build reproducible workflows entirely within R. | R, workflows |
| 2025-05-21 | `git blame -w` | Use `git blame -w` to see the commit hash and timestamp of each change, line by line. | Git |
| 2025-05-22 | `git notes add -m "Add note to commit" 98ab5fd901ee38dcbfd3ae6bbd26c6ffdc801ff7` | Use `git notes` to add notes to a commit; `git log` will show notes. | Git |
| 2025-05-23 | `cp -u some_file .` | Copy only when the SOURCE file is newer than the destination file or when the destination file is missing. | shell, productivity |
| 2025-05-24 | `find . -type f -mtime -2` | Find files that were modified less than 2 days ago. | shell, reminder |
| 2025-05-25 | `grep -r --include="*.conf" "Listen" /etc` | Search recursively `*.conf` files for "Listen" in `/etc`, including subdirectories. | shell, productivity |
| 2025-05-26 | `ps aux --sort=-%mem \| head -n 3` | Show top memory-consuming processes. | shell, processes |
| 2025-05-27 | `bash -x test.sh` | Use `-x` for debugging Bash scripts. | bash scripting |
| 2025-05-28 | [expression for item in iterable if condition] | List comprehension in Python (that I always forget). | python, reminder |
| 2025-05-29 | `name<-"Rei"; glue::glue("Hello, {name}!")` | Use the {glue} package for string interpolation in R! | r |
| 2025-05-30 | `singularity inspect my_image.sif` | Inspect metadata, labels, environment, and scripts of a Singularity image. | singularity |
| 2025-05-31 | `git log --pretty=format:"%h %ad \| %s%d [%an]" --date=short` | Customize `git log` output using `--pretty=format:`. | git, productivity |
| 2025-06-01 | `python3 -c "import sys; print(sys.version)"` | Use `-c` with Python (and Bash) to run a command from the command line. | python, bash, scripting |
| 2025-06-02 | If you are not paying for the product, you are the product. | When services are offered for free, your data, attention, or behaviour are monetised. | reminder |
| 2025-06-03 | Set the seed for reproducibility. | When dealing with randomness, set the seed to ensure that you get the same results. | reminder |
| 2025-06-04 | `getAnywhere("some_function")` | `getAnywhere()` searches all environments for any object matching a provided name. | r, reminder |
| 2025-06-05 | Use Matrix Market for storing sparse matrices in human readable format. | Sparse matrices are not efficiently stored in CSV or TSV format. | r, file format |
| 2025-06-06 | When committing changes, one change should equal one purpose. | Each commit should do one thing: fix a bug, update docs, rename a variable, add a feature, etc. | git, best practice |
| 2025-06-07 | LABEL maintainer="Dave Tang <email_address>" | Using MAINTAINER in Dockerfiles has been deprecated; use LABEL instead. | docker, best practice |
| 2025-06-08 | Always put double quotes around variables in Bash scripts. | Filenames, arguments, or inputs might contain spaces, tabs, or special characters. | bash scripting, best practice |
| 2025-06-09 | Use `withCallingHandlers()` to log messages and warnings in R. | `withCallingHandlers()` is an advanced error and condition handling function in R that can be used for logging and more. | r, defensive programming |
| 2025-06-10 | `find data -path *pca/res.txt -print` | Will only find res.txt inside directories matching `*pca`. | shell, productivity |
| 2025-06-11 | Know about the fallacy of personal validation. | The Barnum effect is when people give high accuracy ratings to descriptions of their personality but the descriptions are in fact vague and general. | psychology |
| 2025-06-12 | Make a habit of using `alias` in the shell. | Use `alias` to create aliases so you have to type (and remember) less. | shell, productivity |
| 2025-06-13 | Remember the 3 R's of Habit Change | Reminder (initiates the behaviour), Routine (the actual behaviour), and Reward (the benefit gained). | good habits |
| 2025-06-14 | Use https://explainshell.com/ to explain shell commands. | The site contains parsed manpages from sections 1 and 8 found in Ubuntu's manpage repository. | shell, productivity |
| 2025-06-15 | Use `CDPATH` to search in other specified paths besides the current directory. | Instead of looking only in the current directory, the shell now checks directories set by `CDPATH`. | shell, productivity |
| 2025-06-16 | `find dir1 dir2 dir3 -type f -name "*.txt"` | Find works on multiple locations! | shell, productivity |
| 2025-06-17 | `compdef _gnu_generic find` | Tab completion for find when using Zsh! | zsh, productivity |
| 2025-06-18 | `sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt` | Perform two separate substitution expressions with just one `sed` command. | sed, reminder |
| 2025-06-19 | `while IFS= read -r line; do echo "$line" done < filename.txt` | Read a file line by line, preserving all whitespace in a Bash script. | Bash, reminder |
| 2025-06-20 | Read the Bash Reference Manual | You will probably need to read and/or write a Bash script, so read https://www.gnu.org/software/bash/manual/bash.html. | Bash |
| 2025-06-21 | `readarray` is synonym for `mapfile`. | `mapfile` read lines from the standard input into the indexed array. | Bash |
| 2025-06-22 | Be aware of Cognitive Debt and don't build it up! | See study: Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task | good habits |
| 2025-06-23 | Check out `fzf`, a command-line fuzzy finder | `fzf` is an interactive filter program for any kind of list; files, command history, processes, hostnames, bookmarks, git commits, etc. | shell, productivity |
| 2025-06-24 | `find . -type f -print0 \| xargs -0 rm` | Use `-print0` with `find` to explicitly mark the end of each filename with a null byte, which works nicely with `xargs`. | shell, best practice |
| 2025-06-25 | Buy The Secret Rules of the Terminal at https://wizardzines.com/zines/terminal/ | Understanding just a little more about the terminal can make your experience WAY better. | shell, productivity |
| 2025-06-26 | `which -a python3` | Use `which -a` to show ALL matches in your PATH for a program, in order! | shell, productivity |
| 2025-06-27 | Use `pbcopy` and `pbpaste` to copy to the clipboard and paste from the clipboard | `pbcopy` and `pbpaste` are only available on macOS but can be mimicked using other tools on Linux. | macOS, productivity |
| 2025-06-28 | echo "export DISPLAY=localhost:10.0" >> ~/.screenrc | Ensure that DISPLAY is set in all `screen` sessions by setting it in `~/.screenrc`. | screen, productivity |
| 2025-06-29 | The terminal emulator is a translator. | The terminal emulator translates all typing/clicks into bytes and and it takes all the bytes from a program and displays them on the screen. | terminal |
| 2025-06-30 | The terminal emulator turns actions into text, escape codes or control characters. | Text is like `cat test.txt`, escape codes can tell the terminal what colour to display text in, and control characters like Ctrl+C (byte 3). | terminal |
| 2025-07-01 | `cat /sys/block/sda/queue/rotational` | Check whether a block device (like /dev/sda) is an SSD (0) or HDD (1). | linux |
| 2025-07-02 | `csvlook file.csv` (after installing csvkit). | Renders a CSV to the command line in a Markdown-compatible, fixed-width format. | terminal, productivity |
| 2025-07-03 | The {ggeasy} package provides {ggplot2} shortcuts. | {ggeasy} is a helper package that makes it easier to make {ggplot2} plots! | r, helper |
| 2025-07-04 | `install.packages("torch")` | R Interface to Torch! | r, machine learning |
| 2025-07-05 | Check out Miller! | Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON! | terminal, productivity |
| 2025-07-06 | Try changing up your environment or daily routine. | Even small shifts can spark new motivation and boost your focus! | productivity |
| 2025-07-07 | Trust, but verify. | You can always trust that a tool performs as advertised but you should verify too. | adage |
| 2025-07-08 | `mlr --icsv --opprint cat example.csv` | Use Miller to output a CSV file in a pretty format! | terminal, productivity |
| 2025-07-09 | `sudo apt install lftp` | Legacy `ftp` is deprecated; use `lftp`, a more modern FTP client. | Linux |
| 2025-07-10 | Check out `tmux` | I have been using GNU Screen for as long as I can remember; time to check out `tmux`? | Linux, productivity |
| 2025-07-11 | Use `"+y` to yank to the clipboard in Nvim! | Instead of using the mouse to copy to the clipboard, use `"+y` to yank to the clipboard! | Nvim |
| 2025-07-12 | Use marks to set a specific position to jump back to in Nvim. | Use `ma` to mark current cursor position. Use `backtick+a` to jump to exact position and `'a` to jump to start of line. | Nvim |
| 2025-07-13 | `Ctrl+o` and `Ctrl+i`: go backward and forward in jump history. | Great for moving back after using search or jumping to the start/end of a file. | Nvim |
| 2025-07-14 | You can open two or more files in Nvim and work with them simultaneously! | Use `:ls` to list open buffers, i.e., files that are open, and `:b number` to switch between them. | Nvim |
| 2025-07-15 | Use `:help` to bring up the help screen in Nvim. | The Nvim help pages are quite detailed; use `CTRL-]` to jump to a subject. | Nvim, reminder |
| 2025-07-16 | `hexdump -C text.txt` | Display the input offset in hexadecimal and its ASCII representation in two columns. | terminal |
| 2025-07-17 | Check out `pixi`, a very fast package manager. | [7 Reasons to Switch from Conda to Pixi](https://prefix.dev/blog/pixi_a_fast_conda_alternative). | productivity |
| 2025-07-18 | A random variable is defined as the numerical outcome of a random experiment. | A random experiment repeated many times will generate results governed by their probabilities. | statistics, reminder |
| 2025-07-19 | Probability measures the _ratio_ of an outcome to the total possible outcomes. | When you want to find how likely something is, you are really asking what fraction of all possibilities does this represent? | statistics, reminder |
| 2025-07-20 | Adding random variables combines different uncertain quantities to get a new uncertain quantity. | Adding random variables represents combining their outcomes in a single experiment. | statistics, reminder |
| 2025-07-21 | A binomial distribution counts successes in $n$ independent trials, each with probability $p$. | As $n$ gets large in a binomial distribution, it approaches a normal distribution. | statistics, reminder |
| 2025-07-22 | `sudo do-release-upgrade` | Upgrade Ubuntu from the terminal; but remember to fully update the system first: `sudo apt update && sudo apt upgrade -y; sudo apt dist-upgrade -y`. | Ubuntu |
| 2025-07-23 | Always keep a "live install" image lying around for when your server runs into issues! | Get a live install Debian image from https://www.debian.org/CD/live/; in case you were wondering, this is unrelated to yesterday's tip! | Debian |
| 2025-07-24 | Use `getSimpleName()` to get the path name without any extension in Nextflow. | See https://nextflow.io/docs/latest/reference/stdlib-types.html for more utilities! | Nextflow |
| 2025-07-25 | `sudo fsck -fy /dev/sda2` | Use `fsck` (File System Consistency Check) to scan and fix disk errors automatically. | Linux, sysadmin |
| 2025-07-26 | `imap(my_list, ~ paste0("Key ", .y, " has value ", .x))` | Use `imap()` if you want both the element and its name/index. | r, functional programming |
| 2025-07-27 | `safe_fn <- safely(some_function)` | `safely()` wraps a function and makes it return a result even if an error occurs. Instead of stopping execution, it returns a list with the actual result or error object. | r, functional programming |
| 2025-07-28 | `purrr::pmap(list(list(1900), list(80), list(4)), \(x,y,z) x+y+z)` | Use `purrr::pmap()` to map over multiple input simultaneously. | r, functional programming |
| 2025-07-29 | Learn [Lua](https://www.lua.org/start.html)! | Lua is a powerful and fast programming language that is easy to learn and use and to embed into your application. | Lua |
| 2025-07-30 | Use the [systemadmin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/systemadmin) plugin in ohmyzsh. | This plugin adds a series of aliases and functions which make a System Administrator's life easier. | ohmyzsh |
| 2025-07-31 | Check out marimo! | marimo is an open-source reactive notebook for Python - reproducible, Git-friendly, AI-native, SQL built-in, executable as a script, shareable as an app. | python |
| 2025-08-01 | Using GNU screen, `Ctrl-a [`, space, space, Esc, and then `Ctrl-a ]` to paste! | You can copy and paste from one GNU screen to another without using the mouse! | screen |
| 2025-08-02 | [Sign your Git commits](https://github.com/davetang/getting_started_with_git?tab=readme-ov-file#signing-commits) to confirm that you made the commit. | A signed commit is cryptographic proof that the commit came from you, using your GPG or SSH key. | git, github |
| 2025-08-03 | Use GPG to encrypt and decrypt files. | Some notes on using GPG on my [bioinformatics tips page](https://davetang.github.io/bioinformatics_tips/security.html). | security |
| 2025-08-04 | In `.screenrc` you can specify how many windows to create when you start `screen`! | Add `screen -t monitor 0 glances` where `monitor` is the name, `0` is the screen number, and `glances` is the command to run. Add as many entries as you need! | screen |
| 2025-08-05 | `ssh-copy-id -i ~/.ssh/id_rsa.pub username@server-ip` | Use `ssh-copy-id` to copy a public key to a server, so you can SSH using your private key. | Linux |
| 2025-08-06 | Put `bindkey -v` in `~/.zshrc` to enable Zsh Vi mode! | Your Zsh shell behaves like a mini Vim editor for command-line editing! | zsh |
| 2025-08-07 | `git clone https://github.com/jeffreytse/zsh-vi-mode $ZSH_CUSTOM/plugins/zsh-vi-mode` | [zsh-vi-mode](https://github.com/jeffreytse/zsh-vi-mode) is a better and friendly vi(vim) mode plugin for Zsh. | zsh |
| 2025-08-08 | `:Gdiffsplit` | When using the vim-fugitive plugin `:Gdiffsplit` will show you the previous version in a split window! | vim |
| 2025-08-09 | Use `^` to go to the first non-blank character. | Instead of pressing `0` and `w`, just press `^` to move to the first non-blank character on the current line; great for indented code! | vim |
| 2025-08-10 | Use `zf` to fold lines and `zo` to open folded lines in Vim. | Sometimes it is useful to fold, i.e., hide, lines; use `zf` and `zo` to fold and open, respectively in Vim. | vim |
| 2025-08-11 | Use ` `` ` to move back and forth between the last jump in Vim. | Searching, marks, `gg`, and more counts as jumps. For example, after searching use ` `` ` to move back to where you were! | vim |
| 2025-08-12 | Press `Shift+Command+G` to bring up the Go To window in Finder. | At least on my computer, Finder does not have a shortcut to click on to bring me to the root directory. | macOS |
| 2025-08-13 | Use `local` inside functions of shell scripts to restrict the scope! | Variables are global within a shell script unless you explicitly mark them local inside a function! | shell, scripting |
| 2025-08-14 | If you edit Markdown files using Vim, use `[[` and `]]` to jump header to header! | `[[` and `]]` are used to jump from function to function but works for headers in Markdown files! | vim, markdown |
| 2025-08-15 | Use `:reg` to view the contents of registers in Vim. | In Vim, registers are like named clipboards; after seeing the registers using `:reg`, type `"2p` to paste from the second register. | vim |
| 2025-08-16 | Use `screen -x` to attach to the same session simultaneously!! | Find the screen session using `screen -ls` then `screen -x 284771` where 284771 is the screen session ID. | screen |
| 2025-08-17 | According to Shannon, information is present whenever a signal is transmitted from one place (sender) to another (receiver). | It does not matter what kind of signal, it could be words, a picture, or even electric impulses. | information theory |
| 2025-08-18 | In Linux, `<`, `<<`, and `<<<` are redirection operators used for input handling. | `<` reads from an existing file; `<<` creates temporary multi-line input; `<<<` provides immediate string input. | Linux |
| 2025-08-19 | Use a block, i.e., `{}` to group together packages to keep quiet: `suppressPackageStartupMessages({ library(ggplot2) })` | `{}` denote a block and they allow you to group multiple expressions together and treat them as a single expression. | r |
| 2025-08-20 | `git config --global completion.branch true` | Enable autocompletion for branch names. | git, config |
| 2025-08-21 | In GNU Make `=` is recursive/late assignment and `:=` simple/early assignment. | `=` is similar to lazy evaluation whereas `:=` is similar to eager evaluation. | make, reminder |
| 2025-08-22 | `pandoc README.md -s -o index.html -f gfm --highlight-style=pygments` | Convert a GitHub flavoured Markdown file to standalone HTML with syntax highlighting! | pandoc |
| 2025-08-23 | Use the [z](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/z) ohmyzsh plugin to access commonly visited directories. | This plugin defines the z command that tracks your most visited directories and allows you to access them with very few keystrokes. | ohmyzsh |
| 2025-08-24 | Use the [copybuffer](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/copybuffer) ohmyzsh plugin to copy the current text in the command line to the system clipboard! | Instead of using the mouse to highlight and copy text in the command line, just press `ctrl-o` with the copybuffer plugin! | ohmyzsh |
| 2025-08-25 | Use [lazy.nvim](https://github.com/folke/lazy.nvim) to manage plugins for Nvim. | Plugins add a lot more functionality into Nvim! | Nvim |
| 2025-08-26 | `singularity exec my_image /bin/bash -c 'echo $SINGULARITY_NAME'` | Use `$SINGULARITY_NAME` to get the name of the Singularity image when inside a container! | singularity |
| 2025-08-27 | `build/output.txt: input.txt \| build` | Use order-only prerequisites to only make sure something exists, but do not force rebuilds if they change! | make |
| 2025-08-28 | Run GNU make with `-d` like `make -d` to get debugging information! | I spent the last hour trying to figure out why my target kept rebuilding and finally found out why with `-d`! | make |
| 2025-08-29 | `tail -f !$` | `!$` expands to the last argument of the previous command; you can even type `!$` and press tab to get the last argument! | shell, productivity |
| 2025-08-30 | Don't ignore your personal life because it affects your professional life! | I wrote a short blog post [on professionalism](https://davetang.org/muse/2025/08/30/on-professionalism/). | self-help, habits |
| 2025-08-31 | Discrete Mutual Information (DMI) measures how much information one categorical variable contains about another. | If two variables are independent, DMI = 0 (knowing one does not help you guess the other). | information theory |
| 2025-09-01 | Use [quarto-ext/lightbox](https://github.com/quarto-ext/lightbox) to create lightbox treatments for images in your HTML documents! | See the [Example Lightbox Document](https://quarto-ext.github.io/lightbox/) for a demo! | quarto |
| 2025-09-02 | `convert input.png -trim +repage output.png` | Use ImageMagick to trim the whitespace from an image; the `+repage` parameter will reset the page size. | imagemagick |
| 2025-09-03 | [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory) is the mathematical study of waiting lines, or queues. | A queueing model is constructed so that queue lengths and waiting time can be predicted. | queueing |
| 2025-09-04 | `nvim -d file1 file2` | Start Nvim in diff mode which can highlight differences between files side by side and apply changes between files! | Nvim |
| 2025-09-05 | `git log -p -- file.txt` | By default, `git log` does not generate any diff output; use `-p` or `--patch` to show all changes of `file.txt`! | git |
| 2025-09-06 | Use Common Table Expressions (CTEs) (`WITH`) to simplify complex queries! | A CTE is a temporary, named result set defined at the start of a query using the `WITH` keyword; it is like creating a "virtual table" that you can reuse inside your query! | sql |
| 2025-09-07 | Press Shift+Insert to paste in MobaXTerm. | Instead of using the right mouse button to paste, use Shift+Insert to paste when using MobaXTerm! | MobaXTerm |
| 2025-09-08 | `awk '$1=$1' test.txt` | AWK trick to turn one or more spaces (by default) into just one space. | awk |
| 2025-09-09 | Use the `combn()` function in base R to generate pairwise combinations | `combn()` [can also be used with a function](https://github.com/davetang/learning_r?tab=readme-ov-file#useful-tips) to apply the function across pairwise combinations! | r |
| 2025-09-10 | Use `(` and `)` to jump to the previous and next sentence. Use `{` and `}` for paragraphs! | If you edit written text in Vim, make sure you use `(`, `)`, `{`, and `}`! | vim |
