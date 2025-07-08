# Roy Fielding 被“挪用”的 REST 博士论文

*2020 年 6 月 28 日*

RESTful API 如今随处可见。这听起来有点意思，因为究竟有多少人真正理解“RESTful”这个词的含义呢？

我想，我们大多数人都能理解 [这位 Hacker News 论坛用户](https://news.ycombinator.com/item?id=7201871) 的心声：

> 我读过好几篇关于 REST 的文章，甚至还翻过一点原始论文。可我还是对它一知半解。我开始觉得，也许根本没人真正懂它，这可能只是一个定义得非常模糊的概念。

我原本打算写一篇博客文章，深入探讨 REST (Representational State Transfer，表征状态转移) 是如何成为互联网通信领域主导范式的。为此，我从阅读 [Roy Fielding 在 2000 年发表的博士论文](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation_2up.pdf) 开始研究，正是这篇论文将 REST 概念引入了世界。然而，读完 Fielding 的论文后，我才发现，真正有趣的故事其实是 Fielding 的思想为何会被如此广泛地误解。

很多人都知道 REST 概念源自 Fielding 的这篇博士论文，但真正读过这篇论文的人却少之又少 (这倒也情有可原)。正因如此，关于这篇论文实际内容的误解才如此普遍。

这些误解中，最普遍的一个就是认为这篇论文直接探讨了如何构建 API (应用程序编程接口) 的问题。我一直以为，就像许多人可能想的那样，REST 从一开始就是为基于 HTTP (超文本传输协议) 构建的 Web API 设计的架构模型。我甚至曾猜测，也许在早期，人们在 HTTP 之上构建 API 时经历了一段混乱的摸索期，然后 Fielding 横空出世，提出了 REST 这种“正道”。然而，这个时间线根本说不通：我们今天所熟知的 Web 服务 API，直到 Fielding 发表他的博士论文几年后才真正兴起。

Fielding 的博士论文 (题为《架构风格与基于网络的软件架构设计》) 并非教你如何在 HTTP 之上构建 API，而是深入探讨 HTTP 本身。Fielding 曾参与 HTTP/1.0 规范的制定，并与他人共同撰写了 1999 年发布的 HTTP/1.1 规范。他真正感兴趣的是从 HTTP 协议设计中能学到哪些架构经验。他的论文将 REST 视为指导 HTTP/1.1 标准化过程的架构原则的精髓。Fielding 正是运用这些原则来决定哪些提案应该被纳入 HTTP/1.1。举个例子，他曾拒绝了一项使用新的 `MGET` 和 `MHEAD` 方法来批量处理请求的提案，因为他认为该提案违反了 REST 所规定的约束，特别是 REST 系统中的消息应该易于代理和缓存的约束 [^1]。因此，HTTP/1.1 被设计成围绕持久连接，通过这种连接可以发送多个 HTTP 请求。(Fielding 还认为，Cookie (小型文本文件) 并不符合 RESTful 原则，因为它们为本应是无状态的系统增加了状态，但当时 Cookie 的使用已经根深蒂固了 [^2]。) 对 Fielding 来说，REST 并非是构建基于 HTTP 系统的指南，而是扩展 HTTP 的指南。

这并不是说 Fielding 不认为 REST 可以用来构建其他系统。只是他假设这些“其他系统”也必须是“分布式超媒体系统”。这正是人们对 REST 的另一个普遍误解：认为它是一种可以用于任何网络应用程序的通用架构。但你可以将 Fielding 在论文中介绍 REST 的那部分，概括为这样一句话：“听着，我们刚刚设计了 HTTP，所以如果你也发现自己正在设计一个 *分布式超媒体系统*，那么你应该使用我们精心设计的 REST 架构，它能让事情变得更简单。” 考虑到万维网 (Web) 已经存在，Fielding 为何会认为有人还会尝试构建这样的系统，这并不显而易见；或许在 2000 年，他觉得世界上可能容纳不止一个分布式超媒体系统。无论如何，Fielding 明确指出，REST 的初衷是为了解决在互联网上连接超媒体时出现的扩展性 (scalability) 和一致性 (consistency) 问题，*而不是* 作为一般分布式应用程序的架构模型。

如今，我们记住 Fielding 的这篇论文，是因为它引入了 REST 概念。但实际上，这篇论文的核心思想是：一刀切的软件架构有多么糟糕，以及我们应该如何根据自身需求，更好地选择合适的软件架构。论文中只有一章专门讨论 REST 本身；大部分篇幅都用于对各种替代架构风格进行分类 [^3]，这些风格都可以用于网络应用程序。其中包括受 Unix (一种操作系统) 管道启发的管道-过滤器 (Pipe-and-Filter, PF) 风格，以及客户端-服务器 (Client-Server, CS) 风格的各种改进，例如分层客户端-服务器 (Layered-Client-Server, LCS)、客户端-缓存-无状态-服务器 (Client-Cache-Stateless-Server, C$SS) 和分层客户端-缓存-无状态-服务器 (Layered-Client-Cache-Stateless-Server, LC$SS)。这些缩写虽然有些拗口，但 Fielding 的核心观点是，你可以混合搭配现有风格所施加的约束，从而派生出新的风格。REST 就是以这种方式派生出来的，它本可以被命名为——但出于显而易见的原因没有——统一分层按需代码客户端缓存无状态服务器 (Uniform-Layered-Code-on-Demand-Client-Cache-Stateless-Server, ULCODC$SS)。Fielding 建立这个分类法，正是为了强调不同的约束适用于不同的应用程序，而最后一组约束，是他认为最适合 HTTP 的。

这正是 REST 如今无处不在的深层讽刺之处。REST 现在被盲目地应用于各种网络应用程序，然而 Fielding 最初提出 REST，却是为了演示如何根据单个应用程序的特定需求，量身定制一套软件架构。

我很难理解这一切是如何发生的，因为 Fielding 对“不让形式服从功能”的弊端阐述得如此明确。他几乎在论文的开篇就警告说，“盲目追逐流行词进行设计是一种常见现象”，这正是由于未能正确理解软件架构所导致的 [^4]。几页之后，他又再次强调了这一主题：

> 有些架构风格常常被描绘成适用于所有软件的“银弹”解决方案。然而，一个优秀的设计师应该选择与所要解决的特定问题需求相匹配的风格 [^5]。

REST 本身就是一个特别糟糕的“银弹”解决方案，因为正如 Fielding 后来指出的那样，它包含了一些权衡取舍，除非你正在构建一个分布式超媒体应用程序，否则这些权衡可能并不合适：

> REST 的设计目标是高效地进行大粒度超媒体数据传输，它针对万维网的常见情况进行了优化，但这也导致其接口对于其他形式的架构交互而言并非最优 [^6]。

Fielding 之所以提出 REST，是因为万维网面临着一个棘手的“无政府主义可扩展性”问题。Fielding 所说的“无政府主义可扩展性”，指的是需要以高性能的方式，跨越组织和国家边界连接文档。REST 所施加的约束，正是为了解决这个无序扩展问题而精心挑选的。那些 *面向公众的* Web 服务 API 也必须处理类似的问题，因此不难理解为何 REST 在这些场景下显得尤为重要。然而，如今我们却常常发现，即使某个工程团队的后端系统只与他们完全掌控的客户端进行通信，他们也依然会选择使用 REST 来构建后端，这已经不足为奇了。我们都变成了 [Monty Python (英国喜剧团体) 短剧](https://www.youtube.com/watch?v=vNoPJqm3DAY) 中的那位建筑师，他因为只擅长建造屠宰场，所以把公寓楼也设计成了屠宰场的风格。(Fielding 在他的博士论文中，就引用了这段短剧中的一句台词作为题词：“对不起……您是说‘刀’吗？”)

那么，既然 Fielding 的博士论文通篇都在强调要避免“银弹”式的软件架构，REST 又是如何成为各种 Web 服务的“事实标准”的呢？

我的理论是，在 2000 年代中期，那些受够了 SOAP (Simple Object Access Protocol，简单对象访问协议) 并渴望另辟蹊径的人们，需要一个属于他们自己的四字母缩写。

我这可不是完全开玩笑。SOAP，全称简单对象访问协议 (Simple Object Access Protocol)，是一个冗长且复杂的协议。如果你不先搞懂一大堆相互关联的 XML (可扩展标记语言) 规范，根本就无法使用它。早期的 Web 服务提供的 API 都基于 SOAP，但到了 2000 年代中期，随着越来越多的 API 涌现，那些被 SOAP 复杂性折磨得焦头烂额的软件开发者们，开始大规模地“逃离”它。

在这群开发者中，SOAP 激起了普遍的鄙视。2007 年，Ruby-on-Rails (一个流行的 Web 开发框架) 甚至放弃了对 SOAP 的支持，其创建者 David Heinemeier Hansson (大卫·海涅迈尔·汉森) 发表了这句极具代表性的评论：“我们觉得 SOAP 过于复杂。它已经被那些‘企业人士’接管了，而一旦发生这种事，通常就不会有什么好结果。” [^7] 那些“企业人士”希望一切都正式规范化，但对于追求效率、讲究“搞定事情”的开发者来说，这简直是浪费时间。

如果那些“搞定事情”的开发者不打算使用 SOAP，他们仍然需要一套标准的行事方式。既然大家都在用 HTTP，而且考虑到 HTTP 提供了大量的代理 (proxy) 和缓存 (caching) 支持，至少作为传输层，HTTP 还会继续被广泛使用，那么最简单的方法就是直接依赖 HTTP 现有的语义。于是，他们就这么做了。他们本可以把这种方法命名为“去他妈的，HTTP 过载” (Fuck It, Overload HTTP, FIOH)，这个名字其实非常贴切——任何曾为业务逻辑错误该返回哪个 HTTP 状态码而纠结的人都能深有体会。但与 SOAP 那些严谨的正式规范工作相比，这个名字听起来未免太过轻率和随意了。

幸运的是，当时正好有一篇博士论文，由 HTTP/1.1 规范的共同作者撰写，它与扩展 HTTP 有着某种模糊的关联，可以为 FIOH 提供一层学术上的“体面外衣”。于是，REST 就这样被“挪用”了，为那些本质上只是 FIOH 的做法提供了理论上的掩护。

我并不是说事情就是这样精确发生的，也不是说那些不拘一格的创业者之间真的存在什么“挪用”REST 的阴谋。但这个故事确实帮助我理解了，当 Fielding 的博士论文根本不是关于 Web 服务 API 时，REST 是如何成为 Web 服务 API 的主流模型的。采纳 REST 的约束在某些情况下确实有道理，特别是对于那些需要跨越组织边界、面向公众的 API 来说，它们能从 REST 的“统一接口”中受益。这种关联，很可能就是 REST 最初与 Web API 构建联系起来的核心原因。然而，如果我们将今天流行的做法想象成一种名为“FIOH”的独立方法，它只是部分地出于营销目的借用了“REST”这个名字，那么这就能很好地解释，为什么我们今天所熟知的 RESTful API 与 Fielding 最初描述的 REST 架构风格之间存在如此多的差异。

举个例子，REST 的“纯粹主义者”们常常抱怨，那些所谓的 REST API 实际上并非真正的 REST API，因为它们没有使用“超媒体作为应用程序状态引擎” (Hypermedia as The Engine of Application State, HATEOAS)。Fielding 本人 [也曾提出过这种批评](https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)。在他看来，一个真正的 REST API 应该允许你从一个基础端点 (endpoint) 出发，通过跟随链接来导航到所有其他端点。如果你认为人们真的在努力构建符合 REST 原则的 API，那么 HATEOAS 的缺失无疑是一个巨大的疏漏——HATEOAS 确实是 Fielding 最初 REST 概念的基石，特别是考虑到“表征状态转移” (Representational State Transfer) 中的“状态转移”指的是通过资源之间的超链接来导航状态机 (而不是像许多人认为的那样，仅仅是在网络上传输资源状态) [^8]。但如果你设想，大家只是在构建 FIOH API，然后心照不宣地将其宣传为 REST API，或者更诚实一点地称之为“RESTful”API，那么 HATEOAS 自然就变得无关紧要了。

同样，你可能会惊讶地发现，Fielding 的博士论文中，根本没有提及哪个 HTTP 动词 (verb) 应该映射到哪个 CRUD (Create, Read, Update, Delete，创建、读取、更新、删除) 操作。尽管软件开发者们总是乐此不疲地争论，究竟是使用 PUT 还是 PATCH 来更新资源更符合 RESTful 规范。将 HTTP 动词标准地映射到 CRUD 操作，这确实是一件有用的事情，但这种标准映射属于 FIOH 的范畴，而非 REST 的一部分。

这就是为什么，与其说没有人真正理解 REST，不如说我们应该把“REST”这个术语看作是被“挪用”了。现代的 REST API 概念与 Fielding 的 REST 架构确实存在历史渊源，但实际上两者是相互独立的。记住这种历史联系，可以很好地指导我们何时应该构建一个 RESTful API。你的 API 是否需要像 HTTP 那样，跨越组织和国家边界？如果是，那么构建一个具有可预测、统一接口的 RESTful API 也许是正确的选择。如果不是，那么最好记住 Fielding 所倡导的“形式服从功能”原则。也许像 GraphQL (一种用于 API 的查询语言) 甚至仅仅是 JSON-RPC (一种远程过程调用协议) 会更适合你想要实现的目标。

*如果您喜欢这篇文章，那么每四周都会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 订阅源](https://twobithistory.org/feed.xml)，确保您不会错过任何新文章。*

*TwoBitHistory 往期精彩回顾…*

> 新文章发布啦！我写了一篇关于如何使用一台 20 世纪 30 年代主要由齿轮构成的模拟计算机来求解微分方程的文章。作为额外福利，里面甚至还包含了一些关于如何瞄准巨型火炮的内容。<https://t.co/fwswXymgZa>
>
> — TwoBitHistory (@TwoBitHistory) [2020 年 4 月 6 日](https://twitter.com/TwoBitHistory/status/1247187881946275841?ref_src=twsrc%5Etfw)

[^1]: Roy Fielding. 《架构风格与基于网络的软件架构设计》，第 128 页。2000 年。加州大学欧文分校博士论文，2020 年 6 月 28 日访问，[https://www.ics.uci.edu/\~fielding/pubs/dissertation/fielding\_dissertation\_2up.pdf](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation_2up.pdf)。
[^2]: Fielding，第 130 页。
[^3]: Fielding 区分了软件架构和软件架构“风格”。REST 是一种架构风格，它在 HTTP 的架构中有一个实例。
[^4]: Fielding，第 2 页。
[^5]: Fielding，第 15 页。
[^6]: Fielding，第 82 页。
[^7]: Paul Krill. 《Ruby on Rails 2.0 发布用于 Web 应用》，InfoWorld。2007 年 12 月 7 日，2020 年 6 月 28 日访问，[https://www.infoworld.com/article/2648925/ruby-on-rails-2-0-released-for-web-apps.html](https://www.infoworld.com/article/2648925/ruby-on-rails-2-0-released-for-web-apps.html)。
[^8]: Fielding，第 109 页。