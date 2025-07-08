# 朋友的朋友：本可能存在的 Facebook

*2020 年 1 月 5 日*

> *我用 FOAF 文件表达我的网络，这就是革命的开始。*
> —Tim Berners-Lee (2007)

FOAF 标准 (Friend of a Friend standard) 是一个如今基本已废弃、被忽视或被取代[^1]的网络标准，它起源于 21 世纪初，让我们得以一窥，如果 Facebook 没有称霸全球，社交网络本可能呈现出怎样的面貌。不过，在我们深入探讨 FOAF 之前，我想先聊聊纽约市地铁。

纽约市地铁由一个单一实体控制，那就是大都会运输署 (Metropolitan Transportation Agency)，简称 MTA。MTA 在纽约市的地铁出行方面拥有垄断地位。在纽约市，不购买 MTA 的车票，就无法合法乘坐地铁。MTA 没有竞争对手，至少在“地铁领域”是这样。

但情况并非总是如此。令人惊讶的是，地铁系统曾一度由两家相互竞争的公司运营。城际快速运输公司 (Inter-borough Rapid Transit Company)，简称 IRT，运营的线路主要穿过曼哈顿；而布鲁克林-曼哈顿运输公司 (Brooklyn-Manhattan Transit Corporation)，简称 BMT，则在布鲁克林运营线路，其中一些也延伸到曼哈顿。1932 年，市政府开通了自己的服务，名为独立地铁系统 (Independent Subway System)，与 IRT 和 BMT 竞争。因此，有一段时间，纽约市有 *三* 家不同的机构运营地铁线路。

不难想象，这不是一种高效的地铁运营方式。事实也确实如此。在各个系统之间修建换乘站极具挑战性，因为 IRT 和 BMT 使用的列车宽度不同。换乘站还必须至少有两个不同的票务区，因为换乘的乘客需要向多个运营商付费。市政府最终于 1940 年接管了 IRT 和 BMT，将整个系统整合到一个运营商之下。然而，最初划分带来的一些低效率问题至今仍然存在：设计用于沿 BMT 继承线路（例如 A、C 或 E 线）运行的列车，无法沿 IRT 继承线路（例如 1、2 或 3 线）运行，因为 IRT 隧道太窄。结果，MTA 必须维护两支不同且相互不兼容的地铁车辆车队，这相对于世界上其他只需处理单一隧道宽度的地铁系统来说，无疑会带来显著的额外开支。

IRT 和 BMT 之间竞争留下的遗产表明，地铁系统自然倾向于垄断 (natural monopoly)。由单一运营商运营，比由相互竞争的运营商运营更有意义。普通乘客因选择权的丧失而得到了充分补偿，因为他们再也不必担心今天是否带了 IRT 地铁卡，却把 BMT 地铁卡忘在了家里。

那么，地铁和社交网络 (social networking) 到底有什么关系呢？嗯，我一直在思考，Facebook 是否像 MTA 一样，拥有天然垄断。Facebook 似乎确实拥有 *某种* 垄断，无论是天然的还是非天然的——它垄断的不是社交媒体本身（我在 Twitter 上花的时间更多），而是我与我认识的真实人物之间的互联网社交连接。它垄断了，正如他们所说的，我的数字化“社交图谱 (social graph)”；如果我不担心这样做会失去许多这些连接，我明天就会退出 Facebook。我对 Facebook 对我拥有的这种权力感到愤怒。这种愤怒不同于我对 MTA 的愤怒，尽管纽约地铁，无论是比喻还是字面意义上，都是一堆烂摊子。我想我之所以愤怒，是因为我从根本上相信 Facebook 的垄断，不像 MTA 的垄断，并非天然。

这必然意味着，我认为 Facebook 现在拥有我们所有的社交数据，是因为他们碰巧抢占了先机，然后在自己周围挖了一条大护城河，而不是因为一个存在相互竞争的 Facebook 类似平台的世界是低效或不可能的。然而，这真的如此吗？有一些很好的理由认为并非如此：Facebook 是仅仅抢占了先机，还是他们只是比其他人做得更好？如果你想联系一位老朋友，只有一个 Facebook 的事实难道不方便吗？在一个存在相互竞争的 Facebook 的世界里，如果你和你的男朋友现在在 Facebook 上正式公开关系，但他还没有在 VisageBook 上更新他的关系状态，那里仍然显示他与他的大学前女友处于恋爱关系，那会意味着什么？人们会信任哪个网站？此外，如果存在多个网站，每个人难道不会花更多时间填写网页表单吗？

在过去的几年里，随着中心化社交网络 (centralized social networks) 的缺点日益明显，许多人试图创建去中心化替代方案 (decentralized alternatives)。这些替代方案基于开放标准 (open standards)，可能支持一个互操作的社交网络生态系统（例如参见 Fediverse）。但这些替代方案都没有取代任何一个主导性的社交网络。一个显而易见的解释是网络效应 (network effects) 的力量：由于每个人都已经在使用 Facebook，任何一个考虑离开的人都面临着高昂的成本。有些人可能会说这证明了社交网络是天然垄断，并就此打住；我会说 Facebook、Twitter 等选择了成为围墙花园 (walled gardens)，鉴于人们已经设想甚至构建了可以互操作的社交网络，封闭平台所享有的网络效应并不能说明社交网络的内在性质。

所以在我看来，真正的问题是：像 Facebook 这样的平台继续主导仅仅是因为它们的网络效应，还是拥有一个单一的主导社交网络，就像地铁系统拥有单一运营商一样，效率更高？

这最终让我回到了 FOAF。世界上大部分人似乎都忘记了 FOAF 标准，但 FOAF 是在人们甚至听说 Facebook 之前，就试图构建一个去中心化和开放社交网络的一次尝试。如果任何去中心化社交网络在 Facebook 出现之前有机会占据 Facebook 现在所占据的阵地，那一定是 FOAF。鉴于现在很大一部分人类拥有 Facebook 账户，并且相对较少的人知道 FOAF，我们是否应该得出结论，社交网络，就像地铁出行一样，确实倾向于中心化和天然垄断？或者 FOAF 项目是否表明去中心化社交网络是一个可行的替代方案，但由于其他原因从未流行起来？

## 21 世纪初的未来

FOAF 项目始于 2000 年，旨在创建一个描述人及其之间关系的通用标准。这在今天看来可能是一个极其雄心勃勃的目标，但在 1990 年代末和 21 世纪初，这样的抱负是司空见惯的。万维网（当时人们仍然这样称呼它）刚刚击败了像 America Online 和 Prodigy 这样的封闭系统。因此，很自然地会认为计算领域的进一步创新将涉及万维网所体现的开放的、基于标准的方法。

许多人相信，下一个重大突破是万维网将演变为所谓的语义网 (Semantic Web)。我之前已经撰文介绍过语义网究竟是什么以及它是如何运作的，所以这里不再赘述。但我将概述推动语义网技术工作者的基本愿景，因为 FOAF 标准正是该愿景在社交网络中的一个应用。

有一篇名为《Google 如何在语义网竞赛中击败亚马逊和 eBay》的文章，它很好地捕捉了语义网的宏伟愿景。这篇文章由 Paul Ford 于 2002 年撰写。文章设想了一个未来（近在 2009 年），其中 Google 通过拥抱语义网，取代了 Amazon 和 eBay 成为主导的电子商务 (e-commerce) 平台。在这个未来中，你可以通过在 Google 中输入 `buy:martin guitar` 来搜索你想购买的东西——也许是一把二手 Martin 吉他。Google 随后会向你展示你邮政编码附近所有出售 Martin 吉他的人。Google 了解这些人及其吉他，因为 Google 可以读取 RDF (Resource Description Framework)，这是一种专注于表达关系的标记语言 (markup language)，也是核心的语义网技术。普通人可以在他们的网页上嵌入 RDF 来宣传（以及许多其他东西）他们要出售的物品。Ford 预测，随着以这种方式搜索和宣传产品的人数增长，Amazon 和 eBay 将分别失去它们在一手和二手电子商务领域的近乎垄断地位。当人们可以搜索整个万维网时，没有人会想在一个单一的中心化数据库中搜索要购买的东西。Ford 写道，即使是 Google，最终也会失去其优势，因为理论上任何人都可以抓取读取 RDF 的万维网，并提供类似于 Google 的搜索功能。至少，如果 Google 想通过对每笔交易收取一定比例的费用来从其语义网市场中赚钱，那么随着时间的推移，这个比例可能会被提供更具吸引力交易的竞争对手压低。

Ford 设想的未来是 RDF（即资源描述框架）在电子商务中的应用，但 RDF 令人兴奋之处在于，理论上它可以用于任何事物。RDF 标准，连同其一系列相关标准，一旦被广泛采用，本应像 HTML 彻底改变互联网上的文档发布一样，彻底改变互联网上基于数据库的软件服务。

RDF 和其他语义网技术似乎即将立即接管的一个领域是社交网络。FOAF 项目，最初被称为“RDF Web Ring”，后来更名，是语义网努力的一个分支，旨在实现这一目标。FOAF 在其初期是如此有前景，以至于有些人认为它将不可避免地使所有其他社交网站过时。2004 年《卫报》一篇关于该项目的文章这样介绍了 FOAF：

> 最初，早在 1996 年，是 SixDegrees。去年是 Friendster。上周是 Orkut。下周可能是 Flickr。所有这些网站，以及几十个其他网站，都旨在建立朋友网络，它们目前处于最时髦的互联网发展前沿：社交网络。但除非它们能开始提供更实质的好处，否则一旦 Friend Of A Friend (FOAF) 标准成为网络生活的常态，很难看到它们都能存活下来。[^2]

文章接着抱怨说，社交网络最大的问题是社交网站太多了。需要某种东西能够将所有不同的网络连接起来。FOAF 就是解决方案，它将因此彻底改变社交网络。

根据文章，FOAF 将通过做三件关键事情来将不同的网络连接起来：

*   它将为社交数据建立一种机器可读格式 (machine-readable format)，任何社交网站都可以读取，从而省去用户反复输入这些信息的麻烦
*   它将允许“个人信息管理程序”，即你的“联系人”应用程序，生成一个这种机器可读格式的文件，你可以将其提供给社交网站
*   它将进一步允许这种机器可读格式托管在个人主页上，并由社交网站远程读取，这意味着你只需将更改推送到自己的主页，就能保持各种个人资料的最新状态

今天很难相信，但在 2004 年，至少对于那些了解所有最新网站的精明网民和科技专栏作家来说，问题不是缺乏替代社交网络，而是它们的泛滥。鉴于 *那个* 问题——现在对我们来说如此陌生——人们可以理解为什么追求一个单一标准是有意义的，它承诺会减轻网络泛滥带来的负担。

## FOAF 规范

根据 FOAF 项目网站上目前的描述，FOAF 是一种“定义了可在结构化数据 (structured data) 中使用的与人相关的术语词典的计算机语言”。早在 2000 年，FOAF 的创建者 Dan Brickley 和 Libby Miller 在一份解释项目目标的文档中，提供了另一种描述，更能揭示该技术的最终目的——他们将 FOAF 介绍为一种工具，它将允许计算机像其他人一样读取你放在主页上的个人信息。[^3] FOAF 将“帮助万维网做那些目前是中心化服务专有提供的事情。”[^4] 通过定义一个描述人及其之间关系的标准化词汇表，FOAF 将允许你向万维网提出问题，例如“查找今天由为医疗机构工作的人提出的网络推荐”，或者“查找我曾共同撰写文档的人的最新出版物”。

由于 FOAF 是一个标准化词汇表，FOAF 项目最重要的产出就是 FOAF 规范。FOAF 规范定义了一小部分 RDF *类 (classes)* 和 RDF *属性 (properties)*。（我这里不解释 RDF，但如果你想了解更多，请再次参阅我关于语义网的帖子。）FOAF 规范定义的 RDF *类* 代表你可能想要描述的主题，例如人（`Person` 类）和组织（`Organization` 类）。FOAF 规范定义的 RDF *属性* 代表你可能对不同主题做出的逻辑陈述。例如，一个人可以有名字（`givenName` 属性）、姓氏（`familyName` 属性），甚至可能有人格类型（`myersBriggs` 属性），并且靠近另一个人或地点（`based_near` 属性）。其想法是，这些类和属性足以表示人们在个人主页上描述自己和朋友的事物。

FOAF 规范给出了以下一个格式良好的 FOAF 文档示例。此示例使用 XML (Extensible Markup Language)，但可以使用 JSON (JavaScript Object Notation) 或其他多种格式编写等效文档：

```
<foaf:Person rdf:about="#danbri" xmlns:foaf="http://xmlns.com/foaf/0.1/">
  <foaf:name>Dan Brickley</foaf:name>
  <foaf:homepage rdf:resource="http://danbri.org/" />
  <foaf:openid rdf:resource="http://danbri.org/" />
  <foaf:img rdf:resource="/images/me.jpg" />
</foaf:Person>

```

这个 FOAF 文档描述了一个名为“Dan Brickley”（该规范的作者之一）的人，他有一个主页在 `http://danbri.org`，一个名为“开放 ID”的东西，以及一张图片可在 `/images/me.jpg` 找到，这大概是相对于 Brickley 主页的基本地址而言的。FOAF 特定的术语以 `foaf:` 为前缀，表明它们是 FOAF 命名空间 (namespace) 的一部分，而更通用的 RDF 术语则以 `rdf:` 为前缀。

为了让你相信 FOAF 不仅限于 XML，这里有一个来自维基百科的类似 FOAF 示例，使用名为 JSON-LD (JSON for Linked Data) 的格式表示[^5]：

```
{
  "@context": {
    "name": "http://xmlns.com/foaf/0.1/name",
    "homepage": {
      "@id": "http://xmlns.com/foaf/0.1/workplaceHomepage",
      "@type": "@id"
    },
    "Person": "http://xmlns.com/foaf/0.1/Person"
  },
  "@id": "https://me.example.com",
  "@type": "Person",
  "name": "John Smith",
  "homepage": "https://www.example.com/"
}

```

这个 FOAF 文档描述了一个名为 John Smith 的人，其主页在 `www.example.com`。

也许了解 FOAF 如何运作的最佳方式是使用 FOAF-a-matic，这是一个用于生成 FOAF 文档的网页工具。它允许你使用网页表单输入关于你自己的信息，然后使用这些信息创建代表你的 FOAF 文档（XML 格式）。FOAF-a-matic 展示了 FOAF 如何能够让每个人免于再次将他们的社交信息输入到网页表单中——如果每个社交网站都能读取 FOAF，你只需将网站指向 FOAF-a-matic 为你生成的 FOAF 文档即可注册新网站。

这是一个稍微复杂一点的 FOAF 示例，代表我，是我使用 FOAF-a-matic 创建的：

```
<rdf:RDF
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      xmlns:foaf="http://xmlns.com/foaf/0.1/"
      xmlns:admin="http://webns.net/mvcb/">
  <foaf:PersonalProfileDocument rdf:about="">
    <foaf:maker rdf:resource="#me"/>
    <foaf:primaryTopic rdf:resource="#me"/>
    <admin:generatorAgent rdf:resource="http://www.ldodds.com/foaf/foaf-a-matic"/>
    <admin:errorReportsTo rdf:resource="mailto:leigh@ldodds.com"/>
  </foaf:PersonalProfileDocument>
  <foaf:Person rdf:ID="me">
    <foaf:name>Sinclair Target</foaf:name>
    <foaf:givenname>Sinclair</foaf:givenname>
    <foaf:family_name>Target</foaf:family_name>
    <foaf:mbox rdf:resource="mailto:sinclairtarget@example.com"/>
    <foaf:homepage rdf:resource="sinclairtarget.com"/>
    <foaf:knows>
      <foaf:Person>
        <foaf:name>John Smith</foaf:name>
        <foaf:mbox rdf:resource="mailto:johnsmith@example.com"/>
        <rdfs:seeAlso rdf:resource="www.example.com/foaf.rdf"/>
      </foaf:Person>
    </foaf:knows>
  </foaf:Person>
</rdf:RDF>

```

这个示例有相当多的前导部分，用于设置文档使用的各种 XML 命名空间。还有一个部分包含关于用于生成文档的工具的数据，这主要是为了让人们知道向谁发送投诉邮件。描述我的 `foaf:Person` 元素告诉你我的姓名、电子邮件地址和主页。还有一个嵌套的 `foaf:knows` 元素，告诉你我与 John Smith 是朋友。

这个示例说明了 FOAF 文档的另一个重要特性：它们可以相互链接。如果你还记得上一个示例，我的朋友 John Smith 的主页在 `www.example.com`。在这个示例中，我将 John Smith 列为与我具有 `foaf:knows` 关系的 `foaf:person`，我还提供了一个 `rdfs:seeAlso` 元素，指向托管在他主页上的 John Smith 的 FOAF 文档。因为我提供了这个链接，任何读取我的 FOAF 文档的程序都可以通过跟随链接并读取他的 FOAF 文档来了解更多关于 John Smith 的信息。在我们上面为 John Smith 提供的 FOAF 文档中，John 没有提供任何关于他朋友的信息（包括我，这意味着，悲剧的是，我们的友谊是单向的）。但如果他提供了，那么读取我的文档的程序不仅可以了解我，还可以了解 John、他的朋友、他们的朋友，等等，直到程序爬取了我和 John 所处的整个社交图谱。

这个功能对于任何使用过 Facebook 的人来说都会很熟悉，也就是说，这个功能对你来说也会很熟悉。没有 `foaf:wall` 属性或 `foaf:poke` 属性来完全复制 Facebook 的功能集。显然，也没有一个光滑的蓝色用户界面供所有人使用来可视化他们的 FOAF 社交网络；FOAF 只是一个词汇表。但 Facebook 的核心功能——我曾论证这是 Facebook 对我（至少是我自己）的垄断权力的关键功能——在这里以分布式方式 (distributed way) 提供。FOAF 允许一群朋友通过在自己的主页上托管 FOAF 文档，以数字方式表示他们的现实社交图谱。它允许他们这样做，而无需将数据控制权交给一个由亿万富翁机器人男运营的、位于云端的中心化数据库，这个机器人男大部分时间都在国会委员会前道歉。

## FOAF 冰封记

如果你访问当前的 FOAF 项目主页，你会注意到，在右上角，有一张来自电视剧《飞出个未来》中角色 Fry 的图片，他被困在某种休眠舱内。这是《飞出个未来》试播集中的一个静止画面，其中 Fry 在 1999 年被冻结在一个低温冷冻舱 (cryogenic tank) 中，一千年后，即 2999 年才醒来。我曾在 Twitter 上简短地给 Brickley 发过消息，他告诉我他把那张图片放在那里，是为了传达 FOAF 项目目前“处于休眠状态”，尽管他希望未来有机会复兴该项目，以及其 21 世纪初对万维网应如何运作的乐观态度。

FOAF 从未像 2004 年《卫报》文章所预期的那样彻底改变社交网络。一些社交网站决定支持该标准：LiveJournal 和 MyOpera 就是例子。[^6] FOAF 甚至在 Howard Dean 2004 年的总统竞选中发挥了作用——一群博主和程序员聚集在一起，创建了一个他们称之为“DeanSpace”的网站网络来宣传竞选活动，这些网站使用 FOAF 来跟踪支持者和志愿者。[^7] 但今天，FOAF 主要以作为 RDF 更广泛使用的词汇表之一而闻名，而 RDF 本身在现代网络上是一个小众标准。如果 FOAF 今天是你的网络体验的一部分，那么它是为 Google 的“知识面板 (knowledge panels)”（如果你搜索简单内容时，告诉你关于一个人或一件事基本信息的小侧边栏）提供动力的技术的祖先。Google 使用 schema.org 项目发布的词汇表——语义网努力的现代继承者——来填充其知识面板。[^8] schema.org 描述人的词汇表似乎在某种程度上受到了 FOAF 的启发，并服务于许多相同的目的。

那么 FOAF 为什么没有成功呢？为什么我们现在都使用 Facebook 呢？我们暂且不提 FOAF 是一个功能远不如 Facebook 简单的标准——这在今天显然是事实，但如果 FOAF 获得了更多发展势头，那么在其之上构建应用程序以提供类似 Facebook 的体验是可能的。有趣的问题是：当 Facebook 尚未出现与之竞争时，这种萌芽形式的分布式社交网络为何没有流行起来？

这个问题可能没有单一的答案，但如果我必须选择一个，我认为最大的问题是 FOAF 只有在每个人都有个人网站的万维网上才有意义。在 1990 年代末和 21 世纪初，很容易假设万维网最终会是这样，特别是考虑到据我所知，许多万维网的早期采用者都是多产的博主或积极参与政治的技术人员，他们很高兴拥有一个平台。但现实是，普通人不想学习如何托管网站。FOAF 允许你控制自己的社交信息并将其广播到社交网络，而不是填写无休止的网页表单，如果你已经有地方托管这些信息，这听起来很棒。但大多数人实际上发现，填写网页表单并注册 Facebook 比弄清楚如何购买域名并托管一些 XML 更容易。

这对我的原始问题——Facebook 的垄断是否是天然的——意味着什么？我想我不得不承认，FOAF 的例子证明社交网络 *确实* 自然倾向于垄断。

人们不想托管自己的数据本身并没有特别的意义——现代分布式社交网络，如 Mastodon，已经通过让普通用户将他们的个人资料托管在由更精明的用户设置的节点上来解决了这个问题。然而，这表明人们是多么讨厌复杂性。这对去中心化社交网络来说是个坏消息，因为它们在底层本质上比中心化网络更复杂，而且这种复杂性往往无法对用户隐藏。

考虑 FOAF：如果我编写一个从个人网站读取 FOAF 数据的应用程序，如果 Sally 的 FOAF 文档提到一个主页在 `example.com` 的 John Smith，而 Sue 的 FOAF 文档提到一个主页在 `example.net` 的 John Smith，我该怎么办？我们是在谈论一个拥有两个网站的 John Smith，还是两个完全不同的 John Smith？如果两个 FOAF 文档都将 John Smith 的电子邮件列为 `johnsmith@gmail.com` 呢？这个身份问题对 FOAF 来说是一个尖锐的问题。在 2003 年的一封电子邮件中，Brickley 写道，因为不存在也可能不应该存在一个“全球范围的人员识别系统”，所以 FOAF 采取的方法是“多元化的”。[^9] FOAF 人员的一些属性，例如电子邮件地址和主页地址，是特殊的，因为它们的值是全球唯一的。因此，这些不同的属性可以用来合并（或者，正如 Libby Miller 所说的，“smoosh”）关于人的 FOAF 文档。但这些特殊属性都没有凌驾于其他属性之上，所以如何处理我们的 John Smith 案例并不明显。我们是相信主页并得出结论我们有两个不同的人？还是相信电子邮件地址并得出结论我们是一个人？我真的能编写一个应用程序，在不涉及（和不方便）用户的情况下解决这个冲突吗？

Facebook 凭借其单一数据库和缺乏政治顾虑，可以创建一个“全球范围的人员识别系统”，从而为每个人分配一个唯一的 Facebook ID。问题解决了。

如果人们关心能够拥有和控制自己的数据，那么仅仅复杂性可能不会注定分布式社交网络的失败。但 FOAF 的未能流行起来表明，人们从未高度重视控制权。正如一位博主所说：“‘用户想要拥有自己的数据’是一种意识形态，而不是一个用例。”[^10] 如果用户不重视控制权到足以忍受额外的复杂性，而且如果中心化系统比分布式系统更简单——而且，如果中心化系统倾向于封闭，从而成功的系统享有强大的网络效应——那么社交网络确实是天然垄断。

话虽如此，我认为地铁系统案例和社交网络案例之间仍然存在区别。我对 MTA 在地铁出行方面的垄断感到满意，因为我预计地铁系统在很长一段时间内都将是天然垄断。如果纽约市地铁只有一个运营商，那么它应该是政府，政府至少在名义上比没有竞争对手的私营公司更负责。但我并不期望社交网络保持天然垄断。地铁是刻在花岗岩上的；数字世界则如水般易逝。分布式社交网络现在可能比中心化网络更复杂，就像携带两张地铁卡比携带一张更复杂一样。然而，在未来，万维网，甚至互联网，可能会发生根本性的变化，使分布式技术更容易使用。

如果发生这种情况，也许 FOAF 将被铭记为人类在短暂尝试了企业巨型数据库之后，现在和将来都将偏爱的那种社交网络的首次尝试。

*如果你喜欢这篇文章，每四周会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS feed](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> I know it's been too long since my last post, but my new one is here! I wrote almost 5000 words on John Carmack, Doom, and the history of the binary space partitioning tree.<https://t.co/SVunDZ0hZ1>
>
> — TwoBitHistory (@TwoBitHistory) [November 6, 2019](https://twitter.com/TwoBitHistory/status/1192196764239093760?ref_src=twsrc%5Etfw)

[^1]: 请注意，我不敢说“已死”。
[^2]: Jack Schofield，“让我们成为 Friendsters”，《卫报》，2004 年 2 月 19 日，2020 年 1 月 5 日访问，<https://www.theguardian.com/technology/2004/feb/19/newmedia.media>。
[^3]: Dan Brickley 和 Libby Miller，“介绍 FOAF”，FOAF 项目，2008 年，2020 年 1 月 5 日访问，[https://web.archive.org/web/20140331104046/http://www.foaf-project.org/original-intro](https://web.archive.org/web/20140331104046/http://www.foaf-project.org/original-intro)。
[^4]: 同上。
[^5]: 维基百科贡献者，“JSON-LD”，维基百科：自由的百科全书，2019 年 12 月 13 日，2020 年 1 月 5 日访问，[https://en.wikipedia.org/wiki/JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)。
[^6]: “数据源”，FOAF 项目维基，2009 年 12 月 11 日，2020 年 1 月 5 日访问，[https://web.archive.org/web/20100226072731/http://wiki.foaf-project.org/w/DataSources](https://web.archive.org/web/20100226072731/http://wiki.foaf-project.org/w/DataSources)。
[^7]: Aldon Hynes，“什么是 Dean Space？”，Extreme Democracy，2020 年 1 月 5 日访问，[http://www.extremedemocracy.com/chapters/Chapter18-Hynes.pdf](http://www.extremedemocracy.com/chapters/Chapter18-Hynes.pdf)。
[^8]: “了解结构化数据如何工作”，Google 开发者门户，2020 年 1 月 5 日访问，[https://developers.google.com/search/docs/guides/intro-structured-data](https://developers.google.com/search/docs/guides/intro-structured-data)。
[^9]: tef，“为什么你的分布式网络不会成功”，Progamming is Terrible，2013 年 1 月 2 日，[https://programmingisterrible.com/post/39438834308/distributed-social-network](https://programmingisterrible.com/post/39438834308/distributed-social-network)。
[^10]: Dan Brickley，“在 FOAF 中识别事物”，rdfweb-dev 邮件列表，2003 年 7 月 10 日，2020 年 1 月 5 日访问，[http://lists.foaf-project.org/pipermail/foaf-dev/2003-July/005463.html](http://lists.foaf-project.org/pipermail/foaf-dev/2003-July/005463.html)。