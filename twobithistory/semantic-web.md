# 语义网 ( Semantic Web ) 究竟去哪儿了？

*2018 年 5 月 27 日*

2001 年，万维网 ( World Wide Web ) 的发明者蒂姆·伯纳斯-李 ( Tim Berners-Lee ) 在《科学美国人》 ( Scientific American ) 上发表了一篇文章。伯纳斯-李与另外两位研究员奥拉·拉西拉 ( Ora Lassila ) 和詹姆斯·亨德勒 ( James Hendler ) 希望向世界预告他们所预见的网络即将发生的革命性新变化。自十年前问世以来，万维网已迅速成为全球共享文档的最佳方式。现在，作者们承诺，万维网将进化，不仅包含文档，还将涵盖人们能想象到的各种数据。

他们将这个新网络称为语义网 ( Semantic Web )。语义网的伟大承诺在于，它不仅人类能读懂，机器也能理解。网页对软件程序来说将是“有意义的”——它们将拥有语义 ( semantics )——从而允许程序像人类一样与网络互动。程序可以在语义网中交换数据，而无需专门编程就能相互通信。根据伯纳斯-李、拉西拉和亨德勒的描述，一个享受语义网诸多便利的典型一天可能看起来是这样的：

> *娱乐系统正播放着披头士乐队的《我们能解决》 ( We Can Work It Out )，这时电话响了。皮特接起电话，他的手机通过向所有其他带有音量控制的本地设备发送消息，调低了音量。他的妹妹露西从医生办公室打来电话：“妈妈需要去看专科医生，然后还得进行一系列的物理治疗。大概每两周一次。我打算让我的智能体 ( agent ) 安排预约。”皮特立刻同意分担接送任务。在医生办公室，露西通过她的手持网络浏览器指示她的语义网智能体。该智能体迅速检索了妈妈在家附近 20 英里半径内、在可信评价服务中评级为优秀或非常好的处方治疗信息。然后，它开始尝试在可用的预约时间 ( 由各个提供商的智能体通过他们的网站提供 ) 与皮特和露西繁忙的日程之间找到匹配。*[^1]

这个愿景是，语义网将成为智能“智能体”的乐园。这些智能体将自动化世界刚刚学会如何在网络上完成的大部分工作。

![](https://twobithistory.org/images/scientific_american_cover.jpg)

一段时间内，这个愿景吸引了很多人。在 AJAX 等新技术导致硅谷 ( Silicon Valley ) 所谓的 Web 2.0 兴起之后，伯纳斯-李开始将语义网称为 Web 3.0。许多人认为语义网确实是不可避免的下一步。2006 年《纽约时报》 ( New York Times ) 发表的一篇文章引用了伯纳斯-李在一次会议上的讲话，他说现有的网络在未来二十年内，只会被视为更伟大事物的“胚胎期”形式 [^2]。文章中还引用了一位风险投资家的话，他声称语义网将是“深远的”，最终“就像今天的网络对我们来说显而易见一样显而易见”。

当然，我们所承诺的语义网尚未实现。在 2018 年，我们有像 Siri 这样的“智能体”可以为我们完成某些任务。但 Siri 之所以能做到这些，是因为苹果 ( Apple ) 的工程师手动将其连接到各种网络服务，而每种服务都只能回答狭窄的问题类别。一个重要的结果是，如果你的服务不够大、不够重要，不足以引起苹果的关注，你就无法直接从自己的网站向 Siri 宣传你的服务。与伯纳斯-李及其合著者想象的物理治疗师可以在网上挂牌营业不同，今天我们只能依赖巨大的、中心化的信息库。今天的物理治疗师必须将他们的诊所信息输入谷歌 ( Google ) 或 Yelp，因为这些是智能手机智能体唯一知道如何使用的服务，也是人类唯一会费心去查看的服务。我们当前现实与承诺的语义未来之间的关键区别，最好地体现在上面摘录中这句不经意的插话中：“*……预约时间 ( 由各个提供商的智能体通过**他们的**网站提供 )……*”

事实上，在过去十年中，万维网不仅未能成为语义网，甚至作为一个概念也面临消退的威胁。我们现在几乎不再谈论“万维网”，而是谈论“互联网”，后者在 2016 年已成为如此常见的术语，以至于报纸不再将其首字母大写。（公平地说，他们也不再将“万维网”首字母大写了。）有些人可能仍然抗议万维网和互联网是两回事，但这种区别正变得越来越模糊。我们今天的万维网正慢慢变成一个美化了的应用商店，只是众多下载使用封闭协议和模式与远程服务器通信的软件的最简单方式，这使得它在功能上与万维网出现之前的软件生态系统几乎相同。我们是如何走到这一步的？如果构建语义网的努力成功了，今天的万维网会是什么样子？或者说，长期以来是否存在太多反对去中心化网络的力量，以至于语义网注定会胎死腹中？

## 语义网推销员和他们的“元数据糟粕”

对于一些更注重实践的工程师来说，语义网从一开始就是一个乌托邦式的梦想。

语义网的基本思想是，每个人都将使用一套新标准，用小段 XML ( Extensible Markup Language ) 代码来标注他们的网页。这些 XML 代码对网页的呈现没有影响，但可以被软件程序读取，以推断出原本只有人类才能理解的意义。

这些 XML 代码是表达网页元数据 ( metadata ) 的一种方式。我们都熟悉文件系统中的元数据：当我们查看计算机上的文件时，可以看到它的创建时间、最后更新时间以及最初创建者。同样，语义网上的网页将能够告诉你的浏览器谁是该页面的作者，甚至这个人去了哪所学校，或者目前在哪里工作。理论上，这些信息将允许语义网浏览器在大量网页集合中回答查询。在《科学美国人》的文章中，伯纳斯-李和他的合著者解释说，例如，你可以使用语义网来查找你在会议上遇到但只记得部分姓名的人。

博客作者兼数字权利活动家科里·多克托罗 ( Cory Doctorow ) 在 2001 年发表了一篇有影响力的文章，指出了依赖自愿提供的元数据所存在的诸多问题。他认为，一个拥有“详尽、可靠”元数据的世界将是美好的，但这样的世界是“一个白日梦，建立在自我欺骗、书呆子式的傲慢和被夸大到离谱的市场机遇之上” [^3]。多克托罗发现自己在一系列技术会议上就语义网问题进行了辩论，并希望整理出语义网狂热者 ( 多克托罗称他们为“语义网推销员” ) 忽视的严重问题 [^4]。这篇题为《元数据糟粕》 ( Metacrap ) 的文章指出了七个问题，其中包括一个显而易见的事实：大多数网络用户很可能根本不提供元数据，或者提供大量旨在吸引点击的误导性元数据。即使所有用户都普遍勤奋且善意，为了使元数据健壮且可靠，所有用户都必须就每个重要概念达成单一表示形式。多克托罗认为，在某些情况下，单一表示形式可能不适合、不可取或对所有用户不公平。

事实上，万维网已经出现人们滥用 HTML `<meta>` 标签 ( 至少在 HTML 4 早期就已引入 ) 的情况，试图提高其网页在搜索结果中的可见性。在 2004 年的一篇论文中，本·穆纳特 ( Ben Munat )，当时常青州立学院 ( Evergreen State College ) 的一位学者，解释了搜索引擎曾如何尝试使用通过 `<meta>` 标签提供的关键词来索引结果，但很快发现不道德的网页作者会包含与网页实际内容无关的标签 [^5]。结果，搜索引擎开始忽略 `<meta>` 标签，转而使用复杂的算法来分析网页的实际内容。穆纳特总结说，通用语义网是不可行的，重点应该放在医学和科学领域的特定领域。

其他人也认为语义网项目存在致命缺陷，尽管他们将缺陷归咎于其他地方。著名程序员兼数字权利活动家亚伦·斯沃茨 ( Aaron Swartz ) 在他去世后出版的一本未完成的关于语义网的书中写道，多克托罗是在“攻击一个稻草人” [^6]。没有人期望网络上的元数据会完全准确可靠，但语义网，或者至少是其范围更现实的版本，仍然是可能的。在斯沃茨看来，问题在于“语义网狂热者”在应对挑战时所带来的“数学的规范化思维和学术界的制度结构”。在万维网联盟 ( World Wide Web Consortium, W3C ) 等论坛中，在没有任何应用需要标准化之前，就投入了大量精力进行标准制定和讨论。而这些“塔木德式辩论”中产生的标准是如此抽象，以至于很少有标准得到广泛采用。少数几个被采用的，比如 XML，则是“对地球来说是普遍的祸害，是对勤奋程序员的冒犯，它们将合理的格式 ( 如 JSON ) 排挤出去，取而代之的是毫无现实基础的过度复杂的‘毛球’”。如果语义网像最初的万维网一样，其标准能被所有人欣然采纳，它或许会蓬勃发展。但这从未发生，因为——正如本博客 [之前讨论过](https://twobithistory.org/2017/09/21/the-rise-and-rise-of-json.html) 的那样——当替代方案既完全足够又更容易理解时，像 XML 这样的所谓益处并不容易向程序员推销。

## 构建语义网

如果说语义网并非完全不可能，那么它始终需要众多聪明人协同合作才能实现。

构建语义网的漫长努力据说包括四个阶段 [^7]。第一阶段从 2001 年持续到 2005 年，是语义网活动的黄金时代。在 2001 年至 2005 年间，W3C 发布了一系列新标准，奠定了语义未来的基础技术。

其中最重要的是资源描述框架 ( Resource Description Framework, RDF )。W3C 于 2004 年发布了 RDF 标准的第一个版本，但 RDF 自 1997 年以来就已存在，当时一个 W3C 工作组在一份规范草案中引入了它。RDF 最初被设想为一种元数据建模工具，部分基于苹果 ( Apple ) 工程师拉马纳坦·古哈 ( Ramanathan Guha ) 早期为苹果计算机上存储的文件开发元数据系统的尝试 [^8]。W3C 的语义网工作组将 RDF 重新用于表示任意类型的通用知识。

RDF 将成为语义网页表达信息的语法。这种语法很简单：关于世界的事实以主语、谓语和宾语的三元组 ( triplets ) 形式在 RDF 中表达。蒂姆·布雷 ( Tim Bray ) 曾与拉马纳坦·古哈合作开发早期版本的 RDF，他给出了以下描述电视节目和电影的例子：[^9]

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

@prefix ex: <http://www.example.org/> .


ex:vincent_donofrio ex:starred_in ex:law_and_order_ci .

ex:law_and_order_ci rdf:type ex:tv_show .

ex:the_thirteenth_floor ex:similar_plot_as ex:the_matrix .

```

语法并不重要，特别是考虑到 RDF 可以用多种格式表示，包括 XML 和 JSON。这个例子采用的是一种名为 Turtle 的格式，它将 RDF 三元组表示为以句号结尾的直白语句。上面 `@prefix` 前缀声明之后出现的三个基本语句，陈述了三个事实：文森特·多诺弗里奥 ( Vincent Donofrio ) 主演了《法律与秩序》 ( Law and Order )，《法律与秩序》是一种电视节目，电影《十三层楼》 ( The Thirteenth Floor ) 的情节与《黑客帝国》 ( The Matrix ) 相似。（如果你不知道文森特·多诺弗里奥是谁，也没看过《十三层楼》，那我也一样，1999 年我在看尼克儿童频道 ( Nickelodeon ) 和喝 Capri Suns 果汁。）

在语义网开发的第一个时代，其他最终确定和起草的规范描述了 RDF 的所有使用方式。属性中的 RDF ( RDF in Attributes, RDFa ) 定义了如何将 RDF 嵌入 HTML 中，以便浏览器、搜索引擎和其他程序可以从网页中获取意义。RDF Schema 和另一个名为 OWL 的标准允许 RDF 作者划定其 RDF 文档中有效和无效 RDF 语句之间的界限。换句话说，RDF Schema 和 OWL 是创建本体 ( ontologies ) 的工具，本体是对特定领域内可以和不可以表达的内容的明确规定。例如，一个本体可能包含一条规则，规定一个人不能在不是另一个人父母的情况下成为其母亲。希望这些本体能够被广泛用于不仅检查野外发现的 RDF 的准确性，还能对省略的信息进行推断。

2006 年，蒂姆·伯纳斯-李发表了一篇短文，他在文中指出，现有的语义网标准工作需要通过协同努力来补充，以使语义数据 ( semantic data ) 在网络上可用 [^10]。此外，一旦数据在网络上可用，重要的是语义数据要链接到其他类型的语义数据，确保一个像现有网络一样互联互通的基于数据的网络兴起。伯纳斯-李使用“链接数据 ( linked data )”一词来描述这种理想情况。尽管“链接数据”在某种意义上只是对语义网最初愿景的重述，但它成为了人们可以团结起来的术语，从而相当于对语义网项目进行了品牌重塑。

伯纳斯-李的文章开启了语义网发展的第二阶段，重点从制定标准和构建玩具示例转向创建和推广大型 RDF 数据集。其中最成功的可能就是 [DBpedia](http://wiki.dbpedia.org/)，这是一个从维基百科 ( Wikipedia ) 文章中提取的巨大 RDF 三元组存储库。DBpedia 大量使用了 2000 年代上半叶开发的语义网标准，是使用 W3C 新格式可以实现什么的杰出范例。如今，DBpedia 描述了 458 万个实体，并被《纽约时报》 ( NY Times )、BBC 和 IBM 等组织使用，IBM 将 DBpedia 用作 IBM Watson 的知识来源，后者是赢得《危险边缘》 ( Jeopardy ) 问答比赛的人工智能系统。

![](https://twobithistory.org/images/linked_data.png)

语义网发展的第三阶段涉及调整 W3C 的标准，以适应网络开发人员的实际实践和偏好。到 2008 年，JSON 已开始迅速崛起并广受欢迎。XML 附带了一堆用途不明的相关技术 ( XLST、XPath、XQuery、XLink )，而 JSON 则只是 JSON。它更简洁、更易读。企业家兼 W3C 成员马努·斯波尼 ( Manu Sporny ) 已经在他的公司开始使用 JSON，并希望找到一种简单的方法让 RDFa 和 JSON 协同工作 [^11]。结果就是 JSON-LD，它本质上是为选择 JSON 而非 XML 的世界重新构想的 RDF。斯波尼与他的首席技术官戴夫·朗利 ( Dave Longley ) 于 2010 年发布了 JSON-LD 的规范草案。在接下来的几年里，JSON-LD 和更新的 RDF 规范将是 W3C 语义网工作的主要焦点。JSON-LD 可以单独使用，也可以嵌入 HTML 页面中的 `<script>` 标签内，使其成为 RDF 和 RDFa 的替代方案。

JSON-LD 的工作与 [schema.org](http://schema.org/) 的发展同时进行，后者是一个集中式的简单模式 ( schemas ) 集合，用于描述网络上可能存在的事物。schema.org 由谷歌 ( Google )、必应 ( Bing ) 和雅虎 ( Yahoo ) 共同发起，其明确目的是通过商定一套共同的词汇表来提供更好的搜索结果。schema.org 的词汇表与 JSON-LD 一起，现在被用于驱动谷歌 ( Google ) 的知识图谱 ( Knowledge Graph ) 等功能。这种方法更实用、更不抽象，重点放在搜索结果中的即时应用。schema.org 团队在其网站上谨慎地声明，他们不打算创建“通用本体” [^12]。

如今，语义网的工作似乎已逐渐消退。W3C 仍在“数据活动 ( Data Activity )”的标题下进行一些语义网工作，这可以宽泛地称之为语义网项目的第四阶段。但具有讽刺意味的是，最近的“数据活动”项目是研究 W3C 如何改进其标准化流程 [^13]。即使是 W3C 现在似乎也认识到，其语义网标准很少被广泛采用，而更简单的标准会更成功。W3C 的态度似乎是收缩和反思，或许是希望在语义网再次展现前景时能做好更充分的准备。

## 挥之不去的影响

因此，正如有人生动描述的那样，语义网“就像去年路边被撞死的动物一样死透了” [^14]。至少，蒂姆·伯纳斯-李最初提出的、曾被认为是即将到来的网络未来的语义网版本，不太可能很快出现。话虽如此，许多在推动创建语义网过程中开发的技术和思想已被重新利用，并存在于各种应用中。如前所述，谷歌 ( Google ) 依赖语义网技术——现在主要是 JSON-LD——来在搜索结果旁边生成有用的概念性摘要。schema.org 维护着一个“词汇表”列表，网络开发人员可以使用它来发布易于广泛受众理解的数据——这是对公共、共享的本体可能是什么样子的一种新的、更实用的构想。在某种程度上，现在许多可用的 REST API 构成了缩减版的语义网。2001 年不可能实现的事情现在可以了：你可以轻松构建利用网络上各种数据的应用程序。不同之处在于，你需要事先逐个注册每个 API，这除了繁琐之外，还赋予了 API 主机对你如何访问其数据的巨大控制权。

语义网技术的另一个现代应用，也许是近年来在谷歌 ( Google ) 之外最流行和最成功的，是脸书 ( Facebook ) 的 [OpenGraph](http://ogp.me/) 协议。OpenGraph 协议定义了一个模式 ( schema )，网络开发人员可以使用它 ( 通过 RDFa ) 来确定网页在社交媒体应用中共享时如何显示。例如，在《纽约时报》 ( New York Times ) 工作的网络开发人员可能会使用 OpenGraph 来指定当《纽约时报》文章在脸书 ( Facebook ) 中共享时应显示的标题和缩略图。从某种意义上说，这是语义网技术的一种应用，忠实于语义网在元数据研究方面的起源。用关于谁撰写了网页以及网页内容是什么的额外信息来标记网页，正是语义网所依赖的那种元数据编写。但从另一个意义上说，OpenGraph 是语义网技术的一种应用，其目的与万维网的理念有些背道而驰。毕竟，这些元数据并非通用目的。人们使用 OpenGraph 标记他们的网页，是因为他们希望其内容的链接能在脸书 ( Facebook ) 中正确展开。脸书 ( Facebook ) 对你的网站了解得越多，它就越接近于在脸书 ( Facebook ) 内部复制你的整个网站，预示着一个开放网络 ( open web ) 成为脸书 ( Facebook ) 高耸蓝色围墙之外的神秘之地的未来。

JSON-LD 和 OpenGraph 的迷人之处在于，你可以在不了解主语-谓语-宾语三元组、RDF、RDF Schema、本体、OWL 或任何其他语义网技术的情况下使用它们——你甚至不需要了解 XML。马努·斯波尼 ( Manu Sporny ) 甚至说过，W3C 的 JSON-LD 工作组特意避免在 JSON-LD 规范中提及 RDF [^15]。这几乎可以肯定就是这些技术成功并持续流行的原因。没有人愿意使用一个只有通过阅读一整套规范才能完全理解的工具。

思考一下，如果像 JSON-LD 这样简单的格式早些出现，会发生什么，这很有趣。语义网本可以避开与 XML 的致命关联。更多人可能会被诱惑用 RDF 标记他们的网站，但即使那样也可能无法拯救语义网。肖恩·B·帕尔默 ( Sean B. Palmer )，一位从互联网上抹去了所有个人传记信息的“互联网人”，但他声称在 2000 年代曾在语义网领域工作过一段时间，他认为真正的问题在于缺乏一个真正去中心化的基础设施来托管语义网 [^16]。要托管你自己的网站，你需要从 ICANN 购买域名，使用 DNS 正确配置它，然后如果你没有自己的服务器，还需要付费找人托管你的内容。如果普通人觉得将信息输入一个巨大的企业数据存储库更容易，我们不应该感到惊讶。而在一个由巨大企业数据存储库组成的网络中，语义网技术就没有引人注目的用例了。

因此，语义网面临的问题比“XML 糟透了”更广泛、更深刻。尽管如此，很难相信语义网真的已经彻底消亡。W3C 在 2000 年代早期构想的一些特定技术可能没有未来，但蒂姆·伯纳斯-李和他的研究伙伴在《科学美国人》中描述的去中心化网络愿景太引人入胜，不会轻易消失。想象一下，在一个网络中，你无需每次注册服务时都填写相同的繁琐表格，而是能够以某种方式授权服务从你自己的网站获取信息。想象一下，一个脸书 ( Facebook ) 能够更新你自己的网站上托管的你的朋友列表，而不是反过来。基本上，语义网将是一个每个人都能拥有自己的个人 REST API 的网络，无论他们是否懂计算机。这样构想，很容易理解为什么语义网尚未实现。从现在到那时，还有太多的工程和安全问题需要解决。但也很容易理解为什么语义网的梦想吸引了如此多的人。

*如果你喜欢这篇文章，更多类似内容每四周发布一次！在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 订阅源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

[^1]: Berners\-Lee, Tim, James Hendler, and Ora Lassila. “The Semantic Web.” *Scientific American*, May 2001, [https://www\-sop.inria.fr/acacia/cours/essi2006/Scientific%20American\_%20Feature%20Article\_%20The%20Semantic%20Web\_%20May%202001\.pdf](https://www-sop.inria.fr/acacia/cours/essi2006/Scientific%20American_%20Feature%20Article_%20The%20Semantic%20Web_%20May%202001.pdf).
[^2]: Shannon, Victoria. “A ‘more Revolutionary’ Web.” The New York Times, May 23, 2006\. [https://www.nytimes.com/2006/05/23/technology/23iht\-web.html](https://www.nytimes.com/2006/05/23/technology/23iht-web.html).
[^3]: Doctorow, Cory. “Metacrap: Putting the Torch to Seven Straw\-men of the Meta\-utopia.” August 26, 2001\. Accessed May 26, 2018\. <https://people.well.com/user/doctorow/metacrap.htm>.
[^4]: Doctorow, Cory. “‘Metacrap’ and the History of the Semantic Web.” [E\-mail message](https://twobithistory.org/doctorow.txt) to author. May 11, 2018\.
[^5]: Munat, Ben. “The Lowercase Semantic Web: Using Semantics on the Existing World Wide Web.” May 2004\. Accessed May 26, 2018\. [http://citeseerx.ist.psu.edu/viewdoc/download?doi\=10\.1\.1\.85\.3445\&rep\=rep1\&type\=pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.85.3445&rep=rep1&type=pdf).
[^6]: Swartz, Aaron. A Programmable Web: An Unfinished Work. Morgan and Claypool, 2013\. March 12, 2013\. Accessed May 26, 2018\. <https://upload.wikimedia.org/wikipedia/commons/3/3f/Aaron_Swartz_s_A_Programmable_Web_An_Unfinished_Work.pdf>.
[^7]: Palmer, Sean B. “What Happened to the Semantic Web?” October 11, 2017\. SW\-forum Web. Accessed May 26, 2018\. [http://lists.w3\.org/Archives/Public/public\-lod/2017Oct/0003\.html](http://lists.w3.org/Archives/Public/public-lod/2017Oct/0003.html).
[^8]: Bray, Tim. “The RDF.net Challenge.” Ongoing by Tim Bray. May 21, 2003\. Accessed May 26, 2018\. <https://www.tbray.org/ongoing/When/200x/2003/05/21/RDFNet>.
[^9]: Bray, Tim, and Joshua Tauberer. “What Is RDF.” XML.com. July 26, 2006\. Accessed May 26, 2018\. <http://www.xml.com/pub/a/2001/01/24/rdf.html>.
[^10]: Berners\-Lee, Tim. “Linked Data.” W3C. June 18, 2009\. Accessed May 26, 2018\. [https://www.w3\.org/DesignIssues/LinkedData.html](https://www.w3.org/DesignIssues/LinkedData.html).
[^11]: Sporny, Manu. “The Origins of JSON\-LD.” The Beautiful, Tormented Machine. January 19, 2014\. Accessed May 26, 2018\. [http://manu.sporny.org/2014/json\-ld\-origins/](http://manu.sporny.org/2014/json-ld-origins/).
[^12]: “Data Model.” Schema.org. Accessed May 26, 2018\. <http://schema.org/docs/datamodel.html>.
[^13]: Raggett, Dave. “W3C Study of Practices and Tooling for Web Data Standardisation.” W3C. December 2017\. Accessed May 26, 2018\. [https://www.w3\.org/2017/12/odi\-study/](https://www.w3.org/2017/12/odi-study/).
[^14]: Rochkind, Jonathan. “Is the Semantic Web Still a Thing?” Bibliographic Wilderness. October 28, 2014\. Accessed May 26, 2018\. [https://bibwild.wordpress.com/2014/10/28/is\-the\-semantic\-web\-still\-a\-thing/](https://bibwild.wordpress.com/2014/10/28/is-the-semantic-web-still-a-thing/). Quoting Hacker News user “bane.” [https://news.ycombinator.com/item?id\=8510970](https://news.ycombinator.com/item?id=8510970).
[^15]: Sporny, Manu. “JSON\-LD and Why I Hate the Semantic Web.” The Beautiful, Tormented Machine. January 21, 2014\. Accessed May 26, 2018\. [http://manu.sporny.org/2014/json\-ld\-origins\-2/](http://manu.sporny.org/2014/json-ld-origins-2/).
[^16]: Palmer, Sean B.