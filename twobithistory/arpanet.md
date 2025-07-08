# ARPANET 的真正创新之处

2021 年 2 月 7 日

如果你搜索“ARPANET”这个词的图片，你会发现许多地图，展示了这个 [政府研究网络](https://en.wikipedia.org/wiki/ARPANET) 在 20 世纪 60 年代末和 70 年代初如何稳步扩展到全国各地。我猜想，大多数人第一次阅读或听说 ARPANET 时，都会看到其中一张地图。

显然，这些地图很有趣——很难相信曾经只有那么几台联网计算机，它们的地理位置竟然可以用相当低保真 (lo-fi) 的制图方式全部呈现出来。（我们这里说的是 20 世纪 60 年代的投影仪图表。你懂那种感觉。）但这些地图的问题在于，它们用粗线横跨大陆，强化了这样一种观念：ARPANET 最重要的成就是首次将计算机连接到美国广阔的地域。

今天，互联网是一条生命线，即使在病毒肆虐、我们都被困在室内的时候，它也能将我们彼此连接。因此，很容易想象，如果 ARPANET 是互联网的初稿，那么它出现之前的世界肯定完全是断开连接的，因为如果没有互联网，我们今天就会是那样，对吧？ARPANET 一定意义重大，因为它在以前不可能的情况下，通过计算机将人们连接起来。

这种观点对历史的理解并不完全正确，也低估了 ARPANET 成为一项突破性技术的原因。

## 首次亮相

华盛顿希尔顿酒店坐落在一个小山丘的顶端附近，距离国家广场东北方向约一英里半。其两面白色的现代立面呈宽阔的半圆形展开，如同鸟儿的翅膀。1965 年，《纽约时报》在报道酒店竣工时评论说，这座建筑看起来“像一只栖息在山顶巢穴中的海鸥”。[^1]

酒店将其最著名的特色隐藏在地下。车道环形交叉路口下方是一个巨大的椭圆形活动空间，被称为国际宴会厅 (International Ballroom)，多年来一直是华盛顿特区最大的无柱宴会厅。1967 年，The Doors 乐队在那里举办了一场音乐会。1968 年，Jimi Hendrix 也曾在此演出。1972 年，一个相对更安静的活动接管了宴会厅，举办了首届国际计算机通信大会 (International Conference on Computing Communication, ICCC)，一个名为 ARPANET 的有前景的研究项目首次公开展示。

1972 年的 ICCC 于 10 月 24 日至 26 日举行，约有 800 人参加。[^2] 它汇集了计算机网络这一新兴领域的所有顶尖研究人员。据互联网先驱 Bob Kahn 所说，“如果有人在华盛顿希尔顿酒店投下一枚炸弹，那几乎会摧毁当时美国所有的网络社区。”[^3]

然而，并非所有与会者都是计算机科学家。会议的一则广告声称，会议将“以用户为中心”，面向“律师、医生、经济学家、政府官员以及工程师和通信人员”。[^4] 会议的一些议程高度技术性，例如题为“数据网络设计问题一”及其后续会议“数据网络设计问题二”的议程。但大多数议程正如承诺的那样，侧重于计算机网络的潜在社会和经济影响。其中一个议程，在今天看来令人毛骨悚然地具有预见性，旨在促进讨论法律系统如何主动行动“以保障计算机数据库中的隐私权”。[^5]

ARPANET 演示旨在作为与会者的一种辅助性景点。在会议期间，与会者可以在国际宴会厅或酒店下层其他地方举行的会议之间，自由地漫步到乔治城宴会厅 (Georgetown Ballroom) （一个比大宴会厅小、位于走廊尽头的宴会厅/会议室），[^6] 那里有来自不同制造商的 40 台终端机，用于访问 ARPANET。[^7] 这些终端是哑终端 (dumb terminals) ——它们只负责输入和输出，无法独立进行计算。（事实上，在 1972 年，这些终端很可能都是硬拷贝终端 (hardcopy terminals)，即电传打字机 (teletype machines)。）所有终端都连接到一台名为终端接口消息处理器 (Terminal Interface Message Processor, TIP) 的计算机，它位于房间中央的一个高台上。TIP 是一种古老的路由器，专门设计用于将哑终端连接到 ARPANET。通过使用这些终端和 TIP，ICCC 的与会者可以尝试登录并访问当时构成 ARPANET 的 29 个主机站点 (host sites) 中的一些计算机。[^8]

为了展示网络功能，全国各地主机站点 (host sites) 的研究人员合作准备了 19 个简单的“场景”，供用户体验。这些场景被汇编成 [一本小册子](https://archive.computerhistory.org/resources/access/text/2019/07/102784024-05-001-acc.pdf)，分发给那些小心翼翼地走向布线和终端迷宫的与会者。[^9] 这些场景旨在证明这项新技术有效且有用，因为到目前为止，ARPANET 是“一个没有汽车的高速公路系统”，其五角大楼的资助者希望通过公开演示激发更多人对网络的兴趣。[^10]

因此，这些场景展示了通过 ARPANET 访问的各种软件：有编程语言解释器 (programming language interpreters)，一个用于麻省理工学院 (MIT) 的基于 Lisp 的语言，另一个用于加州大学洛杉矶分校 (UCLA) 托管的名为 Speakeasy 的数值计算环境；有游戏，包括一个国际象棋程序和康威生命游戏 (Conway’s Game of Life) 的一个实现；或许最受与会者欢迎的是，还有几个 AI 聊天程序 (AI chat programs)，包括 Joseph Weizenbaum 在麻省理工学院开发的著名 ELIZA 聊天程序。

准备这些场景的研究人员仔细列出了用户需要在终端输入的每个命令。这尤其重要，因为连接到任何给定 ARPANET 主机 (host) 的命令序列可能因主机而异。例如，要体验托管在麻省理工学院人工智能实验室 (MIT Artificial Intelligence Laboratory) 的 PDP-10 小型计算机 (minicomputer) 上的 AI 国际象棋程序，与会者被指示输入以下内容：

*下面的 `[LF]`、`[SP]` 和 `[CR]` 分别代表换行符、空格和回车键。我在 `//` 后面解释了每个命令，但原始注释中没有使用这种语法。*

```
@r [LF]                   // 重置 TIP
@e [SP] r [LF]            // “远程回显”设置，由主机而非 TIP 回显字符
@L [SP] 134 [LF]          // 连接到主机号 134
:login [SP] iccXXX [CR]   // 登录麻省理工学院人工智能实验室的系统，其中“XXX”应为用户姓名首字母
:chess [CR]               // 启动国际象棋程序

```

如果与会者成功输入了这些命令，他们的回报就是有机会玩当时最尖端的国际象棋软件，棋盘布局如下所示：

```
BR BN BB BQ BK BB BN BR
BP BP BP BP ** BP BP BP
-- ** -- ** -- ** -- **
** -- ** -- BP -- ** --
-- ** -- ** WP ** -- **
** -- ** -- ** -- ** --
WP WP WP WP -- WP WP WP
WR WN WB WQ WK WB WN WR

```

相比之下，要连接到加州大学洛杉矶分校的 IBM System/360 并运行 Speakeasy 数值计算环境，与会者必须输入以下内容：

```
@r [LF]                   // 重置 TIP
@t [SP] o [SP] L [LF]     // “换行符传输”设置
@i [SP] L [LF]            // “插入换行符”设置，即每次回车时发送换行符
@L [SP] 65 [LF]           // 连接到主机号 65
tso                       // 连接到 IBM 分时选项系统
logon [SP] icX [CR]       // 使用用户名登录，其中“X”应为任意选择的数字
iccc [CR]                 // 这是密码（多么安全！）
speakez [CR]              // 启动 Speakeasy

```

成功通过这些操作，与会者就能在终端上以最快的速度输入矩阵，并对其进行乘法、转置及其他运算：

```
:+! a=m*transpose(m);a [CR]
:+! eigenvals(a) [CR]

```

许多与会者对这次演示印象深刻，但原因可能与我们今天所设想的不同。今天很难记住的一个关键背景是，在 1972 年，远程使用计算机（即使是从不同的城市）并不是什么新鲜事。电传打字机 (Teletype) 设备几十年前就已经被用来与远距离计算机通信了。早在 ICCC 举行近五年前，比尔·盖茨 (Bill Gates) 在西雅图的一所高中里，就曾使用电传打字机在城里其他地方的一台通用电气 (General Electric) 计算机上运行他的第一个 BASIC 程序。仅仅登录到一台主机计算机，运行几个命令或玩一个基于文本的游戏，都是司空见惯的事情。这里展示的软件相当不错，但到目前为止我告诉你的这两个场景，表面上即使没有 ARPANET 也能体验到。

当然，幕后正在发生一些新事情。ICCC 的律师、政策制定者和经济学家可能对巧妙的国际象棋程序和聊天机器人 (chat bots) 着迷，但网络专家则会对另外两个更能展示 ARPANET 项目成就的场景更感兴趣。

第一个场景涉及一个名为 `NETWRK` 的程序，运行在麻省理工学院的 ITS 操作系统 (operating system) 上。`NETWRK` 命令是几个子命令的入口点，这些子命令可以报告 ARPANET 运行状态的各个方面。`SURVEY` 子命令报告网络上哪些主机正在运行且可用（它们都列在一个列表中），而 `SUMMARY.OF.SURVEY` 子命令汇总了过去 `SURVEY` 运行的结果，报告每个主机的“在线百分比”以及每个主机平均响应消息所需的时间。`SUMMARY.OF.SURVEY` 子命令的输出是一个如下所示的表格：

```
--HOST--  -#-  -%-UP-  -RESP-
UCLA-NMC  001  097%    00.80
SRI-ARC   002  068%    01.23
UCSB-75   003  059%    00.63
...

```

如你所见，主机号字段最多只能容纳三位数字（哈！）。其他 `NETWRK` 子命令允许用户查看更长历史时期的调查结果摘要，或检查单个主机的调查结果日志。

第二个场景展示了斯坦福大学 (Stanford) 正在开发的一款名为 SRI-ARC 在线系统 (SRI-ARC Online System) 的软件。这是一款功能丰富的精巧软件（它就是 Douglas Engelbart 在“所有演示之母”中演示的软件系统），但它的众多功能之一是能够利用加州大学圣巴巴拉分校 (UC Santa Barbara) 主机上运行的文件托管服务 (file hosting service)。在华盛顿希尔顿酒店的终端上，与会者只需运行 `copy` 命令并回答计算机的几个问题，就可以将斯坦福大学创建的文件复制到加州大学圣巴巴拉分校的主机上：

*下面的 `[ESC]`、`[SP]` 和 `[CR]` 分别代表 Esc 键、空格键和回车键。括号中的文字是计算机打印的提示。Esc 键用于在第三行自动补全文件名。这里复制的文件名为 `<system>sample.txt;1`，其中末尾的“1”表示文件版本号，`<system>` 表示目录。这是 TENEX 操作系统使用的文件名约定。*[^11]

```
@copy
(TO/FROM UCSB) to
(FILE) <system>sample [ESC] .TXT;1 [CR]
(CREATE/REPLACE) create

```

这两个场景可能看起来与前两个没有太大区别，但它们非同寻常。非同寻常之处在于，它们清楚地表明，在 ARPANET 上，人类可以与计算机对话，但计算机之间也可以*相互对话*。麻省理工学院收集的 `SURVEY` 结果并非由人类定期登录每台机器检查其是否在线，而是由一个知道如何与网络上其他机器通信的程序收集的。同样，从斯坦福大学到加州大学圣巴巴拉分校的文件传输，没有涉及任何人类坐在斯坦福或加州大学圣巴巴拉分校的终端前操作——华盛顿特区终端前的用户只需调用一个软件，就能让两台计算机相互通信。更重要的是，无论你坐在宴会厅的 40 台终端中的哪一台，都无关紧要，因为你可以使用几乎相同的命令序列，通过任何一台终端查看麻省理工学院的网络监控统计数据或在加州大学圣巴巴拉分校存储文件。

这就是 ARPANET 的全新之处。ICCC 的演示不仅仅是人类与远程计算机通信。它不仅仅是远程输入/输出 (I/O) 的演示。它展示的是软件与远程软件通信，这是前所未有的。

要真正理解为什么 ARPANET 项目的这一方面很重要，而不是主机地图所暗示的跨越全国的物理连接（反正那些线路都是租用的电话线，而且早就存在了！），请考虑一下，在 ARPANET 项目于 1966 年启动之前，五角大楼的 ARPA 办公室就有一个终端室。里面有三台终端。每台都连接到不同的计算机；一台计算机在麻省理工学院，一台在加州大学伯克利分校 (UC Berkeley)，另一台在圣莫尼卡 (Santa Monica)。[^12] 对 ARPA 工作人员来说，即使在华盛顿特区也能使用这三台计算机是很方便的。但对他们来说不方便的是，他们必须购买和维护来自三家不同制造商的终端，记住三种不同的登录程序，并熟悉三种不同的计算环境才能使用这些计算机。终端可能彼此相邻，但它们仅仅是线路另一端主机计算系统 (host computing systems) 的延伸，其操作方式与计算机本身一样不同。在 ARPANET 之前，与远程计算机通信是可能的；问题在于计算系统的异构性 (heterogeneity) 限制了通信的复杂程度。

## 齐心协力，就在此刻

所以，我在这里试图强调的是，声明 A“ARPANET 首次通过计算机连接了不同地点的人们”与声明 B“ARPANET 首次将计算机系统相互连接”之间存在一个重要的区别。这可能听起来像是在吹毛求疵，但声明 A 以一种声明 B 没有的方式，省略了一些具有启发性的历史。

首先，历史学家 Joy Lisi Rankin 已经表明，早在 ARPANET 出现之前，人们就已经在网络空间 (cyberspace) 中进行社交了。在《美国计算机发展史》 (*A People’s History of Computing in the United States*) 中，她描述了在 ARPANET 之前或独立于 ARPANET 存在的、全国各地分时网络 (time-sharing networks) 上的几个不同数字社区。从技术上讲，这些分时网络并非计算机网络，因为它们由一台大型机 (mainframe computer) 组成，在某个地下室为许多哑终端运行计算，就像一个肥胖的地下生物，触手遍布全国。然而，它们仍然促成了在后 Facebook 时代“网络”一词所暗示的大部分社交行为。例如，在 Kiewit 网络上，它是达特茅斯分时系统 (Dartmouth Time-Sharing System) 在东北地区大学和高中间的延伸，高中生们共同维护一个“八卦文件”，让他们能够了解其他学校的精彩动态，“从康涅狄格州到缅因州建立社交联系”。[^13] 同时，芒特霍利奥克学院 (Mount Holyoke College) 的女性通过网络与达特茅斯学院 (Dartmouth) 的男性通信，或许是为了约会或与男友保持联系。[^14] 这都发生在 20 世纪 60 年代。Rankin 认为，忽视这些早期的分时网络会削弱我们对过去 50 年美国数字文化如何发展的理解，为“硅谷神话”留下空间，将一切归功于少数几位“开国元勋”的个人天才。

至于 ARPANET 本身，如果我们认识到关键挑战是连接计算机*系统*而不仅仅是物理计算机，那么这可能会改变我们在讲述使 ARPANET 成为可能的技术创新时所强调的重点。ARPANET 是有史以来第一个分组交换网络 (packet-switched network)，许多令人印象深刻的工程技术投入其中。然而，我认为如果仅仅说 ARPANET 是一项突破，因为它是有史以来第一个分组交换网络，那就错了。ARPANET 旨在让全国各地的计算机科学家更容易协作；这个项目更多的是关于如何让不同的操作系统和用不同语言编写的程序相互接口 (interface)，而不是如何有效地在马萨诸塞州和加利福尼亚州之间来回传输数据。所以 ARPANET 是第一个分组交换网络，但它也是一个了不起的标准成功案例——考虑到我在这个博客上写过 [多少次](https://twobithistory.org/2018/05/27/semantic-web.html) [失败](https://twobithistory.org/2018/12/18/rss.html) 的 [标准](https://twobithistory.org/2020/01/05/foaf.html)，我发现这一点尤其有趣。

即使在当时，发明 ARPANET 的协议 (protocols) 也是一个事后才考虑的问题，所以这项任务自然而然地落到了一个主要由研究生组成的团队身上。这个团队，后来被称为网络工作组 (Network Working Group)，于 1968 年 8 月在加州大学圣巴巴拉分校首次会面。[^15] 第一次会议有 12 人出席，其中大多数是来自四所大学的代表，这些大学将在设备准备就绪后成为 ARPANET 的首批主机站点。[^16] 当时在加州大学洛杉矶分校读研究生的 Steve Crocker 参加了会议；他在一次 Zoom 通话中告诉我，第一次会议上都是年轻人，主持会议的 Elmer Shapiro 可能是那里最年长的，大约 38 岁。ARPA 没有指派任何人负责研究计算机连接后如何通信，但很明显，某种协调是必要的。Crocker 一直期待着某个更有经验和权威的“正经大人”从东海岸飞过来接管，但这从未发生。网络工作组得到了 ARPA 的默许——所有这些会议都涉及大量的长途旅行，而且 ARPA 资金支付了差旅费——所以他们就是负责人。[^17]

网络工作组面临着巨大的挑战。从未有人以通用方式将计算机系统连接在一起；这与 20 世纪 60 年代末计算机领域盛行的所有假设背道而驰：

> 那个时期典型的大型机 (mainframe) 表现得好像它是宇宙中唯一的计算机。没有明显或简单的方法让两台不同的机器进行哪怕是传输比特所需的最低限度通信。你可以连接机器，但一旦连接，它们会彼此说什么呢？在那些日子里，计算机与连接到它的设备交互，就像君主与他的臣民通信一样。连接到主计算机的一切都执行特定任务，并且每个外围设备 (peripheral device) 都被假定随时准备好接收“给我拿拖鞋”之类的命令……计算机严格按照这种交互方式设计；它们向从属的读卡器、终端和磁带机发送指令，并启动所有对话。但如果另一个设备实际上用信号轻拍计算机的肩膀说：“嗨，我也是一台计算机”，接收机器就会不知所措。[^18]

因此，网络工作组的进展最初很缓慢。[^19] 该小组直到 1970 年 6 月才确定任何协议的“官方”规范，这距离小组首次会议已近两年。[^20]

但到 1972 年 ICCC 展示 ARPANET 时，所有关键协议都已到位。像国际象棋这样的场景就运用了其中许多协议。当用户运行命令 `@e r`（`@echo remote` 的缩写）时，这会指示 TIP 利用新的 TELNET 虚拟电传协议 (TELNET virtual teletype protocol) 中的一个功能，通知远程主机应该回显用户的输入。当用户随后运行命令 `@L 134`（`@login 134` 的缩写）时，这会使 TIP 调用与主机 134 的初始连接协议 (Initial Connection Protocol)，进而导致远程主机分配连接所需的所有资源，并将用户置于 TELNET 会话 (TELNET session) 中。（我描述的文件传输场景很可能使用了文件传输协议 (File Transfer Protocol)，尽管该协议在会议前不久才准备就绪。[^21]）所有这些协议都被称为“第三层”协议，在它们之下是第二层的主机到主机协议 (host-to-host protocol)（定义了主机之间应期望的消息基本格式），以及第一层的主机到 IMP 协议 (host-to-IMP protocol)（定义了主机如何与它们连接的路由设备通信）。令人难以置信的是，所有协议都奏效了。

在我看来，网络工作组之所以能够及时完成所有工作并普遍出色地完成任务，是因为它采用了开放和非正式的标准化方法，这以著名的征求意见稿 (Request for Comments, RFC) 系列文档为代表。这些文档最初通过普通邮件在网络工作组成员之间传阅，是会议间保持联系和征求意见反馈的一种方式。“征求意见稿”的框架是由 Steve Crocker 提出的，他撰写了第一份 RFC 并在早期负责 RFC 邮件列表，旨在强调该小组工作开放和协作的性质。这种框架以及文档本身的可用性，使得协议设计过程成为一个贡献和对他人贡献进行再创作的熔炉，其中最好的想法可以在不失颜面的情况下涌现。RFC 流程取得了巨大成功，半个世纪后，它仍然被用于制定互联网标准。

我认为在谈论 ARPANET 的影响时，我们应该强调网络工作组的这一遗产。尽管今天互联网最神奇之处之一是它能将我们与地球另一端的人们连接起来，但略带戏谑地说，这项技术自 19 世纪以来就已存在。物理距离早在 ARPANET 出现之前就被电报 (telegraph) 征服了。ARPANET 征服的距离，反而是每个主机站点所采用的操作系统、字符编码、编程语言和组织策略之间的逻辑距离 (logical distance)。实现第一个分组交换网络当然是一项重大的工程壮举，也应该被提及，但就连接从未被设计成能“和睦相处”的计算机达成标准的问题，是构建 ARPANET 所涉及的两个大问题中更难的一个——而它的解决方案是 ARPANET 故事中最奇迹的部分。

1981 年，ARPA 发布了一份“完成报告”，回顾了 ARPANET 历史的第一个十年。其中一个标题冗长乏味的章节名为“成功实现的技术方面和未按原计划实现的技术方面”，作者写道：

> ARPANET 开发过程中最困难的任务，可能是尝试——并成功地——让许多独立的主机计算机系统，尽管它们来自不同的制造商，甚至在同一制造商内部有不同的操作系统，也能相互通信。[^22]

这可是来自美国联邦政府的权威说法。

如果你喜欢这篇文章，每四周都会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。

TwoBitHistory 往期回顾……

> 我知道，已经太久了，但我终于写了一篇新文章。这篇是关于 REST API 实际上应该被称为 FIOH API（管它呢，HTTP 过载）的：<https://t.co/xjMZVZgsEz>
>
> — TwoBitHistory (@TwoBitHistory) [2020 年 6 月 28 日](https://twitter.com/TwoBitHistory/status/1277259930555363329?ref_src=twsrc%5Etfw)

[^1]: “Hilton Hotel Opens in Capital Today.” *The New York Times*, 20 March 1965, [https://www.nytimes.com/1965/03/20/archives/hilton-hotel-opens-in-capital-today.html?searchResultPosition=1](https://www.nytimes.com/1965/03/20/archives/hilton-hotel-opens-in-capital-today.html?searchResultPosition=1). Accessed 7 Feb. 2021.
[^2]: James Pelkey. *Entrepreneurial Capitalism and Innovation: A History of Computer Communications 1968-1988,* Chapter 4, Section 12, 2007, [http://www.historyofcomputercommunications.info/Book/4/4.12-ICCC%20Demonstration71-72.html](http://www.historyofcomputercommunications.info/Book/4/4.12-ICCC%20Demonstration71-72.html). Accessed 7 Feb. 2021.
[^3]: Katie Hafner and Matthew Lyon. *Where Wizards Stay Up Late: The Origins of the Internet*. New York, Simon & Schuster, 1996, p. 178.
[^4]: “International Conference on Computer Communication.” *Computer*, vol. 5, no. 4, 1972, p. c2, <https://www.computer.org/csdl/magazine/co/1972/04/01641562/13rRUxNmPIA>. Accessed 7 Feb. 2021.
[^5]: “Program for the International Conference on Computer Communication.” *The Papers of Clay T. Whitehead*, Box 42, [https://d3so5znv45ku4h.cloudfront.net/Box+042/013_Speech-International+Conference+on+Computer+Communications,+Washington,+DC,+October+24,+1972.pdf](https://d3so5znv45ku4h.cloudfront.net/Box+042/013_Speech-International+Conference+on+Computer+Communications,+Washington,+DC,+October+24,+1972.pdf). Accessed 7 Feb. 2021.
[^6]: It’s actually not clear to me which room was used for the ARPANET demonstration. Lots of sources talk about a “ballroom,” but the Washington Hilton seems to consider the room with the name “Georgetown” more of a meeting room. So perhaps the demonstration was in the International Ballroom instead. But RFC 372 alludes to a booking of the “Georgetown Ballroom” for the demonstration. A floorplan of the Washington Hilton can be found [here](https://www3.hilton.com/resources/media/hi/DCAWHHH/en_US/pdf/DCAWH.Floorplans.Apr25.pdf).
[^7]: Hafner, p. 179.
[^8]: ibid., p. 178.
[^9]: Bob Metcalfe. “Scenarios for Using the ARPANET.” *Collections-Computer History Museum*, <https://www.computerhistory.org/collections/catalog/102784024>. Accessed 7 Feb. 2021.
[^10]: Hafner, p. 176.
[^11]: Robert H. Thomas. “Planning for ACCAT Remote Site Operations.” BBN Report No. 3677, October 1977, [https://apps.dtic.mil/sti/pdfs/ADA046366.pdf](https://apps.dtic.mil/sti/pdfs/ADA046366.pdf). Accessed 7 Feb. 2021.
[^12]: Hafner, p. 12.
[^13]: Joy Lisi Rankin. *A People’s History of Computing in the United States*. Cambridge, MA, Harvard University Press, 2018, p. 84.
[^14]: Rankin, p. 93.
[^15]: Steve Crocker. Personal interview. 17 Dec. 2020.
[^16]: Crocker sent me the minutes for this meeting. The document lists everyone who attended.
[^17]: Steve Crocker. Personal interview.
[^18]: Hafner, p. 146.
[^19]: “Completion Report / A History of the ARPANET: The First Decade.” BBN Report No. 4799, April 1981, [https://walden-family.com/bbn/arpanet-completion-report.pdf](https://walden-family.com/bbn/arpanet-completion-report.pdf), p. II-13.
[^20]: I’m referring here to RFC 54, “Official Protocol Proffering.”
[^21]: Hafner, p. 175.
[^22]: “Completion Report / A History of the ARPANET: The First Decade,” p. II-29.