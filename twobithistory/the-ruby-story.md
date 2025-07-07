# Ruby 的故事

*2017 年 11 月 19 日*

Ruby 一直是我最喜欢的编程语言之一，尽管有时我发现很难说清具体原因。我能给出的最好解释是一个音乐类比：如果说 Python 给我的感觉是朋克摇滚——它简单、可预测，但有些僵硬——那么 Ruby 则更像爵士乐。Ruby 赋予程序员极大的自由来表达自己，但这代价是增加了复杂性，并可能导致程序员写出让其他人难以立即理解的代码。

我一直都知道，表达自由是 Ruby 社区的核心价值观。但我之前没有充分认识到，它对 Ruby 的最初开发和普及是多么地重要。人们可能会为了追求更好的性能，或者为了节省时间的抽象而创建一门编程语言——而 Ruby 的故事之所以有趣，是因为从一开始，它的目标就仅仅是让程序员感到快乐。

## Yukihiro Matsumoto

Yukihiro Matsumoto，也被大家称为“Matz”，于 1990 年毕业于筑波大学。筑波是东京东北部的一个小镇，以科学研究和技术开发中心而闻名。筑波大学的 STEM (科学、技术、工程、数学) 项目尤其受到好评。Matsumoto 学习的是信息科学，主攻编程语言。他曾一度在 Ikuo Nakata 运营的编程语言实验室工作。

Matsumoto 于 1993 年开始开发 Ruby，距离他毕业仅几年时间。他开始开发 Ruby 是因为他正在寻找一种现有脚本语言 (scripting language) 无法提供的特性。当时他正在使用 Perl，但觉得它太像一种“玩具语言”。Python 也未能达到他的要求；用他自己的话说：

> “我当时知道 Python。但我不喜欢它，因为我不认为它是一门真正的面向对象 (object-oriented) 语言——面向对象特性看起来像是语言的附加功能。”
> “作为一名拥有 15 年经验的语言狂热者和面向对象爱好者，我真的想要一门真正的、易于使用的面向对象脚本语言。”
> “我找了很久，但没找到。”[^1]

因此，理解 Matsumoto 创建 Ruby 的动机之一，是他试图创建一个更好、更面向对象的 Perl 版本。

但在其他时候，Matsumoto 也曾表示，他创建 Ruby 的主要动机仅仅是为了让自己和他人更快乐。在 Matsumoto 2008 年的一次 Google 技术演讲接近尾声时，他展示了以下幻灯片：

![](/images/matz.png)

他告诉听众，

> “我希望看到 Ruby 帮助世界上每一位程序员提高效率，享受编程，并感到快乐。这是 Ruby 语言的首要目标。”[^2]

Matsumoto 接着开玩笑说，他创建 Ruby 是出于自私的原因，因为他对其他语言太不满意了，所以他只想创造一些能让自己快乐的东西。

这张幻灯片完美体现了 Matsumoto 谦逊的风格。原来 Matsumoto 是一名虔诚的摩门教徒，我曾想知道他的宗教信仰是否与他传奇般的善良有关。无论如何，这种善良是如此出名，以至于 Ruby 社区有一个名为 MINASWAN 的原则，即“Matz Is Nice And So We Are Nice”（Matz 很好，所以我们也要好）。这张幻灯片肯定让 Google 的听众感到不同寻常——我想象中，Google 技术演讲中随意抽取的任何一张幻灯片，都应该充满了代码示例和衡量某个工程解决方案比另一个更快或更高效的指标。我怀疑，很少有幻灯片能如此简单地阐述如此崇高的目标。

Ruby 主要受到 Perl 的影响。Perl 是 Larry Wall 在 1980 年代末创建的，旨在处理和转换基于文本的报告。它以其文本处理和正则表达式 (regular expression) 功能而闻名。一个 Perl 程序包含许多 Ruby 程序员会熟悉的语法元素——有 `$` 符号、`@` 符号，甚至还有 `elsif`，我一直认为这是 Ruby 比较不那么令人愉快的怪癖之一。在更深层次上，Ruby 借鉴了 Perl 大量的正则表达式处理方式和标准库。

但 Perl 绝不是 Ruby 唯一的灵感来源。在开始开发 Ruby 之前，Matsumoto 曾在一个完全用 Emacs Lisp 编写的邮件客户端上工作。这段经历让他对 Emacs 和 Lisp 语言的内部机制有了很多了解，Matsumoto 曾说这影响了 Ruby 底层的对象模型。在此基础上，他还添加了一个 Smalltalk 风格的消息传递系统，这构成了 Ruby 中依赖 `#method_missing` 的任何行为的基础。Matsumoto 还声称 Ada 和 Eiffel 也对 Ruby 产生了影响。

当决定 Ruby 的名字时，Matsumoto 和同事 Keiju Ishitsuka 考虑了几个备选方案。他们正在寻找一个既能暗示 Ruby 与 Perl 的关系，又能暗示其与 shell 脚本 (shell scripting) 相关的名字。在一段非常值得一读的 [即时消息交流](http://blade.nagaokaut.ac.jp/cgi-bin/scat.rb/ruby/ruby-talk/88819) 中，Ishitsuka 和 Matsumoto 可能花太多时间思考了 shell、蛤蜊、牡蛎和珍珠之间的关系，差点把 Ruby 语言命名为“Coral”或“Bisque”。幸运的是，他们最终决定使用“Ruby”这个名字，寓意是它像“pearl”（珍珠）一样，是一种珍贵的宝石。另外，六月的诞生石是珍珠，而七月的诞生石是红宝石 (ruby)，这意味着“Ruby”这个名字也是一个像 C++ 或 C# 那样，带点幽默感的“渐进式改进”命名。

## Ruby 西行记

Ruby 在日本迅速流行起来。1995 年首次发布后不久，Matz 就被一家名为 Netlab (也称为 Network Applied Communication Laboratory) 的日本软件咨询公司聘用，全职开发 Ruby。到 2000 年，也就是 Ruby 首次发布仅仅五年后，它在日本的受欢迎程度就超过了 Python。但它才刚刚开始进入英语国家。Ruby 诞生之初就有一个日语邮件列表 (mailing list) 用于讨论，但英语邮件列表直到 1998 年才启动。最初，英语邮件列表主要由用英语写作的日本 Ruby 开发者使用，但随着 Ruby 知名度的提高，这种情况逐渐改变。

2000 年，Dave Thomas 出版了《Programming Ruby》，这是第一本介绍 Ruby 的英文书籍。这本书因其封面上印有镐头图案而被称为“镐头书”。它首次将 Ruby 介绍给了许多西方程序员。就像在日本一样，Ruby 迅速传播开来，到 2002 年，英语 Ruby 邮件列表的流量已经超过了最初的日语邮件列表。

到 2005 年，Ruby 变得更受欢迎，但它仍然不是一门主流编程语言。随着 Ruby on Rails 的发布，这种情况发生了改变。Ruby on Rails 是 Ruby 的“杀手级应用 (killer app)”，它比任何其他项目都更能推广 Ruby。Ruby on Rails 发布后，根据 TIOBE 编程语言排行榜 (TIOBE language index) 的衡量，人们对 Ruby 的兴趣全面飙升：

![](/images/tiobe_ruby.png)

有时人们开玩笑说，用 Ruby 编写的唯一程序就是 Ruby on Rails Web 应用程序。这听起来好像 Ruby on Rails 完全占据了 Ruby 社区，但这只是一部分事实。尽管 Ruby 确实因人们用它编写 Rails 应用而闻名，但 Rails 对 Ruby 的贡献，与 Ruby 对 Rails 的贡献是等量的。

Ruby 的哲学深刻影响了 Rails 的设计和实现。Rails 的创建者 David Heinemeier Hansson 经常谈到他第一次接触 Ruby 时，那几乎是一种宗教般的体验。他曾说，这次相遇是如此具有变革性，以至于“赋予了他为 Matz 的创造物进行传教工作的使命。”[^3] 对 Hansson 来说，Ruby 这种“无束缚”的方法，是对 Python 和 Java 等语言自上而下强加限制的一种政治上勇敢的反叛。他很欣赏这门语言信任他，并赋予他自主判断如何最好地表达程序的权力。

像 Matsumoto 一样，Hansson 声称他创建 Rails 是出于对现状的不满，以及希望为自己改善现状的愿望。他，和 Matsumoto 一样，将程序员的快乐放在首位，通过他所谓的“更大的微笑原则 (The Principle of The Bigger Smile)”来评估 Rails 的新增功能。任何让 Hansson 笑得更开心的东西，都会被纳入 Rails 的代码库。因此，Rails 会包含一些非正统的特性，比如“Inflector”类 (Inflector class)（它试图自动将单数类名映射到复数数据库表名）和 Rails 的 `Time` 扩展 (Time extensions)（允许程序员编写诸如 `2.days.ago` 这样有趣的表达式）。对一些人来说，这些功能确实很奇怪，但 Rails 的成功证明了有多少人发现它极大地简化了他们的工作。

因此，尽管 Rails 看起来像是 Ruby 的一个偶然应用，碰巧变得极其流行，但 Rails 实际上体现了 Ruby 的许多核心原则。此外，考虑到 Rails 依赖 Ruby 宏 (macro) 般的类方法调用来实现模型关联 (model associations) 等功能，很难想象 Rails 能用其他任何语言构建。有些人可能会认为，Ruby 的大部分开发都围绕着 Ruby on Rails 展开，这是不健康生态系统的标志，但 Ruby 和 Ruby on Rails 如此紧密地交织在一起，是有充分理由的。

## Ruby 的未来

人们似乎对 Ruby (和 Ruby on Rails) 是否正在消亡有着异乎寻常的兴趣。早在 2011 年，Stack Overflow 和 Quora 上似乎就充斥着程序员们的问题：如果 Ruby 在未来几年内不再流行，他们是否还有必要学习它。这些担忧并非毫无根据；根据 TIOBE 编程语言排行榜和 Stack Overflow 的趋势，Ruby 和 Ruby on Rails 的受欢迎程度一直在下降。尽管 Ruby on Rails 曾是炙手可热的新事物，但它后来被更热门、更新的框架 (framework) 所超越。

这种现象发生的一个理论是，程序员正在放弃动态类型语言 (dynamically typed languages) 而转向静态类型语言 (statically typed languages)。TIOBE 编程语言排行榜的分析师认为，质量要求的提高使得运行时异常 (runtime exceptions) 越来越难以接受。他们引用 TypeScript 作为这一趋势的例子——JavaScript 的一个全新版本被创建，仅仅是为了确保客户端代码能够受益于编译时安全保证 (compile-time safety guarantees)。

我认为，一个更可能的答案是，Ruby on Rails 现在面临的竞争对手比以前多得多。当 Rails 在 2005 年首次推出时，创建 Web 应用程序的方法并不多——主要的替代方案是 Java。如今，你可以使用为 Go、JavaScript 或 Python 构建的优秀框架来创建 Web 应用程序，这只是列举了最受欢迎的几个选项。Web 世界似乎也正朝着更分布式 (distributed) 的应用程序架构发展，这意味着，职责不再由一个代码库负责从数据库访问到视图渲染的所有事情，而是被分配给专注于做好一件事的不同组件。对于像与 JavaScript 前端 (frontend) 通信的 JSON API 这样专注的应用，Rails 显得过于宽泛和臃肿。

尽管如此，我们仍有理由对 Ruby 的未来保持乐观。Rails 和 Ruby 都在持续积极地开发中。Matsumoto 和其他人正在努力开发 Ruby 的第三个主要版本，他们的目标是使其比现有版本快三倍，这可能会缓解一直困扰 Ruby 的性能问题。即使自 2005 年以来 Web 框架的世界变得更加多样化，这也不意味着 Ruby on Rails 将没有立足之地。它现在是一个成熟的工具，拥有巨大的内置能力，对于某些类型的应用程序来说，它将永远是一个不错的选择。

但即使 Ruby 和 Rails 最终走向“恐龙之路”（消亡），有一件事似乎肯定会存活下来，那就是 Ruby 倡导的“程序员快乐”精神。Ruby 对许多新编程语言的设计产生了深远影响，这些语言采纳了它许多最好的思想。其他新语言则试图成为 Ruby 的“更现代化”诠释：例如，Elixir 是一个强调函数式编程范式 (functional programming paradigm) 的 Ruby 版本，而仍在开发中的 Crystal 则旨在成为 Ruby 的静态类型版本。世界上许多程序员都爱上了 Ruby 及其语法，因此我们可以相信它的影响力将在未来很长一段时间内持续存在。

*如果您喜欢这篇文章，每四周会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS feed](https://twobithistory.org/feed.xml)，确保您不会错过新文章。*

[^1]: http://ruby-doc.org/docs/ruby-doc-bundle/FAQ/FAQ.html
[^2]: https://www.youtube.com/watch?v=oEkJvvGEtB4?t=30m55s
[^3]: http://rubyonrails.org/doctrine/