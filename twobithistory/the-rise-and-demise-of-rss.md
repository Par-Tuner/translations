# 翻译 | RSS 的兴起与衰落
原文：[The Rise and Demise of RSS](https://twobithistory.org/2018/12/18/rss.html)

_本文初版发布于 [2018年9月16日](https://twobithistory.org/2018/09/16/the-rise-and-demise-of-rss.html)。此为修订版，增补了对 Ramanathan Guha、Ian Davis、Dan Libby 和 Kevin Werbach 的访谈内容。_

_本文的另一个版本也曾发表于 [Vice News](https://www.vice.com/en_us/article/a3mm4z/the-rise-and-demise-of-rss)。_

大约在十年多前，随便一位网民可能都听说过 RSS。RSS 的全称有两个版本，你可以叫它“真正简单的整合” (Really Simple Syndication)，也可以叫它“丰富站点摘要” (Rich Site Summary)，这取决于你问的是谁。它是一种标准，网站和播客可以通过它向用户提供内容订阅源，并且这种格式能被各种各样的电脑程序轻松解析。然而时至今日，尽管 RSS 仍在为网络上的许多应用提供着动力，但对大多数人来说，它已经成了一门鲜为人知的“古老”技术。

要说清 RSS 的故事，我们得从两条线索讲起。第一条线索，是关于一个宏大却从未完全实现的Web未来构想。第二条线索，则是一场本想齐心协力改进流行标准的技术合作，最终如何演变成了开源软件开发史上最激烈的“路线之争”之一。

时间回到上世纪 90 年代末，那是一个介于 Netscape 上市和互联网泡沫破灭之间的狂飙突进的年代。所有人都预感到，互联网将掀起比以往更巨大的浪潮，尽管没人能确切说出浪潮将涌向何方。当时有一种流行的理论：内容整合 (syndication) 将彻底改变整个 Web。最初，Web 的设计只是为了实现一次简单的双方交易——客户端从一台主机服务器上获取一份文档。但新的标准将打破这一模式，它允许人们将整个网站的内容重新打包，通过五花八门的渠道再次分发。Kevin Werbach 在当时极具投资者影响力的时事通讯 _Release 1.0_ 中预言，内容整合“将演化为互联网经济的核心模型，让企业和个人既能掌控自己的线上形象，又能享受到巨大规模和范围带来的红利。”[^1]

他邀请读者想象这样一幅未来图景：一位击剑爱好者想买一把新重剑，他不必再访问“在线体育用品商店”或“击剑器材零售商”的网站，而是可以直接在他最喜欢的击剑主题网站上，通过嵌入的电子商务插件完成购买。[^2] 这就像电视界的大型电视网将节目授权给地方小电视台播放一样，Web 上的内容整合能让商家和媒体通过无数个中间站点触达消费者。而这自然也意味着，消费者将获得前所未有的控制权，可以自由选择在何时、何地、以何种方式与商家或媒体互动。

RSS，正是当年被寄予厚望、能够实现这一“整合未来”的标准之一。在 Werbach 看来，RSS 是“轻量级内容整合协议的杰出代表”。[^3] 同一时期的另一篇文章则称 RSS 是首个真正发挥出 XML 潜力的协议。[^4] 无论是普通用户还是内容聚合平台，都可以利用它，从浩如烟海的 Web 信息中打造出属于自己的个性化频道。然而二十年过去了，社交媒体巨头崛起，Google Reader 也被送进了坟墓，RSS 似乎成了一项 [日渐式微的技术](https://trends.google.com/trends/explore?date=all\&geo=US\&q=rss)，如今只有播客作者、技术博主和少数记者还在使用它。当然，还是有一小撮人顽固地坚守着 RSS 阅读器。但在 2018 年的今天，给自己的博客加上 RSS 订阅选项，本身就是一种政治姿态。那个小小的橙色图标，已经成为一个怀旧的符号，象征着对那个由少数几家公司控制的中心化网络的无声反抗——这个网络，与 Werbach 当年想象的整合世界，早已判若云泥。

RSS 的未来曾一片光明。到底发生了什么？它的衰落是历史的必然，还是那场阻碍其标准统一的激烈内斗加速了它的灭亡？

## 浑水

RSS 其实被发明了两次。这意味着它从未有过一个明确的“主人”，这种权责不清的局面引发了无尽的争论和敌意。但这也恰恰说明，RSS 是一个顺应时代潮流的重要思想。

1998 年，Netscape 正挣扎于生死存亡之秋，苦苦思索着公司的未来。它的旗舰产品——曾占据超过 80% 市场份额的 Netscape Navigator 浏览器——正被 Microsoft 的 Internet Explorer 迅速蚕食。于是，Netscape 决定开辟新战场。当年 5 月，公司集结了一个团队，启动了内部代号为“60号项目”的计划。[^5] 两个月后，Netscape 推出了名为“My Netscape”的门户网站，意图与 Yahoo、MSN 和 Excite 等当时的门户巨头一较高下。

第二年三月，Netscape 为 My Netscape 门户网站增加了一项新功能，名为“My Netscape Network”。用户可以在自己的 My Netscape 页面上进行个性化定制，添加来自全网各大站点的“频道”，展示最新的头条新闻。只要你喜欢的网站按照 Netscape 的规定格式发布一个特殊文件，你就能把它添加到你的 My Netscape 页面上。通常，参与的网站会在页面上放置一个“添加频道”的按钮，用户点击一下，一个包含最新链接标题的小窗口就会出现在他们的门户页上。

![一个 My Netscape Network 频道](https://s1.ax1x.com/2018/09/22/iupTPJ.gif) 

_图注：一个 Mozilla.org 的 My Netscape Network 频道，在用户即将把它添加到 My Netscape 页面时大概就是这个样子。_

网站们需要发布的那个特殊文件，就是一个 RSS 文件。在 My Netscape Network 的发布公告中，Netscape 解释说 RSS 是“RDF 站点摘要” (RDF Site Summary) 的缩写。[^6] 这个名字其实有点误导人。RDF，即资源描述框架 (Resource Description Framework)，本质上是一种用来描述任意资源属性的语法。(如果你对此很感兴趣，可以读读我那篇关于 [语义网 (Semantic Web) 的文章](/2018/05/27/semantic-web.html)。) 1999 年，万维网联盟 (W3C)——Web 世界的主要标准制定机构——正在审议 RDF 的规范草案。尽管 RSS 号称基于 RDF，但 Netscape 发布的示例文件里却根本没用任何 RDF 标签。RSS 规范的作者之一 Dan Libby 在一份配套文档中解释说：“在 MNN 的这个版本里，Netscape 有意限制了 RSS 格式的复杂性。”[^7] 该规范的版本号被定为 0.90，言下之意是，后续版本会让 RSS 逐渐向 W3C 的 XML 规范和不断演进的 RDF 规范草案看齐。

RSS 是由 Libby 和另外两位 Netscape 员工 Eckart Walther、Ramanathan Guha 共同创造的。根据 Guha 在邮件中的回忆，最初是他和 Walther 在 Libby 的一些建议下捣鼓出了 RSS 的雏形。1998 年 AOL 收购 Netscape 后，他和 Walther 相继离开，RSS 的后续发展就落到了 Libby 肩上。在加入 Netscape 之前，Guha 曾在 Apple 公司工作，并提出了一个名为“元内容框架” (Meta Content Framework, MCF) 的概念。MCF 是一种用来表示元数据 (metadata) 的格式，无论是网页还是本地文件，它都能描述。为了展示其威力，Guha 开发了一款名为 [HotSauce](http://web.archive.org/web/19970703020212/http://mcf.research.apple.com:80/hs/screen_shot.html) 的应用，能将文件间的关系以三维空间中悬浮的节点网络形式可视化。离开 Apple 加入 Netscape 后，Guha 立即与一位名叫 Tim Bray 的顾问合作。Bray 在博客中提到，他和 Guha 最终做出了一个基于 XML 的 MCF 版本，而这个版本又成了 W3C 的 RDF 草案的基础。[^8] 毫无疑问，Guha、Walther 和 Libby 都希望能延续 Guha 此前的工作，将 RDF 融入 RSS。但 Libby 后来写道，由于时间紧迫，加上当时普遍认为 RDF 对“普通用户”来说“太复杂”，最初那个基于 RDF 的宏大构想最终被打了折扣。[^9]

就在 Netscape 投身于后来被称为“门户大战”的流量争夺战时，一种名为“网络日志” (weblogging) 的新事物正在 Web 的另一角悄然兴起。[^10] Dave Winer 便是其中的一位先驱。他是 UserLand Software 公司的 CEO，这家公司开发的早期内容管理系统，让许多不精通技术的人也能轻松写博客。Winer 自己也运营着一个博客，名为 [Scripting News](http://scripting.com)，至今仍是互联网上最古老的博客之一。早在 Netscape 发布 My Netscape Network 的一年多前，即 1997 年 12 月 15 日，Winer 就宣布他的博客将同时提供 XML 和 HTML 两种格式。[^11]

Dave Winer 的这种 XML 格式后来被称为 Scripting News 格式。据说它和 Microsoft 的“频道定义格式” (Channel Definition Format, 一种在 1997 年 3 月提交给 W3C 的“推送技术”标准) 很相似，但我没能找到原始文件来证实这一点。[^12] 和 Netscape 的 RSS 一样，它也将 Winer 博客的内容结构化，以便其他软件能够理解。当 Netscape 发布 RSS 0.90 后，Winer 和他的 UserLand Software 公司开始同时支持这两种格式。但 Winer 认为 Netscape 的格式“严重不足”，并且“缺少了网站作者和读者最需要的东西”。[^13] Netscape 的格式只能呈现一个链接列表，而 Scripting News 格式却能呈现一系列段落，每个段落里还可以包含一个或多个链接。

1999 年 6 月，也就是 Netscape 宣布 My Netscape Network 两个月后，Winer 推出了 Scripting News 格式的新版本——ScriptingNews 2.0b1。Winer 声称，他之所以决定自己动手，是因为他曾试图让 Netscape 的人关注 RSS 0.90 的缺陷，但却无人理睬。[^14] 新版的 Scripting News 格式在 `<header>` 元素中增加了几项，使其在功能上与 RSS 看齐。但两者依然存在一个关键区别：Winer 戏称为“胖”整合格式的 Scripting News，可以包含完整的段落，而不仅仅是链接。

Netscape 紧接着在下个月就发布了 RSS 0.91。这次的更新堪称一次 180 度大转弯。RSS 不再是“RDF 站点摘要”的缩写，而是变成了“丰富站点摘要”。所有的 RDF 元素——本来也几乎没有——被悉数移除，同时吸收了许多 Scripting News 格式的标签。在新规范的说明中，Libby 这样解释：

> RDF 相关引用已被移除。RSS 最初的构想是作为一种提供网站摘要的元数据格式。但现在两点已经很明确：首先，内容提供者更需要的是一种内容整合格式，而非元数据格式。RDF 文件的结构非常严谨，必须遵循 RDF 数据模型才能生效，这对人类来说不易理解，也让创建有用的 RDF 文件变得困难。其次，市面上几乎没有可用于生成、验证和处理 RDF 的工具。基于这些原因，我们决定采用标准的 XML 方式。[^15]

Winer 对 RSS 0.91 极为满意，称其“比我预想的还要好”。[^16] UserLand Software 公司随即采用它取代了自家的 ScriptingNews 2.0b1 格式。在当时看来，RSS 似乎终于有了一份统一的、权威的规范。

## 大分裂

一年之后，RSS 0.91 规范也显得捉襟见肘了。人们想用 RSS 做各种各样的事情，但规范却无法满足需求。规范中的某些限制也显得毫无必要——比如，每个 RSS 频道最多只能包含 15 个项目。

到那时，已经有更多的组织采纳了 RSS。除了在 0.91 版本后就似乎兴味索然的 Netscape，牌桌上的主要玩家包括 Dave Winer 的 UserLand Software、运营着 RSS 聚合器 Meerkat 的 O’Reilly Net，以及同样运营着新闻类 RSS 聚合器的 Moreover.com。[^17] 这些组织的代表们通过邮件列表，定期讨论如何改进 RSS 0.91。但在改进的方向上，他们之间存在着深刻的分歧。

这场讨论主要发生在一个名为“整合” (Syndication) 的邮件列表里。[该邮件列表的存档](https://groups.yahoo.com/neo/groups/syndication/info) 至今仍可访问，是一份惊人的历史资料。它逐分逐秒地记录了这些深刻的分歧最终如何撕裂了整个 RSS 社区。

站在这场分裂风暴一侧的，是 Winer。他迫切地想要推动 RSS 的演进，但只希望以一种相对保守的方式进行。2000 年 6 月，他在 UserLand 网站上发布了自己版本的 RSS 0.91 规范，作为后续开发的起点。这个版本与 Netscape 发布的 0.91 规范相比，并无重大改动。Winer 在一篇配套的博客文章中声称，这只是一次“清理”工作，旨在记录 RSS 在实际应用中的情况，因为 Netscape 的官方规范已经无人维护。[^18] 在同一篇文章中，他坚称 RSS 之所以成功，关键在于其简单性。他认为，如果在格式中重新加入命名空间 (namespaces，一种区分不同 RSS 词汇的方式) 或 RDF——这是邮件列表里一些人的提议——将会“使其变得极其复杂，恕我直言，对于内容提供者来说，这种复杂性几乎带不来任何好处。” 在差不多同一时间发给“整合”邮件列表的一封邮件中，Winer 暗示这些分歧非常严重，甚至可能导致他另起炉灶：

> 我仍在思考如何推动 RSS 向前发展。我非常希望在 RSS2 中加入类似 ICE 的功能，发布和订阅是我的重中之重，但我会为了保持简单性而斗争到底。我喜欢可选元素。我不想走上命名空间和模式 (schema) 的道路，也不想把它变成 RDF 的一种方言。我理解其他人想这么做，所以，我猜我们最终会走向分裂 (fork)。对于另一条路会通向何方，我有自己的看法，但至少现在，我会保留这些看法。[^19]

与 Winer 对立的是另外几位人物，包括 O’Reilly 的 Rael Dornfest、搜索创业公司 Calaba 的负责人 Ian Davis，以及一位年仅 14 岁的早慧少年 Aaron Swartz。没错，就是后来共同创办了 Reddit 并以其黑客行动主义闻名的那个 Aaron Swartz。(据 Davis 在邮件中回忆，2000 年时，他父亲还经常陪他参加技术圈的聚会。) Dornfest、Davis 和 Swartz 都认为，为了满足五花八门的应用需求，RSS 必须引入命名空间。在 O’Reilly 主持的另一个邮件列表里，Davis 提出了一个基于命名空间的模块化系统，他写道，这样的系统能“让 RSS 随心所欲地扩展，而不是硬塞进各种新功能，把规范搞得越来越复杂。”[^20] “命名空间阵营”相信，RSS 的用途很快将远不止于聚合博客文章，因此，命名空间非但不是累赘，反而是防止 RSS 在支持越来越多用例后变得难以管理的唯一出路。

对命名空间的分歧，其根源在于对 RSS 究竟为何物这一根本问题的不同理解。Winer 当初发明 Scripting News 格式，是为了聚合自己博客的文章。Netscape 发布 RSS 时称其为“RDF 站点摘要”，是想在 My Netscape 门户里微缩式地重建一个个网站。有些人觉得，应该尊重 Netscape 最初的愿景。Davis 在给“整合”邮件列表的信中阐述了他的观点：RSS“最初的构想是用来建立迷你版的网站地图”，而现在，他和同伴们希望扩展 RSS，“使其能包含新闻标题之外更多类型的信息，并满足过去 12 个月里涌现出的新用途。”[^21] 这个观点不无道理，因为 Netscape 的 RSS 项目最初的目标甚至比 Davis 描述的还要宏大：Guha 曾告诉我，他想创造一种技术，不仅能支持网站频道，还能支持关于任意实体 (比如歌手麦当娜) 的信息源。从这个角度看，进一步发展 RSS 以实现这一目标，确实符合其初衷。但 Davis 的论点也夸大了 Netscape 在发布 RSS 规范时内部愿景的统一程度。据我与 Libby 的邮件交流，即便在 Netscape 内部，最终也分裂为“我们来构建语义网吧”和“我们把它做得简单点，方便大家用”两个派别。

而 Winer 则认为，Netscape 最初的目标根本不重要，因为他的 Scripting News 格式才是 RSS 的鼻祖，且其初衷截然不同。鉴于 RSS 开发的核心参与者们在“谁创造了 RSS”以及“为何创造”这两个根本问题上都无法达成一致，分裂似乎已在所难免。

当 Dornfest 宣布了一份提议中的 RSS 1.0 规范，并组建了 RSS-DEV 工作组来筹备发布时，分裂最终发生了。这个工作组里有 Davis、Swartz 和其他几位成员，但没有 Winer。在提议的规范中，RSS 的全称又变回了“RDF 站点摘要”，因为 RDF 被重新引入，用于表示某些 RSS 元素的元数据属性。规范指名道姓地感谢了 Winer，称赞他通过“传道式”的热情推广了 RSS。[^22] 但规范也指出，RSS 不能按照 Winer 倡导的方式去改进。仅仅向 RSS 添加更多元素，而不通过模块系统提供可扩展性，将“牺牲其可伸缩性 (scalability)”。规范接着定义了一套基于 XML 命名空间的 RSS 模块系统。

Winer 觉得 RSS-DEV 工作组擅自取名“RSS 1.0”是“不公平的”。[^23] 在另一个关于去中心化的邮件列表里，他写道自己“最近有个标准被一个大牌给偷了”，矛头直指召集了 RSS-DEV 工作组的 O’Reilly。[^24] “整合”邮件列表里的其他成员也认为，在社区就 RSS 的未来达成一致之前，RSS-DEV 工作组不该使用“RSS”这个名字。但工作组坚持己见。工作组的另一位成员 Dan Brickley 辩护道：“我们提议的 RSS 1.0 牢牢植根于 RSS 的最初愿景，而这一愿景本身可以追溯到 MCF (RDF 的前身) 和其他相关规范 (如 CDF) 的悠久传统。”[^25] 他基本上认为，既然 RDF 本就是 RSS 的一部分，那么 RSS 1.0 的努力比 Winer 更有资格继承“RSS”这个名号。RSS-DEV 工作组在当年 12 月发布了规范的最终版。同月，Winer 在 UserLand 网站上发布了他自己对 RSS 0.91 的改进版，命名为 RSS 0.92。RSS 0.92 对 RSS 做了一些小的、可选的改进，其中就包括了后来被播客界广泛采用的 `<enclosure>` 标签。至此，RSS 正式分裂。

如果当初能更努力地将 Winer 纳入 RSS-DEV 工作组，这场分裂或许本可避免。他显然是理应在席的。他是“整合”邮件列表的杰出贡献者，对 RSS 的普及功不可没，这一点连工作组成员自己都承认。但正如 Davis 在邮件中所写，Winer“想要控制权，希望 RSS 成为他的个人遗产，所以不愿与我们合作。” O’Reilly 的创始人兼 CEO Tim O’Reilly 在 2000 年 9 月的一个 UserLand 讨论组中解释说，Winer 基本上是拒绝参与合作：

> 一群参与 RSS 的人聚在一起，开始思考它的未来发展。Dave 也是其中一员。但当团队的共识转向了他不喜欢的方向时，Dave 就退出了，并把这描绘成 O’Reilly 企图从他手中夺取 RSS 的阴谋，尽管 O’Reilly 的 Rael Dornfest 只是 RSS 1.0 提案的十几位作者之一，而且许多参与开发的成员在 RSS 领域的资历至少和 Dave 一样长。[^26]

对此，Winer 回应道：

> 在他们宣布的两周前，我见了 Dale [Dougherty]，他压根没提要叫 RSS 1.0。在宣布前的那个周五，我和 Rael 通了电话，他也只字未提他们要叫它 RSS 1.0。我是直到公之于众时才第一次听说。
>
> 让我直接问你一个问题。如果事实证明，将新规范命名为“RSS 1.0”的计划是私下决定的，没有任何事先通知或协商，也没给‘整合’邮件列表的成员们——不只是我——任何同意或反对的机会，你打算怎么办？
>
> UserLand 为了创造、推广和支持 RSS 付出了巨大努力。我们放弃了这些，让你们的人拿走了这个名字。这是最根本的问题。如果我今后想在 Web 整合领域做任何事，我都得用一个新名字。Tim，这到底是为什么，又是怎么发生的？[^27]

我没能在“整合”邮件列表的存档中找到任何在 RSS 1.0 提案公布前关于命名问题的讨论。Winer 在给我的消息中表示，他并非想控制 RSS，只是想在自己的产品里使用它。

2003 年，RSS 再次分裂。几位对 RSS 社区无休止的争吵感到厌倦的开发者，试图创造一种全新的格式。他们创造了 Atom，一种摒弃了 RDF 但拥抱了 XML 命名空间的格式。Atom 最终由 [一项提议的 IETF 标准](https://tools.ietf.org/html/rfc4287) 进行了规范。Atom 诞生后，市面上出现了三个相互竞争的 RSS 版本：Winer 的 RSS 0.92 (于 2002 年升级为 RSS 2.0，并更名为“真正简单的整合”)、RSS-DEV 工作组的 RSS 1.0，以及 Atom。

## 衰落

多个 RSS 规范并存的局面，可能从其他方面也阻碍了 RSS 的发展，这一点我稍后会谈到。但这并没能阻止 RSS 在 21 世纪的头十年里风靡一时。到 2004 年，《纽约时报》开始用 RSS 提供头条新闻，并专门刊文向普通读者解释什么是 RSS 以及如何使用它。[^28] 2005 年，最终拥有数百万用户的 RSS 聚合器 Google Reader 问世。到 2013 年，RSS 的普及程度似乎让《纽约时报》在为 Aaron Swartz 撰写的讣告中，称其为一项“无处不在”的技术。[^29] 曾几何时，在地球上三分之一的人口注册 Facebook 之前，RSS 就是许多人获取互联网新闻的主要方式。

《纽约时报》发表 Swartz 讣告是在 2013 年 1 月。但实际上，RSS 在那时已经盛极而衰，正一步步走向默默无闻。2013 年 7 月，Google Reader 被关闭，官方给出的理由是用户数“连年下滑”。[^30] 此举引发了各大媒体纷纷发文，宣告 RSS 的死亡。但其实，早在 Google Reader 关闭前，唱衰 RSS 的声音就已持续多年。2009 年 5 月，Steve Gillmor 在 TechCrunch 上撰文建议：“是时候彻底告别 RSS，转向 Twitter 了”，因为“RSS 已经跟不上时代了”。[^31] 他指出，Twitter 本质上就是一个更强大的 RSS 源，因为它不仅能推送文章，还能让你看到大家对文章的看法。它让你关注的是“人”，而不仅仅是“频道”。Gillmor 告诉读者，是时候让 RSS 退居幕后了。他以 Bob Dylan《永远年轻》中的一句歌词结束了文章。

今天，RSS 并未消亡。但它也远没有了往日的辉煌。关于 RSS 为何失宠，众说纷纭。其中最有说服力的解释，或许正是 Gillmor 在 2009 年提出的那个。社交网络，和 RSS 一样，为用户提供了一个聚合互联网最新资讯的信息流。社交网络之所以能取而代之，仅仅因为它们是“更好”的信息流。同时，它们也为背后的公司带来了更多利益。例如，有人指责 Google 关闭 Reader 是为了将用户赶向自家的 Google+。Google 也许能从 Google+ 上找到变现模式，但这种模式在 Google Reader 上是绝无可能的。Instapaper 的创始人 Marco Arment 在 2013 年的博客中写道：

> Google Reader 不过是 Facebook 无意间挑起的那场战争的最新牺牲品：一场旨在‘拥有一切’的战争。虽然 Google 在技术上确实‘拥有’Reader，也能利用流经其中的海量新闻和用户关注度数据，但这与其更重要的 Google+ 战略发生了冲突。他们需要每个人都通过 Google+ 来阅读和分享一切，这样才能在广告定位数据、广告收入、用户增长和市场影响力上与 Facebook 抗衡。[^32]

所以，无论是用户还是科技公司，都发现从社交网络中获得的价值远超 RSS。

另一种理论认为，RSS 对普通人来说，门槛一直太高，太过“极客化” (geeky)。即便是当年积极拥抱并向读者推广 RSS 的《纽约时报》，也在 2006 年抱怨说，RSS 是个由“电脑极客”发明的“不怎么用户友好”的缩写。[^33] 在 2004 年那个橙色的 RSS 图标诞生之前，《纽约时报》等网站用来链接其 RSS 源的，是一个标着“XML”的小方块，这足以吓退大部分普通用户。[^34] 不过这个标签倒是完全准确，因为在那个年代，点开链接，一个倒霉的用户看到的将是一整页天书般的 XML 代码。[这条精彩的推文](https://twitter.com/mgsiegler/status/311992206716203008) 精辟地概括了这种观点。普通人从未对使用 RSS 感到自在；它从设计之初就不是面向消费者的技术，使用起来障碍重重；一旦有更好的替代品出现，人们便会毫不犹豫地“跳船”。

如果能得到持续发展，RSS 或许本可以克服这些局限。也许 RSS 可以扩展出新功能，让订阅了同一频道的朋友们能互相分享对某篇文章的看法。也许浏览器能提供更好的原生支持。但是，当 Facebook 这样的公司能够“快速行动，打破常规” (move fast and break things) 时，RSS 的开发者社区却被困在寻求共识的泥潭里。当他们无法就统一标准达成一致时，本可用于改进 RSS 的精力，却被浪费在无休止的重复造轮子上。例如，Davis 告诉我，如果当初“整合”邮件列表的成员们能够妥协协作，Atom 本无诞生的必要，“所有那些整理完善的工作本可以投入到 RSS 中，使其变得更强大。” 所以，如果我们探究 RSS 为何不再流行，最直接的解释是社交网络取代了它。但如果我们再深究一层，问为什么社交网络能取代它，答案或许是：那些试图让 RSS 成功的人们，面临着一个比（比如说）打造一个 Facebook 要困难得多的问题。正如 Dornfest 曾一度在“整合”邮件列表里写道：“目前来看，真正复杂的远非技术实现，而是政治。”[^35]

于是，今天我们面对的是一个个信息被中心化平台分割的孤岛。即便如此，Werbach 在 1999 年预见的那种“整合网络”其实已经实现了，只是方式与他设想的大相径庭。毕竟，像 _The Onion_ 这样的媒体，不正是依赖于通过 Facebook 和 Twitter 进行内容分发，就像经典美剧《宋飞正传》在首播结束后依靠电视联播大赚数亿美元一样吗？我问 Werbach 对此有何看法，他基本表示同意。他告诉我，从一个层面看，RSS 显然是失败了，因为它如今“并非博客圈、内容界或信息聚合领域的核心技术”。但从另一个层面看，“整个社交媒体革命，其核心之一就是聚合不同内容与资源的能力”，这与 RSS 的理念以及他最初对整合网络的构想遥相呼应。对 Werbach 而言，“这是 RSS 的遗产，即便它并非构建于 RSS 之上。”

不幸的是，当今 Web 上的内容整合，依旧只能通过那几家巨头渠道进行，这意味着我们没有人能像 Werbach 想象的那样，“保留对我们在线角色的控制”。造成这一局面的原因之一，是司空见惯的商业贪婪——RSS 作为一个开放格式，无法给予科技公司售卖广告所需的数据和流量控制权，因此得不到它们的支持。但更平淡无奇的原因是，构建中心化的信息孤岛，远比设计一个通用的公共标准要容易。达成共识困难重重且耗时漫长，而一旦没有共识，被冷落的开发者便会出走，创造相互竞争的标准。这或许给我们的教训是：如果我们想要一个更好、更开放的 Web，我们必须学会如何更好地与彼此协作，而不是互相拆台。


[^1]: Kevin Werbach, “The Web Goes into Syndication,” Release 1.0, July 22, 1999, 1, accessed September 14, 2018, <http://cdn.oreillystatic.com/radar/r1/07-99.pdf>.

[^2]: ibid（同上）.

[^3]: Werbach, 8.

[^4]: Peter Wiggin, “RSS Delivers the XML Promise,” Web Review, October 29, 1999, accessed September 14, 2018, <https://people.apache.org/~jim/NewArchitect/webrevu/1999/10_29/webauthors/10_29_99_2a.html>.

[^5]: Ben Hammersley, RSS and Atom (O’Reilly), 8, accessed September 14, 2018, <https://books.google.com/books?id=kwJVAgAAQBAJ>.

[^6]: “RSS 0.90 Specification,” RSS Advisory Board, accessed September 14, 2018, <http://www.rssboard.org/rss-0-9-0>.

[^7]: “My Netscape Network Future Directions,” RSS Advisory Board, accessed September 14, 2018, <http://www.rssboard.org/mnn-futures>.

[^8]: Tim Bray, “The RDF.net Challenge,” Ongoing by Tim Bray, May 21, 2003, accessed September 14, 2018, <https://www.tbray.org/ongoing/When/200x/2003/05/21/RDFNet>.

[^9]: Dan Libby, “RSS: Introducing Myself,” August 24, 2000, RSS-DEV Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/239>.

[^10]: Alexandra Krasne, “Browser Wars May Become Portal Wars,” CNN, accessed September 14, 2018, <http://www.cnn.com/TECH/computing/9910/04/portal.war.idg/index.html>.

[^11]: Dave Winer, “Scripting News in XML,” Scripting News, December 15, 1997, accessed September 14, 2018, <http://scripting.com/davenet/1997/12/15/scriptingNewsInXML.html>.

[^12]: Joseph Reagle, “RSS History,” 2004, accessed September 14, 2018, <https://reagle.org/joseph/2003/rss-history.html>.

[^13]: Dave Winer, “A Faceoff with Netscape,” Scripting News, June 16, 1999, accessed September 14, 2018, <http://scripting.com/davenet/1999/06/16/aFaceOffWithNetscape.html>.

[^14]: ibid.

[^15]: Dan Libby, “RSS 0.91 Specification (Netscape),” RSS Advisory Board, accessed September 14, 2018, <http://www.rssboard.org/rss-0-9-1-netscape>.

[^16]: Dave Winer, “Scripting News: 7/28/1999,” Scripting News, July 28, 1999, accessed September 14, 2018, <http://scripting.com/1999/07/28.html>.

[^17]: Oliver Willis, “RSS Aggregators?” June 19, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/173>.

[^18]: Dave Winer, “Scripting News: 07/07/2000,” Scripting News, July 07, 2000, accessed September 14, 2018, <http://essaysfromexodus.scripting.com/backissues/2000/06/07/#rss>.

[^19]: Dave Winer, “Re: RSS 0.91 Restarted,” June 9, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/132>.

[^20]: Leigh Dodds, “RSS Modularization,” XML.com, July 5, 2000, accessed September 14, 2018, <http://www.xml.com/pub/a/2000/07/05/deviant/rss.html>.

[^21]: Ian Davis, “Re: [syndication] RSS Modularization Demonstration,” June 28, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/188>.

[^22]: “RDF Site Summary (RSS) 1.0,” December 09, 2000, accessed September 14, 2018, <http://web.resource.org/rss/1.0/spec>.

[^23]: Dave Winer, “Re: [syndication] Re: Thoughts, Questions, and Issues,” August 16, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/410>.

[^24]: Mark Pilgrim, “History of the RSS Fork,” Dive into Mark, September 5, 2002, accessed September 14, 2018, <http://www.diveintomark.link/2002/history-of-the-rss-fork>.

[^25]: Dan Brickley, “RSS-Classic, RSS 1.0 and a Historical Debt,” November 7, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/1136>.

[^26]: Tim O’Reilly, “Re: Asking Tim,” UserLand, September 20, 2000, accessed September 14, 2018, <http://static.userland.com/userLandDiscussArchive/msg021537.html>.

[^27]: Dave Winer, “Re: Asking Tim,” UserLand, September 20, 2000, accessed September 14, 2018, <http://static.userland.com/userLandDiscussArchive/msg021560.html>.

[^28]: John Quain, “BASICS; Fine-Tuning Your Filter for Online Information,” The New York Times, 2004, accessed September 14, 2018, <https://www.nytimes.com/2004/06/03/technology/basics-fine-tuning-your-filter-for-online-information.html>.

[^29]: John Schwartz, “Aaron Swartz, Internet Activist, Dies at 26,” The New York Times, January 12, 2013, accessed September 14, 2018, <https://www.nytimes.com/2013/01/13/technology/aaron-swartz-internet-activist-dies-at-26.html>.

[^30]: “A Second Spring of Cleaning,” Official Google Blog, March 13, 2013, accessed September 14, 2018, <https://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html>.

[^31]: Steve Gillmor, “Rest in Peace, RSS,” TechCrunch, May 5, 2009, accessed September 14, 2018, <https://techcrunch.com/2009/05/05/rest-in-peace-rss/>.

[^32]: Marco Arment, “Lockdown,” Marco.org, July 3, 2013, accessed September 14, 2018, <https://marco.org/2013/07/03/lockdown>.

[^33]: Bob Tedeschi, “There’s a Popular New Code for Deals: RSS,” The New York Times, January 29, 2006, accessed September 14, 2018, <https://www.nytimes.com/2006/01/29/travel/theres-a-popular-new-code-for-deals-rss.html>.

[^34]: “NYTimes.com RSS Feeds,” The New York Times, accessed September 14, 2018, <https://web.archive.org/web/20050326065348/www.nytimes.com/services/xml/rss/index.html>.

[^35]: Rael Dornfest, “RE: Re: [syndication] RE: RFC: Clearing Confusion for RSS, Agreement for Forward Motion,” May 31, 2001, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/messages/1717>.