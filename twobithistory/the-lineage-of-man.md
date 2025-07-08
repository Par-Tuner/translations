# Man 的血脉

*2017 年 9 月 28 日*

我一直觉得 man 手册页 (man pages) 很有意思。它们格式奇特，主要通过终端 (terminal) 访问，总让我感觉像是远古时代的遗物。有些 man 手册页可能 *确实* 很古老：我很想知道，自从 Unix 早期以来，`cat` 或 `tee` 的 man 手册页被修订过多少次，但我敢打赌次数肯定不多。Man 手册页充满了神秘感——它们从何而来，在你的电脑上住在哪里，或者以何种文件类型存储，这些都不那么显而易见——然而，很难相信如此基础且明显受严格规范约束的东西，竟然能如此深不可测。Man 手册页的这些约定俗成是从哪里来的？它们又是在哪里被编纂成文的？如果我想自己写一个 man 手册页，该从何入手呢？

`man` 命令的故事与 Unix 的发展史密不可分。Unix 的第一个版本于 1971 年完成，但当时只在贝尔实验室 (Bell Labs) 内部使用，并没有提供 `man` 命令。然而，时任计算技术研究部负责人并管理 Unix 项目的 Douglas McIlroy 坚持认为，必须提供某种形式的文档 [^1]。他敦促通常被认为是 Unix 创造者的两位程序员 Ken Thompson 和 Dennis Ritchie 编写了一些文档。最终成果便是 [第一版](https://www.bell-labs.com/usr/dmr/www/1stEdman.html) 的《Unix 程序员手册》(Unix Programmer’s Manual)。

《Unix 程序员手册》的第一版由（实体的！）纸质页面组成，这些页面被收集在一个活页夹中。它只记录了 61 个不同的命令，以及几十个系统调用和一些库例程。尽管 `man` 命令本身要到后来才出现，但《Unix 程序员手册》的第一版确立了许多 man 手册页至今仍在遵循的约定，即便当时还没有官方规范。每个命令的文档都包含了众所周知的 NAME（名称）、SYNOPSIS（概要）、DESCRIPTION（描述）和 SEE ALSO（参见）等标题。可选的标志 (flags) 用方括号括起来，元参数 (meta-arguments)（例如，需要文件路径时用“file”表示）则带有下划线。该手册还确立了规范的手册章节，例如用于通用命令的第 1 节、用于系统调用的第 2 节等等；这些章节在当时仅仅是一份很长的打印文档中的不同部分。Thompson 和 Ritchie 当时可能并不知道，他们正在开创一个将延续数十年的传统，但他们确实做到了。

McIlroy 后来推测了 man 手册页格式为何能延续如此之久的原因。在一份关于 Unix 概念发展的技术报告中，他指出，最初的 man 手册页以“简洁却非正式的散文风格”编写，这种风格加上信息的字母顺序排列，“促进了准确的在线文档编写” [^2]。他补充说，man 手册页的格式“深受需要查找事实的入门者欢迎，尽管有时会让不知道该查找哪些事实的初学者感到沮丧”，这暗示了所有程序员都曾有过的 man 手册页使用体验。McIlroy 强调的是教程 (tutorial) 和参考 (reference) 之间有时会被忽视的区别；man 手册页可能不太适合作为教程，但它们是完美的参考资料。

到《Unix 程序员手册》的 [第二版](http://bitsavers.informatik.uni-stuttgart.de/pdf/att/unix/2nd_Edition/UNIX_Programmers_Manual_2ed_Jun72.pdf) 付印时，`man` 命令已经成为 Unix 的一部分。它使得整个手册可以“在线”访问，这意味着可以交互式地使用，这被认为极其有用。`man` 命令在第二版中拥有自己的手册页（这个页面就是最初的 `man man`），其中解释说 `man` 可以用来“run off a particular section of this manual”（运行本手册的特定章节）。在最初的 Unix 大师们看来，“run off”这个词既指打印文档的物理行为，也指他们用来排版 (typeset) 文档的程序 `roff`。`roff` 程序在《Unix 程序员手册》的第一版和第二版印刷前都被用于排版，但现在它也被 `man` 用来在显示 man 手册页之前进行处理。Man 手册页本身则以一种旨在被 `roff` 读取的文件格式存储在每个 Unix 系统上。

`roff` 是一个漫长排版程序 (typesetting programs) 系列中的第一个，这些程序一直被用于格式化 man 手册页。它自身的发展可以追溯到 20 世纪 60 年代中期编写的一个名为 `RUNOFF` 的程序。在贝尔实验室 (Bell Labs)，`roff` 催生了几个后继者，包括 `nroff` (en-roff) 和 `troff` (tee-roff)。`nroff` 旨在改进 `roff` 并更好地将文本输出到终端，而 `troff` 则解决了使用 CAT 照相排版机 (phototypesetter) 进行打印的问题。（如果你像我一样不知道什么是照相排版，我推荐你观看 [这部](https://vimeo.com/127605644) 非常值得一看的影片。）所有这些程序都基于一种标记语言 (markup language)，这种语言由插入在文档每行开头的两个字母命令组成。这些命令可以控制字体大小、文本定位、行间距等。如今，`roff` 系统最常见的实现是 `groff`，它是 GNU 项目的一部分。

只要看看你电脑上存储的一些 man 手册页，就能很容易地了解 `roff` 输入文件是什么样子。至少在基于 BSD 的系统，例如 MacOS 上，你可以使用 `man` 的 `--path` 参数来查找特定命令的 man 手册页存储在哪里。通常，这会在 `/usr/share/man` 或 `/usr/local/share/man` 目录下。通过这种方式使用 `man`，你可以找到 `man` 命令自身的手册页路径，然后用文本编辑器打开它。它看起来会和你平时用 `man` 命令看到的样子完全不同。在我的系统上，前几十行是：

```
.TH man 1 "September 19, 2005"
.LO 1
.SH NAME
man \- format and display the on-line manual pages
.SH SYNOPSIS
.B man
.RB [ \-acdfFhkKtwW ]
.RB [ --path ]
.RB [ \-m
.IR system ]
.RB [ \-p
.IR string ]
.RB [ \-C
.IR config_file ]
.RB [ \-M
.IR pathlist ]
.RB [ \-P
.IR pager ]
.RB [ \-B
.IR browser ]
.RB [ \-H
.IR htmlpager ]
.RB [ \-S
.IR section_list ]
.RI [ section ]
.I "name ..."

.SH DESCRIPTION
.B man
formats and displays the on-line manual pages.  If you specify
.IR section ,
.B man
only looks in that section of the manual.
.I name
is normally the name of the manual page, which is typically the name
of a command, function, or file.
However, if
.I name
contains a slash
.RB ( / )
then
.B man
interprets it as a file specification, so that you can do
.B "man ./foo.5"
or even
.B "man /cd/foo/bar.1.gz\fR.\fP"
.PP
See below for a description of where
.B man
looks for the manual page files.

```

例如，你可以看出所有章节标题都以 `.SH` 开头，所有应该显示为粗体的文本都以 `.B` 开头。这些命令是专门为编写 man 手册页而设计的 `roff` 宏 (macros)。这里使用的宏是名为 `man` 的软件包的一部分，但也有其他软件包，例如 `mdoc`，你可以用于相同的目的。这些宏使得编写 man 手册页比没有它们时简单得多。它们还通过始终编译成同一组低级 `roff` 命令来强制保持一致性。`man` 和 `mdoc` 软件包现在分别在 [GROFF_MAN(7)](http://man7.org/linux/man-pages/man7/groff_man.7.html) 和 [GROFF_MDOC(7)](http://man7.org/linux/man-pages/man7/groff_mdoc.7.html) 中有文档说明。

整个 `roff` 系统让人联想到 LaTeX，这是另一种如今更受欢迎的排版工具。LaTeX 本质上是建立在 Donald Knuth 设计的核心 TeX 系统之上的一大堆宏。与 `roff` 类似，还有许多其他宏包可以整合到你的 LaTeX 文档中。这些宏包意味着你几乎不需要自己编写原始的 TeX 代码。LaTeX 在许多领域已经取代了 `roff`，但它不适合为终端格式化文本，所以没有人用它来编写 man 手册页。

如果你今天（2017 年）要编写一个 man 手册页，你会怎么做呢？你当然 *可以* 使用 `man` 或 `mdoc` 这样的 `roff` 宏包来编写 man 手册页。它的语法虽然不熟悉且笨重，但这些宏抽象掉了大量的复杂性，让你无需学习太多命令就能编写出相当完整的 man 手册页。话虽如此，现在还有其他值得考虑的选项。

[Pandoc](http://pandoc.org/) 是一个广泛使用的软件工具，用于将文档从一种格式转换为另一种格式。你可以使用 Pandoc 将 Markdown 文件转换为基于 `man` 宏的 man 手册页，这意味着你现在可以用像 Markdown 这样简单直观的语言来编写 man 手册页。Pandoc 支持比大多数 Markdown 转换器更多的 Markdown 结构，为你提供了多种格式化 man 手册页的方式。虽然这种便利性会牺牲一些控制权，但你不太可能需要深入到 `roff` 宏层面才能实现的功能。如果你好奇这些 Markdown 文件可能是什么样子，我为我创建的一个用于记录不同命令行工具使用方法的工具，[编写了一些](https://github.com/sinclairtarget/um/tree/02365bd0c0a229efb936b3d6234294e512e8a218/doc) 自己的文档。NPM 的 [文档](https://github.com/npm/npm/blob/20589f4b028d3e8a617800ac6289d27f39e548e8/doc/cli/npm.md) 也是用 Markdown 编写的，然后转换为 `roff` man 格式，不过他们使用的是一个名为 [marked-man](https://www.npmjs.com/package/marked-man) 的 JavaScript 包来完成转换，而不是 Pandoc。

所以现在有多种编写 man 手册页的方法，让你有很大的自由度来选择你认为最好的工具。话虽如此，你最好确保你的 man 手册页 *读起来就像所有其他已编写的 man 手册页一样*。尽管现在工具链有了很大的灵活性，但 man 手册页的约定仍然一如既往地强大。你可能会想完全跳过编写 man 手册页——毕竟，你可能已经在网上有了文档，或者你只想依赖 `--help` 标志——但你将放弃 man 手册页所能提供的那份庄重感。Man 手册页是一个不太可能很快消失或演变的制度，这很有趣，因为我们有很多方法可以做得更好。XML 在我 [上一篇文章](https://twobithistory.org/2017/09/21/the-rise-and-rise-of-json.html) 中表现不佳，但它在这里将是完美的格式，它将允许我们做一些类似查询 `man` 关于某个选项的事情：

```
$ man grep -v
Selected lines are those not matching any of the specified patterns.

```

想象一下！但似乎我们都太习惯 man 手册页现在的样子了。在一个快速变化是常态的领域，也许一些稳定性——特别是在我们遇到困惑和不解时都会求助的文档系统中——是一件好事。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

[^1]: [https://truss.works/blog/2016/12/9/man-splained](https://truss.works/blog/2016/12/9/man-splained)
[^2]: [http://www.cs.dartmouth.edu/~doug/reader.pdf](http://www.cs.dartmouth.edu/~doug/reader.pdf)