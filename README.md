![Status](https://github.com/davetang/daily_tips/actions/workflows/daily-check.yml/badge.svg)

# Daily tips

One tip every day. Use tags to help search for tips; tags are all lowercase.

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
| 2025-04-16 | Use `purrr::walk()` for side effects. | When you do not care about the return value, use `purrr::walk()` instead of `purrr::map()`. | rstats, functional programming |
| 2025-04-17 | Use `fc` to Fix Command. | Opens your last command with `$EDITOR` and after you edit and save, the command runs immediately. | shell, productivity |
| 2025-04-18 | `diff -y --color=always file1.txt file2.txt` | `diff -y` provides a side-by-side comparison to easily spot differences with colour! | shell, productivity |
| 2025-04-19 | `script mysession.log` | `script` save entire shell session (incl. input/output) for logging; use `exit` to stop session. | shell, productivity |
| 2025-04-20 | Use `--containall` with Singularity for better isolation. | Prevents container from reading or writing from the host; useful for testing in a minimal, clean environment. | singularity |
| 2025-04-21 | `pstree -p PID` | Show processes in a tree with PID. | shell, system |
| 2025-04-22 | Good enough now beats perfect later. | A working solution now is more useful than a perfect one that never arrives. | project management |
| 2025-04-23 | Consider using `tryCatch()` over `stopifnot()`. | `tryCatch()` can handle and recover from errors, while `stopifnot()` halts execution. | rstats, defensive programming |
| 2025-04-24 | `apropos unzip` | If you know what a command does, but not the name use `apropos` to search the man pages! | shell, documentation |
| 2025-04-25 | Use `--cleanenv` with Singularity. | Using `--cleanenv` prevents the container from inheriting most of the environment variables from the host. | singularity |
| 2025-04-26 | `tar -cJf archive-name.tar.xz folder/` | xz typically compresses better than gz but is slower; use for long term backups. | shell, compression |
| 2025-04-27 | `watch vcgencmd measure_temp` | Measure the temperature every second. | raspberry pi |
| 2025-04-28 | Use the dot placeholder with {purrr}. | `purrr::map_int(1:5, ~ . + 1)` vs. `purrr::map_int(1:5, function(x) x + 1)`. | rstats, functional programming |
| 2025-04-29 | Use `date` and `bc` to measure elapsed time. | Use `$(date +%s.%N)` to get times then use `echo "${END} - ${START}" \| bc` to get elapsed time. | shell, benchmarking |
| 2025-04-30 | Apply the aggregation of marginal gains. | Follow the philosophy of searching for a tiny margin of improvement in everything you do. | self-help, habits |
| 2025-05-01 | `find ~ -type f -size +100M` | Find files in your home directory that are larger than 100M using `find`. | shell, reminder |
| 2025-05-02 | `purrr::discard(~ stringr::str_detect(., "old"))` | Use `purrr::discard` to discard elements based on their values. | rstats, functional programming |
| 2025-05-03 | `purrr::list_rbind(my_list, names_to = "id")` | Use `purrr::list_rbind()` to combine list elements into a single data structure. | rstats, functional programming |
| 2025-05-04 | `f <- purrr::compose(sqrt, abs)` | Use `purrr::compose()` to combine multiple functions into one, chaining them from right to left. | rstats, functional programming |
| 2025-05-05 | Use `shellcheck` to lint and find potential issues in your script. | ShellCheck is a static analysis and linting tool for sh/bash scripts. | shell, linting |
| 2025-05-06 | Use the {gt} package to make nice looking tables in R. | The gt philosophy: we can construct a wide variety of useful tables with a cohesive set of table parts. | rstats, visualisation |
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
| 2025-05-20 | Use the {targets} package to build workflows in R. | The {targets} package allows you build reproducible workflows entirely within R. | rstats, workflows |
| 2025-05-21 | `git blame -w` | Use `git blame -w` to see the commit hash and timestamp of each change, line by line. | git |
| 2025-05-22 | `git notes add -m "Add note to commit" 98ab5fd901ee38dcbfd3ae6bbd26c6ffdc801ff7` | Use `git notes` to add notes to a commit; `git log` will show notes. | git |
| 2025-05-23 | `cp -u some_file .` | Copy only when the SOURCE file is newer than the destination file or when the destination file is missing. | shell, productivity |
| 2025-05-24 | `find . -type f -mtime -2` | Find files that were modified less than 2 days ago. | shell, reminder |
| 2025-05-25 | `grep -r --include="*.conf" "Listen" /etc` | Search recursively `*.conf` files for "Listen" in `/etc`, including subdirectories. | shell, productivity |
| 2025-05-26 | `ps aux --sort=-%mem \| head -n 3` | Show top memory-consuming processes. | shell, processes |
| 2025-05-27 | `bash -x test.sh` | Use `-x` for debugging Bash scripts. | bash scripting |
| 2025-05-28 | [expression for item in iterable if condition] | List comprehension in Python (that I always forget). | python, reminder |
| 2025-05-29 | `name<-"Rei"; glue::glue("Hello, {name}!")` | Use the {glue} package for string interpolation in R! | rstats |
| 2025-05-30 | `singularity inspect my_image.sif` | Inspect metadata, labels, environment, and scripts of a Singularity image. | singularity |
| 2025-05-31 | `git log --pretty=format:"%h %ad \| %s%d [%an]" --date=short` | Customize `git log` output using `--pretty=format:`. | git, productivity |
| 2025-06-01 | `python3 -c "import sys; print(sys.version)"` | Use `-c` with Python (and Bash) to run a command from the command line. | python, bash, scripting |
| 2025-06-02 | If you are not paying for the product, you are the product. | When services are offered for free, your data, attention, or behaviour are monetised. | reminder |
| 2025-06-03 | Set the seed for reproducibility. | When dealing with randomness, set the seed to ensure that you get the same results. | reminder |
| 2025-06-04 | `getAnywhere("some_function")` | `getAnywhere()` searches all environments for any object matching a provided name. | rstats, reminder |
| 2025-06-05 | Use Matrix Market for storing sparse matrices in human readable format. | Sparse matrices are not efficiently stored in CSV or TSV format. | rstats, file format |
| 2025-06-06 | When committing changes, one change should equal one purpose. | Each commit should do one thing: fix a bug, update docs, rename a variable, add a feature, etc. | git, best practice |
| 2025-06-07 | LABEL maintainer="Dave Tang <email_address>" | Using MAINTAINER in Dockerfiles has been deprecated; use LABEL instead. | docker, best practice |
| 2025-06-08 | Always put double quotes around variables in Bash scripts. | Filenames, arguments, or inputs might contain spaces, tabs, or special characters. | bash scripting, best practice |
| 2025-06-09 | Use `withCallingHandlers()` to log messages and warnings in R. | `withCallingHandlers()` is an advanced error and condition handling function in R that can be used for logging and more. | rstats, defensive programming |
| 2025-06-10 | `find data -path *pca/res.txt -print` | Will only find res.txt inside directories matching `*pca`. | shell, productivity |
| 2025-06-11 | Know about the fallacy of personal validation. | The Barnum effect is when people give high accuracy ratings to descriptions of their personality but the descriptions are in fact vague and general. | psychology |
| 2025-06-12 | Make a habit of using `alias` in the shell. | Use `alias` to create aliases so you have to type (and remember) less. | shell, productivity |
| 2025-06-13 | Remember the 3 R's of Habit Change | Reminder (initiates the behaviour), Routine (the actual behaviour), and Reward (the benefit gained). | good habits |
| 2025-06-14 | Use https://explainshell.com/ to explain shell commands. | The site contains parsed manpages from sections 1 and 8 found in Ubuntu's manpage repository. | shell, productivity |
| 2025-06-15 | Use `CDPATH` to search in other specified paths besides the current directory. | Instead of looking only in the current directory, the shell now checks directories set by `CDPATH`. | shell, productivity |
| 2025-06-16 | `find dir1 dir2 dir3 -type f -name "*.txt"` | Find works on multiple locations! | shell, productivity |
| 2025-06-17 | `compdef _gnu_generic find` | Tab completion for find when using Zsh! | zsh, productivity |
| 2025-06-18 | `sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt` | Perform two separate substitution expressions with just one `sed` command. | sed, reminder |
| 2025-06-19 | `while IFS= read -r line; do echo "$line" done < filename.txt` | Read a file line by line, preserving all whitespace in a Bash script. | bash, reminder |
| 2025-06-20 | Read the Bash Reference Manual | You will probably need to read and/or write a Bash script, so read https://www.gnu.org/software/bash/manual/bash.html. | bash |
| 2025-06-21 | `readarray` is synonym for `mapfile`. | `mapfile` read lines from the standard input into the indexed array. | bash |
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
| 2025-07-03 | The {ggeasy} package provides {ggplot2} shortcuts. | {ggeasy} is a helper package that makes it easier to make {ggplot2} plots! | rstats, helper |
| 2025-07-04 | `install.packages("torch")` | R Interface to Torch! | rstats, machine learning |
| 2025-07-05 | Check out Miller! | Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON! | terminal, productivity |
| 2025-07-06 | Try changing up your environment or daily routine. | Even small shifts can spark new motivation and boost your focus! | productivity |
| 2025-07-07 | Trust, but verify. | You can always trust that a tool performs as advertised but you should verify too. | adage |
| 2025-07-08 | `mlr --icsv --opprint cat example.csv` | Use Miller to output a CSV file in a pretty format! | terminal, productivity |
| 2025-07-09 | `sudo apt install lftp` | Legacy `ftp` is deprecated; use `lftp`, a more modern FTP client. | linux |
| 2025-07-10 | Check out `tmux` | I have been using GNU Screen for as long as I can remember; time to check out `tmux`? | Linux, productivity |
| 2025-07-11 | Use `"+y` to yank to the clipboard in Nvim! | Instead of using the mouse to copy to the clipboard, use `"+y` to yank to the clipboard! | nvim |
| 2025-07-12 | Use marks to set a specific position to jump back to in Nvim. | Use `ma` to mark current cursor position. Use `backtick+a` to jump to exact position and `'a` to jump to start of line. | nvim |
| 2025-07-13 | `Ctrl+o` and `Ctrl+i`: go backward and forward in jump history. | Great for moving back after using search or jumping to the start/end of a file. | nvim |
| 2025-07-14 | You can open two or more files in Nvim and work with them simultaneously! | Use `:ls` to list open buffers, i.e., files that are open, and `:b number` to switch between them. | nvim |
| 2025-07-15 | Use `:help` to bring up the help screen in Nvim. | The Nvim help pages are quite detailed; use `CTRL-]` to jump to a subject. | nvim, reminder |
| 2025-07-16 | `hexdump -C text.txt` | Display the input offset in hexadecimal and its ASCII representation in two columns. | terminal |
| 2025-07-17 | Check out `pixi`, a very fast package manager. | [7 Reasons to Switch from Conda to Pixi](https://prefix.dev/blog/pixi_a_fast_conda_alternative). | productivity |
| 2025-07-18 | A random variable is defined as the numerical outcome of a random experiment. | A random experiment repeated many times will generate results governed by their probabilities. | statistics, reminder |
| 2025-07-19 | Probability measures the _ratio_ of an outcome to the total possible outcomes. | When you want to find how likely something is, you are really asking what fraction of all possibilities does this represent? | statistics, reminder |
| 2025-07-20 | Adding random variables combines different uncertain quantities to get a new uncertain quantity. | Adding random variables represents combining their outcomes in a single experiment. | statistics, reminder |
| 2025-07-21 | A binomial distribution counts successes in $n$ independent trials, each with probability $p$. | As $n$ gets large in a binomial distribution, it approaches a normal distribution. | statistics, reminder |
| 2025-07-22 | `sudo do-release-upgrade` | Upgrade Ubuntu from the terminal; but remember to fully update the system first: `sudo apt update && sudo apt upgrade -y; sudo apt dist-upgrade -y`. | ubuntu |
| 2025-07-23 | Always keep a "live install" image lying around for when your server runs into issues! | Get a live install Debian image from https://www.debian.org/CD/live/; in case you were wondering, this is unrelated to yesterday's tip! | debian |
| 2025-07-24 | Use `getSimpleName()` to get the path name without any extension in Nextflow. | See https://nextflow.io/docs/latest/reference/stdlib-types.html for more utilities! | nextflow |
| 2025-07-25 | `sudo fsck -fy /dev/sda2` | Use `fsck` (File System Consistency Check) to scan and fix disk errors automatically. | linux, sysadmin |
| 2025-07-26 | `imap(my_list, ~ paste0("Key ", .y, " has value ", .x))` | Use `imap()` if you want both the element and its name/index. | rstats, functional programming |
| 2025-07-27 | `safe_fn <- safely(some_function)` | `safely()` wraps a function and makes it return a result even if an error occurs. Instead of stopping execution, it returns a list with the actual result or error object. | rstats, functional programming |
| 2025-07-28 | `purrr::pmap(list(list(1900), list(80), list(4)), \(x,y,z) x+y+z)` | Use `purrr::pmap()` to map over multiple input simultaneously. | rstats, functional programming |
| 2025-07-29 | Learn [Lua](https://www.lua.org/start.html)! | Lua is a powerful and fast programming language that is easy to learn and use and to embed into your application. | lua |
| 2025-07-30 | Use the [systemadmin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/systemadmin) plugin in ohmyzsh. | This plugin adds a series of aliases and functions which make a System Administrator's life easier. | ohmyzsh |
| 2025-07-31 | Check out marimo! | marimo is an open-source reactive notebook for Python - reproducible, Git-friendly, AI-native, SQL built-in, executable as a script, shareable as an app. | python |
| 2025-08-01 | Using GNU screen, `Ctrl-a [`, space, space, Esc, and then `Ctrl-a ]` to paste! | You can copy and paste from one GNU screen to another without using the mouse! | screen |
| 2025-08-02 | [Sign your Git commits](https://github.com/davetang/getting_started_with_git?tab=readme-ov-file#signing-commits) to confirm that you made the commit. | A signed commit is cryptographic proof that the commit came from you, using your GPG or SSH key. | git, github |
| 2025-08-03 | Use GPG to encrypt and decrypt files. | Some notes on using GPG on my [bioinformatics tips page](https://davetang.github.io/bioinformatics_tips/security.html). | security |
| 2025-08-04 | In `.screenrc` you can specify how many windows to create when you start `screen`! | Add `screen -t monitor 0 glances` where `monitor` is the name, `0` is the screen number, and `glances` is the command to run. Add as many entries as you need! | screen |
| 2025-08-05 | `ssh-copy-id -i ~/.ssh/id_rsa.pub username@server-ip` | Use `ssh-copy-id` to copy a public key to a server, so you can SSH using your private key. | linux |
| 2025-08-06 | Put `bindkey -v` in `~/.zshrc` to enable Zsh Vi mode! | Your Zsh shell behaves like a mini Vim editor for command-line editing! | zsh |
| 2025-08-07 | `git clone https://github.com/jeffreytse/zsh-vi-mode $ZSH_CUSTOM/plugins/zsh-vi-mode` | [zsh-vi-mode](https://github.com/jeffreytse/zsh-vi-mode) is a better and friendly vi(vim) mode plugin for Zsh. | zsh, ohmyzsh |
| 2025-08-08 | `:Gdiffsplit` | When using the vim-fugitive plugin `:Gdiffsplit` will show you the previous version in a split window! | vim |
| 2025-08-09 | Use `^` to go to the first non-blank character. | Instead of pressing `0` and `w`, just press `^` to move to the first non-blank character on the current line; great for indented code! | vim |
| 2025-08-10 | Use `zf` to fold lines and `zo` to open folded lines in Vim. | Sometimes it is useful to fold, i.e., hide, lines; use `zf` and `zo` to fold and open, respectively in Vim. | vim |
| 2025-08-11 | Use ` `` ` to move back and forth between the last jump in Vim. | Searching, marks, `gg`, and more counts as jumps. For example, after searching use ` `` ` to move back to where you were! | vim |
| 2025-08-12 | Press `Shift+Command+G` to bring up the Go To window in Finder. | At least on my computer, Finder does not have a shortcut to click on to bring me to the root directory. | macos |
| 2025-08-13 | Use `local` inside functions of shell scripts to restrict the scope! | Variables are global within a shell script unless you explicitly mark them local inside a function! | shell, scripting |
| 2025-08-14 | If you edit Markdown files using Vim, use `[[` and `]]` to jump header to header! | `[[` and `]]` are used to jump from function to function but works for headers in Markdown files! | vim, markdown |
| 2025-08-15 | Use `:reg` to view the contents of registers in Vim. | In Vim, registers are like named clipboards; after seeing the registers using `:reg`, type `"2p` to paste from the second register. | vim |
| 2025-08-16 | Use `screen -x` to attach to the same session simultaneously!! | Find the screen session using `screen -ls` then `screen -x 284771` where 284771 is the screen session ID. | screen |
| 2025-08-17 | According to Shannon, information is present whenever a signal is transmitted from one place (sender) to another (receiver). | It does not matter what kind of signal, it could be words, a picture, or even electric impulses. | information theory |
| 2025-08-18 | In Linux, `<`, `<<`, and `<<<` are redirection operators used for input handling. | `<` reads from an existing file; `<<` creates temporary multi-line input; `<<<` provides immediate string input. | linux |
| 2025-08-19 | Use a block, i.e., `{}` to group together packages to keep quiet: `suppressPackageStartupMessages({ library(ggplot2) })` | `{}` denote a block and they allow you to group multiple expressions together and treat them as a single expression. | rstats |
| 2025-08-20 | `git config --global completion.branch true` | Enable autocompletion for branch names. | git, config |
| 2025-08-21 | In GNU Make `=` is recursive/late assignment and `:=` simple/early assignment. | `=` is similar to lazy evaluation whereas `:=` is similar to eager evaluation. | make, reminder |
| 2025-08-22 | `pandoc README.md -s -o index.html -f gfm --highlight-style=pygments` | Convert a GitHub flavoured Markdown file to standalone HTML with syntax highlighting! | pandoc |
| 2025-08-23 | Use the [z](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/z) ohmyzsh plugin to access commonly visited directories. | This plugin defines the z command that tracks your most visited directories and allows you to access them with very few keystrokes. | ohmyzsh |
| 2025-08-24 | Use the [copybuffer](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/copybuffer) ohmyzsh plugin to copy the current text in the command line to the system clipboard! | Instead of using the mouse to highlight and copy text in the command line, just press `ctrl-o` with the copybuffer plugin! | ohmyzsh |
| 2025-08-25 | Use [lazy.nvim](https://github.com/folke/lazy.nvim) to manage plugins for Nvim. | Plugins add a lot more functionality into Nvim! | nvim |
| 2025-08-26 | `singularity exec my_image /bin/bash -c 'echo $SINGULARITY_NAME'` | Use `$SINGULARITY_NAME` to get the name of the Singularity image when inside a container! | singularity |
| 2025-08-27 | `build/output.txt: input.txt \| build` | Use order-only prerequisites to only make sure something exists, but do not force rebuilds if they change! | make |
| 2025-08-28 | Run GNU make with `-d` like `make -d` to get debugging information! | I spent the last hour trying to figure out why my target kept rebuilding and finally found out why with `-d`! | make |
| 2025-08-29 | `tail -f !$` | `!$` expands to the last argument of the previous command; you can even type `!$` and press tab to get the last argument! | shell, productivity |
| 2025-08-30 | Don't ignore your personal life because it affects your professional life! | I wrote a short blog post [on professionalism](https://davetang.org/muse/2025/08/30/on-professionalism/). | self-help, habits |
| 2025-08-31 | Discrete Mutual Information (DMI) measures how much information one categorical variable contains about another. | If two variables are independent, DMI = 0 (knowing one does not help you guess the other). | information theory |
| 2025-09-01 | Use [quarto-ext/lightbox](https://github.com/quarto-ext/lightbox) to create lightbox treatments for images in your HTML documents! | See the [Example Lightbox Document](https://quarto-ext.github.io/lightbox/) for a demo! | quarto |
| 2025-09-02 | `convert input.png -trim +repage output.png` | Use ImageMagick to trim the whitespace from an image; the `+repage` parameter will reset the page size. | imagemagick |
| 2025-09-03 | [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory) is the mathematical study of waiting lines, or queues. | A queueing model is constructed so that queue lengths and waiting time can be predicted. | queueing |
| 2025-09-04 | `nvim -d file1 file2` | Start Nvim in diff mode which can highlight differences between files side by side and apply changes between files! | nvim |
| 2025-09-05 | `git log -p -- file.txt` | By default, `git log` does not generate any diff output; use `-p` or `--patch` to show all changes of `file.txt`! | git |
| 2025-09-06 | Use Common Table Expressions (CTEs) (`WITH`) to simplify complex queries! | A CTE is a temporary, named result set defined at the start of a query using the `WITH` keyword; it is like creating a "virtual table" that you can reuse inside your query! | sql |
| 2025-09-07 | Press Shift+Insert to paste in MobaXTerm. | Instead of using the right mouse button to paste, use Shift+Insert to paste when using MobaXTerm! | mobaxterm |
| 2025-09-08 | `awk '$1=$1' test.txt` | AWK trick to turn one or more spaces (by default) into just one space. | awk |
| 2025-09-09 | Use the `combn()` function in base R to generate pairwise combinations | `combn()` [can also be used with a function](https://github.com/davetang/learning_r?tab=readme-ov-file#useful-tips) to apply the function across pairwise combinations! | rstats |
| 2025-09-10 | Use `(` and `)` to jump to the previous and next sentence. Use `{` and `}` for paragraphs! | If you edit written text in Vim, make sure you use `(`, `)`, `{`, and `}`! | vim |
| 2025-09-11 | After yanking a word, use `cw<C-r>0` to replace a word with the yanked word! | `<C-r>` is Control+r and `0` is register zero, which holds the text from the most recent yank. | vim |
| 2025-09-12 | Use `]c` and `[c` to jump to the next and previous hunk. Use `]d` and `[d` to jump to the next and previous diagnostic. | In Vim use `]c`, `[c`, `]d`, and `[d` to jump to hunks and diagnostics! | vim |
| 2025-09-13 | `vim.keymap.set({mode}, {lhs}, {rhs}, {opts})` | Use `vim.keymap.set()` to set key maps in Nvim. | nvim |
| 2025-09-14 | Use `:terminal` to run an interactive shell inside a Neovim buffer! | When in the terminal, hold `Ctrl`, press `\`, then `n` to go to Normal mode where you can yank stuff etc. | nvim |
| 2025-09-15 | Use [shfmt](https://github.com/mvdan/sh#shfmt) to format shell scripts consistently! | `shfmt` is a shell parser, formatter, and interpreter | shell, scripting |
| 2025-09-16 | Use the [bash-language-server](https://github.com/bash-lsp/bash-language-server) to make it easier to write Bash scripts! | A language server is a background program that provides language-specific features to your code editor. | bash, scripting |
| 2025-09-17 | If it seems too good to be true, it probably is! | In Cantonese, we say 咁大隻蛤乸隨街跳! | adage |
| 2025-09-18 | `ls tips.yaml README.md; head !*` | `$_` gets the last argument of the previous command; `!*` gets all arguments but relies on history expansion. | shell, productivity |
| 2025-09-19 | `alias diff='diff --color=always'` | Run `diff` with `--color=always` so you can see colour when piping to `less`. | shell, productivity |
| 2025-09-20 | Open files with Vim, e.g. `nvim *.yml`, and use `:n` and `:N` to navigate to the next and previous file. | The argument list is the list of files opened; use `:args` to see the files and `:n` and `:N` to navigate between them. | vim |
| 2025-09-21 | Once inside Vim, `:grep checkout **/*.yml` will create a quickfix list containing files and locations matching the grep. | The quickfix list is a special buffer in Vim that stores file positions (filename + line + column). Use it to create a list of things to fix! | vim |
| 2025-09-22 | `ls **/*.py` | Finds all files ending in `.py` in the current directory and all subdirectories (recursively)! | zsh, productivity |
| 2025-09-23 | Use the [WhichKey](https://github.com/folke/which-key.nvim) plugin to help you remember your Nvim keymaps! | WhichKey helps you remember your Neovim keymaps, by showing available keybindings in a popup as you type! | nvim, gamechanger |
| 2025-09-24 | `comm a b` | Use `comm` to compare two sorted files, showing entries that are unique and common between them. | shell, productivity |
| 2025-09-25 | `xdg-open file.pdf` | Use `xdg-open` to mimic the macOS `open` command on Debian. | shell, productivity |
| 2025-09-26 | Remember to take a holiday! | Every one needs a break! Remember to take a holiday to refresh yourself, physically and mentally. | self-help, productivity |
| 2025-09-27 | Using [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter), press `gnn` to perform incremental selection, and `grn`/`grm` to increase/decrease! | nvim-treesitter makes it easy to select different levels of nested code blocks! | nvim, gamechanger |
| 2025-09-28 | Using [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim), press `<leader>ff` to find and preview files then `<C-n>`/`<C-p>` to go to the next/previous file. | Instead of leaving Nvim to look for files, use telescope.nvim to find, preview, and open files (in a buffer)! | nvim |
| 2025-09-29 | `dplyr::rename_with(my_df, ~ gsub("\\.", "-", .x))` | Use `dplyr::rename_with()` to rename columns using a function! | dplyr, functional programming, reminder |
| 2025-09-30 | `dplyr::summarise(mtcars, dplyr::across(c(mpg, cyl), list(mean = mean, sd = sd)))` | Use `dplyr::across()` to specify columns to perform an operation on! | dplyr, reminder |
| 2025-10-01 | Use `embed-resources: true` in your Quarto files to create self contained HTML output! | Using `embed-resources: true` will produce a [standalone](https://quarto.org/docs/output-formats/html-basics.html#self-contained) HTML file with no external dependencies! | quarto |
| 2025-10-02 | Use Quarto projects to nicely organise multiple Quarto documents! | [Quarto projects](https://quarto.org/docs/projects/quarto-projects.html) provides a way to render all files with a single command, share configurations, and more! | quarto |
| 2025-10-03 | Use [gitlab-ci-local](https://github.com/firecow/gitlab-ci-local) for testing CI/CD locally! | Tired of pushing to test your .gitlab-ci.yml? Use gitlab-ci-local! | gitlab |
| 2025-10-04 | `sudo mount -t exfat /dev/sdb2 /mnt/media/data -o uid=1000,gid=1000` | When using `mount` the mountpoint and its contents are owned by root by default. Use `-o` to specify a user and group. | linux |
| 2025-10-05 | Find more positive-sum activities and engage in them, instead of zero-sum games! | [Zero-sum games](https://nonzerosum.games/whatarenonzerosumgames.html) are where two parties compete and in order for one party to win the other must lose. Positive-sum games result in win-win scenarios! | altruism |
| 2025-10-06 | Use Cohen's Kappa to measure agreement between two raters; use Fleiss' Kappa when there are more than two raters. | [Measures](https://davetang.github.io/muse/rater.html) of inter-rater reliability provide an index indicating how much agreement there is between raters, correcting for chance. | index |
| 2025-10-07 | Little by little. | When things become overwhelming, just do a little. When you don't want to practice something, just do a little. And soon, little by little, a little becomes a lot! | mantra, reminder |
| 2025-10-08 | To measure agreement between two or more raters when the ratings are continuous, use the Intraclass Correlation Coefficient (ICC). | The [ICC](https://davetang.github.io/muse/icc.html) is a descriptive statistic that measures both consistency and agreement between two or more raters that rate the same set of subjects on a continuous scale. | index |
| 2025-10-09 | The {renv} package helps you create reproducible environments for your R projects. | [Introduction to renv](https://rstudio.github.io/renv/articles/renv.html) provides a quick summary of the package. | rstats |
| 2025-10-10 | After searching in Vim, use `:%s//new_word/` to substitute it! | After searching (`/`), Vim remembers the last search pattern, so you can just use `//` without specifying the pattern! | vim |
| 2025-10-11 | `openssl enc -aes-256-cbc -pbkdf2 -salt -in file.txt -out file.txt.enc` | Use OpenSSL to encrypt files; use `-d` to decrypt the encrypted file. | security |
| 2025-10-12 | Use `docker-compose.yml` instead of remembering a long `docker run` command with many flags! | I always thought Docker Compose was for multi-containers but it is also useful for running one container; see [Compose file reference](https://docs.docker.com/reference/compose-file/). | docker |
| 2025-10-13 | A sunk cost is money, time, or resources you've already spent that you can't get back. | A sunk cost is irreversible and therefore it should not affect future decisions. Only future costs and benefits should. | economics |
| 2025-10-14 | `python3 -m venv /opt/venv && . /opt/venv/bin/activate` | To adhere to PEP 668 – Marking Python base environments as "externally managed", install packages in virtual environments even in containers. | python |
| 2025-10-15 | The {renv} package can keep a cache of R packages so you don't need to download and compile again! | See my notes on using [renv](https://davetang.github.io/learning_renv/) for more details about the package! | rstats |
| 2025-10-16 | Use the Node Version Manager to manage multiple active node.js versions. | [nvm](https://github.com/nvm-sh/nvm) allows you to quickly install and use different versions of node via the command line. | node |
| 2025-10-17 | Use Traggo to keep track of how you spend your time! | [Traggo](https://traggo.net/) is a tag-based time tracking tool that you self host giving you complete control! | productivity |
| 2025-10-18 | Successful Common-Pool Resource Management describes how communities can sustainably govern shared resources through locally developed rules, monitoring, and mutual trust. | Elinor Ostrom's work shows that with cooperation and accountability, the tragedy of the commons is not inevitable. | economics |
| 2025-10-19 | Economic scarcity is the condition in which limited resources cannot satisfy all human wants. | People make decisions under economic scarcity by weighing trade-offs, comparing the benefits and costs of each option. | economics |
| 2025-10-20 | If you select lines in Visual mode and then press `:`, Vim will insert the range for you automatically! | Instead of manually typing the range, use Visual mode to help you quickly define it! | vim |
| 2025-10-21 | In Vim, perform a substitution on the current line using `.`; then move to another line and press `@:` to repeat it! | A `.` can be used to specify the current line; `@:` will repeat the last `:` command. | vim |
| 2025-10-22 | Press `Cmd + Shift + R` to perform a hard reload of a webpage on Google Chrome. | Pressing just `Cmd + R` sometimes just reloads the cache; use `Cmd + Shift + R` to refresh without the cache. | chrome |
| 2025-10-23 | Statistical power is the probability that we will correctly reject the Null Hypothesis. | Power is the probability that a statistical test correctly rejects the null hypothesis when the alternative hypothesis is actually true. | statistics |
| 2025-10-24 | You can make UpSet plots using the {ComplexHeatmap} package in R! | The original package for making UpSet plots in R is no longer maintained; use [ComplexHeatmap](https://jokergoo.github.io/ComplexHeatmap-reference/book/upset-plot.html) instead! | rstats |
| 2025-10-25 | `aspell -c file` | Interactively check, and optionally correct, the spelling of all words in file. | productivity |
| 2025-10-26 | `spell file` | The `spell` command prints all words in `file` that are misspelled, according to its dictionary. | productivity |
| 2025-10-27 | Target triples, e.g., x86_64-unknown-linux-gnu, describe what kind of system a binary is built for. | A target triple is usually <architecture>-<vendor>-<system>-<abi>; the Application Binary Interface (ABI), usually implies the C standard library used. | productivity |
| 2025-10-28 | Use `: {tbl-colwidths="[45,55]"}` to control column widths in Quarto. | You can [explicitly specify columns widths](https://quarto.org/docs/authoring/tables.html#column-widths) using the `tbl-colwidths` attribute. | quarto |
| 2025-10-29 | A stateless container is one that does not depend on any internal, persistent data stored inside itself. | A stateless container can be destroyed and recreated at any time, and the application will continue to work correctly. | containerisation |
| 2025-10-30 | In Vim use `/search_term` to search forwards and `?search_term` to search backwards. | I got into the bad habit of just using `/` and then pressing `N` to search backwards. | vim, reminder |
| 2025-10-31 | Use the [countdown](https://github.com/gadenbuie/countdown) plugin to add a timer to Quarto presentations! | Check out the [example](https://github.com/gadenbuie/countdown/blob/main/quarto/example.qmd) to see how to use the plugin. | quarto |
| 2025-11-01 | `start <- Sys.time(); Sys.sleep(3); end <- Sys.time(); elapsed_secs <- as.numeric(difftime(end, start, units = "secs"))` | Use `difftime()` in R to calculate differences in times. | rstats, reminder |
| 2025-11-02 | Check out the [Quarto Extensions](https://quarto.org/docs/extensions/) page for useful extentions! | Extensions are a powerful way to modify and extend the behavior of Quarto. | quarto |
| 2025-11-03 | Use `vim.api.nvim_create_user_command()` to create custom Nvim commands, like one that opens a file with a list of things to practice! | I have a Markdown file of things to practice in Nvim and using `vim.api.nvim_create_user_command()` I can quickly open it! | nvim |
| 2025-11-04 | `build/output.txt: input.txt \| build` | Use an order-only prerequisite (`\|`) just to make sure something exists; no need to rebuild. | make, reminder |
| 2025-11-05 | In a Makefile it is possible to have multiple targets: `first.txt second.txt:`. The associated command/s will run once per target. | It is also possible to build multiple targets in one step using [grouped targets](https://github.com/davetang/learning_linux/blob/main/gnu_make/multi_target/Makefile). | make, reminder |
| 2025-11-06 | `possibly_read <- purrr::possibly(readr::read_csv, otherwise = NA)` | Use `purrr::possibly()` to return some default value, like NA, instead of an error! | rstats, functional programming |
| 2025-11-07 | `base::split(mtcars, ~cyl)` | `base::split()` can be used to split a data frame into a list based on a grouping! | rstats |
| 2025-11-08 | `stringr::str_extract_all(text, "(?<==)[^=]+(?==)")` | Extract content between `=` pairs using a positive lookbehind and positive lookahead! | regex |
| 2025-11-09 | `dplyr::mutate(data, prev = dplyr::lag(value), next_val = dplyr::lead(value), is_peak = value > prev & value > next_val)` | Use `lag()` and `lead()` from the {dplyr} package to easily find peaks! | dplyr |
| 2025-11-10 | `csplit tips.yaml '/- date/' '{*}'` | `csplit` can split a file based on patterns or line numbers! The example splits `tips.yaml` based on a pattern and into as many files as possible! | linux |
| 2025-11-11 | `files = glob.glob("/path/to/data/**/*.h5ad", recursive=True)` | Use the glob package in Python to list files in a way that resembles the R function `list.files()`. | python |
| 2025-11-12 | `route get 8.8.8.8` | Show how traffic to 8.8.8.8 (Google DNS) will be routed. | macos |
| 2025-11-13 | `sudo port install tesseract` and `sudo port install tesseract-eng` | Install Tesseract (Open Source OCR Engine) using MacPorts on macOS. | macos |
| 2025-11-14 | The Likelihood Ratio Test compares how well two competing models explain the observed data. | The Likelihood Ratio Test measures how much better a more complex model fits the data compared to a simpler (null) model. | statistics, reminder |
| 2025-11-15 | Use a gedankenexperiment to explore the implications of something before actually doing it. | Gedankenexperiment is German for thought experiment, which is a mental exercise where you imagine a scenario to explore its implications without actually conducting a physical experiment. | science |
| 2025-11-16 | History doesn't repeat itself, but it often rhymes. --Mark Twain | History doesn't repeat past events _exactly_, but you see similar patterns. | quotes |
| 2025-11-17 | `apt-cache depends chromium` | `apt-cache depends` lists the direct dependencies of a package showing what other packages need to be installed. | debian |
| 2025-11-18 | `ldd $(which samtools)` | `ldd $(which samtools)` shows all the shared libraries (dynamic dependencies) that `samtools` needs in order to run. | debian, reminder |
| 2025-11-19 | `file ~/bin/go-1.25.1/go/bin/go` | You can use `file` to check whether a binary is statically linked or not! | linux, reminder |
| 2025-11-20 | `dpkg -S /usr/bin/env` | Use `dpkg -S` to find which package a file belongs to! | linux, reminder |
| 2025-11-21 | `setopt extended_glob` | Use Zsh's extended globbing to allow for more additional globbing patterns. | zsh |
| 2025-11-22 | Pareto Efficiency: A state where no one can be made better off without making someone else worse off. | This represents an optimal allocation where any redistribution would benefit some only at the expense of others. | economics |
| 2025-11-23 | `git bisect` | `git bisect` is a debugging tool that uses binary search to find the exact commit that introduced a bug or broke something. | git |
| 2025-11-24 | A costly signal is the opposite of cheap talk. | A costly signal is an action or expenditure that credibly communicates information about someone's quality, commitment, or type because the signal itself is expensive to produce or maintain. | economics |
| 2025-11-25 | Opportunity cost is the value of the next best alternative you give up when you make a choice. | When you choose to do one thing, you can't do something else. The opportunity cost is what you lose by not choosing that alternative. | economics |
| 2025-11-26 | Comparative advantage is the ability to produce something at a lower opportunity cost than another producer. | If producing something costs you less (in terms of what you give up) than it costs someone else, you should specialise in that thing and trade for what you need. | economics |
| 2025-11-27 | [R-universe](https://r-universe.dev/) is rOpenSci's platform for improving publication and discovery of research software in R. | R-universe is an open platform for running personal cran-like package repositories. | rstats |
| 2025-11-28 | Use `$\|` to get all order-only prerequisites. | Order-only prerequisites are prerequisites that must exist before building a target but timestamp changes don't trigger rebuilds. | make, reminder |
| 2025-11-29 | `git checkout feature && git rebase main` | `git rebase` replays your commits on top of another branch to keep your history linear and up-to-date. | git |
| 2025-11-30 | `git revert commit_hash` | `git revert` creates a new commit that undoes the changes from a specific previous commit. | git, reminder |
| 2025-12-01 | `git diff main feature_branch` | `git diff main feature_branch` allows you to compare branches. | git, reminder |
| 2025-12-02 | An exact test computes precise probabilities by enumerating all possible outcomes rather than using approximations. | An approximation uses simpler math (like approximating with the normal distribution) that's close enough but not exact. | statistics, reminder |
| 2025-12-03 | Adverse selection occurs when information asymmetry causes markets to attract low-quality participants and repel high-quality ones. | Information asymmetry means one party knows more about the product or transaction than the other. | economics |
| 2025-12-04 | When individuals can enjoy the benefits of something without contributing to its cost, they have an incentive to free ride on others' contributions. | If everyone tries to free ride, the good may not be provided at all or will be provided at levels far below what's socially optimal. | economics |
| 2025-12-05 | `sudo nvme smart-log /dev/nvme0` | Install `nvme` using `sudo apt install nvme-cli` and use it to get NVMe statistics such as the temperature. | linux, sysadmin |
| 2025-12-06 | `quarto create-project . --type website` | Use `quarto create-project` to initialise the current directory as a Quarto website project. | quarto |
| 2025-12-07 | `hash -r` | Use `hash -r` to reset the cached command lookup table, forcing the shell to re-search your PATH next time you run a command. | linux, reminder |
| 2025-12-08 | `sudo systemctl --type=service --state=running` | List all running services only. | linux, sysadmin |
| 2025-12-09 | `sudo iotop -ao` | Use `iotop` to show which processes are using the most disk read/write. | linux, sysadmin |
| 2025-12-10 | `sudo journalctl -b -1 -r` | `journalctl -b -1 -r` shows the logs from the previous boot in reverse chronological order. | linux, sysadmin |
| 2025-12-11 | `sudo mount /dev/cdrom /media/cdrom0` | Use `sudo mount /dev/cdrom /media/cdrom0` to mount a CD-ROM. | linux, reminder |
| 2025-12-12 | `make --debug=b --dry-run` | There are various debug levels with `make`; use `--debug=b` for basic and `--debug=a` for all (most verbose). | make, reminder |
| 2025-12-13 | `mv --exchange a b` | With `mv` (GNU coreutils) 9.9 there is an `--exchange` parameter that can be used to swap files! | shell, productivity |
| 2025-12-14 | P = (s + 1)/(n + 2) | If an event has occurred s times out of n trials, the probability it occurs on the next trial is P = (s + 1)/(n + 2). | statistics |
| 2025-12-15 | Check out AkaRank, an improved Alexa Rank substitute. | [AkaRank](https://www.akamai.com/security-research/akarank) provides these critical global rank metrics to the infosec and security research community as a public service | internet |
| 2025-12-16 | Follow the two-minute rule. | The two-minute rule: if something takes less than 2 minutes, do it now rather than defer it. | productivity |
| 2025-12-17 | Use `.DELETE_ON_ERROR:` in a Makefile to automatically delete target files if recipe fails. | Make has several special targets that modify Make's behaviour such as DELETE_ON_ERROR. | make |
| 2025-12-18 | Before negotiations, research fair prices independently and don't let the first number anchor your expectations. | Anchoring bias is a cognitive bias where people rely too heavily on the first piece of information they encounter (the "anchor") when making decisions. | economics |
| 2025-12-19 | `command > all.out 2>&1` | Use `command > all.out 2>&1` as the POSIX-compliant way to redirect both STDOUT and STDERR to `all.out`. | shell, productivity |
| 2025-12-20 | `pv SRAmetadb.sqlite.gz \| md5sum` | Use `pv` to show the progress for data flowing through a pipe! | linux, gamechanger |
| 2025-12-21 | Use `:changes` to show the change history and `g;` to jump to the previous change location and `g,` to the next. | The output of `:changes` is `change`, `line`, `col`, `text`; it is useful if you make changes throughout the file. | vim |
| 2025-12-22 | `:%norm A;` | `:%norm A;` is the same as running `A;` on every line (`%`) in normal mode (`:norm`)! | vim |
| 2025-12-23 | `:.,$norm I#` | Use `:.,$norm I#` to add a `#` to the current line until the end; use `:1,.norm I# for start to current line.` | vim |
| 2025-12-24 | Data serialisation is like "packaging" data for travel. | Data serialisation is the process of converting data structures or objects from their in-memory representation into a format that can be stored or transmitted over a network and later reconstructed. | data |
| 2025-12-25 | A payload refers to the actual data or information that is being transmitted over a network or within a message. | The payload is the actual data that is separate from any metadata or headers used for managing the communication process. | data |
| 2025-12-26 | Deadweight loss is a term that economists use to mean, basically, something that destroys value in the economy, making society worse off. | Deadweight loss is an economic concept that refers to the loss of total welfare or efficiency in a market, which occurs when resources are not allocated optimally. | economics |
| 2025-12-27 | Preemptive scheduling allows interrupting running tasks; non-preemptive runs each task to completion. | The tradeoff between preemptive and non-preemptive scheduling is responsiveness versus simplicity. | scheduling |
| 2025-12-28 | Variability is the enemy. | High variance in arrival or service times increases wait times dramatically, even at the same average utilisation. | scheduling |
| 2025-12-29 | `g0` | Use `g0` to go to the first tab and `g$` to go the last tab. | vimium |
| 2025-12-30 | `X` | Use `x` to close the current tab and `X` to restore the closed tab. | vimium |
| 2025-12-31 | Make your resolutions specific and actionable rather than vague. | Specific goals are easier to track, you will know clearly whether you are succeeding, and they are more motivating because progress is visible. | self-help, reminder |
| 2026-01-01 | Don't Break the Chain. | For each day you complete your target task, mark a big X on that day and keep it going. | self-help, reminder |
| 2026-01-02 | Never Miss Twice. | The first mistake is never the one that ruins you. It is the spiral of repeated mistakes that follows. Missing once is an accident. Missing twice is the start of a new habit. | self-help, reminder |
| 2026-01-03 | The [illusion of control](https://en.wikipedia.org/wiki/Illusion_of_control) is the tendency for people to overestimate their ability to control events. | The illusion of control is the tendency for people to overestimate their ability to control events, for example, when someone feels a sense of control over outcomes that they demonstrably do not influence. | self-help |
| 2026-01-04 | A Python iterator is an object that implements `__next__()` and `__iter__()` (which returns `self`). | Note that iterators are typically exhausted after one pass-through; once you have iterated through an iterator, it is empty. | python, reminder |
| 2026-01-05 | `lambda arguments: expression` | Creates anonymous functions in Python using `lambda arguments: expression`; for example: `lambda x, y: x + y`. | python, reminder |
| 2026-01-06 | Incentives are the cornerstone of modern life. | Understanding incentives or ferreting them out is the key to solving just about any riddle. | freakonomics |
| 2026-01-07 | There are three basic flavours of incentive: economic, social, and moral. | Each type of incentive has different effects depending on the situation; sometimes social incentives are very strong and sometimes economic incentives are very weak. | freakonomics |
| 2026-01-08 | A consumable resource is a resource that Grid Engine tracks and subtracts as jobs are scheduled. | If a resource is not a consumable resource it will not be taken into account when Grid Engine schedules jobs. | sge |
| 2026-01-09 | In bioinformatics, we are often not interested in absolute gene/transcript expression levels but in relative changes. | One set of results only makes sense with respect or in contrast to another set of results! | bioinformatics, reminder |
| 2026-01-10 | `pigz --decompress --stdout --processes 4 file.gz` | Use `pigz` instead of gzip for faster compression/decompression. | shell, productivity |
| 2026-01-11 | `seqkit stats reads.fastq.gz` | SeqKit is a cross-platform and ultrafast toolkit written in Go for FASTA/Q file manipulation. | bioinformatics, reminder |
| 2026-01-12 | `ps -fp <PID>` | Get more information about a process using `ps -fp <PID>`. | shell, productivity |
| 2026-01-13 | `ge` | Use `ge` to edit the current URL and `gE` to edit and open in a new tab. | vimium |
| 2026-01-14 | Use the Feynman Technique for learning. | Choose a concept to learn; teach it to someone else; learn more if you get stuck; simplify explanations and create analogies. | self-help |
| 2026-01-15 | Always look at your data before analysing it; plots reveal what summary statistics hide. | Visualise your data early and often; patterns not seen in tables are quite obvious in plots. | analysis |
| 2026-01-16 | A dissimilarity matrix measures how different two objects are. | The lower bound of a dissimilarity matrix is always 0 and the upper bound can be unbounded or bounded (normalised). | statistics, reminder |
| 2026-01-17 | The anticipation of most types of rewards increases the level of [dopamine](https://en.wikipedia.org/wiki/Dopamine) in the brain. | In the brain, dopamine functions as a neurotransmitter, a chemical released by neurons (nerve cells) to send signals to other nerve cells. | neuroscience |
| 2026-01-18 | [While](https://pmc.ncbi.nlm.nih.gov/articles/PMC6842680/) dopamine was first synthesised in 1910, it wasn't until 1957 that dopamine was found in the human brain. | Prior to the discovery that dopamine was found in the human brain, dopamine had only been found in peripheral tissues and body fluids of mammalian animals and was assumed to be just a precursor to other catecholamines. | neuroscience |
| 2026-01-19 | `realpath --relative-to=$HOME ./README.md` | You can use `realpath` to get the full and the relative path of a file! | shell, productivity |
| 2026-01-20 | Use `fpc::cluster.stats()` to calculate an assortment of statistics that can be used to assess clustering results. | The Flexible Procedures for Clustering {fpc} R package contains various methods for clustering and cluster validation. | rstats |
| 2026-01-21 | Effect size quantifies the magnitude of a difference or relationship between variables, independent of sample size. | P-values tell you whether an effect exists and the effect size tells you how large or practically meaningful that effect is. | statistics, reminder |
| 2026-01-22 | Alpha diversity is the diversity within a single site and beta diversity is the diversity between different sites, samples, or habitats. | Examples of alpha diversity include Simpson's Index and examples of beta diversity include Bray-Curtis dissimilarity. | ecology |
| 2026-01-23 | The Horn-Morisita is a quantitative measure of similarity between two samples that accounts for species abundances. | The Horn-Morisita emphasises abundant species, is less affected by sample size and species richness, and good for abundance data. | ecology |
| 2026-01-24 | `ncdu` | Ncdu is a disk usage analyzer with an interactive text-mode user interface. | shell, productivity |
| 2026-01-25 | Moral hazard occurs when one party takes on more risk because another party bears the consequences of that risk. | A person with comprehensive car insurance might drive more recklessly because the insurance company, not them, will pay for any damage. | economics |
| 2026-01-26 | For a habit to stick, you need motivation, the ability to do the action, and a reminder or cue to do it. | Behavioural scientist BJ Fogg, founder of Stanford's Behaviour Design Lab, says when those three things come together, the behaviour happens. | self-help, habits |
| 2026-01-27 | `exists("some_var")` | Use `exists()` in R to check if a variable exists in an environment. | rstats |
| 2026-01-28 | Yank the current line into register `a` using `"ayy` and paste using `"ap`. | `"` introduces a register in Vim and the next single character is the name. | vim |
| 2026-01-29 | `sudo journalctl -f` | `sudo journalctl -f` will continuously displays new log entries as they are written. | linux, sysadmin |
| 2026-01-30 | `sudo apt-get install fail2ban` | `fail2ban` automatically blocks IP addresses that show malicious behaviour, like repeated failed login attempts. | linux, sysadmin |
| 2026-01-31 | `sudo iotop -oPa` | `sudo iotop -oPa` only show processes doing I/O, show processes (not threads), and accumulated mode to show processes since running iotop. | linux, sysadmin |
| 2026-02-01 | `:sort nu` | Use `:sort nu` to sort a file numerically and uniquely inside Vim. | vim |
| 2026-02-02 | Use sandbox mode when building Singularity images to enable experimentation before writing a definition file. | A sandbox is a writable directory structure that represents a container; sandboxes allow you to interactively modify the container's filesystem. | singularity |
| 2026-02-03 | Tacit knowledge is the dispersed, context-specific knowledge of time and place held by individuals that cannot be fully centralised or formally articulated, yet is essential for economic coordination (Hayek, 1945). | It is the local, experience-based knowledge people use in practice that markets coordinate through prices rather than through explicit instructions. | economics |
| 2026-02-04 | `ssh -o "ConnectTimeout 10"` | Use `ssh -o "ConnectTimeout 10"` to stop SSH trying to connect after 10 seconds. | shell, productivity |
| 2026-02-05 | `make.names(c("123", "1)3"))` | `make.names()` is a function in base R that can make syntactically valid names out of character vectors. | rstats |
| 2026-02-06 | `sudo apt install apache2-utils` | `apache2-utils` installs a collection of utility programs for Apache, including `htpasswd` for managing password files for basic authentication. | linux, sysadmin |
| 2026-02-07 | In Singularity, [persistent overlays](https://docs.sylabs.io/guides/latest/user-guide/persistent_overlays.html) allow you to overlay a writable file system on an immutable read-only container for the illusion of read-write access. | A persistent overlay in Singularity is a directory or file system image that “sits on top” of your immutable SIF container. | singularity |
| 2026-02-08 | `sudo journalctl -xe` | `sudo journalctl -xe` is a quick way to see the latest log messages with as much context as the system can provide; very useful as a first step when something just broke. | linux, sysadmin |
| 2026-02-09 | `pheatmap::pheatmap(my_mat, breaks=seq(-2, 2, length.out=101))`. | With {pheatmap}, when breaks do not cover the range of values, then any value higher or lower will just get the highest or lowest colour. | rstats |
| 2026-02-10 | `ssh-copy-id -i key.pub user@ipaddr` | Use `ssh-copy-id -i key.pub user@ipaddr` to easily set up SSHing with a key (instead of manually preparing `~/.ssh/authorized_keys`). | shell, productivity |
| 2026-02-11 | Use the [Quarto clean theme](https://github.com/grantmcdermott/quarto-revealjs-clean) for a minimalist and elegant presentation theme. | The clean theme provides an elegant and academic-friendly design, which looks very nice. | quarto |
| 2026-02-12 | `gosu` is a tool specifically designed for Docker containers to cleanly switch from root to another user and execute a command. | `gosu` is the standard, recommended way to drop privileges in Docker entrypoint scripts. | docker |
| 2026-02-13 | If you're using Docker and user permissions are acting strange, check whether you are using rootless mode! | Use `docker info` and under Security Options you will see "rootless" if you are using rootless mode! | docker |
| 2026-02-14 | Use `docker volume` to keep data even after you stop a container. | Containers are ephemeral but volumes are not; use `docker volume create mydata`, then mount it with `-v mydata:/data` to keep data safe across container rebuilds and restarts. | docker |
| 2026-02-15 | Use multi-stage builds to keep Docker images small. | Compile or build in one stage, then `COPY --from=builder` only the final artifacts into a minimal runtime image; this avoids shipping compilers, build tools, and intermediate files. | docker, best practice |
| 2026-02-16 | Use `define`/`endef` in GNU Make to create canned recipes for reusable command sequences. | Canned recipes let you define a sequence of commands once with `define run-tests ... endef` and reuse it across multiple rules with `$(run-tests)`, keeping your Makefile DRY. | make, productivity |
| 2026-02-17 | `docker system df` | Use `docker system df` to show Docker disk usage broken down by images, containers, volumes, and build cache; use `-v` for detailed output. | docker |
| 2026-02-18 | `sudo dmesg -T --level=err,warn` | Use `dmesg -T` for human-readable timestamps and `--level` to filter by severity; great for quickly spotting hardware or driver issues. | linux, sysadmin |
| 2026-02-19 | `sudo nvme smart-log /dev/nvme0` | Check NVMe drive health; look at `media_errors`, `percentage_used`, and `available_spare` to assess whether your drive needs replacing. | linux, sysadmin |
| 2026-02-20 | `pdftotext file.pdf file.txt` | Extracts text from a PDF and saves it to a plain text file. Install via `sudo apt install poppler-utils` on Debian/Ubuntu). | linux, productivity |
| 2026-02-21 | `flock -n /tmp/myjob.lock ./myjob.sh` | Runs `myjob.sh` only if no other instance is running; `-n` exits immediately if the lock is already held rather than waiting. The lock is kernel-level, not file-existence-based, so it is released automatically when the process ends - no cleanup needed. | linux, shell, scripting |
