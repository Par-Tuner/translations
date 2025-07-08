# Vim 从何而来

2018 年 8 月 5 日

我最近偶然发现了一种名为 Intel HEX 的文件格式。据我所知，Intel HEX 文件（使用 `.hex` 扩展名）旨在通过将二进制图像编码为十六进制数字行，使其内容更易读。显然，它们被那些编程微控制器或需要将数据烧录到只读存储器 (ROM) 中的人使用。无论如何，当我第一次在 Vim 中打开一个 HEX 文件时，我发现了一些令人震惊的事情。这种文件格式，至少对我来说，是极其深奥的，但 Vim 竟然对它了如指掌。HEX 文件的每一行都是一个记录，分为不同的字段——Vim 竟然自动给每个字段都涂上了不同的颜色。我敬畏地问道：`set ft?`。Vim 胜利地回答：`filetype=hex`。

Vim 无处不在。它被如此多的人使用，以至于支持 Intel HEX 文件这样的功能不应该令人惊讶。Vim 预装在 Mac OS 上，并在 Linux 世界拥有大量拥趸。即使是那些讨厌它的人也对它很熟悉，因为许多流行的命令行工具默认会将用户带入 Vim，以至于新手被困在 Vim 中已经成为一个 [梗](https://stackoverflow.blog/wp-content/uploads/2017/05/meme.jpeg)。一些主要网站，包括 Facebook，当你按下 `j` 键时会向下滚动，按下 `k` 键时会向上滚动——这成了 Vim 在数字文化中广泛传播的一个奇特标志。

然而，Vim 也是一个谜。例如，与人尽皆知由 Facebook 开发和维护的 React 不同，Vim 没有明显的赞助商。尽管它无处不在且举足轻重，但似乎没有任何委员会或组织来决定 Vim 的发展方向。你可以在 [Vim 网站](https://www.vim.org/) 上花几分钟时间，但仍然无法更好地了解是谁创建了 Vim 或其背后的原因。如果你在不指定文件参数的情况下启动 Vim，你会看到 Vim 的启动信息，上面写着 Vim 是由“Bram Moolenaar 等人”开发的。但这并没有告诉你太多。Bram Moolenaar 究竟是谁，他的那些神秘同伙又是谁呢？

也许更重要的是，当我们提出这些问题时，为什么退出 Vim 需要输入 `:wq`？当然，它是“写入”操作后跟“退出”操作的组合，但这并不是一个特别直观的约定。谁决定复制文本应该被称为“yanking”（拽取）？为什么 `:%s/foo/bar/gc` 是“查找和替换”的缩写？Vim 的这些独特之处似乎过于随意，不像是凭空捏造的，那么它们到底是从哪里来的呢？

答案，正如通常情况一样，始于那个古老的计算熔炉——贝尔实验室 (Bell Labs)。从某种意义上说，Vim 只是一个软件的最新迭代——我们可以称之为“wq 文本编辑器”——它自 Unix 时代黎明以来一直在不断开发和改进。

## 肯·汤普森 (Ken Thompson) 编写行编辑器

1966 年，贝尔实验室 (Bell Labs) 雇佣了肯·汤普森 (Ken Thompson)。汤普森刚在加州大学伯克利分校 (University of California, Berkeley) 完成电气工程和计算机科学硕士学位。在那里，他使用了一个名为 QED 的文本编辑器，该编辑器是为伯克利分时系统 (Berkeley Timesharing System) 在 1965 年至 1966 年间编写的。[^1] 汤普森抵达贝尔实验室后做的第一件事之一就是为麻省理工学院兼容分时系统 (MIT Compatible Time-Sharing System) 重写 QED。他后来又为 Multics 项目编写了另一个版本的 QED。在此过程中，他扩展了该程序，以便用户可以使用正则表达式 (regular expressions) 搜索文件中的行并进行替换。[^2]

Multics 项目，像伯克利分时系统 (Berkeley Timesharing System) 一样，旨在创建一个商业上可行的分时操作系统，是麻省理工学院 (MIT)、通用电气 (General Electric) 和贝尔实验室 (Bell Labs) 之间的合作项目。AT&T 最终认为该项目没有前途并退出了。汤普森和贝尔实验室的同事丹尼斯·里奇 (Dennis Ritchie)，现在无法访问分时系统，并且怀念这种系统提供的“交互式计算的感觉”，于是着手创建他们自己的版本，该版本最终被称为 Unix。[^3] 1969 年 8 月，当他的妻子和年幼的儿子在加利福尼亚度假时，汤普森组装了新系统的基本组件，为“操作系统、Shell、编辑器和汇编器各分配了一周时间。”[^4]

该编辑器将被命名为 `ed`。它基于 QED，但并非完全重新实现。汤普森决定放弃 QED 的某些功能。正则表达式支持被削减，以便只理解相对简单的正则表达式。QED 允许用户通过打开多个缓冲区同时编辑多个文件，但 `ed` 一次只能处理一个缓冲区。而且，QED 可以执行包含命令的缓冲区，但 `ed` 不会这样做。这些简化可能是必要的。丹尼斯·里奇 (Dennis Ritchie) 曾表示，没有 QED 的高级正则表达式“损失不大”。[^5]

`ed` 现在是 POSIX 规范的一部分，所以如果你有一个符合 POSIX 规范的系统，你的电脑上就会安装它。它值得一试，因为许多 `ed` 命令今天仍然是 Vim 的一部分。例如，为了将缓冲区写入磁盘，你必须使用 `w` 命令。为了退出编辑器，你必须使用 `q` 命令。这两个命令可以同时在同一行上指定——因此，就有了 `wq`。像 Vim 一样，`ed` 是一个模式编辑器 (modal editor)；要从命令模式进入输入模式，你可以使用插入命令 (`i`)、追加命令 (`a`) 或更改命令 (`c`)，具体取决于你如何尝试转换文本。`ed` 还引入了 `s/foo/bar/g` 语法用于查找和替换，或“替换”文本。

鉴于所有这些相似之处，你可能会期望普通的 Vim 用户在使用 `ed` 时不会遇到麻烦。但 `ed` 在另一个重要方面与 Vim 完全不同。`ed` 是一个真正的行编辑器。它是在电传打字机 (teletype printer) 时代编写并广泛使用的。当肯·汤普森 (Ken Thompson) 和丹尼斯·里奇 (Dennis Ritchie) 在 Unix 上辛勤工作时，他们看起来是这样的：

![肯·汤普森 (Ken Thompson) 通过电传打字机与 PDP-11 交互。](https://upload.wikimedia.org/wikipedia/commons/8/8f/Ken_Thompson_%28sitting%29_and_Dennis_Ritchie_at_PDP-11_%282876612463%29.jpg)

`ed` 不允许你在打开的缓冲区中原地编辑行，或移动光标，因为每次你对其进行更改时，`ed` 都必须重新打印整个文件。1969 年，`ed` 没有“清除”屏幕内容的机制，因为屏幕只是一张纸，所有已经输出的内容都已用墨水输出。必要时，你可以使用列表命令 (`l`) 要求 `ed` 为你打印出一定范围的行，但大多数时候你都在操作你看不到的文本。因此，使用 `ed` 有点像在一个漆黑的房子里用一个电量不足的手电筒摸索。你一次只能看到这么多，所以你必须尽力记住所有东西在哪里。

以下是一个 `ed` 会话的示例。我添加了注释（在 `#` 字符之后）解释每行的目的，尽管如果这些注释实际输入，`ed` 不会将其识别为注释并会报错：

```
[sinclairtarget 09:49 ~]$ ed
i                           # 进入输入模式
Hello world!

Isn't it a nice day?
.                           # 结束输入
1,2l                        # 列出第 1 到第 2 行
Hello world!$
$
2d                          # 删除第 2 行
,l                          # 列出整个缓冲区
Hello world!$
Isn't it a nice day?$
s/nice/terrible/g           # 全局替换
,l
Hello world!$
Isn't it a terrible day?$
w foo.txt                   # 写入 foo.txt
38                          # (写入的字节数)
q                           # 退出
[sinclairtarget 10:50 ~]$ cat foo.txt
Hello world!
Isn't it a terrible day?

```

如你所见，`ed` 不是一个特别“健谈”的程序。

## 比尔·乔伊 (Bill Joy) 编写文本编辑器

`ed` 对汤普森 (Thompson) 和里奇 (Ritchie) 来说足够好用。但其他人发现它难以使用，并因此获得了 Unix 对新手特别不友好的恶名。[^6] 1975 年，一位名叫乔治·库鲁里斯 (George Coulouris) 的人在伦敦玛丽女王学院 (Queen Mary’s College) 安装的 Unix 系统上开发了一个改进版的 `ed`。库鲁里斯编写他的编辑器是为了利用他在玛丽女王学院可用的视频显示器。与 `ed` 不同，库鲁里斯的程序允许用户在屏幕上原地编辑单行，逐个按键地在行中导航（想象一下一次只在 Vim 中编辑一行）。库鲁里斯将他的程序命名为 `em`，或“凡人编辑器 (editor for mortals)”，据说这是在汤普森 (Thompson) 访问玛丽女王学院，看到库鲁里斯构建的程序后，不屑一顾地说他编辑文件时不需要看到文件状态，从而启发了他。[^7]

1976 年，库鲁里斯 (Coulouris) 将 `em` 带到加州大学伯克利分校 (UC Berkeley)，在那里他作为计算机科学系 (CS department) 的访问学者度过了夏天。这正好是肯·汤普森 (Ken Thompson) 离开伯克利去贝尔实验室 (Bell Labs) 工作十年后。在伯克利，库鲁里斯遇到了比尔·乔伊 (Bill Joy)，他是一名研究生，正在开发伯克利软件发行版 (Berkeley Software Distribution, BSD)。库鲁里斯向乔伊展示了 `em`，乔伊以库鲁里斯的源代码为起点，构建了一个改进版的 `ed`，名为 `ex`，意为“扩展的 `ed`”。`ex` 的 1.1 版本随 1978 年 BSD Unix 的首次发布一起捆绑。`ex` 大致与 `ed` 兼容，但它增加了两种模式：一种是“开放”模式 (open mode)，它实现了像 `em` 那样的单行编辑；另一种是“可视化”模式 (visual mode)，它占据了整个屏幕，并实现了我们今天习惯的整个文件的实时编辑。

1979 年 BSD 的第二个版本发布时，引入了一个名为 `vi` 的可执行文件，它所做的不过是在可视化模式下打开 `ex`。[^8]

`ex`/`vi`（此后简称 `vi`）确立了我们现在与 Vim 相关的大部分约定，这些约定并非 `ed` 已有的。乔伊 (Joy) 使用的视频终端是 Lear Siegler ADM-3A，它的键盘没有光标键。相反，箭头被画在 `h`、`j`、`k` 和 `l` 键上，这就是乔伊在 `vi` 中使用这些键进行光标移动的原因。ADM-3A 键盘上的 Esc 键也位于我们今天会找到 Tab 键的位置，这解释了为什么这样一个难以触及的键会被分配给像退出模式这样常见的操作。命令前缀的 `:` 字符也来自 `vi`，它在常规模式（即运行 `ex` 进入的模式）下使用 `:` 作为提示符。这解决了 `ed` 的一个长期抱怨，即 `ed` 一旦启动，就会以完全的沉默迎接用户。在可视化模式下，保存和退出现在需要输入经典的 `:wq`。“Yanking”（拽取）和“putting”（放置）、标记 (marks) 以及用于设置选项的 `set` 命令都是原始 `vi` 的一部分。我们今天在 Vim 中进行基本文本编辑时使用的功能，大部分都是 `vi` 的功能。

![Lear Siegler ADM-3A 键盘。](https://vintagecomputer.ca/wp-content/uploads/2015/01/LSI-ADM3A-full-keyboard.jpg)

`vi` 是 BSD Unix 捆绑的唯一文本编辑器，除了 `ed`。当时，Emacs 可能要花费数百美元（这在 GNU Emacs 出现之前），所以 `vi` 变得非常流行。但 `vi` 是 `ed` 的直系后代，这意味着如果没有 AT&T 的源代码许可证，就无法修改源代码。这促使一些人创建了 `vi` 的开源版本。STEVIE (ST Editor for VI Enthusiasts) 于 1987 年出现，Elvis 于 1990 年出现，而 `nvi` 则于 1994 年出现。其中一些克隆版本增加了额外的功能，如语法高亮 (syntax highlighting) 和分屏 (split windows)。特别是 Elvis，它的许多功能被整合到 Vim 中，因为许多 Elvis 用户都强烈要求将其包含在内。[^9]

## 布拉姆·穆勒纳尔 (Bram Moolenaar) 编写 Vim

“Vim”，现在是“Vi Improved”（Vi 改进版）的缩写，最初代表“Vi Imitation”（Vi 模仿版）。像许多其他 `vi` 克隆一样，Vim 最初是为了在一个没有 `vi` 的平台上复制 `vi` 而尝试的。布拉姆·穆勒纳尔 (Bram Moolenaar)，一位在荷兰芬洛 (Venlo) 一家复印机公司工作的荷兰软件工程师，希望为他全新的 Amiga 2000 拥有一个类似 `vi` 的东西。穆勒纳尔已经习惯了在他大学的 Unix 系统上使用 `vi`，现在它已经“在他指尖”。[^10] 所以在 1988 年，穆勒纳尔以现有的 STEVIE `vi` 克隆为起点，开始开发 Vim。

穆勒纳尔 (Moolenaar) 能够接触到 STEVIE，因为 STEVIE 之前曾出现在一种名为 Fred Fish 磁盘的东西上。弗雷德·菲什 (Fred Fish) 是一位美国程序员，他每月都会邮寄一张软盘，其中精选了 Amiga 平台上最好的开源软件。任何人都可以免费索取磁盘，只需支付邮费。STEVIE 的几个版本都在 Fred Fish 磁盘上发布。穆勒纳尔使用的版本是在 Fred Fish 磁盘 256 上发布的。[^11]（令人失望的是，Fred Fish 磁盘似乎与 [Freddi Fish](https://en.wikipedia.org/wiki/Freddi_Fish) 没有任何关系。）

穆勒纳尔 (Moolenaar) 喜欢 STEVIE，但很快注意到缺少许多 `vi` 命令。[^12] 因此，在 Vim 的第一个版本中，穆勒纳尔将 `vi` 兼容性作为他的首要任务。其他人编写了一系列 `vi` 宏，当通过一个正确兼容 `vi` 的编辑器运行时，可以解决一个 [随机生成的迷宫](https://github.com/isaacs/.vim/tree/master/macros/maze)。穆勒纳尔成功地让这些宏在 Vim 中工作。1991 年，Vim 首次在 Fred Fish 磁盘 591 上发布，名为“Vi Imitation”。[^13] 穆勒纳尔添加了一些功能（包括多级撤销 (multi-level undo) 和用于编译器错误的“quickfix”模式），这意味着 Vim 已经超越了 `vi`。但 Vim 将一直保持“Vi Imitation”的名称，直到 1993 年通过 FTP 发布的 Vim 2.0。

穆勒纳尔 (Moolenaar) 在各种互联网合作者的偶尔帮助下，稳步地为 Vim 添加功能。Vim 2.0 引入了对 `wrap` 选项和长文本行水平滚动的支持。Vim 3.0 增加了对分屏和缓冲区的支持，这一功能灵感来自 `vi` 克隆 `nvi`。Vim 现在还将每个缓冲区保存到交换文件 (swap file) 中，以便编辑的文本可以在崩溃后幸存。Vimscript 首次出现在 Vim 5.0 中，同时支持语法高亮。与此同时，Vim 的受欢迎程度不断增长。它被移植到 MS-DOS、Windows、Mac，甚至 Unix，在那里它与原始的 `vi` 竞争。

2006 年，Vim 被《Linux Journal》读者评选为最受欢迎的编辑器。[^14] 今天，根据 Stack Overflow 2018 年开发者调查，Vim 是最受欢迎的文本模式（即终端模拟器）编辑器，被 25.8% 的所有软件开发者（以及 40% 的系统管理员/DevOps 人员）使用。[^15] 在一段时间内，在 1980 年代后期和整个 1990 年代，程序员们发动了“编辑器大战 (Editor Wars)”，Emacs 用户与 `vi`（最终是 Vim）用户相互对抗。虽然 Emacs 当然仍然有追随者，但有些人认为编辑器大战已经结束，Vim 赢了。[^16] 2018 年 Stack Overflow 开发者调查表明这是真的；只有 4.1% 的受访者使用 Emacs。

Vim 是如何取得如此成功的？显然，人们喜欢 Vim 提供给他们的功能。但我认为，Vim 背后的悠久历史表明，它不仅仅拥有其功能集所带来的优势。Vim 的代码库只追溯到 1988 年，当时穆勒纳尔 (Moolenaar) 开始开发它。而“wq 文本编辑器”——关于 Unix 风格文本编辑器应如何工作的更广阔愿景——则可以追溯到半个世纪前。“wq 文本编辑器”有几种不同的具体表现形式，但部分归功于比尔·乔伊 (Bill Joy) 和布拉姆·穆勒纳尔 (Bram Moolenaar) 对向后兼容性 (backward compatibility) 的异常关注，好的想法随着时间的推移逐渐积累。从这个意义上说，“wq 文本编辑器”是运行时间最长、最成功的开源项目之一，它得到了计算界一些最伟大思想的贡献。我不认为“初创公司抛弃所有先例并创造颠覆性新软件”的开发方法一定是坏事，但 Vim 提醒我们，协作和增量的方法也能创造奇迹。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> 新文章！这次我们来看看 Altair 8800，第一台家用电脑，以及如何在你的现代电脑上模拟它。<https://t.co/s2sB5njrkd>
>
> — TwoBitHistory (@TwoBitHistory) [2018 年 7 月 22 日](https://twitter.com/TwoBitHistory/status/1021058552352387074?ref_src=twsrc%5Etfw)

---

[^1]: 巴特勒·兰普森 (Butler Lampson)，《系统》，巴特勒·兰普森，访问日期：2018 年 8 月 5 日，<http://bwlampson.site/Systems.htm>。
[^2]: 丹尼斯·里奇 (Dennis Ritchie)，《QED 编辑器不完全历史》，访问日期：2018 年 8 月 5 日，[https://www.bell-labs.com/usr/dmr/www/qed.html](https://www.bell-labs.com/usr/dmr/www/qed.html)。
[^3]: 彼得·萨卢斯 (Peter Salus)，《守护进程、GNU 和企鹅》，Groklaw，2005 年 4 月 14 日，访问日期：2018 年 8 月 5 日，[http://www.groklaw.net/article.php?story=20050414215646742](http://www.groklaw.net/article.php?story=20050414215646742)。
[^4]: 同上。
[^5]: 丹尼斯·里奇 (Dennis Ritchie)，《QED 编辑器不完全历史》，访问日期：2018 年 8 月 5 日，[https://www.bell-labs.com/usr/dmr/www/qed.html](https://www.bell-labs.com/usr/dmr/www/qed.html)。
[^6]: 唐纳德·诺曼 (Donald Norman)，《关于 Unix 的真相：用户界面糟糕透顶》，Datamation，访问日期：2018 年 8 月 5 日，<http://www.ceri.memphis.edu/people/smalley/ESCI7205_misc_files/The_truth_about_Unix_cleaned.pdf>。
[^7]: 乔治·库鲁里斯 (George Coulouris)，《乔治·库鲁里斯：一段历史》，乔治·库鲁里斯个人主页，1998 年 9 月，访问日期：2018 年 8 月 5 日，[http://www.eecs.qmul.ac.uk/~gc/history/index.html](http://www.eecs.qmul.ac.uk/~gc/history/index.html)。
[^8]: 《第二版伯克利软件发行版手册》，Roguelife，访问日期：2018 年 8 月 5 日，[http://roguelife.org/~fujita/COOKIES/HISTORY/2BSD/vi.u.html](http://roguelife.org/~fujita/COOKIES/HISTORY/2BSD/vi.u.html)。
[^9]: 斯文·古克斯 (Sven Guckes)，《VIM 愿望清单》，Vmunix，1995 年 5 月 15 日，访问日期：2018 年 8 月 5 日，<https://web.archive.org/web/20080520075925/http://www.vmunix.com/vim/wish.html>。
[^10]: 布拉姆·穆勒纳尔 (Bram Moolenaar)，《Vim 25》（讲座，苏黎世，2016 年 11 月 2 日），2016 年 12 月 13 日，访问日期：2018 年 8 月 5 日，[https://www.youtube.com/watch?v=ayc_qpB-93o&t=4m58s](https://www.youtube.com/watch?v=ayc_qpB-93o&t=4m58s)
[^11]: 同上。 (?t=6m15s)
[^12]: 同上。 (?t=7m6s)
[^13]: 《Fish 磁盘 1 - 1120》，Amiga Stuff，访问日期：2018 年 8 月 5 日，[http://www.amiga-stuff.com/pd/fish.html](http://www.amiga-stuff.com/pd/fish.html)。
[^14]: 《2005 年 Linux Journal 读者选择奖》，Linux Journal，2005 年 9 月 28 日，访问日期：2018 年 8 月 5 日，[https://www.linuxjournal.com/article/8520#N0x850cd80.0x87983bc](https://www.linuxjournal.com/article/8520#N0x850cd80.0x87983bc)。
[^15]: 《Stack Overflow 2018 年开发者调查》，Stack Overflow，访问日期：2018 年 8 月 5 日，[https://insights.stackoverflow.com/survey/2018/#development-environments-and-tools](https://insights.stackoverflow.com/survey/2018/#development-environments-and-tools)。
[^16]: 布鲁斯·拜菲尔德 (Bruce Byfield)，《编辑器大战的终结》，Linux Magazine，2015 年 5 月 11 日，访问日期：2018 年 8 月 5 日，[http://www.linux-magazine.com/Online/Blogs/Off-the-Beat-Bruce-Byfield-s-Blog/The-End-of-the-Editor-Wars](http://www.linux-magazine.com/Online/Blogs/Off-the-Beat-Bruce-Byfield-s-Blog/The-End-of-the-Editor-Wars)。