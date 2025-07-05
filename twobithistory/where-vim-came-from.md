# Vim 的起源

原文：[Where Vim Came From](https://twobithistory.org/2018/08/05/where-vim-came-from.html)


最近，我偶然接触到一种名为 Intel HEX 的文件格式。据我了解，Intel HEX 文件 (扩展名为 `.hex`) 的作用，是通过将二进制图像编码成一行行十六进制数字，让原本难以捉摸的二进制内容变得更直观一些。一般是给微控制器 (microcontrollers) 编程或需要将数据烧录进只读存储器 (ROM) 的人会用到它。总之，当我第一次在 Vim 里打开一个 HEX 文件时，我被彻底震惊了。这个文件格式，至少在我看来，是如此深奥，但 Vim 却早已对它了如指掌。HEX 文件的每一行都是一条记录，被划分为不同字段——而 Vim 早就贴心地用不同颜色标亮了每个字段。我敬畏地输入 `:set ft?` 并按下回车。“`filetype=hex`”，Vim 自豪地回应。

Vim 的身影无处不在。它的用户群体如此庞大，以至于支持 HEX 这种小众格式其实不足为奇。macOS 系统预装了 Vim，它在 Linux 世界里也拥有一大批忠实拥趸。就连那些讨厌它的人也对它不陌生，因为有太多流行的命令行工具会默认使用 Vim 打开文件，结果导致无数新手被困在 Vim 里出不来，这甚至成了一个经久不衰的 [梗](https://stackoverflow.blog/wp-content/uploads/2017/05/meme.jpeg)。甚至在包括 Facebook 在内的一些大型网站上，你按下 `j` 键页面就会向下滚动，按下 `k` 键就会向上滚动——这堪称 Vim 渗透数字文化的巅峰标志。

然而，Vim 也是一个谜。就拿 React 来说，人人都知道它由 Facebook 开发和维护，但 Vim 却似乎没有任何官方赞助商。尽管它如此普及和重要，却好像没有任何委员会或组织在为它做决策。你可以在 [Vim 官网](https://www.vim.org/) 上逛好几分钟，但对谁创造了 Vim、又为何创造它这些问题，依然一头雾水。如果你启动 Vim 时没有指定文件名，会看到一条启动信息，说 Vim 是由 “Bram Moolenaar 等人” 开发的。但这信息量约等于零。Bram Moolenaar 是谁？他那些神秘的伙伴们又是何方神圣？

或许更重要的是，既然我们已经开始提问了，那为什么退出 Vim 非得用 `:wq` 这么个指令？诚然，这是“写入 (write)” 操作后面跟着“退出 (quit)” 操作，但这实在算不上什么直观的设计。又是谁决定了复制文本不叫“复制”，而叫“yanking” (yank，意为猛地一拉)？为什么 `:%s/foo/bar/gc` 这么一长串就代表了“查找并替换”？Vim 的种种奇特之处显得如此随心所欲，不像是凭空杜撰的，那么它们到底从何而来？

答案，一如既往地，要从那个古老的计算技术摇篮——贝尔实验室 (Bell Labs) 讲起。从某种意义上说，Vim 不过是一款软件的最新迭代版本。我们可以叫它“wq 文本编辑器”，自 Unix 纪元开启以来，它就一直处于持续的开发和改进之中。

## Ken Thompson 开发的行编辑器

1966 年，贝尔实验室聘用了 Ken Thompson。Thompson 当时刚在加州大学伯克利分校获得电气工程与计算机科学硕士学位。在校期间，他曾使用过一款名为 QED 的文本编辑器，这款编辑器是 1965 到 1966 年间为伯克利分时系统编写的。[^1] Thompson 到贝尔实验室后做的第一件事，就是为 MIT 兼容分时系统重写了 QED。后来，他又为 Multics 项目写了另一个版本的 QED。在这一过程中，他扩展了程序功能，让用户可以使用 正则表达式 (regular expressions) 来搜索文件中的特定行并执行替换操作。[^2]

Multics 项目的目标是创建一个商业上可行的分时操作系统 (就像伯克利分时系统一样)，它由 MIT、通用电气和贝尔实验室三方合作。最终，AT\&T 认为该项目前景渺茫而选择退出。就这样，Thompson 和同在贝尔实验室的同事 Dennis Ritchie 突然没法使用分时系统了，他们非常怀念那种系统带来的“交互式计算的感觉”，于是决定自己动手打造一个。这个系统，最终以 Unix 的名字为世人所知。[^3] 1969 年 8 月，趁着妻子和年幼的儿子去加州度假，Thompson 拼凑出了这个新系统的基本雏形，他计划“给操作系统、shell、编辑器和汇编器各一周的开发时间”。[^4]

这款编辑器被命名为 `ed`。它基于 QED，但并非简单的复刻。Thompson 决定砍掉 QED 的一些特性。正则表达式 的支持被削弱了，`ed` 只能理解比较简单的正则。QED 允许用户打开多个 缓冲区 (buffer) 来同时编辑多个文件，但 `ed` 一次只能处理一个缓冲区。此外，QED 可以执行一个包含命令的缓冲区，`ed` 则完全不支持这个功能。这些简化在当时或许是必要的。Dennis Ritchie 就曾说过，缺少 QED 的高级正则表达式“算不上什么大损失”。[^5]

`ed` 现在已经是 POSIX 规范的一部分，所以只要你的系统遵循 POSIX 标准，你的电脑里就有它。`ed` 很值得把玩一番，因为它的许多命令如今已是 Vim 的一部分。例如，要把缓冲区内容写入磁盘，你得用 `w` 命令；要退出编辑器，就得用 `q` 命令。这两个命令可以写在同一行一次性执行——`wq` 就这么来了。和 Vim 一样，`ed` 也是一个 模态编辑器 (modal editor)；要从命令模式进入输入模式，你需要根据操作目的使用插入命令 (`i`)、追加命令 (`a`) 或修改命令 (`c`)。`ed` 还开创性地使用 `s/foo/bar/g` 这种语法来查找和替换文本。

看到这么多相似之处，你可能会觉得 Vim 用户上手 `ed` 应该毫无压力。但在另一个关键方面，`ed` 和 Vim 天差地别。`ed` 是一个纯粹的 行编辑器 (line editor)。它诞生并风靡于电传打字机 (teletype printer) 的年代。当 Ken Thompson 和 Dennis Ritchie 奋力编写 Unix 时，他们的工作场景是这样的：

![Ken Thompson (坐) 和 Dennis Ritchie (站) 通过电传打字机与 PDP-11 交互。](https://s2.loli.net/2024/04/13/Yzk6CW9PntxZilM.jpg)

`ed` 不允许你在文件的多行文本中自由移动光标并就地编辑，因为每当你修改一处，`ed` 就必须把整个文件重新打印一遍。在 1969 年，`ed` 没有任何机制能“清空”屏幕，因为所谓的“屏幕”就是一张纸，打上去的内容都是白纸黑字，覆水难收。需要时，你可以用列表命令 (`l`) 让 `ed` 打印出某几行给你看，但大多数时候，你编辑的文本是你根本看不见的。因此，用 `ed` 的感觉，就好比拿着一盏快没电的手电筒，在一间漆黑的屋子里摸索。你一次只能照亮一小块地方，所以必须竭尽全力记住屋里的一切布局。

下面是一个 `ed` 会话的示例。我在每行后面用 `#` 加了注释来解释其用途 (如果在真实的 `ed` 里输入这些注释，它会报错)：

```
[sinclairtarget 09:49 ~]$ ed
i                               # 进入输入模式
Hello world!

Isn't it a nice day?
.                               # 结束输入
1,2l                            # 列出第 1 到 2 行
Hello world!$
$
2d                              # 删除第 2 行
,l                              # 列出整个缓冲区
Hello world!$
Isn't it a nice day?$
s/nice/terrible/g               # 全局替换
,l
Hello world!$
Isn't it a terrible day?$
w foo.txt                       # 写入 foo.txt
38                              # (写入的字节数)
q                               # 退出
[sinclairtarget 10:50 ~]$ cat foo.txt
Hello world!
Isn't it a terrible day?
```

如你所见，`ed` 是个相当“沉默寡言”的程序。

## Bill Joy 开发的文本编辑器

`ed` 对于 Thompson 和 Ritchie 来说够用了。但其他人觉得它难用得要命，并给它贴上了“Unix 对新手极度不友好”的典型反面教材的标签。[^6] 1975 年，一个叫 George Coulouris 的人在伦敦玛丽女王学院的 Unix 系统上，开发了 `ed` 的一个改进版。Coulouris 编写这个编辑器时，充分利用了他在学院能接触到的视频显示器。和 `ed` 不同，Coulouris 的程序允许用户在屏幕上直接编辑一整行，并通过键盘逐字移动光标 (想象一下，只能在单行里使用 Vim)。Coulouris 将他的程序命名为 `em`，即“editor for mortals (凡人编辑器)”。据说这个名字的灵感来源于一次 Ken Thompson 的到访：Thompson 看了 Coulouris 的程序后不屑一顾，说自己编辑文件时根本不需要看到文件的实时状态。[^7]

1976 年，Coulouris 带着 `em` 来到加州大学伯克利分校，作为计算机科学系的访问学者在这里度过了一个夏天。这恰好是 Ken Thompson 离开伯克利前往贝尔实验室的十年之后。在伯克利，Coulouris 遇到了 Bill Joy，一位正在为 伯克利软件发行版 (Berkeley Software Distribution, BSD) 忙碌的研究生。Coulouris 向 Joy 展示了 `em`，Joy 则在 `em` 的源码基础上，开发出了一个更强大的 `ed` 改进版，取名为 `ex`，意为“extended `ed` (扩展版 `ed`)”。1978 年，`ex` 的 1.1 版本随第一版 BSD Unix 一同发布。`ex` 在很大程度上与 `ed` 兼容，但新增了两种模式：一种是“开放模式”，可以像 `em` 一样进行单行编辑；另一种是“可视模式”，这种模式会占据整个屏幕，实现我们今天所习惯的对整个文件进行实时编辑。

在 1979 年的第二版 BSD 中，一个名为 `vi` 的可执行文件诞生了，它的功能很简单：直接在可视模式下启动 `ex`。[^8]

`ex`/`vi` (下文统称 `vi`) 奠定了我们今天所熟知的、除继承自 `ed` 之外的几乎所有 Vim 的传统。当年 Joy 使用的视频终端是 Lear Siegler ADM-3A，这款终端的键盘上没有方向键。作为替代，`h`、`j`、`k`、`l` 这几个键上印着箭头，这便是 Joy 用这几个键在 `vi` 中移动光标的原因。此外，ADM-3A 键盘上的 `Esc` 键，正好在我们今天键盘上 `Tab` 键的位置，这就解释了为什么“退出模式”这么一个高频操作，会分配给一个如今看来如此“偏僻”的按键。命令前面的冒号 `:` 也源自 `vi`，它在普通模式 (也就是运行 `ex` 后进入的模式) 下，会用 `:` 作为提示符。这解决了 `ed` 长期以来为人诟病的一点——启动后一片死寂，毫无提示。在可视模式下，保存并退出需要输入经典的 `:wq`。“yanking (复制)” 和 “putting (粘贴)”，以及标记功能和用于设置选项的 `set` 命令，都源于最初的 `vi`。可以说，我们今天在 Vim 中进行基本文本编辑所用的功能，绝大部分都来自 `vi`。

![一台 Lear Siegler ADM-3A 终端的键盘。](https://s2.loli.net/2024/04/13/GnTOFa4NMpXo7di.jpg)

在 BSD Unix 中，除了 `ed`，`vi` 是唯一捆绑的文本编辑器。在那个年代，Emacs 可能要花费数百美元 (当时 GNU Emacs 还未问世)，因此 `vi` 迅速流行起来。但 `vi` 是 `ed` 的直系后代，这意味着没有 AT\&T 的源码授权，谁也不能修改它的代码。这激励了许多人去创造 `vi` 的 开源 (open-source) 版本。STEVIE (ST Editor for VI Enthusiasts) 诞生于 1987 年，Elvis 诞生于 1990 年，`nvi` 则在 1994 年问世。这些克隆版中的一些还增加了额外功能，比如 语法高亮 (syntax highlighting) 和分屏。特别是 Elvis，它的许多特性后来都被整合进了 Vim，这很大程度上要归功于 Elvis 用户们的积极推动。[^9]

## Bram Moolenaar 创造 Vim

“Vim”，如今是“Vi Improved (Vi 改进版)”的缩写，但它最初的名字是“Vi Imitation (Vi 模仿版)”。和其它 `vi` 的克隆版一样，Vim 的诞生也是源于在一个无法使用 `vi` 的平台上复刻它的想法。Bram Moolenaar 是一位荷兰软件工程师，在荷兰芬洛的一家复印机公司工作。他想为自己全新的 Amiga 2000 电脑找一款像 `vi` 一样的工具。Moolenaar 在大学时早已习惯了在 Unix 系统上使用 `vi`，那套操作已经融入了他的指尖，形成了肌肉记忆。[^10] 于是，在 1988 年，Moolenaar 以当时已有的 `vi` 克隆版 STEVIE 为起点，开始打造 Vim。

Moolenaar 之所以能用上 STEVIE，是因为 STEVIE 曾被收录在一套叫“Fred Fish 磁盘”的东西里。Fred Fish 是一名美国程序员，他每个月都会向外邮寄一张软盘，里面精选了 Amiga 平台下最优秀的开源软件。任何人只要支付邮费，就能索取一张。STEVIE 的好几个版本都通过 Fred Fish 磁盘发行，Moolenaar 用的是第 256 号磁盘上的版本。[^11] (有点令人失望的是，Fred Fish 磁盘和那个卡通游戏角色 [Freddi Fish (小鲤鱼弗雷迪)](https://en.wikipedia.org/wiki/Freddi_Fish) 似乎没什么关系。)

Moolenaar 很喜欢 STEVIE，但很快就发现它缺少了许多 `vi` 的命令。[^12] 因此，在 Vim 的第一个版本里，Moolenaar 将兼容 `vi` 作为首要目标。当时，有人写了一套 `vi` 宏，只要编辑器能完美兼容 `vi`，运行这套宏就能解开一个 [随机生成的迷宫](https://github.com/isaacs/.vim/tree/master/macros/maze)。Moolenaar 最终成功让这套宏在 Vim 里跑了起来。1991 年，Vim 作为“Vi Imitation”首次在第 591 号 Fred Fish 磁盘上发布。[^13] Moolenaar 已经为它添加了一些新功能 (包括多级撤销和针对编译器错误的“快速修复”模式)，这意味着 Vim 此时已超越了 `vi`。但直到 1993 年通过 FTP 发布的 Vim 2.0，它才正式告别“Vi Imitation”这个名字。

在互联网上各路协作者的偶尔帮助下，Moolenaar 稳步地为 Vim 添加新功能。Vim 2.0 引入了对 `wrap` (自动换行) 选项和长文本行水平滚动的支持。Vim 3.0 增加了分屏和缓冲区支持，这个功能的灵感来源于 `vi` 的另一个克隆版 `nvi`。Vim 还开始将每个缓冲区存入一个 交换文件 (swap file)，这样即使程序崩溃，编辑过的内容也能恢复。Vimscript 在 Vim 5.0 中首次亮相，一同出现的还有语法高亮功能。在这一切发生的同时，Vim 的声望与日俱增。它被移植到了 MS-DOS、Windows、Mac，甚至还“反攻”回了 Unix，与原版 `vi` 一较高下。

2006 年，Vim 被《Linux Journal》的读者票选为最受欢迎的编辑器。[^14] 时至今日，根据 Stack Overflow 2018 年的开发者调查，Vim 是最受欢迎的文本模式 (即在终端模拟器中运行) 编辑器，有 25.8% 的软件开发者 (以及 40% 的系统管理员/DevOps 工程师) 在使用它。[^15] 在上世纪 80 年代末到整个 90 年代，程序员之间曾爆发过一场“编辑器战争”，将 Emacs 用户和 `vi` (以及后来的 Vim) 用户划分为两大对立阵营。尽管 Emacs 至今无疑仍有拥趸，但一些人认为，这场战争已经结束，Vim 最终胜出。[^16] 2018 年 Stack Overflow 的调查数据似乎也印证了这一点：只有 4.1% 的受访者使用 Emacs。

Vim 为何能如此成功？显然，人们喜爱 Vim 提供的各种功能。但我认为，Vim 悠久的历史说明，它的优势远不止功能集那么简单。Vim 的代码库最早只能追溯到 1988 年，也就是 Moolenaar 开始开发它的那年。但“wq 文本编辑器”——这个关于类 Unix 文本编辑器应如何设计的宏大构想——却已存在了半个世纪之久。“wq 文本编辑器”有过几种不同的具体实现，但很大程度上得益于 Bill Joy 和 Bram Moolenaar 对向后兼容性的异乎寻常的重视，各种绝妙的创意得以随着时间推移不断累积。从这个意义上讲，“wq 文本编辑器”是史上持续时间最长、最成功的开源项目之一，它曾汇聚了计算机世界里一些最顶尖大脑的智慧与贡献。我并非认为“创业公司抛弃一切传统，创造颠覆性新软件”的开发模式有什么不好，但 Vim 的故事提醒着我们：协作与迭代，同样能创造奇迹。


[^1]:  Butler Lampson, “Systems,” Butler Lampson, accessed August 5, 2018, <http://bwlampson.site/Systems.htm>.
[^2]:  Dennis Ritchie, “An Incomplete History of the QED Editor,” accessed August 5, 2018, <https://www.bell-labs.com/usr/dmr/www/qed.html>.
[^3]:  Peter Salus, “The Daemon, the GNU, and the Penguin,” Groklaw, April 14, 2005, accessed August 5, 2018, <http://www.groklaw.net/article.php?story=20050414215646742>.
[^4]:  ibid.（同上）
[^5]:  Dennis Ritchie, “An Incomplete History of the QED Editor,” accessed August 5, 2018, <https://www.bell-labs.com/usr/dmr/www/qed.html>.
[^6]:  Donald Norman, “The Truth about Unix: The User Interface Is Horrid,” Datamation, accessed August 5, 2018, <http://www.ceri.memphis.edu/people/smalley/ESCI7205_misc_files/The_truth_about_Unix_cleaned.pdf>.
[^7]:  George Coulouris, “George Coulouris: A Bit of History,” George Coulouris’ Homepage, September 1998, accessed August 5, 2018, <http://www.eecs.qmul.ac.uk/~gc/history/index.html>.
[^8]:  “Second Berkeley Software Distribution Manual,” Roguelife, accessed August 5, 2018, <http://roguelife.org/~fujita/COOKIES/HISTORY/2BSD/vi.u.html>.
[^9]:  Sven Guckes, “VIM Wishlist,” Vmunix, May 15, 1995, accessed August 5, 2018, <https://web.archive.org/web/20080520075925/http://www.vmunix.com/vim/wish.html>.
[^10]: Bram Moolenaar, “Vim 25” (lecture, Zurich, November 2, 2016), December 13, 2016, accessed August 5, 2018, <https://www.youtube.com/watch?v=ayc_qpB-93o&t=4m58>s
[^11]: ibid. (?t=6m15s)
[^12]: ibid. (?t=7m6s)
[^13]: “Fish Disks 1 - 1120,” Amiga Stuff, accessed August 5, 2018, <http://www.amiga-stuff.com/pd/fish.html>.
[^14]: “2005 Linux Journal Reader’s Choice Awards,” Linux Journal, September 28, 2005, accessed August 5, 2018, <https://www.linuxjournal.com/article/8520#N0x850cd80.0x87983bc>.
[^15]: “Stack Overflow Developer Survey 2018,” Stack Overflow, accessed August 5, 2018, <https://insights.stackoverflow.com/survey/2018/#development-environments-and-tools>.
[^16]: Bruce Byfield, “The End of the Editor Wars,” Linux Magazine, May 11, 2015, accessed August 5, 2018, <http://www.linux-magazine.com/Online/Blogs/Off-the-Beat-Bruce-Byfield-s-Blog/The-End-of-the-Editor-Wars>.
