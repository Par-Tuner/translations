# Vim 的诞生
原文：[Where Vim Came From](https://twobithistory.org/2018/08/05/where-vim-came-from.html)

我最近偶然发现了一个名为 Intel HEX 的文件格式。据我所收集，Intel HEX 文件（使用 `.hex` 扩展名）是为了使二值图像更透明，通过将它们编码为一行一行的十六进制数字。显然它们被为单片机编程或需要将数据烧录进 ROM 的人们所使用。无论如何，当我第一次在 Vim 中打开一个 HEX 文件时，我发现了一些令人震惊的事。这个文件格式——至少对我来说——非常难懂，但 Vim 已经知道了关于它的一切。HEX 文件的每一行都是一个被分为不同字段的记录——Vim 已经继续向前并为每一字段着色。我敬畏地问道，`set ft?`。`filetype=hex`，Vim 得意洋洋地回答。

Vim 无处不在。他被无数人使用，因此对 HEX 文件的支持并不令人意外。Vim 在 Mac OS 上被预装，且在 Linux 世界有着大批拥趸。甚至讨厌它的人也对其非常熟悉，因为有充足的命令行工具会默认将用户扔向 Vim，以至于被困在 Vim 中的新手已经成为了[一个梗](https://stackoverflow.blog/wp-content/uploads/2017/05/meme.jpeg)。较多的网站，包括 Facebook，会在你按 `j` 键时向下滚动，按 `k` 键时向上——Vim 在数字文化中奇迹般的高水准传播。

然而 Vim 还是一个谜。不像 React，每个人都知道它被 Facebook 开发与维护，Vim 并没有明显的赞助者。任凭其普遍性与重要性，仍没有任何形式的委员会或组织机构为 Vim 做决定。你可以花费几分钟在 [Vim 官网](https://www.vim.org/) 上闲逛，却不会在谁创造了 Vim 或为何上得到更好的信息。如果你径直打开 Vim，不加文件参数，然后你会看到 Vim 的启动信息，称 Vim 被“Bram Moolenaar 等人”开发。但这并没有告诉你太多。谁是 Bram Moolenaar，谁又是他暗中的盟友？

可能更重要的是，当我们在问问题时，为什么退出 Vim 需要键入 `:wq`？当然，这是一个“写入”操作，其后是“退出”操作，但这并不是一个特别直观的约定。又是谁决定复制文本应被称为“yanking”？（译注：在 Emacs 中，"yanking" 代表的是粘贴（或者说，重新插入刚才删掉的内容），而并不是复制。）为什么 `:%s/foo/bar/gc` 是“查找并替换”的简称？Vim 的特质看起来太武断了，但它们又从何而来呢？

答案是，正如常出现的那样，这些开始于古老的计算机熔炉，贝尔实验室。某种意义上，Vim 仅是一个软件作品——称之为“wq 文本编辑器”——最新的迭代。这个软件自 Unix 纪元的黎明开始就不断地被开发与改进。

## Ken Thompson 写了一个行编辑器

1966 年，贝尔实验室雇佣了 Ken Thompson。Thompson 刚在加州大学伯克利分校完成了电子工程与计算机科学方向的硕士学位。在那里时，他用过一个名为 QED 的文本编辑器，这个编辑器在 1965 年与 1966 年之间为伯克利分时系统而写。[^1] Thompson 在到达贝尔实验室后做的第一件事之一便是为 MIT 相容分时系统重写了 QED。后来他会为 Multics 计划写了另一个版本的 QED。一路上，他扩展了程序以使得用户能够在一个文件中能够搜索行，及使用正则表达式进行替换。[^2]

Multics 计划，与伯克利分时系统相似，寻求于创造一个商业上可行的分时操作系统，是 MIT，通用电气及贝尔实验室间的合作产物。AT&T 最终导致这个计划停滞不前并退出。Thompson 与同事贝尔实验室研究员 Dennis Ritchie，现在没有了对一个分时系统的权限，失去了系统所提供的“交互式计算的感觉”，便着手开始制作他们自己的版本——最终会闻名为 Unix。[^3] 1969 年八月，在他的妻子与儿子在加利福尼亚度假时，Thompson 将新系统的基本组件组合在了一起，分别分配了“一个星期给操作系统、shell、编辑器、及汇编器。”[^4]

这个编辑器会被叫做 `ed`。它基于 QED 但并不是一个精确的重新实现。Thompson 决定抛弃某些 QED 功能。正则表达式的支持被削减所以只有相对简单的正则表达式才会被理解。QED 通过打开多个缓冲区允许用户同时编辑几个文件，但 `ed` 一次只能对一个缓冲区工作。尽管 QED 能执行一个包含命令的缓冲区，`ed` 却不能这么做。这些简化可能是被要求的。Dennis Ritchie 曾说没有 QED 的高级正则表达式是“不大的损失”。[^5]

`ed` 现在是 POSIX 标准的一部分，所以如果你有一个 POSIX 兼容的系统，它已经安装在你的电脑上了。它值得玩一玩，因为 `ed ` 的许多命令现在是 Vim 的一部分。例如，为了将缓冲区写入磁盘，你需要使用 `w` 命令。为了退出编辑器，你需要使用命令 `q`。这两个命令能在一行中同时被指定——也就是 `wq`。如同 Vim，`ed` 是一个模式编辑器；为了从命令模式进入输入模式你需要使用插入命令(`i`)，附加命令(`a`)，或是更改命令(`c`)，取决于你想对文本做些什么。`ed` 同样引进了 `s/foo/bar/g` 格式来查找与替换，或称“取代”文本。

鉴于这些相似之处，你可能会认为普通的 Vim 用户使用 `ed` 没有任何问题。但在另一个重要的方面，`ed` 与 Vim 不尽相同。`ed` 是一个真正的行编辑器。它在电传打字机时代被写下并被广泛使用。当 Ken Thompson 与 Dennis Ritchie 正忙碌于 Unix 时，他们看起来像是这样：

![Ken_Thompson_(sitting)_and_Dennis_Ritchie_at_PDP-11_(2876612463).jpg](https://s1.ax1x.com/2018/10/17/idh2qI.jpg)

`ed` 不允许你在打开的缓冲区里的其他行中编辑恰当的行，或者是移动光标，因为每当你改变了文件，`ed` 会必须重印整个文件。1969 年并没有让 `ed`“清除”屏幕上内容的机制，因为屏幕其实仅仅是一张纸，输出的所有东西都已经被墨水印到了纸上。如有必要，你可以使用列出命令(`l`)让 `ed` 为你打印出一行行内容，但大多数时间你都在操控着你不能看见的文本。因此使用 `ed` 就像是在一个昏暗的房子里用着一个几乎没电的手电筒，尝试着找对路。你一次能看到如此多东西，所以你必须尽你所能来记住一切都在哪里。

下面是一个 `ed` 会话的例子。我已经添加了注释（在 `#` 标记之后）来解释每行的用途，尽管 `ed` 并不会将输入的这些识别为注释且会报错：

```
[sinclairtarget 09:49 ~]$ ed
i                           # 进入输入模式
Hello world!

Isn't it a nice day?
.                           # 结束输入
1,2l                        # 列出1、2行
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

正如你所见到的，`ed` 并不是一个特别健谈的程序。

## Bill Joy 写了一个文本编辑器

`ed` 对 Thompson 和 Ritchie 来说完全够用。其他人则认为其难于使用，并且它成为了 Unix 对新手的敌意的一个臭名昭著的例子。[^6] 1975 年，一个名叫 George Coulouris 的男人在伦敦玛丽王后大学的 Unix 系统上开发了 `ed` 的一个改进版本。Coulouris 写了他的编辑器是为了利用他在伦敦玛丽王后大学能获得的视频显示。不像 `ed`，Coulouris 的程序允许用户编辑屏幕上恰当的一行，通过一下下的击键来在行间移动（想象下你在一次只在一行里使用 Vim）。Coulouris 称他的程序为 `em`，或称"editor for mortals（模式编辑器）"，这可能是他被启发这么做于 Thompson 造访伦敦玛丽王后大学，见了 Coulouris 所写的程序并驳斥之称他不需要在编辑一个文件时查看它的状态之后。

1976 年，Coulouris 带着 `em` 到了加州大学伯克利分校，他在那里作为计算机科学系的访问者待了一整个夏天。这刚好是在 Ken Thompson 离开伯克利前往贝尔实验室的十年之后。在伯克利，Coulouris 见到了 Bill Joy，一个正在工作于伯克利软件套件(BSD)的研究生。Coulouris 给 Joy 展示了 `em`，Joy 便在 Coulouris 的源代码上开始构建了 `ed` 的一个改进版本，称之为 `ex`，即"extended `ed`（扩展版 `ed`）"。1978 年，`ex` 的 1.1 版本与 BSD 的首个发布版本捆绑释出。`ex` 很大程度上与 `ed` 兼容，但添加了两个模式：一个“打开”模式，启用与 `em` 上相似的单行编辑，一个“可视”模式，接管整个屏幕并启用于我们今天用的相似的整个文件实时编辑。

在 1979 年 BSD 的第二个发布版本中，一个名为 `vi` 的可执行程序被引进，它能比可视模式的 `ex` 做的稍多一些。

`ex`/`vi`(自此以后便是 `vi`)确立了很多不是 `ed` 一部分但我们现在在用的大部分约定。Joy 使用的视频终端是一台 Lear Siegler ADM-3A，其键盘上没有方向键。作为替代，箭头被印在 `h`, `j`, `k` 与 `l` 键上，这便是为何 Joy 使用这些按键作为 `vi` 中的光标移动。ADM-3A 键盘上的 ESC 键则位于如今的 Tab 键的位置上，这解释了为何一个极其难按到的按键会被分配为常用到的退出一个模式的操作。使用 `:` 字符作为命令前缀也是来自 `vi`，在正常模式（也就是运行 `ex` 进入的模式）中使用 `:` 作为提示。这解决了 `ed` 中存在已久的一个抱怨，即，一旦启动，用户只会得到彻底的沉默。在可视模式，保存并退出现在是键入经典的 `:wq`。"Yanking" 与 "putting"（译注：即复制与粘贴）出现了，且 `set` 命令打开设置选项都是最初的 `vi` 的一部分。我们现在在 Vim 中使用的基本的文本编辑功能大部分都是 `vi` 的功能。

![LSI-ADM3A-full-keyboard.jpg](https://s1.ax1x.com/2018/10/18/iwGW24.jpg)

`vi` 是 BSD 上除了 `ed` 唯一捆绑安装的文本编辑器。在那时，Emacs 需要花费数百美元（这是在 GNU Emacs 出现之前），所以 `vi` 变得极其流行。但 `vi` 是 `ed` 的直接后代，这意味着如果没有 AT&T 的源代码许可，源代码不能被改动。这使几个人创造了 `vi` 的开源版本。1987 年 STEVIE (ST Editor for VI Enthusiasts)（为 vi 爱好者的 ST 编辑器）出现了，Elvis 出现在 1990 年，`nvi` 则在 1994 年出现。这些克隆中的某些添加了额外的功能，例如语法高亮显示与分割窗口。因为有很多 Elvis 用户为了包含而推动，所以 Elvis 的许多功能被合并进了 Vim。

## Bram Moolenaar 写下 Vim

Vim，现在是"Vi Improved"的缩写，最初却意味着"Vi Imitation"（Vi 的模仿）。如同许多其他的 `vi` 克隆，Vim 最初是一个 `vi` 不能工作的平台上的移植。Bram Moolenaar，一个在荷兰芬洛的一个复印机公司工作的荷兰工程师，想要在他全新的 Amiga 2000 上得到一个像 `vi` 一样的东西。Moolenaar 在大学时代已习惯于在 Unix 系统上使用 `vi`，且它现在“如臂指使”。[^10] 所以在 1988 年，以已存在的 `vi` 克隆 STEVIE 作为起点，Moolenaar 开始着手于 Vim。

Moolenaar 已经有了 STEVIE 因为 STEVIE 已在一个叫 Fred Fish disk 的东西上出现了。Fred Fish 是一个美国程序员，每个月都会寄出一个软盘，其中是 Amiga 平台上可用最好的开源软件的策划选集。每个人都能要一份，只需付出邮费而已。Moolenaar 使用的版本是在 Fred Fish disk 256 上发布的版本。[^11]（很遗憾，看起来 Fred Fish disk 与 [Freddi Fish](https://en.wikipedia.org/wiki/Freddi_Fish) 并没有什么关系。）

Moolenaar 很喜欢 STEVIE 但很快就注意到很多 `vi` 命令缺失了。[^12] 所以，在 Vim 的首个发布版本中，Moolenaar 将与 `vi` 的兼容作为首要工作。有人曾写了一系列的 `vi` 宏，在一个与 `vi` 正确兼容的编辑器上运行时，能解决一个 [随机生成的迷宫](https://github.com/isaacs/.vim/tree/master/macros/maze)。Moolenaar 能使这些宏在 Vim 上工作。1991 年，Vim 在 Fred Fish disk 591 上第一次以"Vi Imitation"发布。[^13] Moolenaar 已经添加了一些功能（包括多级撤销，与对编译错误的"quickfix"模式），这意味着 Vim 已经超越了 `vi`。但 Vim 会保持"Vi Imitation"直到 1993 年通过 FTP 发布的 Vim 2.0。

Moolenaar 在许多网上合作者的偶尔协助下，以稳健的步伐给 Vim 添加功能。Vim 2.0 引入了 `wrap` 选项与较长行内水平滚动的支持。Vim 3.0 添加了对分割窗口与缓冲区的支持，这些功能来自 `vi` 的克隆 `nvi`。Vim 现在也能将每个缓冲区存入一个交换文件，所以已更改的文本能在崩溃中幸免于难。Vimscript 在 Vim 5.0 中首次出现，一同出现的还有对语法高亮显示的支持。在这期间，Vim 的流行程度一直在增长。它被移植到 MS-DOS, Windows, Mac, 甚至 Unix，在其上 Vim 与最初的 `vi` 相竞争。

2006 年，在 *Linux Journal* 读者中，Vim 被投票为最流行的编辑器。[^14] 如今，根据 Stack Overflow 的 2018 年开发者调查，Vim 是最流行的文本模式（即终端模拟器）编辑器，被所有软件开发者中的 25.8% 所使用（以及 40% 的系统管理员/运维）。[^15] 从 1980 年代末期，贯穿整个 90 年代的时间里，程序员们发起了“编辑器战争”，使 EMacs 与 `vi` （后来变成了 Vim）用户相斗争。尽管 Emacs 还有着一批追随者，一些人认为编辑器战争以及结束且 Vim 胜利了。[^16] 2018 年 Stack Overflow 开发者调查佐证了这一说法；只有 4.1% 的调查对象使用 Emacs。

Vim 是怎么变得这么成功的？很明显人们喜欢 Vim 提供的功能。但我认为 Vim 背后悠久的历史说明了它有着比之功能更多的好处。回溯 Vim 的代码库，只是到达 1988 年 Moolenaar 开始在其上工作。"wq text editor"在另一方面——一个类似 Unix 环境的文本编辑器该如何工作的宏大愿景——已走过半个世纪。"wq text editor" 有着几种不同的表达，但幸亏 Bill Joy 与 Bram Moolenaar 两人对兼容性不同寻常的注重，好的想法随着时间不断积累。某种意义上，"wq text editor" 是运行时间最长的、最成功的开源项目之一，享受着计算机世界最伟大思想的贡献。我并不认为“初创公司抛弃先例创造了制造混乱的软件”的开发方式一定很坏，但 Vim 证明了以合作与递增的方式也能创造奇迹。



[^1]: Butler Lampson, “Systems,” Butler Lampson, accessed August 5, 2018, http://bwlampson.site/Systems.htm.

[^2]: Dennis Ritchie, “An Incomplete History of the QED Editor,” accessed August 5, 2018, https://www.bell-labs.com/usr/dmr/www/qed.html.

[^3]: Peter Salus, “The Daemon, the GNU, and the Penguin,” Groklaw, April 14, 2005, accessed August 5, 2018, http://www.groklaw.net/article.php?story=20050414215646742.

[^4]: ibid.（译注：同上）

[^5]: Dennis Ritchie, “An Incomplete History of the QED Editor,” accessed August 5, 2018, https://www.bell-labs.com/usr/dmr/www/qed.html.

[^6]: Donald Norman, “The Truth about Unix: The User Interface Is Horrid,” Datamation, accessed August 5, 2018, http://www.ceri.memphis.edu/people/smalley/ESCI7205_misc_files/The_truth_about_Unix_cleaned.pdf.

[^10]: Bram Moolenaar, “Vim 25” (lecture, Zurich, November 2, 2016), December 13, 2016, accessed August 5, 2018, https://www.youtube.com/watch?v=ayc_qpB-93o&t=4m58s

[^11]: ibid（译注：同上）. (?t=6m15s)

[^12]: ibid（译注：同上）. (?t=7m6s)

[^13]: “Fish Disks 1 - 1120,” Amiga Stuff, accessed August 5, 2018, http://www.amiga-stuff.com/pd/fish.html.

[^14]: “2005 Linux Journal Reader’s Choice Awards,” Linux Journal, September 28, 2005, accessed August 5, 2018, https://www.linuxjournal.com/article/8520#N0x850cd80.0x87983bc.

[^15]: “Stack Overflow Developer Survey 2018,” Stack Overflow, accessed August 5, 2018, https://insights.stackoverflow.com/survey/2018/#development-environments-and-tools.

[^16]: Bruce Byfield, “The End of the Editor Wars,” Linux Magazine, May 11, 2015, accessed August 5, 2018, http://www.linux-magazine.com/Online/Blogs/Off-the-Beat-Bruce-Byfield-s-Blog/The-End-of-the-Editor-Wars.