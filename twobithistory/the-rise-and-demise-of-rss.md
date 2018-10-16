# 翻译 | RSS 的兴起与衰落
原文：[The Rise and Demise of RSS](https://twobithistory.org/2018/09/16/the-rise-and-demise-of-rss.html)

这有两个故事。第一个故事是关于一个从未完全实现的关于互联网未来的愿景。第二个故事则是关于如何将协力改善一个流行标准变为开源软件开发史上最富争议的问题之一。

90 年代末期，在那个网景公司 IPO 与互联网泡沫崩溃间的狂热年代，每个人都能看出互联网正成为一个比之从前更大的生意，尽管没人确切知道如何达到。一种观点是互联网会被信息聚合而彻底改变。最初为了使两端——服务端，与从服务端抓取文档的客户端——间的简单交流成为可能而建立的互联网，会被使网站在一系列频道中重新打包与分发整个网站的新标准而打破开放性。Kevin Werbach，*Release 1.0*，90 年代一封在投资者中影响深远的通讯的作者，曾预测信息聚合“会演变为互联网生态的核心模式，允许企业和个人在享受大规模、大范围的益处时，保留对他们网络形象的控制。”[^1] 他邀请他的读者一同想象一个未来，剑术迷能够直接在他们最爱的网站上通过嵌入其中的网购插件买一把新的重剑，而非直接去“在线运动品商店”或“击剑设备零售商”。[^2] 就如同电视世界中，大的网络提供商能够将他们的节目聚合到一个较小的地方电视台，网络上的信息聚合能使商家和出版商通过大量的中间站点接触到消费者。这意味着，作为结论，消费者能在何地与如何与任何给定的商家与出版社互动上，得到重要控制。

RSS 是承诺提供这样的聚合化未来的标准之一。对于 Werbach，RSS 是“轻量级聚合协议的领先范例。”[^3] 另一篇同期文章将 RSS 称为第一个意识到 XML 的潜力的协议。[^4] 他正成为一个使用户与内容整合者都能够创造自己集合了网络能提供的所有信息的个性化频道的方式。而现在，二十年后，RSS [像是成为了一个正死去的技术](https://trends.google.com/trends/explore?date=all&geo=US&q=rss)，仅仅主要被播客与程序员们的科技博客使用。此外，在后来的群体中，比起实际效用，RSS 可能更主要因其政治上的象征意义而被使用。当然，尽管还是有一些人真的有 RSS 读者，顽固地为博客加上 RSS 服务，即使在 2018 年，也是非常保守的表态。那个小小的橘子泡（指 RSS 标志）已经成为一个象征着对与 Werbach 的想象中的聚合网络一点也不像的巨头垄断式中心化网络的反抗标志。

RSS 的未来曾看起来如此光明。那到底是发生了什么呢？难道它的衰落是不可避免的？还是它在一个单一 RSS 标准的发展中被内斗所挫败？

## 浑水

RSS 曾两度被发明。这意味着，它从未有过一个明白无误的拥有者，一系列的事务又催生了无止境的争吵与辩论。但这也正意味着 RSS 曾是势头正好的一个重要想法。

1998 年，网景正拼命为自己想象一个未来。它的旗舰产品，曾一度被 80% 的互联网用户所选择的网景浏览器，正在 IE 浏览器前迅速失去份额。所以网景决定在一个全新的领域竞争。五月份，一个小组被组建起来，开始了后来被内部称为“Project 60”的项目。[^5] 两个月后，网景宣布了“My Netscape”，一个与其他互联网门户如雅虎，MSN 及 Excite 相竞争的互联网门户。

第二年三月，网景宣布了一个叫"My Netscape Network"的 My Netscape 门户扩展。My Netscape 用户现在可以自定义他们的 My Netscape 页面所以它包含了名为“channels"的功能，汇集网络上最近的头条新闻。只要你最爱的网站发布了一个由网景规定的格式的特殊文件，你就能把这个网站添加到你的 My Netscape 页面，一般只需点击应在参与的网站界面上显示的”Add Channel“按键。一个包含着一列相关头条的小盒子将会出现。

![mnn-channel](https://s1.ax1x.com/2018/09/22/iupTPJ.gif)

这个参与网站必须发布的特殊文件就是一个 RSS 文件。在 My Netscape Network 的声明中，网景解释称 RSS 代表着”RDF Site Summary“。[^6] 这多少有几分用词不当。RDF，全称 Resource Description Framework，主要是一个描述各种资源属性的语法（如果感兴趣的话，看 [我的关于语义网的这篇文章](https://twobithistory.org/2018/05/27/semantic-web.html)）。1999年，W3C 组织开始考虑 RDF 的规范草案。尽管 RSS 应该是基于 RDF 的，网景释出的示例 RSS 文件却没有用任何 RDF 标签，即使它声明了 RDF XML 命名空间。在一份与网景 RSS 规范一同释出的文件中，规范作者之一的 Dan Libby 解释称“在 MNN 的发布中，网景曾有意的限制了 RSS 格式的复杂性”。[^7] 这份规范的版本号是 0.90，因为他们相信在 W3C 的 XML 规范与新的 RDF 标准下，RSS 接下来的版本会更加完善。

RSS 曾被 Libby 与 Ramanathan Guha，另一个网景雇员一同定义。Guha 之前在苹果公司工作，并在那里提出了 Meta Content Framework。MCF 是一个意图描述从网页到本地文件等一切的表示元数据格式。Guha 为证明其力量，开发了一个名为 [HotSauce](http://web.archive.org/web/19970703020212/http://mcf.research.apple.com:80/hs/screen_shot.html) 的程序，能在 3D 空间中以节点网络的形式可视化显示文件间关系。在离开苹果加入网景后，Guha 与 Tim Bray，一个网景顾问，一同为制作一个基于 XML 版本的 MCF 而工作，而这后来成为了 W3C 的 RDF 草案的基础。[^8] 这并不意外，后来，Guha 与 Libby 急于将 RDF 合并进 RSS。但 Libby 后来写道，由于时间限制及 RDF “对于‘一般用户’太‘过于复杂’”，基于 RDF 的 RSS 比之最初的设想，削减了很多。[^9]

正当网景努力在后来被称为“门户大战”中赢得眼球时，在互联网的其他地方，一场闻名为“博客”的现象正被开创。[^10] Dave Winery 正是那些先驱者之一，他是一家叫 UserLand Software 的公司的 CEO，这家公司开发了早期的内容管理系统，以使写博客对于非技术娴熟的人更容易。Winer 经营着他名为 [Scripting News](http://scripting.com/) 的个人博客，这也是网上现存的最古老的博客之一。在1997 年的 12 月 15 日，网景宣布 My Netscape Network 一年多以前，Winer 发布了一篇文章宣布博客现在已能通过 XML 与 HTML 一同获得。[^11]

Dave Winer 的 XML 格式闻名为 Scripting News 格式。它可能与微软的 Channel Definition 格式（一个在 1997 年 3 月提交给 W3C 的“推送技术”标准）相似，但我并不能找到一个原始格式的文件来验证这个说法。[^12] 如同网景的 RSS，它组织了 Winer 的博客内容以便于能被其他的软件应用理解。当网景发布 RSS 0.90 时，Winer 与 UserLand Software 开始同时支持两种格式。但 Winer 相信网景的格式“极其劣质”且“失去了网络作者与读者需要的关键”。[^13] 它只能表现一列链接，反之，Scripting News 格式能够表现一系列的段落，每个都能包含一个或多个链接。

1999 年 6 月，网景宣布 My Netscape Network 两个月后，Winer 介绍了 Scripting News 格式的新版本，称为 ScriptingNews 2.0b1。Winer 声称曾尝试与网景获得联系以关心 RSS 0.90 的不足但失败了，只好决定继续完善他自己的格式。[^14] Scripting News 格式的新版本在 `<header>` 元素中加入了几个新项目以使 Scripting News 格式与 RSS 同等。但这两种格式继续与 Scripting News 格式—— Winer 昵称其为“胖”聚合格式，能够包含整个段落，而非仅仅是链接——不同。

网景在第二个月传播称 RSS 0.91 将会释出。这个更新的规范是一个大转变。 RSS 不再表示"RDF Site Summary"；它现在代表"Rich Site Summary"。所有的 RDF——已经几乎没有了的——被剥离。许多 Scripting News 标签被合并。在新规范的文本中，Libby 解释道：

> RDF 引用被移除了。RSS 最初被构思为一个提供网站摘要的元数据格式。两件事变得明了了：第一个是提供者想要更多的一个聚合格式而非元数据格式。RDF 文件的结构非常严格，而且符合 RDF 的数据模型为了使其有效。这并不能很容易被人所理解，而且非常难以创建有用的 RDF 文件。第二个问题是只有很少的工具可用于 RDF 部署，验证与处理。因为上述原因，我们决定附属于一个标准的 XML 途径。[^15]

Winer 对 RSS 0.91 非常满意，称之”比起我认为它会成为的更好“[^16] UserLand Software 将其采用为已存在的 ScriptingNews 2.0b1 格式的替代。一下子，RSS 貌似终于有了一个单一的权威规范。

## 大分叉

一年后，RSS 0.91 规范变得严重不充分。人们想用 RSS 处理种种标准未处理的事情。规范的另一些部分看起来则是毫无必要的约束——比如每个 RSS 频道最多只能包含 15 项。

在那时，RSS 已经被更多的几个组织所接受。与看起来在 RSS 0.91 后已失去兴趣的网景不同，大玩家分别是 Dave Winer 的 UserLand Software；经营着一个名为 Meerkat 的 RSS 聚合器的 OReilly Net；以及同样经营着一个专注于新闻的 RSS 聚合器的 Moreover.com。[^17] 通过邮件列表，这些组织的代表与其他人定期讨论如何改良 RSS 0.91。但同样也有关于改良应该如何的深深的分歧。

发生最多讨论的邮件列表被称为 the Syndication 邮件列表。[一份 the Syndication 邮件列表的存档](https://groups.yahoo.com/neo/groups/syndication/info) 现在仍可获得。这是一份令人惊异的历史资源。它提供了一份那些深深的分歧如何事实上导致了 RSS 社区的政治分裂的刹那解释。

即将到来的分裂的一方是 Winer。Winer 对于改善 RSS 非常急躁，但他想要以相对保守的方式来改变它。在 2000 年 6 月，他在 UserLand 网站上公布了他自己的 RSS 0.91 标准，意味着 RSS 更深一层的发展的起点。网景公布的 RSS 0.91 标准没有任何的重大改变。Winer 在一篇博文中声称伴随着他的标准的仅仅是一份必要的 RSS 如何在真实环境被使用的“清理”文档，因为网景的标准已经不再维护。[^18] 同一篇文章中，他认为 RSS 之所以成功，是因为它足够简单，如果将命名空间或 RDF 再添加到这个格式中——在 the Syndication 邮件列表中的一些人已经建议做这些事——它“会极大地复杂化，恕我直言，在内容提供者层面，提升复杂性什么都给我们带来”。几乎同时，在一则被发到 the Syndication 邮件列表的信息中，Winer 建议，那些问题已经足够重要，这可能使他去创建一个分支：

> 我仍在思考如何使 RSS 继续向前。我完全想要在 RSS2 中使用 冰一样的东西，在我的列表顶部发布与订阅，但我将拼命包围简单性。我爱可选的元素。我不想走命名空间与提要的老路，或者试着把它变成 RDF 的一个方言。我理解某些人想要这样，因此我猜我们走到了一个分岔点。我对这个分支将会走向何方有着自己的主张，但我至少在现在自己保存着那些。[^19]

一起反对 Winer 的是其他几个人，包括 O'Reilly 的 Rael Dornfest，Ian Davis（一家名为 Calaba 的搜索初创企业的负责人），与一位早熟的 14 岁少年 Aaron Swartz，他们都认为 RSS 需要命名空间以容纳大家想要用它处理的许多不同事物。在另一个由 O'Reilly 主办的邮件列表中，Davis 提出了一个基于命名空间的模块系统，写道这样一个系统会“使 RSS 比起往过分复杂的规范中填充新功能，能像我们想要的那样可扩展”。[^20] “命名空间阵营”相信 RSS  很快会比起作为博客文章聚合，能被用的更多，所以命名空间不是成为并发症，而是保持 RSS 在处理越来越多的情况时保持可被管理的唯一办法。

关于命名空间的争执的根源是关于 RSS 到底是为了什么的更深层面的意见不一。Winer 为了同步聚合他博客的博文而创造了他的 Scripting News 格式。Guha 与 Libby 在网景设计了 RSS 并称其为“RDF Site Summary”因为在他们脑中这是一个在网景的在线门户中以缩略重写一个网站的方法。Davis 在写给 Syndication 邮件列表时解释称他认为 RSS “最初被构思为一个建立迷你站点地图的办法”，现在他和其他人想扩展 RSS “以比起简单的新闻标题包含更多种类的信息，及满足过去十二个月里出现的 RSS 的新应用”。[^21] Winer 写了一篇多刺的回复，陈述称他的 Scripting News 格式是事实上的最初的 RSS，而且它曾意味着一个不同的意思。鉴于参与 RSS 开发的大多数人在 RSS 为何被创造一事上意见不一，一个分支看起来是不可避免的。

分支发生在 Dornfest 宣布提出 RSS 1.0 标准并形成 RSS 开发工作小组——将会包括 Davis, Swartz及其他几位但并没有 Winer——以对发表做好准备。在被提出的标准中，RSS 再一次代表“RDF Site Summary”，因为 RDF 已经又被加了回来以代表几个 RSS 元素的元数据属性。这份标准承认了 Winer 的名字，给了他通过他的“传道”推广 RSS 的声誉。[^22] 但它也争论称仅仅给 RSS 添加更多的元素而没有通过一个模块系统提供可扩展性——这正是 Winer 所建议的——“牺牲了可扩展性”。这份标准继续为 RSS 定义一个基于 XML 命名空间的模块系统。

Winer 对于 RSS 开发工作小组自行霸占了“RSS 1.0”之名非常愤怒。[^23] 在另一个关于分散化的邮件列表中，他将 RSS-DEV 工作团队所作描述为盗窃。[^24] 聚合邮件列表的其他成员也感觉 RSS-DEV 工作团队在社区就如何发展 RSS 这一问题上达成一致之前不该使用“RSS”的名字。但是工作团队坚持使用这个名字。Dan Brickley，RSS-DEV 工作团队的一个成员，为这个决定辩护称“提议中的 RSS 1.0 绝对是基于原始的 RSS 的愿景，其本身曾有相当的遗产影响了 MCF （一个 RDF 的前身）与相关的规格（CDF 等）”。[^25] 他基本上感觉比起 Winer，RSS 1.0 的努力对 RSS 之名有着更好的声明，因为 RDF 原来就是 RSS 的一部分。RSS-DEV 工作团队在 12 月发布了他们的标准的最终版本。同一个月，Winer 发布了他自己对于 RSS 0.91 的改进，他在 UserLand 网站上将其称为 RSS 0.92。RSS 0.92 对 RSS 做了一些小的可选改进，很快增加的 `<enclosure>` 标签被大范围用于播客。RSS 有了官方的分支。

我仍不清楚为何没有更大的努力使 Winer 进入 RSS-DEV 工作团队中。正如工作团队中的人们承认的，他是聚合邮件列表中的一名杰出贡献者，且对 RSS 的流行有着明显的大部分贡献。但 Tim O'Reilly，O'Reilly 的创始人与 CEO，在一个 UserLand 讨论组中解释道 Winer 或多或少地拒绝了参与：

> 一群参与了 RSS 的人聚在一起以思考其未来演变。Dave 是团队的一部分。当团队的一致意见转向了他不喜欢的方向时，Dave 停止了参与，并将其表现的像是 O'Reilly 图谋从他那接管 RSS ，罔顾 O'Reilly 的 Rael Dornfest 只是被提议的 RSS 1.0 标准众多作者之一的事实，且作者中的很多人在开发中都有着与 Dave 同等的历史。[^26]

对此，Winer 曾言：

> 我在那份声明的两周前碰到了 Dale (Dougherty)，他对于其将被称为 RSS 1.0 的事什么都没说。在其被宣布之前的周五，我与 Rael 通了电话，同样他也没说他们将称之为 RSS 1.0。在其公开宣布时我才知道。

> 让我问你一个直接的问题。如果证明了那份标准被命名为“RSS 1.0”的计划完全被秘密的完成，没有任何的警告或商量，或者是一个让聚合邮件列表里的成员们同意与否的机会，而不仅仅是我，你会做什么？

> UserLand 为创造、普及与支持 RSS 做了大量的工作。我们离开了，让你们这些家伙拥有了这个名字。这就是顶级。如果我想对网络聚合做任何进一步工作，我必须用一个不同的名字。Tim 为什么又怎么会这样？[^27]

我不能在聚合邮件列表中找到任何在使用 RSS 1.0 名称声明的提议前的讨论。

RSS 在 2003 年会再度分支，当几位开发者对于 RSS 社区中的争吵非常沮丧，于是寻求创造一个全新的格式。这些开发者创造了 Atom，一个废除了 RDF 而拥抱 XML 命名空间的格式。Atom 最终被 [一个提议的 IETF 标准](https://tools.ietf.org/html/rfc4287) 所规定。在 Atom 的推行之后，有了三个相竞争的 RSS 版本：Winer 的 RSS 0.92（在 2002 年升级为 RSS 2.0 并被重命名为“Really Simple Syndication”），RSS-DEV 工作团队的 RSS 1.0，以及 Atom。

## 衰落

相竞争的 RSS 标准的增加可能在我会简短讨论的其他方面阻碍了 RSS。但这并没有阻止 RSS 在 2000 年间变得极为流行。2004 年，纽约时报开始用 RSS 提供其新闻摘要并写了一篇文章对外行人解释何为 RSS 与如何使用。[^28] Google Reader，一个最终被数百万人使用的 RSS 聚合器，在 2005 年开始。2013 年，RSS 看起来已足够流行到纽约时报，在其对 Aaron Swartz 的讣告中，称之为“无所不在的”技术。[^29] 一时间，在整个世界三分之一的人都注册了 Facebook 前，RSS 一直是网络上很多人了解最新新闻的渠道。

纽约时报在 2013 年一月发行了 Swartz 的讣告。到了那个时候，然而 RSS 已经事实上已经到了拐点，并在其成为一个鲜为人知的技术之路上渐行渐远。Google Reader 在 2013 年七月被关闭，表面上是因为“在过去几年间”用户数量一直在下降。[^30] 这引出了几篇不同途径的文章宣称 RSS 已死。但多年来人们一直宣称 RSS 已死，甚至在 Google Reader 关闭之前。Steve Gillmor，在 2009 年五月为 TechCrunch 的文章中，建议称“是时候完全离开 RSS 并转向 Twitter 了”因为“RSS 再也不能办成事了”。[^31] 他指出 Twitter 基本上是一个更好的 RSS 资讯，因为它在文章自身之外，能展示给你人们正在想什么。它允许你关注人而非只是频道。Gillmor 告诉他的读者，是时候让 RSS 撤回幕后了。他以鲍勃迪伦的“Forever Young”中的一节结束了文章。

现在，RSS 仍未死亡。但也不像过去那样那么流行。很多人对 RSS 为何失去了其普及度做出了种种解释。可能最具说服力的解释是 Gillmor 在 2009 年给出的。社交网络，就像 RSS 一样，提供了一个能看到网络上所有最新信息的信息流。社交网络接替了 RSS 因为它们仅仅是更好的信息流。它们也给所属公司带来了更多的利益。有些人曾指责谷歌，例如，关闭了 Google Reader 以使人们去用 Google+。Google 可能能在 Google+ 上以 Google Reader 无法提供的途径赚钱。Marco Arment，Instapaper 的创始人，于 2013 年在其博客中写道：

> Google Reader 仅仅是 Facebook 发起的战争中最新的伤亡，看起来非常偶然：决定谁来拥有一切的战争。当谷歌事实上“拥有” Google Reader 且能利用其中产生的巨量的新闻与注意力数据，这与它们更重要的 Google+ 策略相冲突：他们需要每个人都通过 Google+ 来阅读与分享一切信息这样他们才能够在广告定位数据，广告收入，增长及关联性上与 Facebook 竞争。[^32]

如此用户与科技公司两者都意识到比起使用 RSS，他们能在使用社交网络时获得更多。

另一个理论则是 RSS 对于普通用户来说一直都太极客了。就连曾急于接受 RSS 并向其读者推广的纽约时报，也在 2006 年抱怨道 RSS 是“电脑极客们”所创造的“对用户极为不友好”的首字母缩略词。[^33] 在 2004 年 RSS 的图标被设计出来之前，像纽约时报一样的网站将他们的 RSS 信息链接到一个标有“XML”的橘色小方块上，显然这只是令人生畏。[^34] 尽管这个标记非常准确，因为点击这个链接会将不幸的用户带到一整页的 XML 代码。[这条非常好的推特](https://twitter.com/mgsiegler/status/311992206716203008) 捕获了 RSS 为何消亡的本质。普通人从未对使用 RSS 感到舒适；它从未真正被设计为一个面向消费者的技术且包含了太多的障碍；人们在更好的选择到来时便跳槽走了。

如果有着更长远的发展，RSS 可能能够克服种种局限性。可能 RSS 能以某种方法被扩展以使订阅了相同频道的朋友们能相互同步他们关于某篇文章的想法。但在
 RSS 开发者社区被卡在试图达成一致的时候，反之，像 Facebook 一样的公司能够“快速行动”。RSS 大分叉仅仅说明了那样做有多么难。所以如果我们扪心自问 RSS 为什么再也不流行，一个非常好的一级解释是社交网络取代了它。如果我们扪心自问社交网络为何能够取代它，答案可能是试图使 RSS 成功的人们面临着远比如建立 Facebook 更难的问题。如 Dornfest 在某个时刻给聚合邮件列表写的，“现在它比起序列化更像是政治，远不简单。”[^35]

所以现在我们只剩下集中的大量信息。某种程度上，我们**确实**有了 Kevin Werbach 在 1999 年预见的聚合互联网。毕竟，《洋葱》是一个依赖通过 Facebook 与推特的出版物，正如《宋飞正传》在其最初的运行后依赖于聚合以至获得了数百万。但是网络上的聚合只出现在极少数频道中，意味着我们中没人能“控制我们的网络形象”如同 Werbach 描述的那样。发生这种情况的一个原因是普通企业的贪婪——RSS 作为一个开放格式，不能使科技公司控制数据及他们所需要的广告观看者，所以他们不支持它。但更为普通的原因是集中存储比起共同标准更易设计。共识非常难以达到，这也需要时间，但没有共识被拒绝的开发者将会离开并创造相竞争的标准。这给我们的教训可能是如果我们想要看见一个更好、更开放的网络，我们必须在不强迫对方上做的更好。

[^1]: Kevin Werbach, “The Web Goes into Syndication,” Release 1.0, July 22, 1999, 1, accessed September 14, 2018, http://cdn.oreillystatic.com/radar/r1/07-99.pdf.

[^2]: ibid.（同上）

[^3]: Werbach, 8.

[^4]: Peter Wiggin, “RSS Delivers the XML Promise,” Web Review, October 29, 1999, accessed September 14, 2018, https://people.apache.org/~jim/NewArchitect/webrevu/1999/10_29/webauthors/10_29_99_2a.html.

[^5]: Ben Hammersley, RSS and Atom (O’Reilly), 8, accessed September 14, 2018, https://books.google.com/books?id=kwJVAgAAQBAJ.

[^6]: “RSS 0.90 Specification,” RSS Advisory Board, accessed September 14, 2018, http://www.rssboard.org/rss-0-9-0.

[^7]: “My Netscape Network Future Directions,” RSS Advisory Board, accessed September 14, 2018, http://www.rssboard.org/mnn-futures. 

[^8]: Tim Bray, “The RDF.net Challenge,” Ongoing by Tim Bray, May 21, 2003, accessed September 14, 2018, https://www.tbray.org/ongoing/When/200x/2003/05/21/RDFNet.

[^9]: Dan Libby, “RSS: Introducing Myself,” August 24, 2000, RSS-DEV Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/239.

[^10]: Alexandra Krasne, “Browser Wars May Become Portal Wars,” CNN, accessed September 14, 2018, http://www.cnn.com/TECH/computing/9910/04/portal.war.idg/index.html.

[^11]: Dave Winer, “Scripting News in XML,” Scripting News, December 15, 1997, accessed September 14, 2018, http://scripting.com/davenet/1997/12/15/scriptingNewsInXML.html.

[^13]: Dave Winer, “A Faceoff with Netscape,” Scripting News, June 16, 1999, accessed September 14, 2018, http://scripting.com/davenet/1999/06/16/aFaceOffWithNetscape.html.

[^14]: ibid.

[^15]: Dan Libby, “RSS 0.91 Specification (Netscape),” RSS Advisory Board, accessed September 14, 2018, http://www.rssboard.org/rss-0-9-1-netscape.

[^16]: Dave Winer, “Scripting News: 7/28/1999,” Scripting News, July 28, 1999, accessed September 14, 2018, http://scripting.com/1999/07/28.html.

[^17]: Oliver Willis, “RSS Aggregators?” June 19, 2000, Syndication Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/syndication/conversations/topics/173.

[^18]: Dave Winer, “Scripting News: 07/07/2000,” Scripting News, July 07, 2000, accessed September 14, 2018, http://essaysfromexodus.scripting.com/backissues/2000/06/07/#rss.

[^19]: Dave Winer, “Re: RSS 0.91 Restarted,” June 9, 2000, Syndication Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/syndication/conversations/topics/132.

[^20]: Leigh Dodds, “RSS Modularization,” XML.com, July 5, 2000, accessed September 14, 2018, http://www.xml.com/pub/a/2000/07/05/deviant/rss.html.

[^21]: Ian Davis, “Re: [syndication] RSS Modularization Demonstration,” June 28, 2000, Syndication Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/syndication/conversations/topics/188.

[^22]: “RDF Site Summary (RSS) 1.0,” December 09, 2000, accessed September 14, 2018, http://web.resource.org/rss/1.0/spec.

[^23]: Dave Winer, “Re: [syndication] Re: Thoughts, Questions, and Issues,” August 16, 2000, Syndication Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/syndication/conversations/topics/410.

[^24]: Mark Pilgrim, “History of the RSS Fork,” Dive into Mark, September 5, 2002, accessed September 14, 2018, http://www.diveintomark.link/2002/history-of-the-rss-fork.

[^25]: Dan Brickley, “RSS-Classic, RSS 1.0 and a Historical Debt,” November 7, 2000, Syndication Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/rss-dev/conversations/topics/1136.

[^26]: Tim O’Reilly, “Re: Asking Tim,” UserLand, September 20, 2000, accessed September 14, 2018, http://static.userland.com/userLandDiscussArchive/msg021537.html.

[^27]: Dave Winer, “Re: Asking Tim,” UserLand, September 20, 2000, accessed September 14, 2018, http://static.userland.com/userLandDiscussArchive/msg021560.html.

[^28]: John Quain, “BASICS; Fine-Tuning Your Filter for Online Information,” The New York Times, 2004, accessed September 14, 2018, https://www.nytimes.com/2004/06/03/technology/basics-fine-tuning-your-filter-for-online-information.html.

[^29]: John Schwartz, “Aaron Swartz, Internet Activist, Dies at 26,” The New York Times, January 12, 2013, accessed September 14, 2018, https://www.nytimes.com/2013/01/13/technology/aaron-swartz-internet-activist-dies-at-26.html.

[^30]: “A Second Spring of Cleaning,” Official Google Blog, March 13, 2013, accessed September 14, 2018, https://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html.

[^31]: Steve Gillmor, “Rest in Peace, RSS,” TechCrunch, May 5, 2009, accessed September 14, 2018, https://techcrunch.com/2009/05/05/rest-in-peace-rss/.

[^32]: Marco Arment, “Lockdown,” Marco.org, July 3, 2013, accessed September 14, 2018, https://marco.org/2013/07/03/lockdown.

[^33]: Bob Tedeschi, “There’s a Popular New Code for Deals: RSS,” The New York Times, January 29, 2006, accessed September 14, 2018, https://www.nytimes.com/2006/01/29/travel/theres-a-popular-new-code-for-deals-rss.html.

[^34]: “NYTimes.com RSS Feeds,” The New York Times, accessed September 14, 2018, https://web.archive.org/web/20050326065348/www.nytimes.com/services/xml/rss/index.html.

[^35]: Rael Dornfest, “RE: Re: [syndication] RE: RFC: Clearing Confusion for RSS, Agreement for Forward Motion,” May 31, 2001, Syndication Mailing List, accessed September 14, 2018, https://groups.yahoo.com/neo/groups/syndication/conversations/messages/1717.