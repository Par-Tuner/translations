# Git 诞生前的版本控制系统：CVS

*2018 年 7 月 7 日*

Github 于 2008 年推出。如果你的软件工程职业生涯和我一样，没有比 Github 更早开始，那么 Git 可能就是你唯一使用过的版本控制软件。尽管人们有时会抱怨 Git 学习曲线陡峭或界面不直观，但它已成为大家进行版本控制的首选。在 Stack Overflow 2015 年的开发者调查中，有 69.3% 的受访者使用 Git，几乎是第二受欢迎的版本控制系统 Subversion 的两倍 [^1]。2015 年之后，Stack Overflow 停止询问开发者他们使用的版本控制系统，也许是因为 Git 已经变得如此流行，以至于这个问题变得索然无味。

Git 本身也比 Github 早不了多少。Linus Torvalds 于 2005 年发布了 Git 的第一个版本。尽管如今的年轻开发者可能很难想象一个“版本控制软件”这个词几乎就等同于 Git 的世界，但这样的世界在不久前确实存在。当时有很多替代方案可供选择。开源开发者偏爱 Subversion，企业和视频游戏公司使用 Perforce (有些至今仍在用)，而 Linux 内核项目则以依赖名为 BitKeeper 的版本控制系统而闻名。

其中一些系统，特别是 BitKeeper，对于穿越回过去的年轻 Git 用户来说可能会感到熟悉。但大多数则不会。除了 BitKeeper，Git 之前的版本控制系统都遵循着根本不同的范式。在《版本控制示例》(Version Control by Example) 一书作者 Eric Sink 提出的分类法中，Git 是第三代版本控制系统，而 Git 的大多数前辈，即 20 世纪 90 年代和 21 世纪初流行的系统，则是第二代版本控制系统 [^2]。第三代版本控制系统是分布式 (distributed) 的，而第二代版本控制系统则是集中式 (centralized) 的。你几乎肯定听说过 Git 被描述为“分布式版本控制系统”。我从未完全理解分布式/集中式的区别，至少在我自己安装并尝试了一个集中式第二代版本控制系统之前是这样。

我安装的系统是 CVS。CVS，全称并发版本系统 (Concurrent Versions System)，是第一个第二代版本控制系统。它也是最受欢迎的版本控制系统，持续了大约十年，直到 2000 年被 Subversion 取代。即便如此，Subversion 也被认为是“更好的 CVS”，这更凸显了 CVS 在整个 20 世纪 90 年代的主导地位。

CVS 最初由荷兰计算机科学家 Dick Grune 于 1986 年开发，他当时正在寻找一种与学生合作进行编译器项目的方法 [^3]。CVS 最初只不过是一系列封装了 RCS (Revision Control System) 的 Shell 脚本 (shell scripts)，RCS 是 Dick Grune 想要改进的第一代版本控制系统。RCS 遵循悲观锁定模型 (pessimistic locking model)，这意味着不能有两个程序员同时处理一个文件。为了编辑文件，你必须首先向 RCS 请求对该文件的独占锁定，并一直持有直到编辑完成。如果其他人已经在编辑你需要编辑的文件，你就必须等待。CVS 通过将悲观锁定模型替换为乐观模型 (optimistic model) 来改进 RCS，并开创了第二代版本控制系统。程序员现在可以同时编辑同一个文件，稍后合并他们的修改并解决任何冲突。(Brian Berliner 是一位后来接管 CVS 项目的工程师，他在 1990 年写了一篇关于 CVS 创新的非常易读的[论文](https://docs.freebsd.org/44doc/psd/28.cvs/paper.pdf)。)

从这个意义上说，CVS 与 Git 并没有太大不同，Git 也遵循乐观模型。但相似之处仅此而已。事实上，当 Linus Torvalds 开发 Git 时，他的指导原则之一是 WWCVSND，即“CVS 不会做什么”。每当他对某个决定犹豫不决时，他都会努力选择 CVS 设计中未曾选择的选项 [^4]。因此，尽管 CVS 比 Git 早了十多年，但它作为一种反面模板影响了 Git。

我非常喜欢玩 CVS。我认为没有比这更好的方式来理解为什么 Git 的分布式特性是对前代系统的巨大改进。所以，我邀请你和我一起踏上这段激动人心的旅程，花上你生命中接下来的十分钟，了解一个在过去十年中几乎无人使用的软件。（*参见[更正](#correction)。*）

## CVS 入门

CVS 的安装说明可以在[项目主页](https://www.nongnu.org/cvs/)上找到。在 MacOS 上，你可以使用 Homebrew 安装 CVS。

由于 CVS 是集中式版本控制系统，它以 Git 等系统所没有的方式区分客户端环境 (client-side universe) 和服务端环境 (server-side universe)。这种区别并没有明显到需要不同的可执行文件。但为了开始使用 CVS，即使是在你自己的机器上，你也必须设置 CVS 后端。

CVS 后端，即所有代码的中央存储，被称为仓库 (repository)。在 Git 中，你通常会为每个项目设置一个仓库，而在 CVS 中，一个仓库则包含你所有的项目。所有项目都只有一个中央仓库，尽管也有方法可以一次只处理一个项目。

要创建本地仓库，你需要运行 `init` 命令。你可以在像你的主目录这样的全局位置执行此操作。

```
$ cvs -d ~/sandbox init

```

CVS 允许你将选项传递给 `cvs` 命令本身或 `init` 子命令。出现在 `cvs` 命令之后的选项是全局性的，而出现在子命令之后的选项则特定于该子命令。在这种情况下，`-d` 标志是全局的。在这里，它告诉 CVS 我们想在哪里创建仓库，但通常 `-d` 标志指向我们希望用于任何给定操作的仓库位置。一直提供 `-d` 标志会很繁琐，因此可以设置 `CVSROOT` 环境变量来代替。

由于我们正在本地工作，我们只是为 `-d` 参数传递了一个路径，但我们也可以包含一个主机名。

该命令会在你的主目录中创建一个名为 `sandbox` 的目录。如果你列出 `sandbox` 的内容，你会发现它包含另一个名为 `CVSROOT` 的目录。这个目录，不要与环境变量混淆，它保存着仓库的管理文件。

恭喜！你刚刚创建了你的第一个 CVS 仓库。

## 提交代码

假设你决定维护一份你最喜欢的颜色列表。你是一个有艺术天赋但极度健忘的人。你打出你的颜色列表，并将其保存为 `favorites.txt` 文件：

```
blue
orange
green

definitely not yellow

```

我们还假设你已将文件保存在一个名为 `colors` 的新目录中。现在你想将你最喜欢的颜色列表置于版本控制之下，因为五十年后回顾你的品味如何随时间变化会很有趣。

为此，你必须将你的目录作为一个新的 CVS 项目导入。你可以使用 `import` 命令来完成：

```
$ cvs -d ~/sandbox import -m "" colors colors initial
N colors/favorites.txt

No conflicts created by this import

```

在这里，我们再次使用 `-d` 标志指定仓库的位置。其余参数传递给 `import` 子命令。我们必须提供一条消息，但这里我们并不真正需要，所以我们将其留空。下一个参数 `colors` 指定了我们在仓库中新目录的名称；这里我们只是使用了与我们当前所在目录相同的名称。最后两个参数分别指定了供应商标签 (vendor tag) 和发布标签 (release tag)。我们稍后会详细讨论标签。

你刚刚将你的“colors”项目拉入 CVS 仓库。将代码导入 CVS 有几种不同的方法，但这是《实用版本控制：使用 CVS》(Pragmatic Version Control Using CVS) 这本关于 CVS 的 Pragmatic Programmer 书籍推荐的方法 [http://shop.oreilly.com/product/9780974514000.do](http://shop.oreilly.com/product/9780974514000.do)。这种方法有点笨拙的地方在于，你必须重新检出你的工作，即使你已经有一个现有的 `colors` 目录。你将删除该目录，然后检出 CVS 已经知道的版本：

```
$ cvs -d ~/sandbox co colors
cvs checkout: Updating colors
U colors/favorites.txt

```

这将创建一个新目录，也叫 `colors`。在这个目录中，你会找到你原始的 `favorites.txt` 文件以及一个名为 `CVS` 的目录。`CVS` 目录基本上是 CVS 中与每个 Git 仓库中的 `.git` 目录等效的部分。

## 进行更改

准备好一次穿越之旅吧。

就像 Git 一样，CVS 也有一个 `status` 子命令：

```
$ cvs status
cvs status: Examining .
===================================================================
File: favorites.txt    	Status: Up-to-date

   Working revision:	1.1.1.1	2018-07-06 19:27:54 -0400
   Repository revision:	1.1.1.1	/Users/sinclairtarget/sandbox/colors/favorites.txt,v
   Commit Identifier:	fD7GYxt035GNg8JA
   Sticky Tag:		(none)
   Sticky Date:		(none)
   Sticky Options:	(none)

```

这里开始看起来很陌生。CVS 没有提交对象 (commit object)。在上面，有一个叫做“提交标识符 (Commit Identifier)”的东西，但这可能只是一个相对较新的版本——2003 年出版的《实用版本控制：使用 CVS》中没有提到“提交标识符”。(CVS 的最后一次更新是在 2008 年发布的 [^5]。)

在 Git 中，你会谈论与提交 `45de392` 关联的文件版本，而在 CVS 中，文件是单独版本化 (versioned separately) 的。你的文件的第一个版本是 1.1，下一个版本是 1.2，依此类推。当涉及分支时，会附加额外的数字，所以你可能会得到像上面 `1.1.1.1` 这样的东西，这在我们的例子中似乎是默认值，即使我们没有创建任何分支。

如果你在一个有许多文件和提交 (commit) 的项目中运行 `cvs log` (相当于 `git log`)，你会看到每个文件的独立历史记录。你可能在同一个项目中有版本 1.2 的文件和版本 1.14 的文件。

让我们继续对 `favorites.txt` 文件的 1.1 版本进行更改：

```
 blue
 orange
 green
+cyan

 definitely not yellow

```

完成更改后，我们可以运行 `cvs diff` 来查看 CVS 认为我们做了什么：

```
$ cvs diff
cvs diff: Diffing .
Index: favorites.txt
===================================================================
RCS file: /Users/sinclairtarget/sandbox/colors/favorites.txt,v
retrieving revision 1.1.1.1
diff -r1.1.1.1 favorites.txt
3a4
> cyan

```

CVS 识别出我们向文件中添加了一行包含颜色“cyan”的新内容。（实际上，它说我们对“RCS”文件进行了更改；你可以看到 CVS 从未完全摆脱其与 RCS 的原始关联。）我们看到的差异是我们工作目录 (working directory) 中 `favorites.txt` 的副本与仓库中存储的 1.1.1.1 版本之间的差异。

为了更新仓库中存储的版本，我们必须提交 (commit) 更改。在 Git 中，这将是一个多步骤的过程。我们必须暂存 (stage) 更改，使其出现在我们的索引 (index) 中。然后我们提交更改。最后，为了让其他人看到更改，我们必须将提交推送 (push) 到原始仓库。

在 CVS 中，当你运行 `cvs commit` 时，所有这些事情都会发生。CVS 只是将它能找到的所有更改打包并放入仓库：

```
$ cvs commit -m "Add cyan to favorites."
cvs commit: Examining .
/Users/sinclairtarget/sandbox/colors/favorites.txt,v  <--  favorites.txt
new revision: 1.2; previous revision: 1.1

```

我太习惯 Git 了，这让我感到恐惧。如果没有机会暂存更改，你在工作目录中碰过的任何东西都可能最终成为公共仓库的一部分。你是否因为宣泄的需要，被动攻击性地重写了同事写得不好的函数，从未打算让他知道？太糟糕了，他现在认为你是个混蛋。你也不能在推送提交之前编辑它们，因为提交 *就是* 推送。你喜欢花 40 分钟反复运行 `git rebase -i`，直到你的本地提交历史像数学证明的推导一样流畅吗？抱歉，你在这里做不到，每个人都会发现你实际上并没有先写测试。

但我也现在理解了为什么这么多人觉得 Git 过于复杂。如果你习惯了 `cvs commit`，那么我确信暂存和推送更改对你来说会是毫无意义的苦差事。

当人们谈论 Git 是一个“分布式系统 (distributed system)”时，这主要是他们所指的区别。在 CVS 中，你不能在本地进行提交。提交是将代码提交到中央仓库，所以没有连接你就无法完成。你在本地拥有的只是你的工作目录。在 Git 中，你有一个功能齐全的本地仓库，所以即使断开连接，你也可以整天进行提交。而且你可以随意编辑这些提交、回滚、分支和 cherry pick，而无需其他人知道。

由于提交是件大事，CVS 用户通常不经常提交。提交会包含像我们今天可能在十个提交的拉取请求 (pull request) 中看到的那样多的更改。如果提交触发了持续集成构建 (CI build) 和自动化测试套件 (automated test suite)，情况尤其如此。

如果我们现在运行 `cvs status`，我们可以看到我们的文件有了新版本：

```
$ cvs status
cvs status: Examining .
===================================================================
File: favorites.txt    	Status: Up-to-date

   Working revision:	1.2	2018-07-06 21:18:59 -0400
   Repository revision:	1.2	/Users/sinclairtarget/sandbox/colors/favorites.txt,v
   Commit Identifier:	pQx5ooyNk90wW8JA
   Sticky Tag:		(none)
   Sticky Date:		(none)
   Sticky Options:	(none)

```

## 合并

如上所述，在 CVS 中，你可以编辑其他人已经在编辑的文件。这是 CVS 相对于 RCS 的重大改进。当你需要将你的更改合并 (merge) 回来时会发生什么？

假设你邀请了一些朋友将他们最喜欢的颜色添加到你的列表中。当他们添加颜色时，你决定你不再喜欢绿色，并将其从列表中删除。

当你提交更改时，你可能会发现 CVS 注意到了一个问题：

```
$ cvs commit -m "Remove green"
cvs commit: Examining .
cvs commit: Up-to-date check failed for `favorites.txt'
cvs [commit aborted]: correct above errors first!

```

看起来你的朋友们先提交了他们的更改。所以你的 `favorites.txt` 版本与仓库中的版本不是最新的。如果你运行 `cvs status`，你会看到你的本地 `favorites.txt` 副本是 1.2 版本，带有一些本地更改，但仓库版本是 1.3：

```
$ cvs status
cvs status: Examining .
===================================================================
File: favorites.txt    	Status: Needs Merge

   Working revision:	1.2	2018-07-07 10:42:43 -0400
   Repository revision:	1.3	/Users/sinclairtarget/sandbox/colors/favorites.txt,v
   Commit Identifier:	2oZ6n0G13bDaldJA
   Sticky Tag:		(none)
   Sticky Date:		(none)
   Sticky Options:	(none)

```

你可以运行 `cvs diff -r HEAD favorites.txt` 来准确查看 1.2 和 1.3 之间的差异：

```
$ cvs diff -r HEAD favorites.txt
Index: favorites.txt
===================================================================
RCS file: /Users/sinclairtarget/sandbox/colors/favorites.txt,v
retrieving revision 1.3
diff -r1.3 favorites.txt
3d2
< green
7,10d5
<
< pink
< hot pink
< bubblegum pink

```

看来我们的朋友真的很喜欢粉色。无论如何，他们编辑了文件的不同部分，所以更改很容易合并。当我们运行 `cvs update` 时，CVS 可以为我们完成这项工作，这类似于 `git pull`：

```
$ cvs update
cvs update: Updating .
RCS file: /Users/sinclairtarget/sandbox/colors/favorites.txt,v
retrieving revision 1.2
retrieving revision 1.3
Merging differences between 1.2 and 1.3 into favorites.txt
M favorites.txt

```

如果你现在查看 `favorites.txt`，你会发现它已经被修改，包含了你朋友对文件所做的更改。你的更改也还在那里。现在你可以自由地提交文件了：

```
$ cvs commit
cvs commit: Examining .
/Users/sinclairtarget/sandbox/colors/favorites.txt,v  <--  favorites.txt
new revision: 1.4; previous revision: 1.3

```

最终结果与你在 Git 中运行 `git pull --rebase` 得到的结果相同。你的更改已添加到你朋友的更改之上。没有“合并提交 (merge commit)”。

有时，对同一文件的更改可能不兼容。例如，如果你的朋友将“green”改为“olive”，那就会与你完全删除“green”的更改发生冲突。在 CVS 的早期，正是这种案例让人们担心 CVS 不安全；RCS 的悲观锁定确保了这种情况永远不会发生。但 CVS 通过确保任何人的更改都不会自动被覆盖来保证安全。你必须告诉 CVS 你希望保留哪种更改，所以当你运行 `cvs update` 时，CVS 会像 Git 检测到合并冲突 (merge conflict) 时一样，用两种更改标记文件。然后你必须手动编辑文件并选择你想要保留的更改。

这里值得注意的有趣一点是，合并冲突必须在提交之前修复。这是 CVS 集中式性质的另一个结果。在 Git 中，你无需担心解决合并问题，直到你推送你在本地的提交。

## 标签和分支

由于 CVS 没有易于寻址的提交对象 (commit object)，因此对一组更改进行分组的唯一方法是使用标签 (tag) 标记特定的工作目录状态。

创建标签很简单：

```
$ cvs tag VERSION_1_0
cvs tag: Tagging .
T favorites.txt

```

稍后，你可以通过运行 `cvs update` 并将标签传递给 `-r` 标志来将文件恢复到此状态：

```
$ cvs update -r VERSION_1_0
cvs update: Updating .
U favorites.txt

```

因为你需要一个标签才能回溯到更早的工作目录状态，CVS 鼓励大量抢先打标签 (preemptive tagging)。例如，在重大重构之前，你可能会创建一个 `BEFORE_REFACTOR_01` 标签，如果重构出错，你以后可以使用它。人们也使用标签来生成项目范围的差异。基本上，我们今天使用提交哈希 (commit hash)  routinely 完成的所有事情，在使用 CVS 时都必须预先设想和计划，因为你需要已经有可用的标签。

CVS 中可以创建分支 (branch)，某种程度上。分支只是一种特殊类型的标签：

```
$ cvs rtag -b TRY_EXPERIMENTAL_THING colors
cvs rtag: Tagging colors

```

这只创建了分支（顺便说一句，所有人都能看到），所以你仍然需要使用 `cvs update` 切换到它：

```
$ cvs update -r TRY_EXPERIMENTAL_THING

```

上述命令会在你当前的工作目录中切换到新分支，但《实用版本控制：使用 CVS》实际上建议你创建一个新目录来存放你的新分支。大概其作者认为在 CVS 中切换目录比切换分支更容易。

《实用版本控制：使用 CVS》也建议不要从现有分支创建分支。他们建议只从主线分支 (mainline branch) 创建分支，这在 Git 中被称为 `master` 分支。总的来说，分支被认为是“高级 CVS 技能”。在 Git 中，你几乎可以出于任何微不足道的原因开始一个新分支，但在 CVS 中，分支通常只在真正必要时才使用，例如用于发布版本。

分支稍后可以使用 `cvs update` 和 `-j` 标志合并回主线：

```
$ cvs update -j TRY_EXPERIMENTAL_THING

```

## 感谢提交历史

2007 年，Linus Torvalds 在 Google 举办了一场关于 Git 的[演讲](https://www.youtube.com/watch?v=4XpnKHJAok8)。当时 Git 还很新，所以那次演讲基本上是为了说服一群持怀疑态度的程序员，让他们使用 Git，尽管 Git 与当时可用的任何东西都大相径庭。如果你还没看过那次演讲，我强烈建议你观看。Linus 是一位有趣的演讲者，即使他总是那么直言不讳。他出色地解释了为什么分布式版本控制模型优于集中式模型。他的许多批评都特别针对 CVS。

Git 是一个[复杂的工具](https://xkcd.com/1597/)。学习它可能是一次令人沮丧的经历。但我也不断地惊叹于 Git 所能做到的事情。相比之下，CVS 简单明了，尽管通常无法完成我们现在认为理所当然的许多操作。回过头来使用 CVS 一段时间，是让你对 Git 的强大和灵活性产生新认识的绝佳方式。它很好地说明了为什么理解软件开发的历史如此有益——拿起并重新审视过时的工具，会让你对我们今天使用的工具背后的“为什么”有更深刻的理解。

*如果你喜欢这篇文章，每四周会有更多类似的文章发布！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS feed](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

### 更正

有人告诉我，许多组织，特别是那些规避风险的组织，例如制造医疗设备软件的组织，仍然在使用 CVS。这些组织中的程序员已经开发出一些小技巧来规避 CVS 的局限性，例如几乎为每个更改都创建一个新分支，以避免直接提交到 HEAD (HEAD)。（感谢 Michael Kohne 指出这一点。）

[^1]: “2015 Developer Survey,” Stack Overflow, 访问日期：2018 年 7 月 7 日, [https://insights.stackoverflow.com/survey/2015\#tech\-sourcecontrol](https://insights.stackoverflow.com/survey/2015#tech-sourcecontrol)。
[^2]: Eric Sink, “A History of Version Control,” Version Control By Example, 2011, 访问日期：2018 年 7 月 7 日, <https://ericsink.com/vcbe/html/history_of_version_control.html>。
[^3]: Dick Grune, “Concurrent Versions System CVS,” dickgrune.com, 访问日期：2018 年 7 月 7 日, [https://dickgrune.com/Programs/CVS.orig/\#History](https://dickgrune.com/Programs/CVS.orig/#History)。
[^4]: “Tech Talk: Linus Torvalds on Git,” YouTube, 2007 年 5 月 14 日, 访问日期：2018 年 7 月 7 日, [https://www.youtube.com/watch?v\=4XpnKHJAok8](https://www.youtube.com/watch?v=4XpnKHJAok8)。
[^5]: “Concurrent Versions System \- News,” Savannah, 访问日期：2018 年 7 月 7 日, [http://savannah.nongnu.org/news/?group\=cvs](http://savannah.nongnu.org/news/?group=cvs)。