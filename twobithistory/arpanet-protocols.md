# ARPANET 协议的工作原理

*2021 年 3 月 8 日*

ARPANET 通过证明来自不同厂商的计算机可以使用标准化协议连接起来，彻底改变了计算机领域。在我关于 [ARPANET 历史意义的帖子](https://twobithistory.org/2021/02/07/arpanet.html) 中，我提到了其中一些协议，但没有详细描述。因此，我想更深入地研究它们。我还想看看这些早期协议的设计理念，有多少沿用至今。

ARPANET 协议与我们现代的互联网协议一样，都是分层组织的 [^1]。上层协议运行在下层协议之上。如今，TCP/IP 协议栈有五层 (物理层 (Physical layer)、数据链路层 (Link layer)、网络层 (Network layer)、传输层 (Transport layer) 和应用层 (Application layer))，但 ARPANET 只有三层——或者根据计数方式，可能是四层。

我将解释这些层级的工作原理，但首先要插播一段关于 ARPANET 各部分由谁构建的背景信息，这有助于理解其分层设计的原因。

## 快速历史背景

ARPANET 由美国联邦政府资助，具体来说是国防部高级研究计划局 (Advanced Research Projects Agency，简称 ARPA，DARPA 的前身)，这也是其名称“ARPANET”的由来。美国政府没有直接构建这个网络；相反，它将这项工作外包给了一家名为 Bolt, Beranek, and Newman (简称 BBN) 的波士顿咨询公司。

BBN 负责了网络实现的许多职责，但并非全部。BBN 的工作是设计和维护一种名为接口消息处理器 (Interface Message Processor，简称 IMP) 的机器。IMP 是一台定制的霍尼韦尔 (Honeywell) 小型计算机，全国各地每个要连接到 ARPANET 的站点都收到了一台。IMP 作为 ARPANET 的网关，每个主机站点最多可连接四台主机。它本质上就是一个路由器。BBN 控制着 IMP 上运行的软件，这些软件负责在 IMP 之间转发数据包 (packet)，但该公司对连接到 IMP 并成为 ARPANET 实际主机的机器没有直接控制权。

主机由作为网络最终用户的计算机科学家控制。这些来自全国各地主机站点的计算机科学家负责编写软件，使主机之间能够相互通信。IMP 赋予了主机相互发送消息 (message) 的能力，但除非主机就消息使用的格式达成一致，否则这种能力用处不大。为了解决这个问题，一群主要由各主机站点研究生组成的团队组成了网络工作组 (Network Working Group)，致力于制定主机计算机使用的协议。

因此，如果你想象一次 ARPANET 上成功的网络交互 (比如发送一封电子邮件)，那么促成这次交互成功的一些工程部分是由一组人 (BBN) 负责的，而另一些工程部分则由另一组人 (网络工作组和各主机站点的工程师) 负责。这种组织和后勤上的巧合可能在很大程度上推动了 ARPANET 协议采用分层方法，这反过来又影响了 TCP/IP 协议栈的分层设计。

## 好的，回到协议

![ARPANET Network Stack](https://twobithistory.org/images/arpanet-stack.png)
*图 1: ARPANET 协议层级。*

协议层级被组织成一个层次结构。最底层是“0 级 (level 0)” [^2]。从某种意义上说，这一层并不“算数”，因为在 ARPANET 上，这一层完全由 BBN 控制，因此不需要标准协议。0 级管理数据如何在 IMP 之间传递。在 BBN 内部，有规则管理 IMP 如何做到这一点；在 BBN 外部，IMP 子网络 (sub-network) 是一个黑盒 (black box)，它只会传递你给它的任何数据。因此，0 级是一个没有真正协议的层级，因为它没有一套公开已知且达成一致的规则，并且其存在可以被 ARPANET 主机上运行的软件忽略。粗略地说，它处理了今天 TCP/IP 协议栈中物理层、数据链路层和网络层所涵盖的一切，甚至还包括相当一部分传输层的功能，这一点我将在本文末尾再次提及。

“1 级 (level 1)”层建立了 ARPANET 主机与其连接的 IMP 之间的接口。如果你愿意，可以把它看作是 BBN 构建的黑盒 0 级的一个应用程序编程接口 (API)。当时它也被称为 IMP-主机协议 (IMP-Host Protocol)。这个协议必须编写并发布，因为当 ARPANET 最初建立时，每个主机站点都必须编写自己的软件来与 IMP 交互。如果 BBN 不提供一些指导，他们就不会知道如何做到这一点。

IMP-主机协议由 BBN 在一份名为 [BBN Report 1822](https://walden-family.com/impcode/BBN1822_Jan1976.pdf) 的冗长文档中详细说明。随着 ARPANET 的发展，该文档经过多次修订；我在这里描述的，大致是 IMP-主机协议最初设计的工作方式。根据 BBN 的规则，主机可以向其 IMP 传递不超过 8095 比特的**消息** (message)，每条消息都有一个**引导头** (leader)，其中包含目标主机号和一种称为**链路号** (link number) 的东西 [^3]。IMP 会检查目标主机号，然后尽职地将消息转发到网络中。当从远程主机接收到消息时，接收 IMP 会在将其传递给本地主机之前，用源主机号替换目标主机号。消息实际上并不是在 IMP 之间直接传递的——IMP 会将消息分解成更小的**数据包** (packet) 以便在网络上传输——但这个细节对主机是隐藏的。

![1969 Host-IMP Leader](https://twobithistory.org/images/host-imp-1969.png)
*图 2: 1969 年的主机-IMP 消息引导头格式。图表来自 [BBN Report 1763](https://walden-family.com/impcode/1969-initial-IMP-design.pdf)。*

链路号可以是 0 到 255 之间的任何数字，它有两个目的。它被更高层协议用来在网络上的任意两台主机之间建立多个通信通道，因为可以想象在任何给定时间可能有多个本地用户与同一个目标主机通信。(换句话说，链路号允许在主机之间进行多路复用 (multiplexing) 通信。) 但它也用于 1 级层，以控制主机之间可以发送的流量，这对于防止更快的计算机压垮较慢的计算机是必要的。根据最初的设计，IMP-主机协议限制每台主机在每条链路上一次只能发送一条消息。一旦给定主机通过某个链路向远程主机发送了一条消息，它就必须等待从远程 IMP 接收到一种特殊的消息，称为 RFNM (请求下一条消息 Request for Next Message)，然后才能通过同一链路发送下一条消息。后来为了提高性能而对该系统进行的修订，允许一台主机在任何给定时间最多有八条消息在传输中 [^4]。

“2 级 (level 2)”层是事情真正开始变得有趣的地方，因为正是这一层及其上层，BBN 和国防部完全留给了学者和网络工作组 (Network Working Group) 自行发明。2 级层包括主机-主机协议 (Host-Host Protocol)，该协议最初在 RFC 9 中概述，并首次在 RFC 54 中正式规定。在 [ARPANET 协议手册](http://mercury.lcs.mit.edu/~jnc/tech/arpaprot.html) 中对主机-主机协议有更易读的解释。

主机-主机协议管理主机如何相互创建和管理**连接** (connection)。连接是两台主机之间的一个单向数据管道，一端是其中一台主机上的**写入套接字** (write socket)，另一端是另一台主机上的**读取套接字** (read socket)。引入“套接字 (socket)”概念是为了在有限的 1 级链路功能之上 (请记住链路号只能是 256 个值之一)，为程序提供一种寻址远程主机上特定进程 (process) 的方式。读取套接字是偶数，而写入套接字是奇数；套接字是读取套接字还是写入套接字被称为套接字的类型 (gender)。当时没有像 TCP 那样的“端口号 (port number)”。连接可以通过使用链路 0 (专门为此目的保留) 在主机之间发送特殊格式的主机-主机控制消息来打开、操作和关闭。一旦通过链路 0 交换控制消息以建立连接，就可以使用接收方选择的另一个链路号发送更多数据消息。

主机-主机控制消息通过三字母助记符来标识。当两台主机交换一条 STR (发送方到接收方 sender-to-receiver) 消息和一条匹配的 RTS (接收方到发送方 receiver-to-sender) 消息时，连接就建立了——这些控制消息都被称为连接请求消息。连接可以通过 CLS (关闭 close) 控制消息关闭。还有其他控制消息用于改变数据消息从发送方到接收方的发送速率，这再次是为了确保更快的宿主机不会压垮较慢的宿主机。1 级协议已经提供的流量控制 (flow control) 在 2 级显然不足；我怀疑这是因为从远程 IMP 接收 RFNM 仅保证远程 IMP 已将消息传递给目标主机，而不是主机已完全处理了该消息。还有一条 INR (接收方中断 interrupt-by-receiver) 控制消息和一条 INS (发送方中断 interrupt-by-sender) 控制消息，它们主要供更高层协议使用。

更高层协议都位于“3 级 (level 3)”，这是 ARPANET 的应用层 (Application layer)。Telnet 协议提供了到另一台主机的虚拟电传连接，可能是其中最重要的协议，但这一层还有许多其他协议，例如用于文件传输的 FTP 以及各种用于发送电子邮件的实验性协议。

这一层有一个协议与众不同：初始连接协议 (Initial Connection Protocol，简称 ICP)。ICP 被认为是 3 级协议，但实际上它是一种 2.5 级协议，因为其他 3 级协议都依赖于它。需要 ICP 是因为 2 级主机-主机协议提供的连接是单向的，但大多数应用程序需要双向 (即全双工 full-duplex) 连接才能做任何有趣的事情。ICP 规定了一个两步过程，客户端在一台主机上运行，可以连接到另一台主机上长期运行的服务进程。第一步涉及使用服务进程的知名套接字号 (well-known socket number) 从服务器到客户端建立一个单向连接。然后服务器会通过已建立的连接向客户端发送一个新的套接字号。此时，现有连接将被丢弃，并打开两个新连接：一个基于传输的套接字号的读取连接，以及一个基于传输的套接字号加一的写入连接。这套巧妙的流程是大多数操作的必要序曲——例如，它是建立 Telnet 连接的第一步。

至此，我们完成了 ARPANET 协议层级的“攀升”。你可能一直期待我会在某个时候提到“网络控制协议 (Network Control Protocol)”。在我为这篇帖子和上一篇帖子做研究之前，我确实认为 ARPANET 运行在一个名为 NCP 的协议上。这个缩写有时被用来指代整个 ARPANET 协议，这可能就是我产生这个想法的原因。例如，[RFC 801](https://tools.ietf.org/html/rfc801) 谈到将 ARPANET 从“NCP”过渡到“TCP”，听起来 NCP 就像是 ARPANET 中与 TCP 等效的协议。但 ARPANET 从来没有一个“网络控制协议” (即使 [大英百科全书 (Encyclopedia Britannica) 这么认为](https://www.britannica.com/topic/ARPANET))，我怀疑人们错误地将“NCP”解读为“网络控制协议”，而实际上它代表的是“网络控制程序 (Network Control Program)”。网络控制程序是运行在每台主机中的内核级程序 (kernel-level program)，负责处理网络通信，相当于如今操作系统 (operating system) 中的 TCP/IP 协议栈。“NCP”，在 RFC 801 中的用法，是一个转喻，而不是一个协议。

## 与 TCP/IP 的比较

ARPANET 协议后来都被 TCP/IP 协议取代了 (Telnet 和 FTP 除外，它们很容易适应在 TCP 之上运行)。ARPANET 协议都基于网络由单一实体 (BBN) 构建和管理的假设，而 TCP/IP 协议栈则是为“互联网络”而设计的，即一个由多个网络组成的网络，其中一切都更加灵活且可能不可靠。这导致了我们现代协议栈与 ARPANET 协议之间一些更显而易见的差异，例如我们现在如何区分网络层和传输层。在 ARPANET 中部分由 IMP 实现的类似传输层的功能，现在完全由网络边缘 (network edge) 的主机负责。

然而，我对 ARPANET 协议最感兴趣的是，如今 TCP 中如此多的传输层功能，在 ARPANET 上经历了一个磕磕绊绊的演变过程。我不是网络专家，所以我翻出了我的大学网络教科书 (Kurose 和 Ross，冲啊)，他们对传输层通常负责什么给出了一个非常棒的概述。总结他们的解释，一个传输层协议至少必须做以下事情。这里的**段** (segment) 基本等同于 ARPANET 中使用的**消息** (message) 一词：

*   在**进程** (process) 之间而非仅仅主机之间提供传输服务 (传输层多路复用 (multiplexing) 和解复用 (demultiplexing))
*   对每个段 (segment) 进行完整性检查 (即确保传输中没有数据损坏)

传输层还可以像 TCP 那样，提供**可靠数据传输** (reliable data transfer)，这意味着：

*   段按顺序交付
*   没有段丢失
*   段的传输速度不会快到被接收方丢弃 (流量控制 (flow control))

看起来 ARPANET 在如何进行多路复用和解复用以使进程能够通信方面存在一些困惑——BBN 引入了链路号 (link number) 来在 IMP-主机级别实现这一点，但结果是，无论如何，在主机-主机级别上，套接字号 (socket number) 仍然是必需的。然后链路号就只用于 IMP-主机级别的流量控制，但 BBN 似乎后来放弃了这种做法，转而选择在独特的主机对之间进行流量控制，这意味着链路号最初是一个多功能的设计，但最终基本上退化了。TCP 现在使用端口号 (port number) 代替，对每个 TCP 连接单独进行流量控制。进程-进程 (process-process) 的多路复用和解复用完全在 TCP 内部进行，不像 ARPANET 那样会“泄露”到下层。

有趣的是，从 Kurose 和 Ross 阐述 TCP 背后思想的角度来看，ARPANET 最初在 IMP-主机级别采用了 Kurose 和 Ross 所称的严格的“停等协议 (stop-and-wait)”方法来实现可靠数据传输。“停等协议”方法是传输一个段，然后拒绝传输任何更多段，直到收到最近传输的段的确认 (acknowledgment)。这是一种简单的方法，但它意味着在网络中一次只有一个段在传输，这使得协议非常慢——这就是为什么 Kurose 和 Ross 将“停等协议”仅仅视为通往功能完备的传输层协议 (fully featured transport layer protocol) 的垫脚石。在 ARPANET 上，“停等协议”曾是工作方式，因为在 IMP-主机级别，每发送一条消息都必须收到一个请求下一条消息 (Request for Next Message) 的响应，然后才能发送更多消息。公平地说，BBN 最初认为这对于在主机之间提供流量控制是必要的，所以这种减速是故意的。正如我之前提到的，RFNM 要求后来为了更好的性能而放宽了，IMP 开始为消息附加序列号 (sequence number) 并跟踪一个“窗口 (window)”内的在途消息，这与今天 TCP 实现的方式或多或少相同 [^5]。

因此，ARPANET 表明，如果所有人都同意一些基本规则，异构计算系统 (heterogeneous computing systems) 之间的通信是可能的。正如我之前所说，这是 ARPANET 最重要的遗产。但我希望通过对这些基本规则的深入研究，能揭示 ARPANET 协议对我们今天使用的协议产生了多大的影响。传输层职责在主机和 IMP 之间共享的方式确实存在很多笨拙之处，有时甚至是冗余的。回想起来，主机最初在任何给定链路上一次只能发送一条消息，这几乎有点好笑。但 ARPANET 实验是一个独特的机会，通过实际构建和运营网络来学习这些经验，而且这些经验似乎在升级到我们今天所知的互联网时得到了很好的利用。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS feed](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> 努力重拾旧业！
>
> 我的最新文章是我对 ARPANET 为何如此重要的突破的看法 (当然，是令人惊讶且巧妙的)，重点关注了 ARPANET 首次亮相的会议：<https://t.co/8SRY39c3St>
>
> — TwoBitHistory (@TwoBitHistory) [2021 年 2 月 7 日](https://twitter.com/TwoBitHistory/status/1358487195905064960?ref_src=twsrc%5Etfw)

[^1]: 协议分层是由网络工作组 (Network Working Group) 发明的。这一论点在 [RFC 871](https://tools.ietf.org/html/rfc871) 中提出。分层也是 BBN 划分主机和 IMP 之间职责的自然延伸，因此 BBN 也应获得一些赞誉。
[^2]: “层级 (level)”术语由网络工作组 (Network Working Group) 使用。参见例如 [RFC 100](https://www.rfc-editor.org/info/rfc100)。
[^3]: 在 IMP-主机协议 (IMP-Host Protocol) 的后续修订中，引导头 (leader) 得到了扩展，链路号 (link number) 升级为消息 ID (message ID)。但主机-主机协议 (Host-Host Protocol) 继续只使用消息 ID 字段的高八位，并将其视为链路号。参见 [ARPANET 协议手册](http://mercury.lcs.mit.edu/~jnc/tech/arpaprot.html) 的“主机到主机 (Host-to-Host)”协议部分。
[^4]: John M. McQuillan 和 David C. Walden。《ARPA 网络设计决策》(The ARPA Network Design Decisions)，第 284 页，[https://www.walden-family.com/public/whole-paper.pdf](https://www.walden-family.com/public/whole-paper.pdf)。访问日期：2021 年 3 月 8 日。
[^5]: 同上。