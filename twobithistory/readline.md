# 你可能不知道的 GNU Readline

*2019 年 8 月 22 日*

我有时会把我的电脑想象成一座巨大的房子。我每天都会拜访这座房子，熟悉大部分一楼的房间，但有些卧室我从未踏足，有些壁橱我从未打开，还有一些角落和缝隙我从未探索过。我感到有必要更多地了解我的电脑，就像任何人都会想去看看自己家里从未去过的房间一样。

GNU Readline 是一个默默无闻的小型软件库，我多年来一直依赖它，却从未意识到它的存在。成千上万的人可能每天都在使用它，却从未察觉。如果你使用 Bash shell，那么每次你自动补全文件名、在单行输入文本中移动光标，或者搜索你之前的命令历史时，你都在使用 GNU Readline。当你使用 Postgres 的命令行界面 ( `psql` ) 或 Ruby 的 REPL ( `irb` ) 执行同样的操作时，你同样在使用 GNU Readline。许多软件都依赖 GNU Readline 库来实现用户期望的功能，但这些功能是如此辅助性且不引人注目，以至于我猜想很少有人会停下来思考它们从何而来。

GNU Readline 最初由自由软件基金会 ( Free Software Foundation ) 在 20 世纪 80 年代创建。如今，它已成为每个人计算基础设施中一个重要但又“隐形”的部分，由一位志愿者独自维护。

## 功能丰富

GNU Readline 库的主要作用是为任何命令行界面增强一套通用的按键操作，让你可以在单行输入中移动和编辑文本。例如，如果你在 Bash 提示符下按下 `Ctrl-A`，光标会跳到行首；而按下 `Ctrl-E` 则会跳到行尾。另一个有用的命令是 `Ctrl-U`，它会删除光标前行的所有内容。

在很长一段时间里，我曾尴尬地通过反复敲击方向键来在命令行中移动。不知为何，我从未想过会有更快的方法。当然，熟悉 Vim 或 Emacs 等文本编辑器的程序员不会长时间屈尊使用方向键，所以像 Readline 这样的工具注定会被创造出来。使用 Readline，你不仅可以跳来跳去，还可以像使用文本编辑器一样编辑单行文本。它有删除单词、调换单词、将单词转换为大写、复制粘贴字符等命令。事实上，Readline 的大部分按键操作/快捷方式都基于 Emacs。Readline 本质上就是单行文本的 Emacs。你甚至可以录制和回放宏。

我从未使用过 Emacs，所以很难记住所有不同的 Readline 命令。但 Readline 有一个非常酷的功能，那就是你可以切换到基于 Vim 的模式。要在 Bash 中实现这一点，你可以使用内置的 `set` 命令。以下命令会告诉 Readline 为当前 shell 使用 Vim 风格的命令：

```
$ set -o vi
```

启用此选项后，你可以使用 `dw` 等命令删除单词。Emacs 模式下 `Ctrl-U` 的等效命令是 `d0`。

当我第一次了解到这个功能时，我非常兴奋地尝试了它，但我发现它对我来说效果不佳。我很高兴有这个对 Vim 用户的让步，你可能比我更幸运，特别是如果你还没有习惯 Readline 的默认命令按键。我的问题是，当我听说基于 Vim 的界面时，我已经学会了几个 Readline 按键。即使启用了 Vim 选项，我还是会不小心使用默认按键。此外，如果没有某种指示器，Vim 的模式设计在这里显得很笨拙——你很容易忘记自己处于哪种模式。所以我发现自己陷入了一种尴尬的境地：我的文本编辑器是 Vim，但 Readline 命令却是 Emacs 风格的。我怀疑很多人也处于同样的情况。

如果你觉得 Vim 和 Emacs 的键盘命令系统都古怪且晦涩难懂，这并非不合理，你可以自定义 Readline 的按键绑定，让它们变成你喜欢的样子。这并不难。Readline 在启动时会读取一个 `~/.inputrc` 文件，该文件可用于配置各种选项和按键绑定。我做的一件事是重新配置了 `Ctrl-K`。通常它会删除从光标到行尾的内容，但我很少这样做。所以我把它绑定为按下 `Ctrl-K` 会删除整行，无论光标在哪里。我是通过在 `~/.inputrc` 中添加以下内容来实现的：

```
Control-k: kill-whole-line
```

每个 Readline 命令 ( 文档中称它们为 *函数* ) 都有一个名称，你可以通过这种方式将其与按键序列关联起来。如果你在 Vim 中编辑 `~/.inputrc`，你会发现 Vim 知道文件类型，并且会通过高亮显示有效的函数名来帮助你，而不会高亮显示无效的函数名！

你还可以使用 `~/.inputrc` 来创建预设宏，方法是将按键序列映射到输入字符串。 [Readline 手册](https://tiswww.case.edu/php/chet/readline/readline.html) 提供了一个我认为特别有用的例子。我经常需要将程序的输出保存到文件中，这意味着我经常在 Bash 命令后附加类似 `> output.txt` 的内容。为了节省时间，你可以将其设置为 Readline 宏：

```
Control-o: "> output.txt"
```

现在，每当你按下 `Ctrl-O` 时，你就会看到 `> output.txt` 出现在命令行光标之后。真棒！

但宏的作用远不止为文本字符串创建快捷方式。 `~/.inputrc` 中的以下条目意味着，每当我按下 `Ctrl-J` 时，行上已有的任何文本都会被 `$(` 和 `)` 包裹。该宏会通过 `Ctrl-A` 移动到行首，添加 `$(`，然后通过 `Ctrl-E` 移动到行尾并添加 `)`：

```
Control-j: "\C-a$(\C-e)"
```

如果你经常需要将一个命令的输出用作另一个命令的输入，这可能会很有用，例如：

```
$ cd $(brew --prefix)
```

`~/.inputrc` 文件还允许你为 Readline 手册中称为 *变量* 的内容设置不同的值。这些变量可以启用或禁用某些 Readline 行为。你可以使用这些变量来改变，例如，Readline 自动补全的工作方式或 Readline 历史搜索的工作方式。我建议开启的一个变量是 `revert-all-at-newline` 变量，它默认是关闭的。当该变量关闭时，如果你使用反向搜索功能从命令历史中拉取一行，对其进行编辑，但随后决定搜索另一行，你所做的编辑会保留在历史中。我发现这很令人困惑，因为它会导致你的 Bash 命令历史中出现你从未实际运行过的行。所以，将以下内容添加到你的 `~/.inputrc` 中：

```
set revert-all-at-newline on
```

当你使用 `~/.inputrc` 设置选项或按键绑定时，它们会应用于所有使用 Readline 库的地方。这最明显地包括 Bash，但你也会在 `irb` 和 `psql` 等其他程序中受益于你的更改！一个插入 `SELECT * FROM` 的 Readline 宏，如果你经常使用关系型数据库 ( relational database ) 的命令行界面，可能会非常有用。

## Chet Ramey

GNU Readline 目前由 Chet Ramey 维护，他是凯斯西储大学 ( Case Western Reserve University ) 的高级技术架构师。Ramey 也维护着 Bash shell。这两个项目最初都由自由软件基金会的一名员工 Brian Fox 于 1988 年开始编写。但自 1994 年左右以来，Ramey 一直是唯一的维护者。

Ramey 通过电子邮件告诉我，Readline 远非一个原创想法，它的创建是为了实现 POSIX 规范所规定的功能，该规范在 20 世纪 80 年代末刚刚诞生。许多早期的 shell，包括 Korn shell 和至少一个版本的 Unix System V shell，都包含了行编辑功能。1988 年版的 Korn shell ( `ksh88` ) 提供了 Emacs 风格和 Vi/Vim 风格的编辑模式。据我从 [手册页](https://web.archive.org/web/20151105130220/http://www2.research.att.com/sw/download/man/man1/ksh88.html) 所知，Korn shell 会通过查看 `VISUAL` 和 `EDITOR` 环境变量来决定你想要使用哪种模式，这非常巧妙。POSIX 中规定 shell 功能的部分是紧密模仿 `ksh88` 的，因此 GNU Bash 必须实现一个类似灵活的行编辑系统才能保持兼容。Readline 因此应运而生。

当 Ramey 第一次参与 Bash 开发时，Readline 是 Bash 项目目录中的一个单一源文件。它实际上只是 Bash 的一部分。随着时间的推移，Readline 文件慢慢地朝着成为一个独立项目发展，但直到 1994 年 ( 随着 Readline 2.0 版本的发布 )，Readline 才完全成为一个独立的库。

Readline 与 Bash 紧密相关，Ramey 通常将 Readline 的发布与 Bash 的发布同步。但正如我上面提到的，Readline 是一个可以被任何实现命令行界面的软件使用的库。而且它真的非常容易使用。这是一个简单的例子，但这里展示了你如何在自己的 C 程序中使用 Readline。 `readline()` 函数的字符串参数是你希望 Readline 向用户显示的提示符：

```c
#include <stdio.h> // 标准输入/输出库
#include <stdlib.h> // 通用工具标准库
#include "readline/readline.h" // Readline 库头文件

int main(int argc, char** argv)
{
    char* line = readline("my-rl-example> "); // 读取一行用户输入，并显示自定义提示符
    printf("You entered: \"%s\"\n", line); // 打印输入的行

    free(line); // 释放 readline() 分配的内存

    return 0; // 表示程序成功执行
}
```

你的程序将控制权交给 Readline，Readline 负责从用户那里获取一行输入 ( 以允许用户执行所有高级行编辑操作的方式 )。一旦用户实际提交了该行，Readline 就会将其返回给你。我能够通过链接 Readline 库来编译上述代码，这个库显然在我的某个库搜索路径中，通过调用以下命令：

```
$ gcc main.c -lreadline
```

当然，Readline 的 API ( 应用程序编程接口 ) 远比这一个函数丰富得多，任何使用它的人都可以调整该库的各种行为。库用户甚至可以添加新功能，供终端用户通过 `~/.inputrc` 进行配置，这意味着 Readline 非常容易扩展。但据我所知，即使是 Bash 最终也调用了简单的 `readline()` 函数来获取输入，就像上面的例子一样，尽管在此之前有很多配置。( 请参阅 GNU Bash 源代码中的 [这一行](https://github.com/bminor/bash/blob/9f597fd10993313262cab400bf3c46ffb3f6fd1e/parse.y#L1487)，这似乎是 Bash 将获取输入的责任交给 Readline 的地方。)

Ramey 至今已在 Bash 和 Readline 上工作了十多年。他从未因其工作获得过报酬——他现在是，也一直是一名志愿者。Bash 和 Readline 仍在积极开发中，尽管 Ramey 表示 Readline 的变化比 Bash 慢得多。我问 Ramey 独自维护如此多人使用的软件是何感受。他说，数百万人可能在不知不觉中使用 Bash ( 因为每台 Apple 设备都运行 Bash )，这让他担心一个破坏性变更可能造成多大的干扰。但他已经慢慢习惯了有那么多人使用他的软件这个事实。他说他继续在 Bash 和 Readline 上工作，因为目前他投入很深，而且他只是喜欢向世界提供有用的软件。

*你可以在 Chet Ramey 的 [网站](https://tiswww.case.edu/php/chet/) 上找到更多信息。*

*如果你喜欢这篇文章，每四周会有更多类似的文章发布！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> 请欣赏我迟来的新文章，其中我以 BBC Micro 和计算机扫盲计划的故事为引子，来吐槽 Codecademy。<https://t.co/PiWKLjDjK>
>
> — TwoBitHistory (@TwoBitHistory) [2019 年 3 月 31 日](https://twitter.com/TwoBitHistory/status/1112492084383092738?ref_src=twsrc%5Etfw)