# JSON 的崛起与持续繁荣

*2017 年 9 月 21 日*

JSON 已经席卷全球。如今，当两个应用程序在互联网上相互通信时，它们很可能都在使用 JSON。各大巨头都已采纳它：在十大最受欢迎的 Web API (应用程序编程接口) 中，这份榜单主要由 Google、Facebook 和 Twitter 等大公司提供的 API 组成，其中只有一个 API 采用 XML 而非 JSON 来公开数据。[^1] 以 Twitter 为例，它在 2013 年之前一直支持 XML，但随后发布了新版 API，彻底放弃了 XML，转而只使用 JSON。JSON 也被广大程序员广泛采用：根据程序员问答网站 Stack Overflow 的数据，现在关于 JSON 的提问比其他任何数据交换格式都多。[^2]

![](https://twobithistory.org/images/json.svg)

XML 在许多地方仍然存在。它在网络上用于 SVG (可缩放矢量图形) 以及 RSS 和 Atom 订阅源。当 Android 开发者需要声明他们的应用需要用户权限时，他们会在应用的清单文件 (manifest) 中进行声明，而这个文件就是用 XML 编写的。XML 也不是 JSON 的唯一替代品——现在有些人会使用 YAML 或 Google 的 Protocol Buffers (协议缓冲区) 等技术。但这些技术远不如 JSON 流行。目前来看，JSON 似乎是互联网上程序间通信的首选格式。

考虑到早在 2005 年，Web 世界还在对“异步 JavaScript 和 XML (Asynchronous JavaScript and XML)”的潜力垂涎三尺，而不是“异步 JavaScript 和 JSON (Asynchronous JavaScript and JSON)”，JSON 的主导地位着实令人惊讶。当然，这可能与当时两种格式的相对流行度无关，而仅仅是因为“AJAX”这个缩写听起来比“AJAJ”更吸引人。但即便在 2005 年已经有人开始使用 JSON 而非 XML (实际上当时用的人并不多)，人们仍然会好奇，XML 的命运怎么会如此急剧衰落，以至于仅仅十多年后，“异步 JavaScript 和 XML”就成了一个具有讽刺意味的错误名称。这十年间发生了什么？JSON 是如何在如此多的应用程序中取代 XML 的？又是谁发明了这种如今被全球工程师和系统所依赖的数据格式呢？

## JSON 的诞生

第一条 JSON 消息于 2001 年 4 月发出。由于这是计算领域一个具有历史意义的时刻，这条消息是从旧金山湾区一个车库里的电脑发出的。State Software (一家技术咨询公司) 的联合创始人 Douglas Crockford 和 Chip Morningstar 聚集在 Morningstar 的车库里，测试一个想法。

Crockford 和 Morningstar 早在“AJAX”这个术语被创造出来之前，就已经在尝试构建 AJAX 应用程序了。当时浏览器对他们所尝试的技术支持并不理想。他们希望在初始页面加载后将数据传递给他们的应用程序，但一直没有找到一种能兼容他们目标所有浏览器的方法。

尽管今天很难相信，但在 2001 年，Internet Explorer (IE 浏览器) 代表着网页浏览的前沿技术。早在 1999 年，Internet Explorer 5 就支持了一种原始形式的 XMLHttpRequest (异步 HTTP 请求)，程序员可以通过一个名为 ActiveX 的框架来访问它。Crockford 和 Morningstar 本可以使用这项技术为他们的应用程序获取数据，但他们无法在 Netscape 4 (他们也希望支持的另一个浏览器) 中使用相同的解决方案。因此，Crockford 和 Morningstar 必须使用一种在两种浏览器中都能工作的不同系统。

第一条 JSON 消息看起来是这样的：

```
<html><head><script>
    document.domain = 'fudco';
    parent.session.receive(
        { to: "session", do: "test",
          text: "Hello world" }
    )
</script></head></html>

```

这条消息中只有一小部分与我们今天所知的 JSON 相似。消息本身实际上是一个包含 JavaScript (脚本语言) 的 HTML (超文本标记语言) 文档。与 JSON 相似的部分只是一个 JavaScript 对象字面量，被传递给一个名为 `receive()` 的函数。

Crockford 和 Morningstar 决定，他们可以巧妙地利用 HTML 框架来向自己发送数据。他们可以将一个框架指向一个 URL (统一资源定位符)，该 URL 会返回一个如上所示的 HTML 文档。当 HTML 被接收后，JavaScript 就会运行，将对象字面量传回应用程序。只要你小心翼翼地避开浏览器阻止子窗口访问其父窗口的保护机制，这种方法就能奏效；你可以看到 Crockford 和 Morningstar 通过显式设置文档域来实现了这一点。(这种基于框架的技术，有时被称为隐藏框架技术，在 90 年代末 XMLHttpRequest 广泛实现之前曾被普遍使用。[^3])

关于第一条 JSON 消息，令人惊奇的是，它根本不像是一种新型数据格式的首次使用。它就是 JavaScript！事实上，以这种方式使用 JavaScript 的想法非常直接，以至于 Crockford 自己都说他不是第一个这样做的人——他声称 Netscape 的某个人早在 1996 年就使用 JavaScript 数组字面量来传递信息了。[^4] 由于消息就是 JavaScript，它不需要任何特殊的解析。JavaScript 解释器可以完成所有工作。

有史以来第一条 JSON 消息实际上与 JavaScript 解释器发生了冲突。JavaScript 保留了大量的词——截至 ECMAScript 6 (一种 JavaScript 标准)，有 64 个保留词——而 Crockford 和 Morningstar 在他们的消息中无意中使用了其中一个。他们使用了 `do` 作为键，但 `do` 是保留词。由于 JavaScript 有如此多的保留词，Crockford 决定，与其避免使用所有这些保留词，不如直接规定所有 JSON 键都必须加引号。加引号的键会被 JavaScript 解释器视为字符串，这意味着保留词可以安全使用。这就是为什么直到今天 JSON 键都带引号的原因。

Crockford 和 Morningstar 意识到他们拥有了一种可以在各种应用程序中使用的东西。他们想把他们的格式命名为“JSML”，即 JavaScript Markup Language (JavaScript 标记语言)，但发现这个缩写已经被用于一种名为 Java Speech Markup Language (Java 语音标记语言) 的东西了。所以他们决定采用“JavaScript Object Notation”，简称 JSON。他们开始向客户推销，但很快发现客户不愿意冒险尝试一种缺乏官方规范的未知技术。于是 Crockford 决定自己编写一个规范。

2002 年，Crockford 购买了 [JSON.org](http://JSON.org) 域名，并在上面发布了 JSON 语法和一个解析器 (parser) 的示例实现。该网站至今仍在运行，尽管现在它包含了一个指向 2013 年批准的 JSON ECMA 标准的显著链接。在网站上线后，Crockford 并没有做太多推广 JSON 的工作，但很快发现许多人提交了各种不同编程语言的 JSON 解析器实现。JSON 的血统显然与 JavaScript 紧密相连，但很快就显而易见，JSON 非常适合任意两种语言之间的数据交换。

## “错误地”使用 AJAX

JSON 在 2005 年获得了巨大的推动。那一年，一位名叫 Jesse James Garrett 的网页设计师兼开发者在一篇博客文章中创造了“AJAX”这个术语。他特意强调 AJAX 并非某一项新技术，而是“多种技术，各自蓬勃发展，以强大的新方式结合在一起”。[^5] AJAX 是 Garrett 为他注意到日益受到青睐的一种新的 Web 应用程序开发方法所起的名字。他的博客文章接着描述了开发者如何利用 JavaScript 和 XMLHttpRequest 来构建比传统网页更具响应性和状态感知能力的新型应用程序。他指出 Gmail 和 Flickr 就是已经依赖 AJAX 技术的网站示例。

当然，“AJAX”中的“X”代表的是 XML (可扩展标记语言)。但在随后的问答文章中，Garrett 指出 JSON 是 XML 完全可接受的替代品。他写道：“XML 是将数据进出 AJAX 客户端的最成熟方式，但你完全可以使用 JavaScript Object Notation (JavaScript 对象表示法) 或任何类似的数据结构化方式来实现相同的效果。”[^6]

开发者们确实发现他们可以轻松地使用 JSON 来构建 AJAX 应用程序，并且许多人开始更喜欢它而不是 XML。因此，具有讽刺意味的是，对 AJAX 的兴趣反而导致了 JSON 普及度的爆炸式增长。大约在这个时候，JSON 引起了博客圈的关注。

2006 年，Dave Winer (一位多产的博主，也是 RSS 和 XML-RPC 等多种基于 XML 技术背后的工程师) 抱怨说，JSON 毫无理由地重新发明了 XML。尽管人们可能会认为数据交换格式之间的竞争不太可能引发死亡威胁，但 Winer 写道：

> 毫无疑问，我可以编写一段程序来解析 [JSON]，但看看他们为了另起炉灶 (re-invent) 竟然做得如此彻底，连 XML (Extensible Markup Language) 都无法满足他们的要求，其中必有原因 ( 我很想知道原因 )。谁搞出了这种荒谬之举 (travesty)？真该把他们揪出来好好问问！现在就问！[^7]

不难理解 Winer 的沮丧。XML 从未受到广泛喜爱。甚至 Winer 自己也说过他不喜欢 XML。[^8] 但 XML 的设计初衷是一个可以被所有人用于几乎任何可想象用途的系统。为此，XML 实际上是一种元语言 (meta-language)，允许你为特定应用程序定义领域特定语言 (domain-specific languages)——RSS (一种网络订阅技术) 和 SOAP (简单对象访问协议) 就是例子。Winer 认为，达成共识很重要，因为一种通用的交换格式能带来诸多好处。他认为 XML 的灵活性应该能够满足所有人的需求。然而，JSON 却出现了，这种格式除了抛弃了让 XML 如此灵活的那些冗余部分所带来的好处之外，并没有比 XML 提供更多优势。

Crockford 看到了 Winer 的博客文章，并在上面留下了评论。针对 JSON 重新发明 XML 的指责，Crockford 写道：“重新发明轮子的好处是，你可以得到一个圆的。”[^9]

## JSON 对比 XML

到 2014 年，JSON 已通过 ECMA 标准和 RFC (请求评论) 两种方式获得官方规范。它拥有了自己的 MIME (多用途互联网邮件扩展) 类型。JSON 已经跻身主流。

为什么 JSON 会比 XML 流行这么多呢？

在 [JSON.org](http://JSON.org) 网站上，Crockford 总结了 JSON 相对于 XML 的一些优势。他写道，JSON 对人类和机器都更容易理解，因为它的语法极简，结构可预测。[^10] 其他博主则关注 XML 的冗长和“尖括号税”。[^11] XML 中的每个开始标签都必须与一个结束标签匹配，这意味着一个 XML 文档包含大量冗余信息。这可能导致 XML 文档在未压缩时比等效的 JSON 文档大得多，但更重要的是，它也使得 XML 文档更难阅读。

Crockford 还声称，JSON 的另一个巨大优势在于它被设计为一种数据交换格式。[^12] 从一开始，它就是为了在程序之间传输结构化信息而设计的。XML 尽管也被用于相同目的，但最初是作为一种文档标记语言 (document markup language) 设计的。它从 SGML (标准通用标记语言) 演变而来，而 SGML 又从一种名为 Scribe 的标记语言演变而来，Scribe 的设计初衷是作为一种类似于 LaTeX (一种排版系统) 的文字处理系统。在 XML 中，一个标签可以包含所谓的“混合内容 (mixed content)”，即带有内联标签 (inline tags) 包裹单词或短语的文本。这让人联想到编辑用红笔或蓝笔批注手稿的画面，这可以说是标记语言的核心隐喻。另一方面，JSON 不支持与混合内容明确对应的概念，但这同时也意味着它的结构可以更简单。文档最好建模为树状结构，但通过抛弃文档的概念，Crockford 可以将 JSON 限制为字典 (dictionaries) 和数组 (arrays)，这些是所有程序员用来构建程序的基本且熟悉的元素。

最后，我自己的直觉是，人们不喜欢 XML 是因为它令人困惑，而它令人困惑的原因在于它似乎有太多不同的“风味”或变体。乍一看，XML 本身与其子语言 (如 RSS、ATOM、SOAP 或 SVG) 之间的界限并不明显。一个典型的 XML 文档的开头几行会确定 XML 版本，然后是该 XML 文档应遵循的特定子语言。这已经需要考虑大量的变体了，特别是与 JSON 相比，JSON 如此直截了当，以至于人们预计永远不会编写新的 JSON 规范版本。XML 的设计者们，在试图让 XML 成为“一统天下”的数据交换格式时，却陷入了程序员经典的陷阱：过度工程化 (over-engineering)。XML 过于通用化，以至于用于简单的事情反而变得困难。

2000 年，一项旨在让 HTML 符合 XML 标准的运动启动了。随后发布了符合 XML 标准的 HTML 规范，此后被称为 XHTML (可扩展超文本标记语言)。一些浏览器厂商立即开始支持新标准，但很快就显而易见，广大的 HTML 内容生产者不愿改变他们的习惯。新标准要求对 XHTML 进行比 HTML 更严格的验证，但太多网站依赖于 HTML 宽松的规则。到 2009 年，当 HTML 的未来明确将是 HTML5 (一种不强制要求 XML 兼容性的标准) 时，编写 XHTML 标准第二版的尝试被中止了。

如果 XHTML 的努力成功了，那么 XML 也许会成为其设计者所期望的通用数据格式。想象一下，在一个 HTML 文档和 API 响应具有完全相同结构的世界里。在这样的世界里，JSON 可能就不会像今天这样无处不在了。但我将 XHTML 的失败解读为 XML 阵营的一种“道义上的失败”。如果 XML 不是 HTML 的最佳工具，那么也许对于其他应用程序来说，也有更好的工具存在。在那个世界，也就是我们所处的世界里，很容易理解像 JSON 这样简单且专门定制的格式为何能取得巨大成功。

*如果您喜欢这篇文章，更多类似内容每四周发布一次！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 订阅源](https://twobithistory.org/feed.xml)，确保您不会错过任何新文章。*

[^1]: [http://www.cs.tufts.edu/comp/150IDS/final\_papers/tstras01\.1/FinalReport/FinalReport.html\#software](http://www.cs.tufts.edu/comp/150IDS/final_papers/tstras01.1/FinalReport/FinalReport.html#software)
[^2]: [https://insights.stackoverflow.com/trends?tags\=json%2Cxml%2Cprotocol\-buffers%2Cyaml%2Ccsv](https://insights.stackoverflow.com/trends?tags=json%2Cxml%2Cprotocol-buffers%2Cyaml%2Ccsv)
[^3]: Zakas, Nicholas C., et al. “What Is Ajax?” Professional Ajax, 2nd ed., Wiley, 2007.
[^4]: [https://youtu.be/\-C\-JoyNuQJs?t\=32s](https://youtu.be/-C-JoyNuQJs?t=32s)
[^5]: [http://adaptivepath.org/ideas/ajax\-new\-approach\-web\-applications/](http://adaptivepath.org/ideas/ajax-new-approach-web-applications/)
[^6]: ibid.
[^7]: [http://scripting.com/2006/12/20\.html](http://scripting.com/2006/12/20.html)
[^8]: [http://blogoscoped.com/archive/2009\-03\-05\-n15\.html](http://blogoscoped.com/archive/2009-03-05-n15.html)
[^9]: [https://scripting.wordpress.com/2006/12/20/scripting\-news\-for\-12202006/\#comment\-26383](https://scripting.wordpress.com/2006/12/20/scripting-news-for-12202006/#comment-26383)
[^10]: <http://www.json.org/xml.html>
[^11]: [https://blog.codinghorror.com/xml\-the\-angle\-bracket\-tax](https://blog.codinghorror.com/xml-the-angle-bracket-tax)
[^12]: [https://youtu.be/\-C\-JoyNuQJs?t\=33m50sgg](https://youtu.be/-C-JoyNuQJs?t=33m50sgg)