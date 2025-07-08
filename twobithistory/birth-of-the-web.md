# 万维网及其发明者

*2018 年 6 月 10 日*

蒂姆·伯纳斯-李 (Tim Berners-Lee) 的过人之处在于，他仿佛就是为这项工作而生。

1989 年，当伯纳斯-李 (Berners-Lee) 首次提出后来成为万维网 (World Wide Web) 的构想时，计算机领域正发生着激动人心的变化。一套名为 TCP/IP 的新标准，让原本相互独立的计算机网络能够彼此“对话”。这些标准变得非常流行，尤其是在美国科学界。到 1989 年，TCP/IP 也刚刚开始被 CompuServe 等商业服务提供商采用。

与此同时，一个年度会议也刚刚成立，旨在讨论一个充满前景的计算机研究新方向：超文本 (hypertext)。超文本 (hypertext) 的概念最早诞生于 20 世纪 60 年代，在苹果公司于 1987 年发布了一款名为 HyperCard 的 Macintosh 程序后，它再次成为焦点。HyperCard 是一种简化的软件开发环境 (software development environment)，即使是最不精通技术的 Mac 用户，也能用它将一叠相互关联的“卡片”组合成一个交互式应用程序。尽管这些卡片不包含我们今天所理解的文本主体超链接 (hyperlinks)，但一张卡片可以包含按钮，点击后可以导航到其他卡片。HyperCard 取得了巨大的成功，甚至深受许多人喜爱，以至于去年还有一位粉丝 [重新创建](https://www.vipercard.net/) 了它。HyperCard 的成功激发了人们对超文本 (hypertext) 的新兴趣，一些人认为它将取代印刷文字，成为未来的主要媒介。根据当时一本关于超文本 (hypertext) 的书所说，它将“对我们的文化，特别是文学、教育、评论和学术领域，产生像古腾堡 (Gutenberg) 活字印刷术 (movable type) 那样颠覆性的影响。”[^1]

当时存在的一个主要问题是，在 1989 年，所有现有的超文本 (hypertext) 系统都是封闭系统 (closed systems)。超文本 (hypertext) 技术的商业应用通常涉及将复杂的文档转换为超文本 (hypertext) 形式，然后通过软盘 (floppy disk) 交付给用户。用户可以比阅读印刷书籍更轻松地导航文档，但他们无法跟随链接跳转到软盘 (floppy disk) 上未存储的文档。一些人，比如在 20 世纪 60 年代首次创造“超文本 (hypertext)”一词的特德·尼尔森 (Ted Nelson)，正在拼命寻找一种方法，通过让超文本 (hypertext) 系统在网络上运行来开放它们——但这些努力进展甚微。直到伯纳斯-李 (Berners-Lee) 出现，他的个人兴趣和专业经验将所有零散的“拼图块”摆在了他面前，才将互联网和超文本 (hypertext) 完美结合。

![伯纳斯-李在 1994 年使用他的网页浏览器。](https://twobithistory.org/images/tbl_photo.jpg)

## ENQUIRE、打印机和 RPC

早在 HyperCard 出现之前，伯纳斯-李 (Berners-Lee) 就对类似超文本 (hypertext) 的前景着迷。小时候，他曾和父亲（他的父母都是数学家和程序员）讨论过，如果计算机能像人类思维一样，以一系列松散的关联来构建世界，而不是以僵化的层级结构来建模世界，那该多好。[^2] 1980 年，在牛津大学 (Oxford University) 获得物理学学位四年后，他前往瑞士日内瓦的欧洲核子研究中心 (CERN)——一个粒子物理实验室 (particle physics laboratory) 工作。正如伯纳斯-李 (Berners-Lee) 在他关于万维网 (World Wide Web) 创建的书中描述的那样，欧洲核子研究中心 (CERN) 的机构文化近乎无政府状态。[^3] 大约一万人名义上是欧洲核子研究中心 (CERN) 的一部分，但任何时候只有一半人真正在日内瓦。实际受薪员工只有 3000 人；其余的都是合同工或流动学者。作为一名合同工，伯纳斯-李 (Berners-Lee) 发现他面临的最大挑战之一，就是如何在人员来来往往、项目不断更迭的洪流中，简单地理解人与项目之间的关系。

天气好的时候，伯纳斯-李 (Berners-Lee) 和他的同事们会在户外吃午饭时交流想法，周围是田园诗般的葡萄园，沿着山坡向上延伸。[^4] 晚上和休息时间，伯纳斯-李 (Berners-Lee) 则忙于一个他称之为 ENQUIRE 的程序。ENQUIRE 是他试图梳理出欧洲核子研究中心 (CERN) 内部错综复杂的关系网的尝试，它基本上是后来万维网 (World Wide Web) 的第一个迭代版本。它使用超文本 (hypertext) 来捕捉那些人类在纸上最自然地用圆圈和箭头表示的关系。用户可以在文档、人物和概念之间创建和跟随链接。这些链接都属于特定类型，例如，“真空控制系统 (Vacuum Control System)”概念可以与“真空设备模块 (Vacuum Equipment Modules)”概念建立“包含 (includes)”关系，并与名为 *Controle du System a Vide du Booster* 的文档建立“描述 (described-by)”关系。伯纳斯-李 (Berners-Lee) 以一本维多利亚时代的家庭百科全书和礼仪指南 *Enquire Within Upon Everything* 命名他的程序，他喜欢这个名字，因为它仿佛通往一个充满信息的魔法传送门。[^5] 伯纳斯-李 (Berners-Lee) 发现 ENQUIRE 很好地履行了它的名字，并且非常适合欧洲核子研究中心 (CERN) 这种混沌而充满活力的系统。但他在欧洲核子研究中心 (CERN) 的合同在他有机会向其他人推销它的实用性之前就结束了。离开时，伯纳斯-李 (Berners-Lee) 将程序交给了他的经理，放在一张软盘 (floppy disk) 上，但这张软盘 (floppy disk) 后来丢失了。[^6] （然而，ENQUIRE 的 [手册](https://www.w3.org/History/1980/Enquire/manual/) 仍然可用。）

ENQUIRE 无法跨计算机网络工作，因此，就像 20 世纪 80 年代后期出现的超文本 (hypertext) 系统一样，它是一个封闭系统 (closed systems)。尽管如此，伯纳斯-李 (Berners-Lee) 在如此早期阶段就探索超文本 (hypertext) 的可能性，这仍然值得称赞。为了将 ENQUIRE 转化为万维网 (World Wide Web)，伯纳斯-李 (Berners-Lee) 还需要整合另外两项关键技术。

其中第一项是标记语言 (markup language)。巧合的是，伯纳斯-李 (Berners-Lee) 离开欧洲核子研究中心 (CERN) 后做的下一件事，就是去为他的朋友约翰·普尔 (John Poole) 开发打印机软件。约翰·普尔 (John Poole) 经营着一家名为 Image Computer Systems 的公司，该公司正试图通过集成微处理器 (microprocessor) 来制造更智能的打印机。伯纳斯-李 (Berners-Lee) 帮助编写了，除其他之外，一种用于准备打印文档的新标记语言 (markup language)。[^7] SGML 这种标记语言 (markup language)——后来 HTML 正是基于它构建的，HTML 本质上只是 SGML 的一种特定应用或“标签集”——其草案规范 (draft specification) 于 1980 年首次发布并标准化。因此，伯纳斯-李 (Berners-Lee) 在 Image Computer Systems 工作期间，很可能接触过 SGML。即使没有，这段经历也肯定教会了他很多关于在物理或数字页面上呈现标记文本所固有的挑战。

1983 年，伯纳斯-李 (Berners-Lee) 决定回到欧洲核子研究中心 (CERN) 工作。他申请了一份研究员职位，并于 1984 年搬回瑞士，加入了欧洲核子研究中心 (CERN) 的电子与计算物理部门。他的首批任务之一是开发一个远程过程调用 (RPC) 协议，该协议将允许一台欧洲核子研究中心 (CERN) 计算机调用存储在另一台欧洲核子研究中心 (CERN) 计算机上的函数。这本应相对简单，但欧洲核子研究中心 (CERN) 的计算机并非都在同一个网络上。伯纳斯-李 (Berners-Lee) 离开期间，欧洲核子研究中心 (CERN) 变得更加复杂，欧洲核子研究中心 (CERN) 的员工习惯于自行选择技术，现在使用着来自 IBM、DEC 和 Control Data 的各种计算机和操作系统 (operating system)。因此，没有一套所有欧洲核子研究中心 (CERN) 计算机都能理解的统一网络协议 (networking protocols)。于是，伯纳斯-李 (Berners-Lee) 确保他的 RPC 系统支持多种网络协议 (networking protocols)。特别是，他确保支持 TCP/IP 协议套件，该协议当时只受到欧洲核子研究中心 (CERN) 的 Unix 用户群体的推崇，但伯纳斯-李 (Berners-Lee) 认为它潜力巨大。[^8] 正是在那时，正如伯纳斯-李 (Berners-Lee) 所写，“互联网 (Internet) 进入了我的生活。”[^9]

互联网 (Internet) 是促成万维网 (World Wide Web) 的第二项关键技术。在欧洲核子研究中心 (CERN) 的第二次任职初期，伯纳斯-李 (Berners-Lee) 曾零星地尝试重写 ENQUIRE，因为他看到欧洲核子研究中心 (CERN) 仍然需要一个像它这样的程序。[^10] 但 ENQUIRE 的封闭性限制太多。伯纳斯-李 (Berners-Lee) 开始思考是否可以将 ENQUIRE 与他为 RPC 项目开发的通信方案结合起来。一个依赖日益普及的 TCP/IP 标准的网络版 ENQUIRE，将允许欧洲核子研究中心 (CERN) 的研究人员不仅可以链接到自己计算机上的文档，还可以链接到其他所有计算机上的文档。至此，所有要素都已到位。伯纳斯-李 (Berners-Lee) 将他的想法告诉了经理迈克·森德尔 (Mike Sendall)。森德尔 (Sendall) 让他写一份提案。于是，在 1989 年，伯纳斯-李 (Berners-Lee) 照做了。

## 超文本 : 文本

伯纳斯-李 (Berners-Lee) 意识到欧洲核子研究中心 (CERN) 不太可能支持一个没有明确目的的研究项目，于是他将自己的想法包装成欧洲核子研究中心 (CERN) 急需的文档系统。随着大型强子对撞机 (Large Hadron Collider, LHC) 项目即将启动——如今，大型强子对撞机 (LHC) 是地球上最大的机器——欧洲核子研究中心 (CERN) 需要一种更好的方式来记录和组织信息。他提议的软件，暂定名为信息“网格” (information “mesh”)，将把欧洲核子研究中心 (CERN) 现有的众多文档系统整合为一个易于导航、可远程访问的超文本 (hypertext) 体系。重要的是，他的新系统不会对存储的数据施加任何人为的层级结构。这与埃德加·F·科德 (Edgar F. Codd) 有趣地呼应——他早在 [十年前](https://twobithistory.org/2017/12/29/codd-relational-model.html) 就展示了关系型数据库模型 (relational database model) 相较于当时流行的层级模型 (hierarchical models) 的诸多优势——伯纳斯-李 (Berners-Lee) 警告不要让层级存储方式对存储的信息施加不必要的限制。相反，用户应该能够在结构中的节点 (nodes) 之间任意创建链接。

伯纳斯-李 (Berners-Lee) 的 [原始提案](https://www.w3.org/History/1989/proposal.html) 技术细节不多，更像是一份哲学宣言而非技术方案。其中没有提及标记语言 (markup language)，甚至没有提及类似 HTTP 的任何东西，尽管伯纳斯-李 (Berners-Lee) 确实表示，项目的一个重要部分将是定义客户端 (clients) 和 服务器 (servers) 之间的接口。他最接近描述其系统实际工作方式的地方，是当他要求读者想象“本文档中的所有引用，都与它们所指向的网络地址相关联，这样在阅读本文档时，您只需点击鼠标即可跳转到它们。”今天阅读这份提案，我们很清楚伯纳斯-李 (Berners-Lee) 描述的是什么——那就是万维网 (World Wide Web)！但是，在 1989 年，要理解这个元文档系统究竟是什么，会很困难。据说森德尔 (Sendall) 在他的提案副本上写道，它“模糊但令人兴奋。”[^11]

也许这份提案最引人入胜的地方在于，至少在 1989 年，伯纳斯-李 (Berners-Lee) 似乎认为他将要创建一个支持网络的 ENQUIRE。他在提案首页包含的图表显示了多种不同类型的节点 (nodes)——有人物、概念、文档和软件程序——它们根据一组固定的关系连接起来。ENQUIRE 确实是这样工作的；你必须告诉它事物是如何关联的。节点 (nodes) 和链接都是*有类型的*。但万维网 (World Wide Web) 最终根本没有采用有类型的链接。ENQUIRE 的有类型链接和节点 (nodes) 有助于进行有趣的分析，因为理论上你可以问，例如，“有多少人在欧洲核子研究中心 (CERN) 的电子与计算物理部门工作？”在万维网 (World Wide Web) 上回答这类问题是不可能的。十年后，伯纳斯-李 (Berners-Lee) 和数百人曾 [尝试通过鼓励所有人使用语义网技术](https://twobithistory.org/2018/05/27/semantic-web.html) 来“带回”类型，但效果喜忧参半。令人着迷的是，万维网 (World Wide Web)，至少在最初构想时，从一开始就应该是语义网 (semantic web)。

![1989 年提案封面上的图表。](https://twobithistory.org/images/web_diagram.gif)

伯纳斯-李 (Berners-Lee) 将他的提案发给了欧洲核子研究中心 (CERN) 的几个人，但它大多被礼貌地忽视了。一年后，伯纳斯-李 (Berners-Lee) 比以往任何时候都更确信自己有所发现，他与欧洲核子研究中心 (CERN) 的资深员工罗伯特·卡约 (Robert Cailliau) 合作，用更具体的措辞重写了他的原始提案。[^12] [1990 年的提案](https://www.w3.org/Proposal.html) 侧重于构建伯纳斯-李 (Berners-Lee) 现在称之为“WorldWideWeb”的工作原型所需的资源。它还明确指出，该项目将包括创建，除其他之外，一种用于检索文档的标准协议 (standard protocol)、一种用于表示文档的标准格式 (standard format)，以及一个允许用户查看检索到的文本文档和可能包含图形 (graphics) 的程序。这份第二份提案使伯纳斯-李 (Berners-Lee) 能够组建一个小团队，开始创建万维网 (World Wide Web)。

伯纳斯-李 (Berners-Lee) 首先着手开发的是一个客户端 (client)。伯纳斯-李 (Berners-Lee) 的经理迈克·森德尔 (Mike Sendall) 刚刚允许他购买一台 NeXTSTEP 工作站 (workstation)。NeXTSTEP 是史蒂夫·乔布斯 (Steve Jobs) 被苹果公司 (Apple) 罢免后创立的 NeXT 公司生产的新操作系统 (operating system)。伯纳斯-李 (Berners-Lee) 决定，以其强大且易于使用的软件开发框架而闻名的 NeXTSTEP 系统，将使“浏览器 (browser)”程序的开发变得简单。[^13] 事实上，这个用 Objective-C 编写并利用最新编程范式（一种名为“面向对象编程 (object-oriented programming)”的东西）的框架，使得创建新子类 (subclass) 就像从现有 `Text` 类创建一个名为 `HyperText` 的新子类 (subclass) 一样简单。伯纳斯-李 (Berners-Lee) 编写的其他类都带有 `HT` 前缀，代表超文本 (hypertext)，因为在使用 NeXTSTEP 的应用程序框架时，给类名加前缀是一种惯例。如果这听起来很熟悉，那是因为 NeXT 最终被苹果公司 (Apple) 收购了。如今 iOS 和 Mac 开发者非常熟悉的 AppKit 框架，正是伯纳斯-李 (Berners-Lee) 用来构建第一个网页浏览器 (browser) 的框架的现代版本。伯纳斯-李 (Berners-Lee) 的浏览器 (browser) `WorldWideWeb.app` 甚至有一个 [应用程序委托](https://github.com/sinclairtarget/www-beginnings/blob/master/1991-WWW-NeXT/Implementation/HyperManager.m) (application delegate)。

伯纳斯-李 (Berners-Lee) 必须编写的另一部分软件是一个基本的 HTTP 服务器 (HTTP server)。那段代码最终被称为 CERN HTTPd。最初的版本运行在 NeXT 系统和一种名为 VAX/VMS 的操作系统 (operating system) 上，该系统由 Digital Equipment Corporation 开发，在欧洲核子研究中心 (CERN) 的一些人中很受欢迎。最初的版本只有一个文件，名为 [daemon.c](https://github.com/sinclairtarget/www-beginnings/blob/master/cern-httpd/v0.1/daemon.c)，非常值得一读。默认情况下，第一个 HTTP 服务器 (HTTP server) 运行在 2784 端口 (port) 上，只支持 GET 请求 (GET requests) 和另一种名为 FIND 的请求。它实现了 [原始的 HTTP 规范](https://www.w3.org/Protocols/HTTP/AsImplemented.html)。

很快，伯纳斯-李 (Berners-Lee) 就有了一个客户端 (client) 和一个服务器 (server) 使用 HTTP 相互通信。但他构建的网页浏览器 (browser) 只能在 NeXT 机器上运行，尽管 NeXT 在计算领域留下了深远影响，但它实际上并不那么受欢迎。这让伯纳斯-李 (Berners-Lee) 感到困扰，因为拥有一个万维网 (World Wide Web) 的全部意义在于它的普适性。一个只能在一个系统上运行的网页浏览器 (browser) 无法很好地展示万维网 (World Wide Web) 的潜力。因此，在另一位欧洲核子研究中心 (CERN) 员工本·西格尔 (Ben Segal) 的建议下，伯纳斯-李 (Berners-Lee) 聘请了一位名叫尼古拉·佩洛 (Nicola Pellow) 的实习生来创建一个他们称之为“行模式浏览器 (line-mode browser)”的东西。[^14] 行模式浏览器 (line-mode browser) 将是纯文本的，这使得它很容易移植到许多不同的系统上。现在很少有人记得行模式浏览器 (line-mode browser) 了，但更多的人是通过行模式浏览器 (line-mode browser) 而非伯纳斯-李 (Berners-Lee) 最初的 NeXT 浏览器 (browser) 首次接触到万维网 (World Wide Web)。行模式浏览器 (line-mode browser) 的酷炫之处在于，欧洲核子研究中心 (CERN) 最近创建了一个它的 [模拟](http://line-mode.cern.ch/www/hypertext/WWW/TheProject.html) 版本，所以如果你觉得在 1991 年那样浏览万维网 (World Wide Web) 很有趣，现在就可以做到。

## 万维网走向公众

伯纳斯-李 (Berners-Lee) 首次向欧洲核子研究中心 (CERN) 以外的人介绍万维网 (World Wide Web)，是在 1991 年 8 月向 alt.hypertext 新闻组 (newsgroup) [发布的一篇文章](https://www.w3.org/People/Berners-Lee/1991/08/art-6484.txt) 中。他当时正在回应别人提出的一个问题，即是否有人正在开发一个可以从“异构 (heterogeneous)”来源检索信息的超文本 (hypertext) 系统。在这篇文章中，伯纳斯-李 (Berners-Lee) 阐述了“WorldWideWeb”项目迄今为止所做的工作，并邀请任何有兴趣查看代码的人给他发电子邮件。

同年 9 月，万维网 (World Wide Web) 从欧洲传播到斯坦福直线加速器中心 (Stanford Linear Accelerator Center)。从那里，它又传播到世界各地的其他研究中心。其他人开始为不同的操作系统 (operating system) 制作自己的网页浏览器 (browser)，其中一些网页浏览器 (browser) 比伯纳斯-李 (Berners-Lee) 最初的浏览器 (browser) 有了显著改进。1993 年，伊利诺伊州国家超级计算应用中心 (National Center for Supercomputing Applications) 的一个年轻研究生团队创建了 Mosaic，它的一项重要成就是成为第一个能够内联显示图像 (display images inline) 而不是在单独窗口中显示的浏览器 (browser)。Mosaic 安装和使用都非常简单，它极大地推动了万维网 (World Wide Web) 的普及，并有效地开启了互联网时代 (internet age)。

到 Mosaic 发布时，万维网 (World Wide Web) 早已不再由伯纳斯-李 (Berners-Lee) 一人掌控。在未来的岁月里，其他人将对其演变和发展产生更大的影响。但万维网 (World Wide Web) 当然永远会被铭记为伯纳斯-李 (Berners-Lee) 的发明。

还有其他人能发明万维网 (World Wide Web) 吗？正如新技术有时会发生的那样，在 1989 年，万维网 (World Wide Web)——或者至少是类似的东西——似乎几乎是不可避免的。人们对超文本 (hypertext) 的兴趣日益增长，与此同时 TCP/IP 也使得不同的计算机系统更容易相互通信。alt.hypertext 新闻组 (newsgroup) 上关于超文本 (hypertext) 连接“异构 (heterogeneous)”系统的问题表明，其他人也开始看到这种系统的潜力。然而，像特德·尼尔森 (Ted Nelson) 这样的人花费了数年时间试图创建一个通用的超文本 (hypertext) 系统，却一无所获。伯纳斯-李 (Berners-Lee) 足够幸运，在短时间内接触并研究了超文本 (hypertext) 系统、标记语言 (markup language) 和 RPC 协议，这使他具备独特的优势，能够将这些零散的线索汇集起来。如果没有伯纳斯-李 (Berners-Lee)，一个“网络”最终可能也会出现，但可能要再过几年，而且它可能不会像伯纳斯-李 (Berners-Lee) 赋予我们的自由开放的万维网 (World Wide Web) 那样。

*如果您喜欢这篇文章，每四周会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保您能及时了解新文章的发布。*

[^1]: Coover, Robert. “The End of Books.” The New York Times, June 21, 1992\. Accessed June 2, 2018, [https://archive.nytimes.com/www.nytimes.com/books/98/09/27/specials/coover-end.html?pagewanted=all](https://archive.nytimes.com/www.nytimes.com/books/98/09/27/specials/coover-end.html?pagewanted=all).
[^2]: Berners-Lee, Tim, and Mark Fischetti. *Weaving the Web: The Original Design and Ultimate Destiny of the World Wide Web*. (Harper Business, 2000), 3.
[^3]: Berners-Lee, 9.
[^4]: ibid.
[^5]: Berners-Lee, 1.
[^6]: Berners-Lee, 11.
[^7]: Berners-Lee, 12.
[^8]: Berners-Lee, 19.
[^9]: ibid.
[^10]: Berners-Lee, 15.
[^11]: “Tim Berners-Lee’s Proposal”. CERN, accessed June 10, 2018, <http://info.cern.ch/Proposal.html>.
[^12]: Berners-Lee, 26.
[^13]: Berners-Lee, 23.
[^14]: Berners-Lee, 29.