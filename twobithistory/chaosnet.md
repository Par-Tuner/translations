# Chaosnet 的简短历史

*2018 年 9 月 30 日*

如果你启动 `dig` 命令，对 `google.com` 执行一次 DNS 查询，你会得到类似下面的响应：

```
$ dig google.com

; <<>> DiG 9.10.6 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27120
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		194	IN	A	216.58.192.206

;; Query time: 23 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Sep 21 16:14:48 CDT 2018
;; MSG SIZE  rcvd: 55

```

输出结果包含两部分：一部分描述了你提出的“问题”（“`google.com` 的 IP 地址是什么？”），另一部分则描述了你收到的答案。在答案部分，我们看到 `dig` 找到了一个记录，它看起来有五个字段。记录的类型由从左数第四个字段的 `A` 表示——这是一个“地址”记录。在 `A` 的右侧，即第五个字段，我们可以看到 `google.com` 的 IP 地址是 `216.58.192.206`。第二个字段中的 `194` 值则指定了该记录可以被缓存的秒数。

那么 `IN` 字段告诉我们什么呢？在很长一段时间里，我一直以为 `IN` 是一个介词，所以每条 DNS 记录都在说类似“`google.com` *在* `A` 中，并且 IP 地址是 `216.58.192.206`”这样的话。结果发现，`IN` 实际上代表“internet”（互联网）。DNS 记录中的 `IN` 部分告诉我们该记录的*类别*。

为什么 DNS 记录的类别会是“internet”以外的值呢？那又意味着什么？你如何搜索一个*不在*互联网上的主机？看起来 `IN` 似乎是唯一有意义的值。确实，当你尝试查询 `google.com` 的地址，同时指定你期望的记录类别不是 `IN` 时，你查询的 DNS 服务器很可能会报错。在下面的例子中，当我们尝试使用 `HS` 类别查询 `google.com` 的 IP 地址时，`8.8.8.8`（Google 公共 DNS）上的域名服务器返回了 `SERVFAIL` 状态：

```
$ dig -c HS google.com

; <<>> DiG 9.10.6 <<>> -c HS google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 31517
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;google.com.			HS	A

;; Query time: 34 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Tue Sep 25 14:48:10 CDT 2018
;; MSG SIZE  rcvd: 39

```

所以，除了 `IN` 之外的类别并没有得到广泛支持。但它们确实存在。除了 `IN`，DNS 记录还可以有 `HS` 类别（正如我们刚刚看到的）或 `CH` 类别。`HS` 类别是为名为 Hesiod 的系统保留的，该系统使用域名系统 (Domain Name System) 存储和分发简单的文本数据。它通常在本地环境中用作 LDAP 的替代品。`CH` 类别则为一种名为 Chaosnet 的系统保留。

如今，世界属于 TCP/IP。这两种协议（以及 UDP）管理着计算机之间发生的大部分远程通信。但我认为，你仍然能在互联网的底层结构中找到这个早已灭绝、名字富有启发性的其他系统的痕迹，这真是太棒了。Chaosnet 是什么？它又是如何像恐龙一样走向消亡的呢？

## 麻省理工学院的机房

Chaosnet 是由麻省理工学院 (MIT) 人工智能实验室的研究人员在 20 世纪 70 年代开发的。它是为了设计和构建一种能够比通用计算机更高效地运行 Lisp 编程语言的机器而进行的一项更大规模工作的一部分。

Lisp 是麻省理工学院教授 John McCarthy 的心血结晶，他开创了人工智能 (Artificial Intelligence) 领域。他于 1960 年发表的一篇论文中首次向世界描述了 Lisp。到 1962 年，解释器 (interpreter) 和编译器 (compiler) 都已编写完成。Lisp 引入了惊人数量的特性，这些特性在今天被我们认为是许多编程语言的标准配置。它是第一个拥有垃圾回收器 (garbage collector) 的语言。它是第一个拥有 REPL（Read-Eval-Print Loop，交互式编程环境）的语言。它也是第一个支持动态类型 (dynamic typing) 的语言。它受到了从事人工智能工作的程序员的青睐，举个例子，著名的 SHRDLU 演示就是用它开发的，该演示允许人类用自然语言向计算机口述涉及玩具积木的简单动作。

Lisp 的问题在于它可能很慢。简单的操作可能需要两倍于其他语言的执行时间，因为 Lisp 变量是在运行时进行类型检查的，而不仅仅是在编译期间。Lisp 的垃圾回收器在麻省理工学院的 IBM 7090 上运行时，甚至可能占用整整一秒的时间 [^1]。这些性能问题尤其不受欢迎，因为使用 Lisp 的人工智能研究人员正试图构建像 SHRDLU 这样与用户实时交互的应用程序。在 20 世纪 70 年代末，麻省理工学院人工智能实验室的一群研究人员决定通过构建专门设计用于运行 Lisp 程序的机器来解决这些问题。这些“Lisp 机器”拥有更多的内存和更适合 Lisp 的精简指令集。类型检查将由专用电路 (dedicated circuitry) 完成，从而将速度提高几个数量级。与当时大多数计算机系统不同，Lisp 机器不会采用分时 (time-shared) 模式，因为雄心勃勃的 Lisp 程序需要计算机所有可用的资源。每个用户都将拥有自己的 CPU。在一份备忘录中，麻省理工学院的 Lisp 机器小组描述了这将如何显著简化 Lisp 编程：

> Lisp 机器是一种个人计算机。个人计算意味着处理器和主内存 (main memory) 不会进行时分复用，而是每个人都拥有自己的处理器和主内存。个人计算系统由一个处理器池组成，每个处理器都有自己的主内存和用于交换的磁盘。当用户登录时，他会被分配一个处理器，并在会话期间独占使用它。当他注销时，处理器会返回到池中，供下一个人使用。这样，就不会有其他用户争用内存；用户经常引用的页面会保留在核心内存中，从而大大减少了交换开销。因此，Lisp 机器解决了分时 Lisp 系统的基本问题 [^2]。

Lisp 机器在某种意义上是一种个人计算机，但与我们今天所认为的个人计算机不同。正如 Lisp 机器小组最初设想的那样，用户坐在办公室里，面前不是自己的 Lisp 机器，而是终端。这些终端将连接到实际的 Lisp 机器，而 Lisp 机器则位于其他地方。尽管每个用户都将拥有自己的处理器，但这些处理器仍将“放在机房里”，因为它们会产生噪音并占用空间，因此“不受办公室欢迎” [^3]。处理器将通过一个“完全分布式控制”的高速局域网共享对文件系统和打印机等设备的访问 [^4]。这个网络就是 Chaosnet。

Chaosnet 既是一种硬件标准，也是一种软件协议。其硬件标准类似于以太网 (Ethernet)，事实上，Chaosnet 软件协议最终也运行在以太网上。该软件协议规定了网络层 (network-layer) 和传输层 (transport-layer) 的交互，与 TCP/IP 不同，它始终旨在管理一个*本地*网络。在麻省理工学院人工智能实验室发布的另一份备忘录中，Lisp 机器小组成员 David Moon 解释说，Chaosnet“没有为低速链路、噪声链路、多路径以及具有显著传输时间的长距离链路等情况提供特殊规定” [^5]。相反，重点是设计一种在小型网络上性能优于其他协议的协议。

速度很重要，因为 Chaosnet 位于每个 Lisp 处理器和文件系统之间。网络延迟会显著减慢查看文本文档内容等基本操作。为了足够快，Chaosnet 在当时 Arpanet 上使用的网络控制程序 (Network Control Program) 的基础上进行了多项改进。根据 Moon 的说法，“设计消除 Arpanet 中存在的瓶颈非常重要，例如多个连接共享的控制链路以及在发送下一条消息之前需要确认每条消息的需求” [^6]。Chaosnet 协议以与当今 TCP 类似的方式批量确认数据包，从而将需要传输的数据包数量减少了一半到三分之一。

Chaosnet 还可以使用相对简单的路由算法，因为 Lisp 机器网络上的大多数主机可能都通过一根短线连接。Moon 写道，Chaosnet 的路由方案“基于网络拓扑简单、多路径少且任何路径长度都非常短的假设。这使得更复杂的方案变得不必要” [^7]。算法的简单性意味着实现 Chaosnet 协议很容易。据说其实现程序的大小是 Arpanet 网络控制程序的一半 [^8]。

Chaosnet 协议还有其他独特之处。Chaosnet 地址只有 16 比特，是 IPv4 地址大小的一半，考虑到 Chaosnet 仅用于本地网络，这很合理。Chaosnet 也不使用端口号；相反，一个想要连接到另一台机器上另一个进程的进程首先会发出一个连接请求，该请求指定一个目标“联系名称”。这个联系名称通常只是特定服务的名称。例如，一个主机可能会尝试使用联系名称 `TELNET` 连接到另一个主机。实际上，我猜这或多或少就像 TCP 一样工作，因为像端口 80 这样众所周知的端口也可以有 `HTTP` 这样的联系名称。

Chaosnet DNS 类别由 RFC 973 于 1986 年添加到域名系统 (Domain Name System) 中。它取代了早期可用的另一个类别，即 `CSNET` 类别，该类别用于支持一个名为计算机科学网络 (Computer Science Network) 的网络。我一直无法弄清楚为什么 Chaosnet 会被域名系统特别对待。还有其他协议族本可以被添加，但从未实现。例如，域名系统的主要架构师之一 Paul Mockapetris 曾写道，他最初设想 DNS 将包含 Xerox 网络协议的类别 [^9]。但这从未发生。Chaosnet 可能被添加仅仅是因为 Arpanet 和互联网的早期工作大部分发生在马萨诸塞州剑桥市的 Bolt, Beranek and Newman 公司，其员工通常与麻省理工学院有某种联系。Chaosnet 在当时相对较小的计算机网络工作者群体中可能广为人知。

随着 Lisp 机器越来越不受欢迎，Chaosnet 的使用量也随之减少。尽管 Lisp 机器在短时间内是商业上可行的产品——在 20 世纪 80 年代由 Symbolics 和 Lisp Machines Inc. 等公司销售——但它们很快就被更便宜的微型计算机取代，这些微型计算机无需专用电路也能同样快速地运行 Lisp。TCP/IP 也解决了 Chaosnet 最初旨在规避的许多 Arpanet 原始协议问题。

## 壳中幽灵

不幸的是，关于 Chaosnet 的信息已经不多了。RFC 675，基本上是 TCP/IP 的第一个草案，于 1974 年发布。Chaosnet 于 1975 年首次开发 [^10]。TCP/IP 最终征服了世界，但 Chaosnet 似乎是一个技术死胡同。尽管 Chaosnet 可能影响了后续的 TCP/IP 工作，但我尚未找到任何具体的例子。

Chaosnet 唯一真正可见的残余是 `CH` DNS 类别。我发现这个事实有点奇怪地令人着迷。`CH` 类别是另一种网络协议的残余幽灵，而我们所处的世界早已选择了 TCP/IP。至少对我来说，知道 Chaosnet 的最后痕迹仍然潜伏在我们网络化社会的基础设施中，这令人兴奋。`CH` DNS 类别是数字考古学的一个有趣文物。但它也活生生地提醒我们，互联网并非一蹴而就，TCP/IP 并非连接计算机的唯一方式，而且“互联网”远不是我们全球通信系统所能拥有的最酷的名字。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 RSS 订阅源，以确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> RSS 从何而来？为什么有这么多相互竞争的格式？为什么人们似乎不再那么频繁地使用它了？
>
> 本周关于 RSS 的文章将回答这些问题以及更多问题：<https://t.co/BsCN5GQidR>
>
> — TwoBitHistory (@TwoBitHistory) [2018 年 9 月 17 日](https://twitter.com/TwoBitHistory/status/1041485204802756608?ref_src=twsrc%5Etfw)

[^1]: LISP 1.5 Programmer’s Manual, The Computation Center and Research Laboratory of Electronics, 90, accessed September 30, 2018, [http://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf](http://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf)
[^2]: Lisp Machine Progress Report (Artificial Intelligence Memo 444), MIT Artificial Intelligence Laboratory, August, 1977, 3, accessed September 30, 2018, [https://dspace.mit.edu/bitstream/handle/1721.1/5751/AIM-444.pdf](https://dspace.mit.edu/bitstream/handle/1721.1/5751/AIM-444.pdf).
[^3]: Lisp Machine Progress Report (Artificial Intelligence Memo 444), 4.
[^4]: ibid.
[^5]: Chaosnet (Artificial Intelligence Memo 628), MIT Artificial Intelligence Laboratory, June, 1981, 1, accessed September 30, 2018, [https://dspace.mit.edu/bitstream/handle/1721.1/6353/AIM-628.pdf](https://dspace.mit.edu/bitstream/handle/1721.1/6353/AIM-628.pdf).
[^6]: ibid.
[^7]: Chaosnet (Artificial Intelligence Memo 628), 16.
[^8]: Chaosnet (Artificial Intelligence Memo 628), 9.
[^9]: Paul Mockapetris and Kevin Dunlap, “The Design of the Domain Name System,” Computer Communication Review 18, no. 4 (August 1988): 3, accessed September 30, 2018, <http://www.cs.cornell.edu/people/egs/615/mockapetris.pdf>.
[^10]: Chaosnet (Artificial Intelligence Memo 628), 1.