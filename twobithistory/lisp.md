# Lisp 如何成为“上帝的编程语言”

*2018 年 10 月 14 日*

当程序员们讨论不同编程语言的相对优劣时，他们常常用平实的语言来形容，仿佛这些语言只是工具箱里的一堆工具——一种可能更适合系统编程，另一种可能更适合将其他程序粘合起来完成一些临时任务。这本应是常态。语言各有长处，如果脱离具体用例就声称某种语言比其他语言更好，只会引发无益且充满火药味的争论。

然而，有一种语言似乎能激发出一种奇特的普遍崇敬：Lisp。那些平时会猛烈抨击任何胆敢宣称某种语言优于其他语言的“键盘侠”，却会承认 Lisp 处于另一个层次。Lisp 超越了衡量其他语言的功利性标准，因为普通程序员从未用 Lisp 构建过任何实用的东西，将来可能也不会，但对 Lisp 的崇敬却如此之深，以至于 Lisp 常被赋予神秘的特性。大家最喜欢的网络漫画 *xkcd* 至少两次以这种方式描绘了 Lisp：在 [一则漫画](https://xkcd.com/224/) 中，一个角色达到了某种 Lisp 顿悟，这似乎让他能够理解宇宙的基本结构。在 [另一则漫画](https://xkcd.com/297/) 中，一位身披长袍、年迈的程序员将一叠括号递给他的 padawan，说这些括号是“更文明时代的优雅武器”，暗示 Lisp 拥有原力的所有神秘力量。

另一个很好的例子是 Bob Kanefsky 对歌曲《God Lives on Terra》的戏仿。他的戏仿作品写于 20 世纪 90 年代中期，名为《Eternal Flame》，描述了上帝是如何用 Lisp 创造世界的。以下是节选，完整歌词可在 [GNU Humor Collection](https://www.gnu.org/fun/jokes/eternal-flame.en.html) 中找到：

> *For God wrote in Lisp code*
>
> *When he filled the leaves with green.*
>
> *The fractal flowers and recursive roots:*
>
> *The most lovely hack I’ve seen.*
>
> *And when I ponder snowflakes,*
>
> *never finding two the same,*
>
> *I know God likes a language*
>
> *with its own four-letter name.*

我想，我只能代表我自己，但我认为这种“Lisp 是神秘魔法”的文化梗是我见过最离奇也最引人入胜的事情。Lisp 是在象牙塔中构思出来的，作为人工智能 (Artificial Intelligence) 研究的工具，所以它对编程门外汉来说总是陌生，甚至有点神秘。但现在的程序员们 [互相敦促“死前一定要尝试 Lisp”](https://www.reddit.com/r/ProgrammerHumor/comments/5c14o6/xkcd_lisp/d9szjnc/)，仿佛它是一种能拓展思维的迷幻剂。他们这样做，即使 Lisp 现在是广泛使用的第二古老的编程语言，只比 Fortran 年轻一年而已。[^1] 想象一下，如果你的工作是代表某个组织或团队推广一种新的编程语言。如果你能说服所有人，你的新语言拥有神圣的力量，那岂不是太棒了？但你该怎么做到呢？一种编程语言是如何成为隐藏知识的源泉的呢？

Lisp 是如何变成这样的呢？

![Byte Magazine Cover, August, 1979.](https://twobithistory.org/images/byte_lisp.jpg)
图 1: 《Byte》杂志封面，1979 年 8 月。

## 理论 A: 公理化语言

Lisp 的创造者 John McCarthy 最初并没有打算让 Lisp 成为计算原理的优雅提炼。但是，经过一两次幸运的洞察和一系列的改进，Lisp 最终成为了这样。Paul Graham——我们稍后会更多地谈到他——曾写道，McCarthy 之于 Lisp，“就像欧几里得之于几何学”。[^2] 人们可能在 Lisp 中看到了更深层的含义，因为 McCarthy 构建 Lisp 所用的基本元素，使其难以界定究竟是发明还是发现。

McCarthy 在 1956 年的达特茅斯人工智能夏季研究项目 (Darthmouth Summer Research Project on Artificial Intelligence) 期间开始思考创建一种语言。这个夏季研究项目实际上是一个持续数周的学术会议，也是人工智能领域的首次会议。McCarthy 当时是达特茅斯学院的数学助理教授，他实际上在提出这个活动时就创造了“人工智能”这个术语。[^3] 大约有十来个人全程参加了这次会议。[^4] 其中包括 Allen Newell 和 Herbert Simon，这两位研究人员隶属于 RAND Corporation 和 Carnegie Mellon，他们刚刚设计了一种名为 IPL 的语言。

Newell 和 Simon 一直在尝试构建一个能够生成命题演算证明的系统。他们意识到，在计算机原生指令集的层面上工作会很困难，所以他们决定创建一种语言——或者，正如他们所说的，“伪代码”——来帮助他们更自然地表达其“逻辑理论机”的工作原理。[^5] 他们的语言，名为 IPL (Information Processing Language)，与其说是我们今天所说的编程语言，不如说更像是一种高级汇编方言。Newell 和 Simon，可能指的是 Fortran，指出当时正在开发的其他“伪代码”都“专注于”用标准数学符号表示方程。[^6] 他们的语言则专注于将命题演算中的语句表示为符号表达式 (Symbolic Expression) 列表。IPL 中的程序基本上会利用一系列汇编语言宏来操作和评估一个或多个列表中的表达式。

McCarthy 认为，像 Fortran 那样在语言中包含代数表达式会很有用。所以他不太喜欢 IPL。[^7] 但他认为符号列表是建模人工智能问题的好方法，特别是涉及演绎的问题。这是 McCarthy 想要创建一种代数列表处理语言的萌芽，这种语言既要像 Fortran，又要能像 IPL 那样处理符号列表。

当然，今天的 Lisp 并不像 Fortran。在接下来的几年里，McCarthy 关于理想列表处理语言应该是什么样子的想法不断演变。他的想法始于 1957 年，当时他开始用 Fortran 编写国际象棋程序的例程。长时间接触 Fortran 使 McCarthy 确信其设计存在一些缺陷，其中最主要的是笨拙的 `IF` 语句。[^8] McCarthy 发明了一种替代方案，即“真正的”条件表达式，如果提供的测试成功则返回子表达式 A，如果测试失败则返回子表达式 B，并且 *只* 评估实际返回的子表达式。在 1958 年夏天，当 McCarthy 致力于设计一个可以执行求导的程序时，他意识到他的“真正的”条件表达式使得编写递归函数 (Recursive Function) 变得更容易、更自然。[^9] 求导问题也促使 McCarthy 设计了 *maplist* 函数，该函数接受另一个函数作为参数，并将其应用于列表中的所有元素。[^10] 这对于对任意多项的和进行求导非常有用。

这些东西都无法用 Fortran 表达，因此，在 1958 年秋天，McCarthy 让一些学生着手实现 Lisp。由于 McCarthy 当时是麻省理工学院 (MIT) 的助理教授，这些学生都是 MIT 的学生。当 McCarthy 和他的学生将他的想法转化为可运行的代码时，他们做出了进一步简化语言的改变。最大的改变涉及 Lisp 的语法。McCarthy 最初打算让语言包含一种名为“M-表达式”的东西，这将是一个语法糖 (Syntactic Sugar) 层，使 Lisp 的语法类似于 Fortran。尽管 M-表达式可以转换为 S-表达式——Lisp 以其闻名的由括号括起来的基本列表——但 S-表达式实际上是为机器设计的低级表示。唯一的问题是 McCarthy 一直用方括号表示 M-表达式，而 McCarthy 团队在 MIT 使用的 IBM 026 打孔机键盘上没有方括号键。[^11] 所以 Lisp 团队坚持使用 S-表达式，不仅用它们来表示数据列表，也表示函数应用。McCarthy 和他的学生还做了一些其他简化，包括转向前缀表示法 (Prefix Notation) 和内存模型改变，这意味着该语言只有一个真正的类型。[^12]

1960 年，McCarthy 发表了他关于 Lisp 的著名论文，题为《符号表达式的递归函数及其机器计算》 (Recursive Functions of Symbolic Expressions and Their Computation by Machine)。那时，该语言已经被精简到如此程度，以至于 McCarthy 意识到他拥有了“一个优雅的数学系统”的雏形，而不仅仅是另一种编程语言。[^13] 他后来写道，Lisp 所做的许多简化使其“成为一种描述可计算函数的方式，比图灵机 (Turing Machine) 或递归函数理论 (Recursive Function Theory) 中使用的通用递归定义要整洁得多”。[^14] 因此，在他的论文中，他将 Lisp 既作为一种可工作的编程语言，又作为一种研究递归函数行为的形式化方法。

McCarthy 通过仅用一小部分规则构建 Lisp 来向读者解释它。Paul Graham 后来在他的文章 [《Lisp 的根源》](http://languagelog.ldc.upenn.edu/myl/llog/jmc.pdf) 中，用更易读的语言重述了 McCarthy 的步骤。Graham 能够仅使用七个基本运算符、两种不同的函数表示法以及半打用基本运算符定义的高级函数来解释 Lisp。Lisp 可以通过如此少量的基本规则来指定，这无疑助长了它的神秘感。Graham 称 McCarthy 的论文是“计算的公理化”的尝试。[^15] 我认为这是思考 Lisp 吸引力的一种绝佳方式。其他语言有明显的、由 `while` 或 `typedef` 或 `public static void` 等保留字表示的人工构造，而 Lisp 的设计似乎是由计算本身的逻辑所决定。这种特质以及 Lisp 最初与“递归函数理论”这样深奥的领域之间的联系，使得 Lisp 今天拥有如此高的声望也就不足为奇了。

## 理论 B: 未来机器

在 Lisp 创建二十年后，根据著名的 [《黑客词典》](https://en.wikipedia.org/wiki/Jargon_File) (Hacker’s Dictionary) 记载，Lisp 已成为人工智能研究的“母语”。早期，Lisp 传播迅速，可能是因为其规则的语法使其在新机器上实现相对简单。后来，研究人员继续使用它，因为它能很好地处理符号表达式，这在人工智能大量依赖符号的时代非常重要。Lisp 被用于开创性的人工智能项目，如 [SHRDLU 自然语言程序](https://hci.stanford.edu/winograd/shrdlu/)、[Macsyma 代数系统](https://en.wikipedia.org/wiki/Macsyma) 和 [ACL2 逻辑系统](https://en.wikipedia.org/wiki/ACL2)。

然而，到了 20 世纪 70 年代中期，人工智能研究人员的计算能力开始不足。特别是 PDP-10——每个人最喜欢的人工智能工作机器——其 18 位地址空间越来越不足以满足 Lisp AI 程序的需求。[^16] 许多 AI 程序也应该是交互式的，而在分时系统 (Time-Sharing System) 上使一个要求苛刻的交互式程序表现良好是很有挑战性的。解决方案最初由 MIT 的 Peter Deutsch 提出，即设计一台专门用于运行 Lisp 程序的计算机。这些 Lisp 机器，正如我在 [上一篇关于 Chaosnet 的文章](https://twobithistory.org/2018/09/30/chaosnet.html) 中所描述的，将为每个用户提供一个专为 Lisp 优化的专用处理器。它们最终还将配备完全用 Lisp 编写的开发环境，供核心 Lisp 程序员使用。Lisp 机器诞生于小型机时代 (Minicomputer Era) 的尾声，但又在微型计算机革命 (Microcomputer Revolution) 全面爆发之前，它们是为编程精英打造的高性能个人计算机。

一度，Lisp 机器似乎是未来的潮流。几家公司应运而生，竞相将这项技术商业化。其中最成功的公司名为 Symbolics，由 MIT AI Lab 的资深人士创立。整个 20 世纪 80 年代，Symbolics 生产了一系列名为 3600 系列的计算机，这些计算机在 AI 领域和需要高性能计算的行业中很受欢迎。3600 系列计算机具有大屏幕、位图图形 (Bit-Mapped Graphics)、鼠标界面和 [强大的图形和动画软件](https://youtu.be/gV5obrYaogU?t=201)。这些是令人印象深刻的机器，能够运行令人印象深刻的程序。例如，从事机器人研究并通过 Twitter 联系我的 Bob Culley，在 1985 年成功地在 Symbolics 3650 上实现并可视化了一个寻路算法 (Path-Finding Algorithm)。他向我解释说，位图图形和面向对象编程 (Object-Oriented Programming) （通过 [Flavors 扩展](https://en.wikipedia.org/wiki/Flavors_(programming_language)) 在 Lisp 机器上可用）在 20 世纪 80 年代是非常新的技术。Symbolics 处于尖端地位。

![Bob Culley's path-finding program.](https://twobithistory.org/images/symbolics.jpg)
图 2: Bob Culley 的寻路程序。

因此，Symbolics 机器极其昂贵。Symbolics 3600 在 1983 年的售价为 110,000 美元。[^16] 所以大多数人只能远远地惊叹于 Lisp 机器的强大和 Lisp 程序员的精湛技艺。但他们确实惊叹了。《Byte》杂志从 1979 年到 20 世纪 80 年代末多次刊登 Lisp 和 Lisp 机器。在 1979 年 8 月的 Lisp 专题中，该杂志的编辑对 MIT 正在开发的新机器赞不绝口，称其拥有“海量内存”和“先进的操作系统”。[^17] 他认为它们前景如此光明，以至于相比之下，前两年——苹果 Apple II、Commodore PET 和 TRS-80 的推出——都显得无聊了。五年半后，在 1985 年，《Byte》杂志的一位撰稿人描述了为“复杂、超强的 Symbolics 3670”编写 Lisp 程序，并敦促读者学习 Lisp，声称它既是“大多数从事 AI 工作的人的首选语言”，也将很快成为一种通用编程语言。[^18]

我问了 Paul McJones，他为 Mountain View 的计算机历史博物馆 (Computer History Museum) 做了很多 Lisp [保存工作](http://www.softwarepreservation.org/projects/LISP/)，关于人们何时开始谈论 Lisp 仿佛它是来自更高维度存在的礼物。他说，语言固有的特性无疑与此有很大关系，但他也说，Lisp 与 20 世纪 60 年代和 70 年代强大的人工智能应用之间的紧密联系可能也起到了作用。当 Lisp 机器在 20 世纪 80 年代开始销售时，MIT 和 Stanford 等地之外的更多人接触到了 Lisp 的强大，传奇不断壮大。今天，Lisp 机器和 Symbolics 鲜为人知，但它们帮助 Lisp 的神秘感得以延续到 20 世纪 80 年代末。

## 理论 C: 学习编程

1985 年，MIT 教授 Harold Abelson 和 Gerald Sussman，以及 Sussman 的妻子 Julie Sussman，出版了一本名为《计算机程序的构造与解释》 (Structure and Interpretation of Computer Programs) 的教科书。这本教科书使用 Scheme 语言（Lisp 的一种方言）向读者介绍编程。它被用于 MIT 的入门编程课程长达二十年。我的猜测是，SICP （该书名的常用缩写）大约使 Lisp 的“神秘感系数”翻了一番。SICP 运用 Lisp 展示了它如何能够阐释计算机编程艺术中深刻的、近乎哲学性的概念。这些概念足够通用，任何语言都可以使用，但 SICP 的作者选择了 Lisp。因此，Lisp 的声誉因这本奇特而卓越的书的声名而进一步提升，这本书吸引了一代又一代的程序员 （也成为了 [一个非常奇怪的梗](https://knowyourmeme.com/forums/meme-research/topics/47038-structure-and-interpretation-of-computer-programs-hugeass-image-dump-for-evidence)）。Lisp 曾一直是“McCarthy 优雅的形式化体系”；现在它也成为了“那门教你编程隐藏秘密的语言”。

值得花点时间深入探讨 SICP 到底有多怪异，因为我认为这本书的怪异和 Lisp 的怪异在今天被混为一谈了。这种“怪异”从书的封面就开始了。它描绘了一个巫师或炼金术士走向一张桌子，准备施展某种魔法。他一只手拿着卡尺或圆规，另一只手拿着一个刻有“eval”和“apply”字样的地球仪。他对面的一个女人正对着桌子做手势；背景中，希腊字母 Lambda 悬浮在空中，散发着光芒。

![The cover art for SICP.](https://twobithistory.org/images/sicp.jpg)
图 3: SICP 的封面艺术。

老实说，这里到底发生了什么？为什么桌子有动物的脚？为什么那个女人对着桌子做手势？墨水瓶有什么意义？我们是否应该得出结论，巫师已经解开了宇宙的隐藏奥秘，而这些奥秘包括 eval/apply 循环和 Lambda 演算 (Lambda Calculus)？似乎就是这样。仅凭这张图片，就足以极大地影响人们今天谈论 Lisp 的方式。

但书中的文字本身也常常同样怪异。SICP 与你读过的其他大多数计算机科学教科书都不同。作者在书的序言中解释说，这本书不仅仅是关于如何用 Lisp 编程——它更是关于“三种现象的焦点：人类思维、计算机程序集合以及计算机本身”。[^19] 后来，他们进一步阐述，描述了他们的信念，即编程不应被视为计算机科学的一个学科，而应被视为“过程认识论”的一种新符号。[^20] 程序是一种新的思维结构方式，只是偶然地被输入到计算机中。本书的第一章简要介绍了 Lisp，但此后的大部分内容都是关于更抽象的概念。书中讨论了不同的编程范式 (Programming Paradigm)，讨论了面向对象 (Object-Oriented) 系统中“时间”和“身份”的本质，甚至在某个地方讨论了同步问题 (Synchronization Problem) 如何因通信的基本限制而产生，这些限制的作用类似于相对论中光速不变的原理。[^21] 这都是些深奥的内容。

所有这些并不是说这本书不好。它是一本很棒的书。它以我读过的任何其他书籍都更高层次地讨论了重要的编程概念，这些概念我曾长期思考但却不知如何描述。令人印象深刻的是，一本入门编程教科书能够如此迅速地描述面向对象编程的根本缺陷以及最小化可变状态的函数式语言的优势。更令人惊叹的是，这随后演变成对流式范式 (Stream Paradigm) 的讨论，也许就像今天的 [RxJS](https://rxjs-dev.firebaseapp.com/)，它能让你两全其美。SICP 以一种让人想起 McCarthy 最初 Lisp 论文的方式，提炼了高级程序设计的精髓。读完它之后，你最想做的第一件事就是让你的程序员朋友也去读它；如果他们查阅了它，看到了封面，但却没有读下去，他们唯一带走的印象就是，某种神秘的、根本的“eval/apply”东西赋予了魔法师对有动物脚的桌子的特殊力量。如果我是他们，我也会深感震撼。

但也许 SICP 最重要的贡献是将 Lisp 从一个奇特的异类提升为教学必备。早在 SICP 之前，人们就互相告知要学习 Lisp，以此来提高编程能力。1979 年《Byte》杂志的 Lisp 专刊就是这一事实的证明。那位对 MIT 新 Lisp 机器赞不绝口的编辑也解释说，这门语言值得学习，因为它“代表了一种分析问题的不同视角”。[^22] 但 SICP 将 Lisp 呈现为不仅仅是其他语言的衬托；SICP 将 Lisp 用作一门 *入门* 语言，隐含地论证了 Lisp 是掌握计算机编程基础的最佳语言。今天，当程序员们互相告知死前要尝试 Lisp 时，很大程度上可以说是因为 SICP。毕竟，语言 [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) 大概也提供了“一种分析问题的不同视角”。但人们学习 Lisp，是因为他们知道，在大约二十年里，Lisp 的视角被认为如此有用，以至于 MIT 在教授其他任何东西之前，都先教本科生 Lisp。

## Lisp 归来

SICP 发布同年，Bjarne Stroustrup 出版了《C++ 编程语言》 (The C++ Programming Language) 的第一版，将面向对象编程带给大众。几年后，Lisp 机器市场崩溃，AI 寒冬开始。在接下来的十年多时间里，C++ 和 Java 将成为未来的语言，而 Lisp 则被冷落。

当然，我们不可能准确指出人们何时再次对 Lisp 感到兴奋。但这可能发生在 Y-Combinator 联合创始人兼 Hacker News 创始人 Paul Graham 发表了一系列有影响力的文章，将 Lisp 推崇为初创公司的最佳语言之后。例如，在他的文章 [《超越平均水平》](http://www.paulgraham.com/avg.html) 中，Graham 认为 Lisp 宏 (Lisp Macro) 简单地使 Lisp 比其他语言更强大。他声称，在他的初创公司 Viaweb 中使用 Lisp 帮助他比竞争对手更快地开发功能。 [至少一些程序员](https://web.archive.org/web/20061004035628/http://wiki.alu.org/Chris-Perkins) 被说服了。但绝大多数程序员并没有转向 Lisp。

相反，发生的是越来越多的 Lisp 风格的特性被整合到大家最喜欢的编程语言中。Python 获得了列表推导式 (List Comprehension)。C# 获得了 Linq。Ruby 获得了……嗯，Ruby [就是一种 Lisp](http://www.randomhacks.net/2005/12/03/why-ruby-is-an-acceptable-lisp/)。正如 Graham 早在 2001 年就指出的那样，“默认语言，体现在一系列流行语言中，已逐渐向 Lisp 演进”。[^23] 尽管其他语言正逐渐变得像 Lisp，但 Lisp 本身却设法保留了其特殊的声誉，即那种鲜为人知但人人都应学习的神秘语言。1980 年，在 Lisp 诞生 20 周年之际，McCarthy 写道，Lisp 之所以能存活这么久，是因为它占据了“编程语言空间中的某种近似局部最优解”。[^24] 这低估了 Lisp 的真正影响力。Lisp 之所以能存活半个多世纪，并非因为程序员们几十年来不情愿地承认它是最适合这项工作的工具；事实上，它之所以能存活下来，即使大多数程序员根本不使用它。多亏了它在人工智能研究中的起源和应用，或许也得益于 SICP 的遗产，Lisp 继续吸引着人们。在我们能想象上帝用某种更新的语言创造世界之前，Lisp 不会消失。

*如果您喜欢这篇文章，每四周会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS feed](https://twobithistory.org/feed.xml)，以确保您能及时了解新文章的发布。*

*TwoBitHistory 往期回顾…*

> This week's post: A look at Chaosnet, the network that gave us the "CH" DNS class.<https://t.co/dC7xqPYzi5>
>
> — TwoBitHistory (@TwoBitHistory) [September 30, 2018](https://twitter.com/TwoBitHistory/status/1046437600658169856?ref_src=twsrc%5Etfw)

[^1]: John McCarthy, “History of Lisp”, 14, Stanford University, February 12, 1979, accessed October 14, 2018, <http://jmc.stanford.edu/articles/lisp/lisp.pdf>.
[^2]: Paul Graham, “The Roots of Lisp”, 1, January 18, 2002, accessed October 14, 2018, <http://languagelog.ldc.upenn.edu/myl/llog/jmc.pdf>.
[^3]: Martin Childs, “John McCarthy: Computer scientist known as the father of AI”, The Independent, November 1, 2011, accessed on October 14, 2018, [https://www.independent.co.uk/news/obituaries/john-mccarthy-computer-scientist-known-as-the-father-of-ai-6255307.html](https://www.independent.co.uk/news/obituaries/john-mccarthy-computer-scientist-known-as-the-father-of-ai-6255307.html).
[^4]: Lisp Bulletin History. [http://www.artinfo-musinfo.org/scans/lb/lb3f.pdf](http://www.artinfo-musinfo.org/scans/lb/lb3f.pdf)
[^5]: Allen Newell and Herbert Simon, “Current Developments in Complex Information Processing,” 19, May 1, 1956, accessed on October 14, 2018, [http://bitsavers.org/pdf/rand/ipl/P-850_Current_Developments_In_Complex_Information_Processing_May56.pdf](http://bitsavers.org/pdf/rand/ipl/P-850_Current_Developments_In_Complex_Information_Processing_May56.pdf).
[^6]: ibid.
[^7]: Herbert Stoyan, “Lisp History”, 43, Lisp Bulletin #3, December 1979, accessed on October 14, 2018, [http://www.artinfo-musinfo.org/scans/lb/lb3f.pdf](http://www.artinfo-musinfo.org/scans/lb/lb3f.pdf)
[^8]: McCarthy, “History of Lisp”, 5.
[^9]: ibid.
[^10]: McCarthy “History of Lisp”, 6.
[^11]: Stoyan, “Lisp History”, 45
[^12]: McCarthy, “History of Lisp”, 8.
[^13]: McCarthy, “History of Lisp”, 2.
[^14]: McCarthy, “History of Lisp”, 8.
[^15]: Graham, “The Roots of Lisp”, 11.
[^16]: Guy Steele and Richard Gabriel, “The Evolution of Lisp”, 22, History of Programming Languages 2, 1993, accessed on October 14, 2018, [http://www.dreamsongs.com/Files/HOPL2-Uncut.pdf](http://www.dreamsongs.com/Files/HOPL2-Uncut.pdf).
[^17]: Carl Helmers, “Editorial”, Byte Magazine, 154, August 1979, accessed on October 14, 2018, [https://archive.org/details/byte-magazine-1979-08/page/n153](https://archive.org/details/byte-magazine-1979-08/page/n153).
[^18]: Patrick Winston, “The Lisp Revolution”, 209, April 1985, accessed on October 14, 2018, [https://archive.org/details/byte-magazine-1985-04/page/n207](https://archive.org/details/byte-magazine-1985-04/page/n207).
[^19]: Harold Abelson, Gerald Jay. Sussman, and Julie Sussman, Structure and Interpretation of Computer Programs (Cambridge, Mass: MIT Press, 2010), xiii.
[^20]: Abelson, xxiii.
[^21]: Abelson, 428.
[^22]: Helmers, 7.
[^23]: Paul Graham, “What Made Lisp Different”, December 2001, accessed on October 14, 2018, <http://www.paulgraham.com/diff.html>.
[^24]: John McCarthy, “Lisp—Notes on its past and future”, 3, Stanford University, 1980, accessed on October 14, 2018, <http://jmc.stanford.edu/articles/lisp20th/lisp20th.pdf>.