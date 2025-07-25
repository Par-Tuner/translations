# 你从未听说过的最重要的数据库

*2017 年 10 月 7 日*

1962 年，肯尼迪 (JFK) 总统向美国人民发出挑战，要在十年内将人类送上月球。这激发了一项英勇的工程壮举，最终以尼尔·阿姆斯特朗 (Neil Armstrong) 首次踏上月球表面而告终。这项工程的许多成果都非常引人注目且令人兴奋——例如新型航天器、新式宇航服和月球车。但阿波罗计划 (Apollo Program) 极其复杂，以至于即使是处理日常事务，也需要发明新的技术。其中一项技术就是 IBM 的信息管理系统 (Information Management System, IMS)。

IMS 是一种数据库管理系统。美国国家航空航天局 (NASA) 需要一个系统来跟踪建造土星五号 (Saturn V) 火箭所需的所有零件，由于零件数量高达两百万个，这无疑是一项巨大的挑战。数据库在 20 世纪 60 年代还是一个新概念，当时 NASA 并没有现成的系统可用。因此，在 1965 年，NASA 请求 IBM 与北美航空 (North American Aviation) 和卡特彼勒拖拉机公司 (Caterpillar Tractor) 合作开发一个。到了 1968 年，IBM 已经在 NASA 安装了一个可运行的 IMS 版本，尽管当时它被称为 ICS/DL/I，意为“信息控制系统和数据语言/接口” (Informational Control System and Data Language/Interface)。 (IBM 似乎曾短暂地、不幸地迷恋过斜杠符号；参见 PL/I)。两年后，IBM 将 ICS/DL/I 更名为“IMS”，并开始向其他客户销售。它是首批商用数据库管理系统之一。

IMS 令人难以置信之处在于，它至今仍在被使用。而且并非小规模使用：银行、保险公司、医院和政府机构仍然使用 IMS 来处理各种关键任务。超过 95% 的财富 1000 强 (Fortune 1000) 公司都在某种程度上使用 IMS，美国前五大银行也无一例外 [^1]。每当你从自动取款机 (ATM) 取款时，你的交易过程中极有可能在某个环节与 IMS 发生交互。在一个关系型数据库 (relational database) 已经成为老牌主力，并日益与时髦的新型 NoSQL 数据库 (NoSQL databases) 竞争的世界里，IMS 简直就是个活化石。它是一个关系型数据库尚未发明之前的时代的遗物，关系型数据库直到 1970 年才出现。然而，它似乎正是负责所有重要事务的数据库系统。

我认为这使得 IMS 相当有趣。取决于你对关系型数据库的看法，它要么能让你深入了解关系模型 (relational model) 如何在其前辈的基础上进行改进，要么就展示了一种更适合特定问题的替代模型。

IMS 采用的是一种层次模型 (hierarchical model)，这意味着 IMS 不像关系型数据库那样将数据视为可以通过 JOIN 操作 (JOIN operations) 连接起来的表格，而是将数据视为树状结构。你存储的每种记录都可以有其他类型的记录作为子记录；这些子记录类型代表了在给定父记录类型的情况下，你可能感兴趣的额外信息。

举个例子，假设你想存储银行客户的信息。你可能有一种记录类型来表示客户，另一种记录类型来表示账户。就像关系型数据库中每个表都有列一样，这些记录也会有不同的字段；我们可能希望为每个客户设置姓名字段、名字字段和城市字段。然后我们必须决定，是更有可能先查找客户，再查找该客户的账户信息，还是更有可能先查找账户，再查找该账户所有者的信息。假设我们决定先访问客户，那么我们就会将账户记录类型设为客户记录类型的子级。绘制成图，我们的数据库模型将大致如下所示 [^2]：

![](https://twobithistory.org/images/hierarchical-model.png)

而一个实际的数据库可能看起来像这样：

![](https://twobithistory.org/images/hierarchical-db.png)

通过这种方式建模数据，我们与数据实际存储的方式非常接近。每个父记录都包含指向其子记录的指针，这意味着从树的根节点向下遍历是高效的。(实际上，每个父记录基本上只存储一个指向其第一个子记录的指针。子记录反过来包含指向其兄弟记录的指针。这确保了记录的大小不会随其子记录的数量而变化。) 这种效率可以使数据访问非常快速，前提是我们以在最初构建数据库时所预期的方式访问数据。根据 IBM 的说法，一个 IMS 实例每秒可以处理超过 10 万笔事务，这可能就是 IMS 至今仍被广泛使用，尤其是在银行领域的重要原因 [^3]。但缺点是，我们失去了很大的灵活性。如果我们想以未曾预期的方式访问数据，就会遇到困难。

为了说明这一点，设想一下如果我们决定在查找客户之前先访问账户会发生什么。也许客户打电话来更新地址，我们希望他们使用自己的账户号码来唯一标识自己。因此，我们想使用账户号码来查找账户，然后从那里找到账户的所有者。但由于所有访问都从树的根节点开始，如果没有先确定一个客户，我们就无法高效地找到一个账户。为了解决这个问题，我们可以引入第二个以账户记录开始的树或层次结构；这些账户记录将把客户记录作为子级。这将使我们能够高效地访问账户，然后再访问客户。但这将涉及重复存储数据库中已有的信息——我们将有两棵树以不同的顺序存储相同的信息。另一种选择是建立一个账户索引 (index)，给定一个账户号码，它可以指向正确的账户记录。这也行得通，但未来在插入 (insert) 和更新 (update) 操作时会增加额外的工作量。

正是这种不灵活性和信息重复的问题，促使 E. F. Codd 提出了关系模型。在他 1970 年的论文《大型共享数据库的数据关系模型》 (*A Relational Model of Data for Large Shared Data Banks*) 中，他开篇就指出，他旨在提出一种数据存储模型，能够让用户无需了解数据是如何存储的。从某种角度看，层次模型完全是 IMS 设计者选择数据存储方式的产物。它是一个 *自下而上* (bottom-up) 的模型，是物理现实的体现。另一方面，关系模型是一个基于关系代数 (relational algebra) 的抽象模型，它是 *自上而下* (top-down) 的，只要数据存储方案能够适应这个模型，它就可以是任何形式。关系模型的巨大优势在于，即使你做出了导致数据库以特定方式存储数据的决策，你也不会发现自己实际上无法执行某些查询 (queries)。

尽管如此，关系模型毕竟是一种抽象，而我们都知道抽象并非没有代价。银行和大型机构之所以坚持使用 IMS，部分原因是其性能优势，尽管很难说如果他们不是为了避免重写关键的遗留代码 (legacy code)，这些优势是否足以阻止他们转向现代数据库。然而，当今流行的 NoSQL 数据库表明，有人愿意为了更好的性能而放弃关系模型的便利性。像 MongoDB 这样的数据库，鼓励用户以非规范化 (denormalized) 的形式存储数据，这与 IMS 并没有太大区别。如果你选择将某个实体存储在另一个 JSON 记录 (JSON record) 中，那么实际上你就创建了类似于 IMS 层次结构的东西，并且限制了你未来查询该数据的能力。但也许这是你愿意做出的权衡。因此，即使 IMS 没有比 E. F. Codd 的关系模型早出现几年，IMS 的创建者仍然有理由不完全采用关系模型。

不幸的是，IMS 并不是你可以下载并在自己电脑上试用的东西。首先，IMS 并非免费，你需要从 IBM 购买。但更大的问题是，IMS 只能在 IBM 大型机 (mainframe) 上运行，比如 IBM z13。这很可惜，因为如果能亲自体验 IMS，了解它与 MySQL 等数据库究竟有何不同，那将是一件乐事。但即使没有这个机会，思考那些以我们不熟悉或意想不到的方式运行的软件系统，也很有趣。当这些看似陌生的系统，竟然支撑着你当地的医院、整个金融业乃至联邦政府时，那就尤其引人入胜了。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

[^1]: [https://youtu.be/DhlpnSbSuJE?t=3m13s](https://youtu.be/DhlpnSbSuJE?t=3m13s)
[^2]: Klein, Barbara. *An Introduction to IMS: Your Complete Guide to IBM Information Management System.* IBM Press, 2012.
[^3]: [https://www.slideshare.net/roberthain/ims05-ims-100-k-benchmark](https://www.slideshare.net/roberthain/ims05-ims-100-k-benchmark)