# RSS 的兴衰

*2018 年 12 月 18 日*

*本文最初发布于 [2018 年 9 月 16 日](https://twobithistory.org/2018/09/16/the-rise-and-demise-of-rss.html)。以下是修订版，其中包含了从 Ramanathan Guha、Ian Davis、Dan Libby 和 Kevin Werbach 的采访中获取的额外信息。*

*本文的一个版本也曾发布于 [Vice News](https://www.vice.com/en_us/article/a3mm4z/the-rise-and-demise-of-rss)。*

大约十年前，普通互联网用户很可能听说过 RSS。这个缩写究竟代表“真正简单的整合 (Really Simple Syndication)”还是“丰富站点摘要 (Rich Site Summary)”，取决于你问谁。RSS 是一种标准，网站和播客可以利用它向用户提供内容订阅源，这种订阅源很容易被各种不同的计算机程序理解。然而，如今尽管 RSS 仍在为许多网络应用提供支持，但对大多数人来说，它已成为一项鲜为人知的技术。

这个故事的发生，实际上是两个故事的交织。第一个故事讲述了一个关于网络未来的宏大愿景，但这个愿景最终未能完全实现。第二个故事则揭示了为改进一项流行标准而进行的协作努力，是如何演变成开源软件开发史上最具争议的分支之一的。

在 20 世纪 90 年代末，也就是网景公司 (Netscape) 首次公开募股 (IPO) 和互联网泡沫破裂之间的高速发展时期，每个人都清楚地看到，互联网将变得比当时更加重要，尽管他们不确定具体会如何发展。其中一种理论认为，互联网即将被内容整合 (syndication) 所彻底改变。互联网最初是为了实现两方之间简单的交易——客户端从单个主机服务器获取文档——而构建的，但新的标准将打破这一模式，这些标准可以用于通过各种渠道重新打包和分发整个网站。Kevin Werbach 在 20 世纪 90 年代对投资者颇具影响力的时事通讯《Release 1.0》中写道，他预测内容整合“将演变为互联网经济的核心模式，使企业和个人在享受大规模和广阔范围优势的同时，保留对其在线身份的控制权。”[^1]

他邀请读者想象这样一个未来：击剑爱好者无需直接访问“在线体育用品网站”或“击剑器材零售商”，而是可以通过嵌入到他们最喜欢的击剑网站中的电子商务小部件，直接购买新的重剑 (épée) [^2]。就像电视行业中，大型网络将节目整合 (syndicate) 给小型地方电视台一样，网络上的内容整合将使企业和出版物能够通过众多中间网站接触到消费者。作为推论，这意味着消费者将对他们在网络上与任何特定企业或出版物互动的位置和方式获得显著的控制权。

RSS 是有望实现这种内容整合未来的标准之一。在 Werbach 看来，RSS 是“轻量级内容整合协议 (lightweight syndication protocol) 的典范”[^3]。另一篇同期文章称 RSS 是第一个实现 XML 潜力的协议[^4]。它将成为用户和内容聚合器 (content aggregators) 从网络上所有内容中创建自己定制频道的方式。然而，二十年后，在社交媒体兴起和谷歌 (Google) 决定关闭 Google 阅读器 (Google Reader) 之后，RSS 似乎正在成为 [一项缓慢消亡的技术](https://trends.google.com/trends/explore?date=all&geo=US&q=rss)，现在主要由播客制作者、拥有技术博客的程序员以及偶尔的记者使用。当然，尽管有些人确实仍然依赖 RSS 阅读器，但在 2018 年，固执地为你的博客添加 RSS 订阅源，已经成为一种政治声明。那个小小的橘色气泡图标，已经变成了一种对中心化网络的反抗，带着一丝怀旧的意味，这个网络正日益被少数公司控制，与 Werbach 想象中的内容整合网络几乎判若两地。

RSS 的未来曾一度如此光明。究竟发生了什么？它的衰落是不可避免的吗，还是被阻碍单一 RSS 标准开发的激烈内斗所加速了呢？

## 一团乱麻

RSS 被发明了两次。这意味着它从未有过一个明确的归属方，这种状况引发了无休止的争论和敌意。但这也表明，RSS 是一个应运而生的重要理念。

1998 年，网景公司 (Netscape) 正在努力构想自己的未来。其旗舰产品——网景导航者 (Netscape Navigator) 网页浏览器——曾一度受到超过 80% 的网络用户青睐，但很快就迅速失势于微软 (Microsoft) 的 Internet Explorer。因此，网景公司决定在一个新的领域展开竞争。同年 5 月，一个团队组建起来，开始着手内部称为“Project 60”的项目[^5]。两个月后，网景公司宣布推出“My Netscape”，这是一个网络门户，将与雅虎 (Yahoo)、MSN 和 Excite 等其他门户网站展开竞争。

次年 3 月，网景公司宣布为 My Netscape 门户添加一项名为“My Netscape Network”的功能。My Netscape 用户现在可以自定义他们的 My Netscape 页面，使其包含显示来自网络上最新头条新闻的“频道”。只要你喜欢的网站以网景公司规定的格式发布一个特殊文件，你就可以将该网站添加到你的 My Netscape 页面，通常是通过点击参与网站应该添加到其界面上的“添加频道”按钮。然后，一个包含链接标题列表的小框就会出现。

![A My Netscape Network Channel](https://twobithistory.org/images/mnn-channel.gif)
*一个 Mozilla.org 的 My Netscape Network 频道，用户可能看到它并将其添加到 My Netscape 页面。*

参与网站必须发布的特殊文件就是 RSS 文件。在 My Netscape Network 的发布公告中，网景公司解释说 RSS 代表“资源描述框架站点摘要 (RDF Site Summary)”[^6]。这在某种程度上是一个用词不当。资源描述框架 (RDF, or the Resource Description Framework) 本质上是一种描述任意资源特定属性的语法。（如果你觉得这听起来很激动人心，可以看看 [我关于语义网 (Semantic Web) 的文章](https://twobithistory.org/2018/05/27/semantic-web.html)。）1999 年，万维网联盟 (W3C)——网络的主要标准制定机构——正在审议 RDF 的草案规范。尽管 RSS 本应基于 RDF，但网景公司实际发布的 RSS 示例文档根本没有使用任何 RDF 标签。在随网景 RSS 规范发布的一份文档中，该规范的作者之一 Dan Libby 解释说，“在 MNN 的这个版本中，网景公司有意限制了 RSS 格式的复杂性。”[^7] 该规范被赋予 0.90 版本号，其理念是后续版本将使 RSS 更符合 W3C 的 XML 规范和不断演进的 RDF 规范草案。

RSS 是由 Libby 和另外两名网景公司员工 Eckart Walther 和 Ramanathan Guha 共同创建的。根据 Guha 发给我的一封电子邮件，他和 Walther 最初在 Libby 的一些建议下构思出了 RSS；1998 年美国在线 (AOL) 收购网景公司后，他和 Walther 离开了，RSS 的责任就落到了 Libby 身上。在加入网景公司之前，Guha 曾在苹果公司 (Apple) 工作，在那里他提出了一种名为元内容框架 (Meta Content Framework, MCF) 的东西。MCF 是一种用于表示从网页到本地文件等任何事物的元数据 (metadata) 的格式。Guha 通过开发一个名为 [HotSauce](http://web.archive.org/web/19970703020212/http://mcf.research.apple.com:80/hs/screen_shot.html) 的应用程序展示了它的强大功能，该应用程序将文件之间的关系可视化为悬浮在三维空间中的节点网络。离开苹果公司加入网景公司后，Guha 立即与网景公司顾问 Tim Bray 合作，Tim Bray 在他博客上的一篇文章中提到，他和 Guha 最终开发了一个基于 XML 的 MCF 版本，而这个版本又成为了 W3C 的 RDF 草案的基础[^8]。因此，Guha、Walther 和 Libby 热衷于在 Guha 之前的工作基础上发展，并将 RDF 整合到 RSS 中，这也就不足为奇了。但 Libby 后来写道，最初基于 RDF 的 RSS 愿景有所削减，原因在于时间限制以及人们认为 RDF 对“普通用户”来说“过于复杂”[^9]。

当网景公司试图在被称为“门户网站大战”中吸引眼球时，网络上的其他地方正在开创一种名为“网络日志 (weblogging)”的新现象[^10]。其中一位先驱是 Dave Winer，他是一家名为 UserLand Software 公司的首席执行官，该公司开发了早期内容管理系统，使不具备深厚技术能力的人也能轻松进行博客写作。Winer 运营着自己的博客 [Scripting News](http://scripting.com)，该博客如今是互联网上最古老的博客之一。在网景公司宣布 My Netscape Network 之前一年多，即 1997 年 12 月 15 日，Winer 发布了一篇文章，宣布该博客现在将提供 XML 和 HTML 两种格式[^11]。

Dave Winer 的 XML 格式被称为 Scripting News 格式。据称，它与微软 (Microsoft) 的频道定义格式 (Channel Definition Format) 相似（这是一项于 1997 年 3 月提交给 W3C 的“推送技术 (push technology)”标准），但我未能找到原始格式的文件来验证这一说法[^12]。与网景公司 (Netscape) 的 RSS 类似，它对 Winer 博客的内容进行了结构化，以便其他软件应用程序能够理解。当网景公司发布 RSS 0.90 时，Winer 和 UserLand Software 开始同时支持这两种格式。但 Winer 认为网景公司的格式“严重不足”，并且“缺少网络写作者和读者所需的核心功能”[^13]。它只能表示一个链接列表，而 Scripting News 格式可以表示一系列段落，每个段落包含一个或多个链接。

1999 年 6 月，在网景公司 (Netscape) 宣布 My Netscape Network 两个月后，Winer 推出了 Scripting News 格式的新版本，名为 ScriptingNews 2.0b1。Winer 声称，他是在尝试但未能让网景公司任何人关注 RSS 0.90 的缺陷后，才决定继续推进自己的格式的[^14]。新版本的 Scripting News 格式在 `<header>` 元素中添加了几个项目，使 Scripting News 格式与 RSS 达到了对等。但两种格式仍然存在差异，Scripting News 格式（Winer 昵称其为“胖”内容整合格式）可以包含整个段落，而不仅仅是链接。

网景公司 (Netscape) 终于在下个月发布了 RSS 0.91。更新后的规范是一个重大转变。RSS 不再代表“资源描述框架站点摘要 (RDF Site Summary)”；它现在代表“丰富站点摘要 (Rich Site Summary)”。所有的 RDF——反正也几乎没有——都被移除了。许多 Scripting News 标签被整合进来。在新规范的文本中，Libby 解释道：

> 移除了 RDF 引用。RSS 最初被构想为一种提供网站摘要的元数据格式。有两点变得清晰：首先，提供者更需要一种内容整合格式，而非元数据格式。RDF 文件的结构非常精确，必须符合 RDF 数据模型才能有效。这不容易被人类理解，并且可能使创建有用的 RDF 文件变得困难。其次，用于 RDF 生成、验证和处理的工具很少。基于这些原因，我们决定采用标准的 XML 方法。[^15]

Winer 对 RSS 0.91 非常满意，称其“比我想象的还要好”[^16]。UserLand Software 采纳它作为现有 ScriptingNews 2.0b1 格式的替代品。一度，RSS 似乎终于有了一个单一的权威规范。

## 大分叉

一年后，RSS 0.91 规范变得严重不足。人们试图用 RSS 做各种事情，但该规范并未涵盖。规范中还有其他部分似乎施加了不必要的限制——例如，每个 RSS 频道最多只能包含 15 个项目。

到那时，RSS 已经被更多组织采纳。除了在 RSS 0.91 之后似乎失去兴趣的网景公司 (Netscape) 之外，主要参与者包括 Dave Winer 的 UserLand Software；运营着名为 Meerkat 的 RSS 聚合器 (RSS aggregator) 的 O’Reilly Net；以及同样运营着专注于新闻的 RSS 聚合器的 Moreover.com [^17]。通过邮件列表，这些组织及其他机构的代表定期讨论如何改进 RSS 0.91。但对于这些改进应该是什么样子，存在着深刻的分歧。

大部分讨论发生的邮件列表被称为内容整合邮件列表 (Syndication mailing list)。[内容整合邮件列表的存档](https://groups.yahoo.com/neo/groups/syndication/info) 至今仍可查阅。它是一个令人惊叹的历史资源。它逐刻记录了这些深刻分歧最终如何导致 RSS 社区的政治分裂。

即将到来的分裂一方是 Winer。Winer 急于发展 RSS，但他只想以相对保守的方式进行改变。2000 年 6 月，他在 UserLand 网站上发布了自己的 RSS 0.91 规范，旨在作为 RSS 进一步开发的起点。它对网景公司 (Netscape) 发布的 0.91 规范没有做出任何重大改变。Winer 在随其规范发布的一篇博客文章中声称，这只是一个“清理”文档，记录了 RSS 在实际使用中的情况，之所以需要它，是因为网景公司的规范不再维护了[^18]。在同一篇文章中，他认为 RSS 迄今为止之所以成功，是因为它很简单，而通过向格式中添加命名空间 (namespaces)（一种明确区分不同 RSS 词汇表的方式）或重新引入 RDF——有人在内容整合邮件列表 (Syndication mailing list) 中建议这样做——它“将变得复杂得多，恕我直言 (IMHO)，在内容提供商层面，这种额外的复杂性几乎不会给我们带来任何好处。”在同一时间发送给内容整合邮件列表的一条消息中，Winer 暗示这些问题非常重要，可能会导致他创建一个分支：

> 我仍在思考如何推动 RSS 发展。我当然希望 RSS2 中有类似 ICE 的功能，发布和订阅是我的首要任务，但我将竭力争取简洁性。我喜欢可选元素。我不想走命名空间和模式 (schema) 的道路，也不想尝试将其变成 RDF 的一种方言。我理解其他人想这样做，因此我猜我们将会出现一个分支。对于另一个分支将走向何方，我自有看法，但至少目前我会保留这些看法。[^19]

与 Winer 对立的是其他几个人，包括 O’Reilly 公司的 Rael Dornfest、Ian Davis（负责一家名为 Calaba 的搜索初创公司）以及早熟的 14 岁 Aaron Swartz。这位 Aaron Swartz 后来共同创立了 Reddit，并因其黑客行动主义 (hacktivism) 而闻名。（根据 Davis 发给我的一封电子邮件，在 2000 年，他的父亲经常陪他参加技术聚会。）Dornfest、Davis 和 Swartz 都认为 RSS 需要命名空间 (namespaces) 来适应人们希望用它做的许多不同事情。在 O’Reilly 托管的另一个邮件列表上，Davis 提出了一个基于命名空间的模块系统，他写道，这样的系统将“使 RSS 像我们希望的那样可扩展，而不是塞入使规范过于复杂的新功能。”[^20] “命名空间阵营”认为 RSS 很快将不仅仅用于博客文章的内容整合，因此命名空间非但不是一种复杂性，反而是防止 RSS 在支持越来越多使用场景时变得难以管理的唯一途径。

关于命名空间 (namespaces) 的分歧，其根源在于对 RSS 究竟为何物存在更深层次的意见不合。Winer 发明 Scripting News 格式是为了整合他为博客撰写的文章。网景公司 (Netscape) 发布 RSS 时称其为“资源描述框架站点摘要 (RDF Site Summary)”，因为它是在 My Netscape 在线门户中微缩重建一个网站的方式。有些人认为网景公司的最初愿景应该得到尊重。Davis 在写给内容整合邮件列表 (Syndication mailing list) 的信中解释了他的观点，即 RSS“最初被构想为一种构建迷你站点地图的方式”，而现在他和其他人希望扩展 RSS，“以涵盖比简单新闻头条更多类型的信息，并满足过去 12 个月来出现的 RSS 新用途。”[^21] 这是一个合理的观点，因为网景公司 RSS 项目最初的目标甚至比 Davis 所说的更宏伟：Guha 告诉我，他想创建一种技术，不仅能支持网站频道，还能支持关于任意实体（例如麦当娜）的订阅源。进一步开发 RSS 以实现这一点，确实符合最初的动机。但 Davis 的论点也夸大了在 RSS 规范发布时网景公司内部存在统一愿景的程度。根据我通过电子邮件与 Libby 的交流，即使在网景公司内部，最终也存在“让我们构建语义网 (Semantic Web)”小组和“让我们让人们更容易创作”小组之间的争论。

就 Winer 而言，他认为网景公司 (Netscape) 的最初目标无关紧要，因为他的 Scripting News 格式实际上是第一个 RSS，而且它的目的截然不同。鉴于最参与 RSS 开发的人们对谁创建了 RSS 以及为何创建 RSS 存在分歧，一个分支似乎是不可避免的。

分叉发生在 Dornfest 宣布了一项提议的 RSS 1.0 规范，并成立了 RSS-DEV 工作组——该工作组将包括 Davis、Swartz 和其他几个人，但不包括 Winer——以准备发布该规范之后。在提议的规范中，RSS 再次代表“资源描述框架站点摘要 (RDF Site Summary)”，因为 RDF 被重新添加进来，以表示某些 RSS 元素的元数据属性。该规范点名承认了 Winer，赞扬他通过其“推广工作”普及了 RSS [^22]。但它也认为，RSS 无法以 Winer 所倡导的方式进行改进。仅仅向 RSS 添加更多元素而不通过模块系统提供可扩展性，将“牺牲可扩展性”。该规范接着定义了一个基于 XML 命名空间 (namespaces) 的 RSS 模块系统。

Winer 认为 RSS-DEV 工作组擅自占用“RSS 1.0”这个名称是“不公平的”[^23]。在另一个关于去中心化 (decentralization) 的邮件列表上，他写道，他“最近有一个标准被一个大公司窃取了”，大概是指召集了 RSS-DEV 工作组的 O’Reilly 公司[^24]。内容整合邮件列表 (Syndication mailing list) 的其他成员也认为，RSS-DEV 工作组在没有获得社区关于如何推进 RSS 的一致同意之前，不应该使用“RSS”这个名称。但该工作组坚持使用这个名称。RSS-DEV 工作组的另一位成员 Dan Brickley 为这一决定辩护，他认为“提议的 RSS 1.0 坚实地根植于最初的 RSS 愿景，而这个愿景本身就有着悠久的历史，可以追溯到 MCF（RDF 的前身）和相关规范（CDF 等）。”[^25] 他本质上认为，RSS 1.0 的努力比 Winer 更有资格使用 RSS 这个名称，因为 RDF 最初就是 RSS 的一部分。RSS-DEV 工作组于 12 月发布了他们规范的最终版本。同月，Winer 在 UserLand 的网站上发布了他对 RSS 0.91 的改进版本，他称之为 RSS 0.92。RSS 0.92 对 RSS 进行了几项小的可选改进，其中包括添加了很快被各地播客制作者使用的 `<enclosure>` 标签。RSS 正式分叉了。

如果当时能更好地努力将 Winer 纳入 RSS-DEV 工作组，这次分叉或许可以避免。他显然应该在那里。他是内容整合邮件列表 (Syndication mailing list) 的重要贡献者，也是 RSS 普及的主要功臣，正如工作组成员自己所承认的那样。但是，正如 Davis 在给我的一封电子邮件中所写，Winer“想要控制权，并希望 RSS 成为他的遗产，所以不愿与我们合作。”O’Reilly 公司的创始人兼首席执行官 Tim O’Reilly 在 2000 年 9 月的一个 UserLand 讨论组中解释说，Winer 基本上拒绝参与：

> 一群参与 RSS 的人聚在一起，开始思考它的未来发展。Dave 是这个群体的一员。当群体的共识转向他不喜欢的一个方向时，Dave 停止了参与，并将其描述为 O’Reilly 公司企图从他手中接管 RSS 的一场阴谋，尽管 O’Reilly 公司的 Rael Dornfest 只是提议的 RSS 1.0 规范的大约十几位作者之一，而且许多参与其开发的人与 Dave 拥有同样长的 RSS 历史。[^26]

对此，Winer 说：

> 我在公告发布前两周与 Dale [Dougherty] 见了面，他没有提到任何关于将其命名为 RSS 1.0 的事情。我在公告发布前的那个周五与 Rael 通了电话，他同样没有说他们会将其命名为 RSS 1.0。我第一次知道这件事，是在它被公开宣布的时候。
>
> 让我问你一个直接的问题。如果事实证明，将新规范命名为“RSS 1.0”的计划是在私下进行的，没有任何事先通知或协商，也没有给内容整合邮件列表 (Syndication list) 成员（不仅仅是我）同意或不同意的机会，你打算怎么做？
>
> UserLand 在创建、推广和支持 RSS 方面做了大量工作。我们放弃了这一切，让你们的人拥有了这个名字。这是最根本的问题。如果我想在网络内容整合方面做任何进一步的工作，我必须使用一个不同的名字。Tim，这究竟是为什么，又是怎么发生的？[^27]

我未能找到在 RSS 1.0 提案公布之前，内容整合邮件列表 (Syndication mailing list) 中关于使用 RSS 1.0 名称的讨论。Winer 在给我的一条消息中表示，他并非试图控制 RSS，只是想在自己的产品中使用它。

RSS 在 2003 年再次分叉，当时一些厌倦了 RSS 社区争吵的开发者试图创建一个全新的格式。这些开发者创建了 Atom，这是一种放弃了 RDF 但拥抱了 XML 命名空间 (namespaces) 的格式。Atom 最终将由 [一项提议的互联网工程任务组 (IETF) 标准](https://tools.ietf.org/html/rfc4287) 来规范。在 Atom 推出后，出现了三个相互竞争的 RSS 版本：Winer 的 RSS 0.92（于 2002 年更新为 RSS 2.0 并更名为“真正简单的整合 (Really Simple Syndication)”）、RSS-DEV 工作组的 RSS 1.0 和 Atom。

## 衰落

相互竞争的 RSS 规范的激增，可能在其他方面阻碍了 RSS 的发展，我稍后会讨论。但这并没有阻止 RSS 在 21 世纪初变得极其流行。到 2004 年，《纽约时报》已经开始提供 RSS 格式的头条新闻，并撰写了一篇文章向普通人解释 RSS 是什么以及如何使用它[^28]。Google 阅读器 (Google Reader) 这个最终被数百万人使用的 RSS 聚合器 (RSS aggregator)，于 2005 年推出。到 2013 年，RSS 似乎足够流行，以至于《纽约时报》在 Aaron Swartz 的讣告中称这项技术“无处不在”[^29]。有一段时间，在地球上三分之一的人口注册 Facebook 之前，RSS 简直就是许多人及时了解互联网新闻的方式。

《纽约时报》于 2013 年 1 月发表了 Swartz 的讣告。然而，到那时，RSS 实际上已经急转直下，正在迅速成为一项鲜为人知的技术。Google 阅读器 (Google Reader) 于 2013 年 7 月关闭，表面上是因为用户数量“多年来”一直在下降[^30]。这促使多家媒体发表文章，宣称 RSS 已死。但早在 Google 阅读器关闭之前，人们就已经宣称 RSS 已死多年了。Steve Gillmor 于 2009 年 5 月在 TechCrunch 上撰文，建议“是时候彻底放弃 RSS，转用推特 (Twitter) 了”，因为“RSS 已经不再够用”[^31]。他指出，推特 (Twitter) 基本上是一个更好的 RSS 订阅源，因为它除了文章本身，还能向你展示人们对文章的看法。它允许你关注个人，而不仅仅是频道。Gillmor 告诉他的读者，是时候让 RSS 淡出人们的视线了。他用鲍勃·迪伦 (Bob Dylan) 的《Forever Young》中的一节诗结束了他的文章。

如今，RSS 并没有消亡。但它也远不如从前那么流行。许多人对 RSS 为何失去广泛吸引力提出了各种解释。也许最有说服力的解释正是 Gillmor 在 2009 年提出的那个。社交网络，就像 RSS 一样，提供了一个包含互联网上所有最新新闻的订阅源。社交网络取代 RSS，仅仅是因为它们提供了更好的订阅源。它们也为拥有它们的科技公司带来了更多好处。例如，有些人指责谷歌 (Google) 关闭 Google 阅读器 (Google Reader) 是为了鼓励人们使用 Google+。谷歌可能能够以一种无法通过 Google 阅读器实现的方式，将 Google+ 变现。Instapaper 的创建者 Marco Arment 在 2013 年的博客中写道：

> Google 阅读器 (Google Reader) 只是 Facebook 似乎无意中发起的那场战争的最新牺牲品：一场争夺一切所有权的战争。虽然谷歌 (Google) 在技术上“拥有”阅读器，并且可以利用其中流动的海量新闻和关注数据，但这与他们更为重要的 Google+ 战略相冲突：他们需要每个人都通过 Google+ 阅读和分享一切，这样他们才能与 Facebook 竞争广告定向数据、广告收入、增长和相关性。[^32]

因此，用户和科技公司都意识到，使用社交网络比使用 RSS 能获得更多好处。

另一种理论是，RSS 对普通人来说总是过于技术化。即使是《纽约时报》——它似乎曾热衷于采用 RSS 并向其受众推广——也在 2006 年抱怨说，RSS 是一个“不太用户友好”的缩写，由“电脑极客 (computer geeks)”创造[^33]。在 2004 年 RSS 图标设计出来之前，《纽约时报》等网站使用标有“XML”的小橘色方框链接到他们的 RSS 订阅源，这无疑是令人生畏的[^34]。不过，这个标签是完全准确的，因为当时点击链接会把一个不幸的用户带到一个满是 XML 的页面。[这条精彩的推文](https://twitter.com/mgsiegler/status/31199206716203008) 抓住了 RSS 衰落这一解释的精髓。普通人从未觉得使用 RSS 舒适；它并非真正设计为面向消费者的技术，并且涉及太多障碍；一旦出现更好的东西，人们就转投他处了。

如果 RSS 得到进一步发展，它或许能够克服其中一些局限性。也许 RSS 可以以某种方式扩展，让订阅同一频道的朋友们能够相互整合他们对一篇文章的看法。也许浏览器支持可以得到改进。但是，当像 Facebook 这样的公司能够“快速行动，打破常规”时，RSS 开发者社区却陷入了寻求共识的困境。当他们未能就单一标准达成一致时，本可以用于改进 RSS 的精力却浪费在重复已完成的工作上。例如，Davis 告诉我，如果内容整合邮件列表 (Syndication mailing list) 的成员能够妥协和协作，Atom 就没有必要了，而且“所有那些清理工作都可以投入到 RSS 中以增强它。”因此，如果我们问自己为什么 RSS 不再流行，一个首要解释是社交网络取代了它。如果我们问自己为什么社交网络能够取代它，那么答案可能是，那些试图让 RSS 成功的人面临的问题比，比如说，构建 Facebook 要困难得多。正如 Dornfest 曾写给内容整合邮件列表 (Syndication mailing list) 的那样，“目前，远非简单的，更多的是政治而非序列化。”[^35]

因此，今天我们只剩下中心化的信息孤岛。即便如此，Werbach 在 1999 年预见的内容整合网络已经实现，只是并非以他想象的方式。毕竟，《洋葱报 (The Onion)》是一个通过 Facebook 和推特 (Twitter) 进行内容整合的出版物，就像《宋飞正传 (Seinfeld)》在原版播出结束后依靠内容整合赚取数百万美元一样。我问 Werbach 对此有何看法，他或多或少同意。他告诉我，从某种程度上说，RSS 显然是失败的，因为它现在不再是“整个博客世界、内容世界或将不同元素组装成网站的核心技术”。但是，从另一个层面看，“整个社交媒体革命部分在于聚合不同内容和资源的能力”，这让人想起 RSS 和他最初对内容整合网络的愿景。对 Werbach 来说，“这是 RSS 的遗产，即使它并非建立在 RSS 之上。”

不幸的是，现代网络上的内容整合仍然只通过极少数渠道进行，这意味着我们没有人能像 Werbach 想象的那样“保留对我们在线身份的控制权”。发生这种情况的一个原因是司空见惯的企业贪婪——RSS 作为一个开放格式，没有给科技公司提供销售广告所需的数据和用户注意力的控制权，所以他们不支持它。但更平淡的原因是，中心化孤岛比通用标准更容易设计。达成共识是困难且耗时的，但如果没有共识，被排斥的开发者就会另起炉灶，创建相互竞争的标准。这里的教训可能是，如果我们想看到一个更好、更开放的网络，我们就必须更好地避免互相拆台。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！在推特 (Twitter) 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 订阅源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> 我一直想知道我的 Macbook 上的 Unix 命令是否与 20 或 30 年前构建它们的代码相同。事实证明，答案是“有点”！
>
> 我的最新文章，关于 cat 的实现多年来如何变化：<https://t.co/dHizjK50ES>
>
> — TwoBitHistory (@TwoBitHistory) [2018 年 11 月 12 日](https://twitter.com/TwoBitHistory/status/1062114484209311746?ref_src=twsrc%5Etfw)

[^1]: Kevin Werbach, “The Web Goes into Syndication,” Release 1.0, July 22, 1999, 1, accessed September 14, 2018, [http://cdn.oreillystatic.com/radar/r1/07-99.pdf](http://cdn.oreillystatic.com/radar/r1/07-99.pdf)。
[^2]: ibid.
[^3]: Werbach, 8.
[^4]: Peter Wiggin, “RSS Delivers the XML Promise,” Web Review, October 29, 1999, accessed September 14, 2018, [https://people.apache.org/~jim/NewArchitect/webrevu/1999/10_29/webauthors/10_29_99_2a.html](https://people.apache.org/~jim/NewArchitect/webrevu/1999/10_29/webauthors/10_29_99_2a.html)。
[^5]: Ben Hammersley, RSS and Atom (O’Reilly), 8, accessed September 14, 2018, [https://books.google.com/books?id=kwJVAgAAQBAJ](https://books.google.com/books?id=kwJVAgAAQBAJ)。
[^6]: “RSS 0.90 Specification,” RSS Advisory Board, accessed September 14, 2018, [http://www.rssboard.org/rss-0-9-0](http://www.rssboard.org/rss-0-9-0)。
[^7]: “My Netscape Network Future Directions,” RSS Advisory Board, accessed September 14, 2018, [http://www.rssboard.org/mnn-futures](http://www.rssboard.org/mnn-futures)。
[^8]: Tim Bray, “The RDF.net Challenge,” Ongoing by Tim Bray, May 21, 2003, accessed September 14, 2018, <https://www.tbray.org/ongoing/When/200x/2003/05/21/RDFNet>。
[^9]: Dan Libby, “RSS: Introducing Myself,” August 24, 2000, RSS-DEV Mailing List, accessed September 14, 2018, [https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/239](https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/239)。
[^10]: Alexandra Krasne, “Browser Wars May Become Portal Wars,” CNN, accessed September 14, 2018, <http://www.cnn.com/TECH/computing/9910/04/portal.war.idg/index.html>。
[^11]: Dave Winer, “Scripting News in XML,” Scripting News, December 15, 1997, accessed September 14, 2018, <http://scripting.com/davenet/1997/12/15/scriptingNewsInXML.html>。
[^12]: Joseph Reagle, “RSS History,” 2004, accessed September 14, 2018, [https://reagle.org/joseph/2003/rss-history.html](https://reagle.org/joseph/2003/rss-history.html)。
[^13]: Dave Winer, “A Faceoff with Netscape,” Scripting News, June 16, 1999, accessed September 14, 2018, <http://scripting.com/davenet/1999/06/16/aFaceOffWithNetscape.html>。
[^14]: ibid.
[^15]: Dan Libby, “RSS 0.91 Specification (Netscape),” RSS Advisory Board, accessed September 14, 2018, [http://www.rssboard.org/rss-0-9-1-netscape](http://www.rssboard.org/rss-0-9-1-netscape)。
[^16]: Dave Winer, “Scripting News: 7/28/1999,” Scripting News, July 28, 1999, accessed September 14, 2018, [http://scripting.com/1999/07/28.html](http://scripting.com/1999/07/28.html)。
[^17]: Oliver Willis, “RSS Aggregators?” June 19, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/173>。
[^18]: Dave Winer, “Scripting News: 07/07/2000,” Scripting News, July 07, 2000, accessed September 14, 2018, [http://essaysfromexodus.scripting.com/backissues/2000/06/07/#rss](http://essaysfromexodus.scripting.com/backissues/2000/06/07/#rss)。
[^19]: Dave Winer, “Re: RSS 0.91 Restarted,” June 9, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/132>。
[^20]: Leigh Dodds, “RSS Modularization,” XML.com, July 5, 2000, accessed September 14, 2018, <http://www.xml.com/pub/a/2000/07/05/deviant/rss.html>。
[^21]: Ian Davis, “Re: [syndication] RSS Modularization Demonstration,” June 28, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/188>。
[^22]: “RDF Site Summary (RSS) 1.0,” December 09, 2000, accessed September 14, 2018, [http://web.resource.org/rss/1.0/spec](http://web.resource.org/rss/1.0/spec)。
[^23]: Dave Winer, “Re: [syndication] Re: Thoughts, Questions, and Issues,” August 16, 2000, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/topics/410>。
[^24]: Mark Pilgrim, “History of the RSS Fork,” Dive into Mark, September 5, 2002, accessed September 14, 2018, [http://www.diveintomark.link/2002/history-of-the-rss-fork](http://www.diveintomark.link/2002/history-of-the-rss-fork)。
[^25]: Dan Brickley, “RSS-Classic, RSS 1.0 and a Historical Debt,” November 7, 2000, Syndication Mailing List, accessed September 14, 2018, [https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/1136](https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/1136)。
[^26]: Tim O’Reilly, “Re: Asking Tim,” UserLand, September 20, 2000, accessed September 14, 2018, [http://static.userland.com/userLandDiscussArchive/msg021537.html](http://static.userland.com/userLandDiscussArchive/msg021537.html)。
[^27]: Dave Winer, “Re: Asking Tim,” UserLand, September 20, 2000, accessed September 14, 2018, [http://static.userland.com/userLandDiscussArchive/msg021560.html](http://static.userland.com/userLandDiscussArchive/msg021560.html)。
[^28]: John Quain, “BASICS; Fine-Tuning Your Filter for Online Information,” The New York Times, 2004, accessed September 14, 2018, [https://www.nytimes.com/2004/06/03/technology/basics-fine-tuning-your-filter-for-online-information.html](https://www.nytimes.com/2004/06/03/technology/basics-fine-tuning-your-filter-for-online-information.html)。
[^29]: John Schwartz, “Aaron Swartz, Internet Activist, Dies at 26,” The New York Times, January 12, 2013, accessed September 14, 2018, [https://www.nytimes.com/2013/01/13/technology/aaron-swartz-internet-activist-dies-at-26.html](https://www.nytimes.com/2013/01/13/technology/aaron-swartz-internet-activist-dies-at-26.html)。
[^30]: “A Second Spring of Cleaning,” Official Google Blog, March 13, 2013, accessed September 14, 2018, [https://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html](https://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html)。
[^31]: Steve Gillmor, “Rest in Peace, RSS,” TechCrunch, May 5, 2009, accessed September 14, 2018, [https://techcrunch.com/2009/05/05/rest-in-peace-rss/](https://techcrunch.com/2009/05/05/rest-in-peace-rss/)。
[^32]: Marco Arment, “Lockdown,” Marco.org, July 3, 2013, accessed September 14, 2018, <https://marco.org/2013/07/03/lockdown>。
[^33]: Bob Tedeschi, “There’s a Popular New Code for Deals: RSS,” The New York Times, January 29, 2006, accessed September 14, 2018, [https://www.nytimes.com/2006/01/29/travel/theres-a-popular-new-code-for-deals-rss.html](https://www.nytimes.com/2006/01/29/travel/theres-a-popular-new-code-for-deals-rss.html)。
[^34]: “NYTimes.com RSS Feeds,” The New York Times, accessed September 14, 2018, <https://web.archive.org/web/20050326065348/www.nytimes.com/services/xml/rss/index.html>。
[^35]: Rael Dornfest, “RE: Re: [syndication] RE: RFC: Clearing Confusion for RSS, Agreement for Forward Motion,” May 31, 2001, Syndication Mailing List, accessed September 14, 2018, <https://groups.yahoo.com/neo/groups/syndication/conversations/messages/1717>。