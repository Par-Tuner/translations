# 面向对象编程 (OOP) 诞生前夜的 Simula

*2019 年 1 月 31 日*

想象一下，你正坐在河岸边的草地上。眼前，河水湍急地流淌而过。午后的阳光让你陷入了一种闲适而富有哲思的心情，你开始思考眼前的这条河是否真的存在。当然，大量的水就在几英尺外流过。但你所称的“河”到底是什么呢？毕竟，你看到的水转瞬即逝，取而代之的又是更多不同的水。看起来，“河”这个词似乎根本没有指代你眼前任何固定的实体。

2009 年，Clojure 的创造者 Rich Hickey 发表了一场精彩的演讲，探讨了这种哲学困境为何给面向对象编程 (Object-Oriented Programming, OOP) 范式带来了问题。他认为，我们看待计算机程序中的对象 (object) 的方式，就像我们看待河流一样——我们想象对象拥有固定的身份 (fixed identity)，即使对象的许多或所有属性 (property) 都会随时间变化。这样做是错误的，因为我们无法区分处于一种状态的对象实例 (object instance) 和处于另一种状态的同一个对象实例。在我们的程序中，我们没有明确的时间概念。我们只是随意地在任何地方使用同一个名字，并希望在引用对象时，它处于我们预期的状态。不可避免地，我们会编写出错误 (bug)。

Hickey 总结道，解决方案是：我们不应该将世界建模为可变对象 (mutable object) 的集合，而应该将其建模为作用于不可变数据 (immutable data) 的**过程** (process) 集合。我们应该将每个对象视为一个由因果关联的状态 (causally related state) 组成的“河流”。总而言之，你应该使用像 Clojure 这样的函数式语言 (Functional Language)。

![](https://twobithistory.org/images/river.jpg)
*作者在徒步旅行中，思考面向对象编程的本体论承诺。*

自 Hickey 在 2009 年发表他的演讲以来，人们对函数式编程语言 (Functional Programming Language) 的兴趣日益增长，函数式编程 (Functional Programming) 惯用法也已融入最流行的面向对象语言中。即便如此，大多数程序员仍然每天都在实例化对象 (instantiate object) 并原地修改 (mutate in place) 它们。他们这样做已经太久了，以至于很难想象编程还能有什么不同。

我本想写一篇关于 Simula 的文章，并设想它主要会讲述我们今天所熟悉的面向对象构造 (object-oriented construct) 是何时以及如何被添加到该语言中的。但我认为，更有趣的故事是 Simula 最初与现代面向对象编程语言**多么不同**。这不应该令人惊讶，因为我们现在所知的面向对象范式并非一蹴而就、完全成形。Simula 有两个主要版本：Simula I 和 Simula 67。Simula 67 为世界带来了类 (class)、类层次结构 (class hierarchy) 和虚方法 (virtual method)。但 Simula I 是一个初稿，它尝试了其他关于数据 (data) 和过程 (procedure) 如何捆绑在一起的想法。Simula I 模型不像 Hickey 提出的那样是函数式模型，但它确实侧重于随时间展开的**过程**，而不是具有隐藏状态 (hidden state) 且相互作用的对象。如果 Simula 67 坚持了更多 Simula I 的想法，我们今天所知的面向对象范式可能真的会大相径庭——这种偶然性应该提醒我们，要警惕地认为当前的范式将永远占据主导地位。

## 从 Simula 0 到 Simula 67

Simula 是由两位挪威人 Kristen Nygaard 和 Ole-Johan Dahl 创建的。

在 20 世纪 50 年代末，Nygaard 受雇于挪威国防研究机构 (Norwegian Defense Research Establishment, NDRE)，这是一个隶属于挪威军队的研究机构。在那里，他开发了用于核反应堆设计和运筹学 (operations research) 的蒙特卡洛模拟 (Monte Carlo simulation)。这些模拟最初是手工完成的，后来才被编程并在 Ferranti Mercury 计算机上运行 [^1]。Nygaard 很快发现，他需要一种更高层次的方式来向计算机描述这些模拟。

Nygaard 普遍开发的那种模拟被称为“离散事件模型 (discrete event model)”。这种模拟捕捉了一系列事件如何随时间改变系统状态——但这里的关键特性是，模拟可以从一个事件跳到下一个事件，因为事件是离散的，并且在事件之间系统没有任何变化。根据 Nygaard 和 Dahl 在 1966 年发表的一篇关于 Simula 的论文，这种建模方式正越来越多地被用于分析“神经网络、通信系统、交通流量、生产系统、行政系统、社会系统等” [^2]。因此 Nygaard 认为，其他人可能也需要一种更高层次的方式来描述这些模拟。他开始寻找能够帮助他实现他所谓的“模拟语言 (Simulation Language)”或“蒙特卡洛编译器 (Monte Carlo Compiler)”的人 [^3]。

Dahl 曾受雇于 NDRE，在那里他从事语言设计工作，此时他加入进来，扮演了 Nygaard 的沃兹尼亚克之于乔布斯的角色。在接下来的一年左右时间里，Nygaard 和 Dahl 致力于开发被称为“Simula 0”的版本 [^4]。这个早期版本的语言最初只是 ALGOL 60 的一个适度扩展，计划将其实现为一个预处理器 (preprocessor)。当时的语言比后来的版本抽象程度低得多。主要的语言构造是“站点 (station)”和“客户 (customer)”。这些可以用来建模某些离散事件网络 (discrete event network)；Nygaard 和 Dahl 举了一个模拟机场离港的例子 [^5]。但 Nygaard 和 Dahl 最终想出了一种更通用的语言构造，既可以表示“站点”和“客户”，也可以建模更广泛的模拟。这是 Simula 从一个应用程序专用 (application-specific) 的 ALGOL 包 (package) 变为通用编程语言 (general-purpose programming language) 的两次重大泛化中的第一次。

在 Simula I 中，没有“站点”或“客户”，但可以使用“过程”来重新创建它们。一个过程是与一个被称为该过程的**操作规则** (operating rule) 的单一动作相关联的数据属性 (data attribute) 的集合。你可能会把一个过程想象成一个只有一个方法 (method) 的对象，这个方法可能叫做 `run()`。然而，这个类比并不完美，因为每个过程的操作规则都可以随时暂停或恢复——这些操作规则是一种协程 (coroutine)。一个 Simula I 程序会将系统建模为一组概念上并行运行的过程。在任何时候，只有一个过程可以真正处于“当前”状态，但一旦一个过程暂停自身，下一个排队的过程就会自动接管。当模拟运行时，在幕后，Simula 会维护一个“事件通知 (event notice)”的时间线，跟踪每个过程何时应该恢复。为了恢复一个暂停的过程，Simula 需要跟踪多个调用栈 (call stack)。这意味着 Simula 不能再是一个 ALGOL 预处理器，因为 ALGOL 只有一个调用栈。Nygaard 和 Dahl 致力于编写自己的编译器 (compiler)。

在他们介绍这个系统的论文中，Nygaard 和 Dahl 通过实现一个工厂模拟来阐述其用法，该工厂拥有数量有限的机器，可以处理订单 [^6]。这里的过程是订单，它首先寻找可用的机器，如果没有可用机器则暂停自身等待，然后一旦找到空闲机器就运行直到完成。有一个订单过程的定义，然后用于实例化 (instantiate) 几个不同的订单实例，但从未在这些实例上调用任何方法。程序的主体部分只是创建过程并让它们运行。

第一个 Simula I 编译器于 1965 年完成。该语言在挪威计算机中心 (Norwegian Computer Center) 变得流行起来，Nygaard 和 Dahl 在离开 NDRE 后在那里工作。Simula I 的实现可供 UNIVAC 用户和 Burroughs B5500 用户使用 [^7]。Nygaard 和 Dahl 与一家名为 ASEA 的瑞典公司签订了咨询协议，涉及使用 Simula 运行作业车间模拟 (job shop simulation)。但 Nygaard 和 Dahl 很快意识到 Simula 可以用来编写与模拟完全无关的程序。

奥斯陆大学 (University of Oslo) 的教授 Stein Krogdahl 曾撰写过关于 Simula 历史的文章，他声称“真正促使新通用语言开发起飞的火花”是英国计算机科学家 C.A.R. Hoare 的一篇名为“记录处理 (Record Handling)”的论文 [^8]。如果你现在阅读 Hoare 的论文，这一点很容易相信。我很惊讶当人们谈论面向对象语言的历史时，Hoare 的名字不常被提及。请看他论文中的这段摘录：

> 该提议设想在程序执行期间，计算机内部存在任意数量的记录 (record)，每个记录都代表程序员过去、现在或将来感兴趣的某个对象。程序动态控制存在的记录数量，并可以根据手头任务的要求创建新记录或销毁现有记录。

> 计算机中的每个记录都必须属于有限数量的不相交的记录类 (record class) 之一；程序员可以根据需要声明任意数量的记录类，并为每个类关联一个标识符来命名它。记录类名可以被认为是像“奶牛”、“桌子”或“房子”这样的通用术语，而属于这些类的记录则代表个体奶牛、桌子和房子。

Hoare 在这篇特定论文中没有提及子类 (subclass)，但 Dahl 认为他向 Nygaard 和自己介绍了这个概念 [^9]。Nygaard 和 Dahl 注意到 Simula I 中的过程通常具有共同的元素。使用超类 (superclass) 来实现这些共同元素会很方便。这也提出了一个可能性，即“过程”这个想法本身可以作为超类来实现，这意味着并非每个类都必须是具有单一操作规则的过程。这便是使 Simula 67 成为真正通用编程语言 (general-purpose programming language) 的第二次重大泛化。这是一个如此大的焦点转变，以至于 Nygaard 和 Dahl 曾短暂考虑更改语言名称，以便人们知道它不仅仅用于模拟 [^10]。但“Simula”这个名字已经太深入人心，他们不敢冒险。

1967 年，Nygaard 和 Dahl 与 Control Data 签署了一份合同，以实现这个新版本的 Simula，即 Simula 67。同年 6 月举行了一次会议，Control Data、奥斯陆大学和挪威计算中心的人员与 Nygaard 和 Dahl 会面，以确定这种新语言的规范。这次会议最终形成了一份名为“Simula 67 通用基础语言 (Simula 67 Common Base Language)”的文档，它定义了该语言未来的发展方向。

几家不同的供应商将制作 Simula 67 编译器。Simula 用户协会 (Association of Simula Users, ASU) 成立并开始举办年度会议。Simula 67 很快在超过 23 个不同的国家拥有了用户 [^11]。

## 21 世纪的 Simula

Simula 之所以被人们记住，是因为它对后来取代它的语言产生了影响。你现在很难找到还在使用 Simula 编写应用程序 (application program) 的人。但这并不意味着 Simula 是一种完全消亡的语言。多亏了 GNU cim，你今天仍然可以在你的计算机上编译和运行 Simula 程序。

cim 编译器实现了 1986 年修订后的 Simula 标准。但这主要是 Simula 67 版本的语言。你可以像使用 Simula 67 那样编写类、子类 (subclass) 和虚方法。所以你可以创建一个小型面向对象程序，它看起来很像你用 Python 或 Ruby 轻松编写的程序：

```
! dogs.sim ;
Begin
    Class Dog;
        ! cim 编译器要求虚过程 (virtual procedure) 必须完全指定；
        Virtual: Procedure bark Is Procedure bark;;
    Begin
        Procedure bark;
        Begin
            OutText("Woof!");
            OutImage;           ! 输出一个新行；
        End;
    End;

    Dog Class Chihuahua;        ! Chihuahua 被 Dog “前缀”；
    Begin
        Procedure bark;
        Begin
            OutText("Yap yap yap yap yap yap");
            OutImage;
        End;
    End;

    Ref (Dog) d;
    d :- new Chihuahua;         ! :- 是引用赋值运算符 (reference assignment operator)；
    d.bark;
End;
```

你可以像这样编译和运行它：

```
$ cim dogs.sim
Compiling dogs.sim:
gcc -g -O2 -c dogs.c
gcc -g -O2 -o dogs dogs.o -L/usr/local/lib -lcim
$ ./dogs
Yap yap yap yap yap yap
```

(你可能会注意到 cim 将 Simula 编译成 C 语言，然后交给 C 编译器处理。)

这就是 1967 年面向对象编程的样子，我希望你同意，除了语法差异，这与 2019 年面向对象编程的样子也大同小异。所以你可以明白为什么 Simula 被认为是一种具有历史重要性的语言。

但我更感兴趣的是向你展示 Simula I 的核心——过程模型 (process model)。这个过程模型在 Simula 67 中仍然可用，但只有当你使用 `Process` 类和一个特殊的 `Simulation` 块时才能使用。

为了向你展示过程是如何工作的，我决定模拟以下场景。想象一下，有一个村庄，里面住满了村民，旁边有一条河。河里有很多鱼，但村民们之间只有一根钓鱼竿。村民们胃口大开，大约每 60 分钟就会感到饥饿。当他们饿了的时候，他们必须使用钓鱼竿来捕鱼。如果一个村民因为另一个村民正在等待而无法使用钓鱼竿，那么这个村民就会排队等待使用钓鱼竿。如果一个村民为了捕鱼不得不等待超过五分钟，那么这个村民就会失去健康值。如果一个村民失去太多健康值，那么这个村民就会饿死。

这是一个有点奇怪的例子，我不确定为什么它会首先出现在我的脑海中。但就这样吧。我们将把村民表示为 Simula 过程，看看在一个有四个村民的村庄里，一天的模拟时间会发生什么。

完整的程序可以在这里找到：Gist。

我的输出的最后几行如下所示。这里我们看到了一天中最后几个小时发生的事情：

```
1299.45: John is hungry and requests the fishing rod.
1299.45: John is now fishing.
1311.39: John has caught a fish.
1328.96: Betty is hungry and requests the fishing rod.
1328.96: Betty is now fishing.
1331.25: Jane is hungry and requests the fishing rod.
1340.44: Betty has caught a fish.
1340.44: Jane went hungry waiting for the rod.
1340.44: Jane starved to death waiting for the rod.
1369.21: John is hungry and requests the fishing rod.
1369.21: John is now fishing.
1379.33: John has caught a fish.
1409.59: Betty is hungry and requests the fishing rod.
1409.59: Betty is now fishing.
1419.98: Betty has caught a fish.
1427.53: John is hungry and requests the fishing rod.
1427.53: John is now fishing.
1437.52: John has caught a fish.
```

可怜的 Jane 饿死了。但她比 Sam 坚持得更久，Sam 甚至没能活到早上 7 点。现在只剩下 Betty 和 John 两个人需要钓鱼竿了，他们的日子过得真不错。

我希望你在这里看到的是，程序的主体、顶层部分除了创建四个村民过程并让它们运行之外，什么也没做。这些过程以我们今天操作对象的方式来操作钓鱼竿对象。但程序的主体部分没有调用任何方法，也没有修改过程的任何属性。这些过程有内部状态 (internal state)，但这种内部状态只由过程自身修改。

这里仍然有原地修改的字段 (field)，所以这种编程风格并没有直接解决纯函数式编程 (Pure Functional Programming) 所能解决的问题。但正如 Krogdahl 所观察到的，“这种机制促使模拟程序的程序员将底层系统 (underlying system) 建模为一组过程，每个过程都描述了该系统中一些自然的事件序列 (natural sequence of events)” [^12]。我们不再主要从名词或执行者 (actor) 的角度思考——即对象对其他对象做事情——而是从持续进行的过程 (ongoing process) 的角度思考。这样做的好处是，我们可以将程序的整体控制权交给 Simula 的事件通知系统，Krogdahl 称之为“时间管理器 (time manager)”。因此，即使我们仍然在原地修改过程，也没有任何过程对另一个过程的状态做出任何假设。每个过程只与其他过程间接交互。

目前尚不清楚这种模式如何用于构建，比如说，一个编译器或一个 HTTP 服务器。（另一方面，如果你曾经在 Unity 游戏引擎中编程游戏，这应该看起来很熟悉。）我也承认，尽管我们现在有了一个“时间管理器”，但这可能并非 Hickey 所说的我们需要在程序中明确的时间概念 (explicit notion of time) 的确切含义。（我想他会想要类似 Ada Lovelace 用来区分变量在不同时间所取值的上标符号。）尽管如此，我认为非常有趣的是，在面向对象编程的开端，我们就能找到一种与我们所习惯的面向对象编程完全不同的编程风格。我们可能理所当然地认为面向对象编程只有一种工作方式——即程序只是某个对象对其他对象执行操作的精确顺序的冗长列表。Simula I 的过程系统表明还有其他方法。函数式语言可能是更深思熟虑的替代方案，但 Simula I 提醒我们，现代面向对象编程的替代方案这一概念本身就不应该令人惊讶。

*如果你喜欢这篇文章，每四周都会有更多类似的文章发布！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 RSS feed，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> 大家好！很遗憾我没有时间写任何新文章，但我刚刚发布了我的 RSS 历史的更新版本。这个版本包含了后来我对 RSS 背后一些关键人物（如 Ramanathan Guha 和 Dan Libby）进行的采访。https://t.co/WYPhvpTGqB
>
> — TwoBitHistory (@TwoBitHistory) [2018 年 12 月 18 日](https://twitter.com/TwoBitHistory/status/1075075139543449600?ref_src=twsrc%5Etfw)

[^1]: Jan Rune Holmevik，“The History of Simula”，2019 年 1 月 31 日访问，[http://campus.hesge.ch/daehne/2004-2005/langages/simula.htm](http://campus.hesge.ch/daehne/2004-2005/langages/simula.htm)。
[^2]: Ole-Johan Dahl 和 Kristen Nygaard，“SIMULA—An ALGOL-Based Simulation Langauge”，Communications of the ACM 9，no. 9 (September 1966)：671，2019 年 1 月 31 日访问，[http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.95.384&rep=rep1&type=pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.95.384&rep=rep1&type=pdf)。
[^3]: Stein Krogdahl，“The Birth of Simula”，2，2019 年 1 月 31 日访问，[http://heim.ifi.uio.no/~steinkr/papers/HiNC1-webversion-simula.pdf](http://heim.ifi.uio.no/~steinkr/papers/HiNC1-webversion-simula.pdf)。
[^4]: 同上。
[^5]: Ole-Johan Dahl 和 Kristen Nygaard，“The Development of the Simula Languages”，ACM SIGPLAN Notices 13，no. 8 (August 1978)：248，2019 年 1 月 31 日访问，[https://hannemyr.com/cache/knojd_acm78.pdf](https://hannemyr.com/cache/knojd_acm78.pdf)。
[^6]: Dahl 和 Nygaard (1966)，676。
[^7]: Dahl 和 Nygaard (1978)，257。
[^8]: Krogdahl，3。
[^9]: Ole-Johan Dahl，“The Birth of Object-Orientation: The Simula Languages”，3，2019 年 1 月 31 日访问，[http://www.olejohandahl.info/old/birth-of-oo.pdf](http://www.olejohandahl.info/old/birth-of-oo.pdf)。
[^10]: Dahl 和 Nygaard (1978)，265。
[^11]: Holmevik。
[^12]: Krogdahl，4。