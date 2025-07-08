# `cat` 命令的“身世之谜”

*2018 年 11 月 12 日*

我曾与我的大家庭成员争论过，计算机科学学位是否值得一读。当时我还在上大学，正纠结于是否要主修计算机科学。我的姑姑和一位表亲认为我不应该。他们承认编程技能确实有用且能带来丰厚收入，但他们争辩说，计算机科学领域发展如此迅速，以至于我所学的一切几乎会立刻过时。他们觉得，最好是业余时间学习编程，而主修经济学或物理学等领域，因为这些领域的基本原理将终身适用。

我知道我的姑姑和表亲错了，所以我决定主修计算机科学。（抱歉了，姑姑和表亲！）普通人可能会认为计算机科学领域或软件工程这样的职业每隔几年就会彻底革新，这很容易理解。我们先有了个人电脑，然后是互联网，接着是手机，再后来是机器学习……技术总是在变化，所以其底层原理和技术也必然随之改变。然而，令人惊奇的是，实际变化却微乎其微。我相信，大多数人都会惊讶地发现他们电脑上一些重要软件的实际“年龄”。我说的不是那些华丽的应用软件——我的 Firefox 浏览器（我电脑上可能用得最多的程序）甚至还不到两周大。但是，如果你打开像 `grep` 这样的命令的手册页，你会发现它自 2010 年以来就没有更新过（至少在 MacOS 上是这样）。而 `grep` 的最初版本写于 1974 年，那在计算世界里，简直是恐龙漫步硅谷的时代。然而，人们（和程序）至今每天仍然依赖 `grep`。

我的姑姑和表亲把计算机技术想象成一系列越来越精巧的沙堡，每次潮水退去后，新的沙堡就会取代旧的。但现实是，至少在许多领域，我们稳步积累那些已经解决问题的程序。我们可能需要偶尔修改这些程序以避免“软件腐烂” (software rot)，但除此之外，它们可以保持不变。`grep` 是一个简单的程序，它解决了一个至今仍然相关的问题，所以它得以存活。大多数应用程序编程都是在非常高的层次上完成的，它建立在一个由更古老代码组成的金字塔之上，这些代码解决了更古老的问题。三四十年前的思想和概念，远非今日的过时之物，在许多情况下已经体现在你笔记本电脑上仍然安装的软件中。

我觉得，看看这样一个老程序，并了解它自首次编写以来发生了多少变化，会很有趣。`cat` 也许是所有 Unix 工具中最简单的一个，所以我就用它作为例子。Ken Thompson 在 1969 年编写了 `cat` 的最初实现。如果我告诉别人我的电脑上有一个 1969 年的程序，这准确吗？几十年来，`cat` 究竟演变了多少？我们电脑上的软件到底有多老？

多亏了像 [这个](https://github.com/dspinellis/unix-history-repo) 这样的代码库，我们才能准确地看到 `cat` 自 1969 年以来的演变过程。我将重点关注那些作为我 MacBook 上 `cat` 实现“祖先”的版本。你会看到，当我们追溯 `cat` 从最初的 Unix 版本到今天 MacOS 中的 `cat` 时，这个程序被重写了不止一次——但它最终的工作方式与五十年前大同小异。

## 研究型 Unix (Research Unix)

Ken Thompson 和 Dennis Ritchie 开始在 PDP 7 上编写 Unix。那是在 1969 年，C 语言尚未问世，所以早期的 Unix 软件都是用 PDP 7 汇编语言编写的。他们使用的汇编语言版本是 Unix 独有的，因为 Ken Thompson 编写了自己的汇编器，在 DEC（PDP 7 的制造商）提供的汇编器基础上增加了一些功能。Thompson 所做的更改都记录在 [最初的 Unix 程序员手册](https://www.bell-labs.com/usr/dmr/www/man11.pdf) 中，位于 `as`（汇编器）的条目下。

因此，`cat` 的 [第一个实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-1-cat-pdp7-s) 是用 PDP 7 汇编语言编写的。我添加了注释，试图解释每条指令的作用，但除非你了解 Thompson 在编写汇编器时所做的一些扩展，否则这个程序仍然难以理解。其中有两个重要的扩展。首先，分号 (`;`) 字符可以用来在同一行上分隔多个语句。这似乎最常用于将系统调用参数放在与 `sys` 指令同一行。其次，Thompson 添加了对使用数字 0 到 9 的“临时标签” (temporary labels) 的支持。这些标签可以在整个程序中重复使用，因此根据 Unix 程序员手册的说法，它们“既减轻了程序员的想象力负担，也减少了汇编器的符号空间占用。”从任何给定的指令，你可以分别使用 `nf` 和 `nb` 来引用下一个或最近的临时标签 `n`。例如，如果你在标记为 `1:` 的代码块中有一些代码，你可以通过使用指令 `jmp 1b` 从更下方跳回该块。（但你不能在上方不使用 `jmp 1f` 的情况下 *向前* 跳到该块。）

这个 `cat` 第一个版本最有趣的地方在于它包含了两个我们应该认识的名字。有一个标记为 `getc` 的指令块和一个标记为 `putc` 的指令块，这表明这些名字比 C 标准库 (C standard library) 还要古老。`cat` 的第一个版本实际上包含了这两个函数的实现。这些实现缓冲了输入，这样读写就不是一次一个字符地进行。

`cat` 的第一个版本并没有持续多久。Ken Thompson 和 Dennis Ritchie 说服贝尔实验室 (Bell Labs) 给他们买了一台 PDP 11，这样他们就可以继续扩展和改进 Unix。PDP 11 有一个不同的指令集，所以 `cat` 必须重写。我也为 `cat` 的 [第二个版本](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-2-cat-pdp11-s) 添加了注释。它使用了新的汇编器助记符来适应新的指令集，并利用了 PDP 11 的各种 [寻址模式](https://en.wikipedia.org/wiki/PDP-11_architecture#Addressing_modes)。（如果你对源代码中的括号和美元符号感到困惑，它们是用来指示不同的寻址模式的。）但它也像 `cat` 的第一个版本一样，利用了分号 (`;`) 字符和临时标签，这意味着当 `as` 适应 PDP 11 时，这些功能一定得到了保留。

`cat` 的第二个版本比第一个版本简单得多。它也更“Unix 化”，因为它不只是期望一个文件名参数列表——当没有给出参数时，它会从标准输入 (stdin) 读取，这正是 `cat` 至今仍在做的事情。你也可以给这个版本的 `cat` 一个参数 `-` 来指示它应该从标准输入 (stdin) 读取。

1973 年，为了发布 Unix 第四版，大部分 Unix 代码都用 C 语言重写了。但 `cat` 似乎直到那之后一段时间才用 C 语言重写。`cat` 的 [第一个 C 语言实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-3-cat-v7-c) 只出现在 Unix 第七版中。这个实现看起来非常有趣，因为它太简单了。在所有后续的实现中，这个版本最像 K&R C 中作为教学演示的理想化 `cat`。程序的核心是经典的“两行代码”：

```c
while ((c = getc(fi)) != EOF) // 循环读取文件直到文件结束
    putchar(c); // 将读取到的字符输出
```

当然，代码远不止这些，但额外的代码主要是为了确保你不会同时读写同一个文件。另一个值得注意的有趣之处是，这个 `cat` 实现只识别一个标志，即 `-u`。`-u` 标志可以用来避免输入和输出的缓冲，否则 `cat` 会以 512 字节的块进行缓冲。

## BSD

第七版之后，Unix 催生了各种衍生版本和分支。MacOS 构建在 Darwin 之上，而 Darwin 又源自伯克利软件发行版 (Berkeley Software Distribution, BSD)，所以 BSD 是我们最感兴趣的 Unix 分支。BSD 最初只是 Unix 的一系列实用程序和附加组件，但它最终成为一个完整的操作系统。BSD 似乎一直依赖于最初的 `cat` 实现，直到第四个 BSD 版本，即 4BSD，才添加了对一系列新标志的支持。`cat` 的 [4BSD 实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-4-cat-bsd4-c) 显然源自最初的实现，尽管它添加了一个新函数来实现由新标志触发的行为。文件中已有的命名约定得到了遵守——用于标记输入是来自标准输入 (stdin) 还是文件的 `fflg` 变量，又加入了 `nflg`、`bflg`、`vflg`、`sflg`、`eflg` 和 `tflg`，所有这些都用于记录程序调用时是否提供了每个新标志。这些是 `cat` 最后添加的命令行标志；`cat` 的手册页 (man page) 今天仍然列出这些标志，没有其他（至少在 Mac OS 上是这样）。4BSD 发布于 1980 年，所以这组标志已经有 38 年的历史了。

`cat` 为 BSD Net/2 进行了最后一次彻底重写。BSD Net/2 的目的之一是通过用新代码替换所有源自 AT&T Unix 的代码来避免许可问题。BSD Net/2 于 1991 年发布。`cat` 的这次最终重写是由 Kevin Fall 完成的，他于 1988 年从伯克利毕业，并在接下来的一年里在计算机系统研究组 (Computer Systems Research Group, CSRG) 担任工作人员。Fall 告诉我，CSRG 的墙上贴出了一份仍然使用 AT&T 代码实现的 Unix 工具列表，工作人员被告知选择他们想要重新实现的工具。Fall 选择了 `cat` 和 `mknod`。今天 MacOS 中捆绑的 `cat` 实现就是从一个源文件构建的，该文件的顶部仍然标有他的名字。他的 `cat` 版本，尽管是一个相对简单的程序，如今却被数百万人使用。

Fall 的 [最初实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-5-cat-net2-c) 比我们目前看到的任何版本都要长得多。除了支持 `-?` 帮助标志外，它没有增加任何新功能。概念上，它与 4BSD 的实现非常相似。它之所以更长，是因为 Fall 将实现分为“原始”模式 (raw mode) 和“处理”模式 (cooked mode)。“原始”模式是经典的 `cat`；它逐字符打印文件。“处理”模式是带有所有 4BSD 命令行选项的 `cat`。这种区分是合理的，但它也使得实现看起来比实际更复杂。文件末尾还有一个精巧的错误处理函数，进一步增加了它的长度。

## MacOS

2001 年，苹果公司 (Apple) 推出了 Mac OS X。这次发布对苹果公司来说意义重大，因为苹果公司多年来一直试图取代其现有操作系统（经典 Mac OS），但都未能成功，而经典 Mac OS 早已显露出老态。之前曾两次尝试在内部创建新操作系统，但都无疾而终；最终，苹果公司收购了史蒂夫·乔布斯 (Steve Jobs) 的公司 NeXT，该公司开发了一个名为 NeXTSTEP 的操作系统和面向对象编程框架。苹果公司以 NeXTSTEP 为基础开发了 Mac OS X。NeXTSTEP 部分基于 BSD 构建，因此以 NeXTSTEP 作为 Mac OS X 的起点，将源自 BSD 的代码直接带入了苹果生态系统的核心。

因此，Mac OS X 的第一个版本包含了从 NetBSD 项目中提取的 `cat` [实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-6-cat-macosx-c)。NetBSD 至今仍在开发中，它最初是 386BSD 的一个分支 (fork)，而 386BSD 又直接基于 BSD Net/2。所以 Mac OS X 的第一个 `cat` 实现 *就是* Kevin Fall 的 `cat`。在这十年间唯一的变化是，Fall 的错误处理函数 `err()` 被移除，取而代之的是 `err.h` 提供的 `err()` 函数。`err.h` 是 C 标准库 (C standard library) 的一个 BSD 扩展。

NetBSD 的 `cat` 实现后来被 FreeBSD 的 `cat` 实现替换。 [根据维基百科 (Wikipedia) 的说法](https://en.wikipedia.org/wiki/Darwin_(operating_system))，苹果公司 (Apple) 在 Mac OS X 10.3 (Panther) 中开始使用 FreeBSD 而非 NetBSD。但根据苹果公司自己的开源发布，Mac OS X 的 `cat` 实现直到 2007 年 Mac OS X 10.5 (Leopard) 发布才被替换。苹果公司为 Leopard 版本替换的 [FreeBSD 实现](https://gist.github.com/sinclairtarget/47143ba52b9d9e360d8db3762ee0cbf5#file-7-cat-macos-10-13-c) 与今天苹果电脑上使用的实现相同。截至 2018 年，该实现自 2007 年以来从未更新或更改。

所以 Mac OS 的 `cat` 很老了。事实上，它比它在 Mac OS X 中 2007 年的出现所暗示的还要早两年。 [2005 年的这次更改](https://github.com/freebsd/freebsd/commit/a76898b84970888a6fd015e15721f65815ea119a#diff-6e405d5ab5b47ca2a131ac7955e5a16b)，在 FreeBSD 的 Github 镜像中可见，是苹果公司 (Apple) 将其引入 Mac OS X 之前，FreeBSD 的 `cat` 所做的最后一次更改。因此，Mac OS X 的 `cat` 实现，由于没有与 FreeBSD 的 `cat` 实现保持同步，官方“年龄”为 13 岁。关于软件需要改变多少才算作是“同一个软件”的问题，还有更大的争论空间；在这种情况下，源文件自 2005 年以来 *完全没有改变*。

Mac OS 今天使用的 `cat` 实现与 Fall 为 1991 年 BSD Net/2 版本编写的实现没有太大不同。最大的区别是添加了一个全新的函数来提供 Unix 域套接字 (Unix domain socket) 支持。在某个时候，一位 FreeBSD 开发者似乎还决定将 Fall 的 `raw_args()` 函数和 `cook_args()` 合并为一个名为 `scanfiles()` 的函数。除此之外，程序的核心仍然是 Fall 的代码。

我问 Fall，对于他编写的 `cat` 实现如今被数百万苹果用户直接或间接通过依赖 `cat` 存在的程序使用，他有何感受。Fall 如今是一名顾问，也是最新版《TCP/IP 详解》(TCP/IP Illustrated) 的合著者，他说当人们得知他在 `cat` 上的工作时如此兴奋，他感到很惊讶。Fall 在计算领域有着漫长的职业生涯，并参与了许多备受瞩目的项目，但似乎许多人仍然对他 1989 年重写 `cat` 所投入的六个月工作最感兴趣。

## 百年老程序

从宏观角度来看，计算机并不是一项古老的发明。我们习惯了百年老照片，甚至是百年历史的摄像片段。但计算机程序属于不同的范畴——它们是高科技且新颖的。至少，现在是这样。随着计算行业成熟，我们有一天会发现自己使用的程序接近百年历史吗？

计算机硬件大概会发生足够大的变化，以至于我们无法将今天编译的可执行文件在百年后的硬件上运行。也许编程语言设计方面的进步也可能意味着未来没有人会理解 C 语言，而 `cat` 也早已用另一种语言重写。（尽管 C 语言已经存在了五十年，而且看起来短期内不会被取代。）但抛开所有这些不谈，为什么不永远使用我们现有的 `cat` 呢？

我认为 `cat` 的历史表明，计算机科学 (computer science) 中的一些思想实际上非常持久。事实上，对于 `cat` 来说，思想和程序本身都很古老。说我电脑上的 `cat` 来自 1969 年可能不准确。但我可以说我电脑上的 `cat` 来自 1989 年，那时 Fall 编写了他的 `cat` 实现。许多其他软件也同样古老。所以，也许我们不应该将计算机科学和软件开发主要视为颠覆现状和创造新事物的领域。我们的计算机系统是由历史遗迹构建而成的。在某个时候，我们可能花更多时间理解和维护这些历史遗迹，而不是编写新代码。

*如果你喜欢这篇文章，每四周会有更多类似的文章发布！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> My post on Lisp. It's basically a long explanation of that xkcd comic where Lisp is the key to understanding the structure of the universe. When and why did people start talking about Lisp that way?
>
> Would love to know if your theories differ from mine!<https://t.co/yHF3CxG7oN>
>
> — TwoBitHistory (@TwoBitHistory) [October 15, 2018](https://twitter.com/TwoBitHistory/status/1051826516844322821?ref_src=twsrc%5Etfw)