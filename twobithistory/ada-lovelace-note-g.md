# 埃达·洛夫莱斯的程序到底做了什么？

*2018 年 8 月 18 日*

微软 (Microsoft) 的创立故事是计算机历史上最著名的篇章之一。1975 年，保罗·艾伦 (Paul Allen) 飞往阿尔伯克基，演示了他和比尔·盖茨 (Bill Gates) 为 Altair 微型计算机编写的 BASIC 解释器。由于他们都没有一台能正常工作的 Altair 计算机，艾伦和盖茨使用他们编写并在哈佛大学计算机系统上运行的模拟器 (emulator) 来测试他们的解释器。这个模拟器完全基于已发布的 Intel 8080 处理器规格。当艾伦最终在真实的 Altair 计算机上运行他们的解释器时——就在他和盖茨希望购买他们软件的人面前——他完全不知道它是否能成功运行。但它成功了。接下来的一个月，艾伦和盖茨正式创立了他们的新公司。

在艾伦和盖茨编写 BASIC 解释器的一个多世纪前，埃达·洛夫莱斯 (Ada Lovelace) 编写并发表了一个计算机程序。她也为一个只被描述给她的计算机编写了程序。但她的程序与微软 BASIC 解释器不同，从未运行过，因为她所针对的计算机从未被建造出来。

洛夫莱斯的程序常被称为世界上第一个计算机程序。并非所有人都同意这个说法。事实证明，洛夫莱斯的遗产是计算机历史上备受争议的话题之一。沃尔特·艾萨克森 (Walter Isaacson) 曾写道，关于她贡献的范围和价值的争议构成了一个“小众的学术领域” [^1]。不可避免地，洛夫莱斯是女性这一事实使得这场争议充满了火药味。历史学家们引用了各种原始证据来论证对洛夫莱斯的赞誉是恰当的还是不应得的。但他们似乎很少花时间解释她已发表著作的技术细节，这很可惜，因为技术细节才是故事中最引人入胜的部分。谁不想知道一个写于 1843 年的程序究竟是如何工作的呢？

公平地说，洛夫莱斯的程序在不加详述的情况下，对普通人来说并不容易解释。然而，正是她程序的复杂精妙之处，才使其如此非凡。无论她是否应该被称为“第一位程序员”，她的程序都以远超以往任何作品的严谨性进行了规范。她仔细思考了如何将操作组织成可以重复的组，从而发明了循环 (loop)。她意识到追踪变量 (variable) 状态变化的重要性，并引入了一种符号系统来图示这些变化。作为一名程序员，我惊讶地发现洛夫莱斯所做的事情与我们今天编写软件的体验是如此相似。

那么，让我们仔细看看洛夫莱斯的程序。她设计它来计算伯努利数 (Bernoulli numbers)。要理解伯努利数是什么，我们必须回到几千年前，追溯数学中最古老问题之一的起源。

## 幂次和

毕达哥拉斯学派 (Pythagoreans) 生活在地中海沿岸，他们崇拜数字。他们的一种消遣方式是用小石子摆出三角形。

![](https://twobithistory.org/images/triangular_numbers1.png)

图 1: 三角形数

一个石子后面跟着一排两个石子，就构成了一个包含三个石子的三角形。再加一排三个石子，你就得到了一个包含六个石子的三角形。你可以这样继续下去，每次都比前一排多加一个石子。一个有六排的三角形包含 21 个石子。但是一个有 423 排的三角形包含多少个石子呢？

毕达哥拉斯学派想要找到一种方法，无需进行所有加法就能计算出以下结果：

\\\[1 \+ 2 \+ 3 \+ \\cdots \+ n\\]

他们最终意识到，如果将两个大小相同的三角形并排放在一起，形成一个矩形，你可以计算出矩形的面积，然后除以二，就能得到每个三角形中的石子数量：

![](https://twobithistory.org/images/triangular_numbers2.png)

图 2: 两个三角形可以组成一个矩形

\\\[1 \+ 2 \+ 3 \+ \\cdots \+ n \= \\frac{n(n\+1\)}{2}\\]

阿基米德 (Archimedes) 后来探索了一个类似的问题。他对以下数列感兴趣：

\\\[1^2 \+ 2^2 \+ 3^2 \+ \\cdots \+ n^2\\]

你可以通过想象一堆逐渐增大的正方形 (由小方块构成)，一个叠一个，形成一个金字塔来可视化这个数列。阿基米德想知道是否有简单的方法来计算建造一个例如有 423 层的金字塔需要多少个方块。他记录了一个也允许几何解释的解决方案 [^2]。

三个金字塔可以拼在一起形成一个长方体棱柱，一端有一个微小的、一个方块高的突出部分。这个小突出部分恰好是一个遵循毕达哥拉斯学派用来制作石子三角形相同规则的三角形。（这个视频 https://www.youtube.com/watch?v=aXbT37IlyZQ 可能会更清楚地解释我的意思。）所以整个形状的体积由以下方程给出：

\\\[3(1^2 \+ 2^2 \+ 3^2 \+ \\cdots \+ n^2\) \= (n\+1\)n^2 \+ (1 \+ 2 \+ 3 \+ \\cdots \+ n)\\]

通过代入毕达哥拉斯学派关于前 *n* 个整数和的方程并进行一些代数运算，你会得到：

\\\[1^2 \+ 2^2 \+ 3^2 \+ \\cdots \+ n^2 \= \\frac{n(n\+1\)(2n\+1\)}{6}\\]

公元 499 年，印度数学家兼天文学家阿耶波多 (Aryabhata) 出版了一部名为《阿耶波多历数书》 (Aryabhatiya) 的著作，其中包含了计算立方和的公式：

\\\[1^3 \+ 2^3 \+ 3^3 \+ \\cdots \+ n^3 \= (1 \+ 2 \+ 3 \+ \\cdots \+ n)^2\\]

计算前 *n* 个正整数的四次方和的公式又过了 500 年才发表 [^3]。

你可能想知道，此时是否存在一种通用方法来计算前 *n* 个整数的 *k* 次方和。数学家们也在思考这个问题。德国数学家兼有点古怪的数字命理学家约翰·福尔哈伯 (Johann Faulhaber) 能够计算出高达 17 次方整数和的公式，并于 1631 年发表。但这可能花费了他数年时间，而且他没有给出通用解法 [^4]。布莱兹·帕斯卡 (Blaise Pascal) 最终在 1665 年概述了一种通用方法，尽管它依赖于首先知道如何计算每个较低次方的整数和 [^5]。例如，要计算前 *n* 个正整数的六次方和，你必须首先知道如何计算前 *n* 个正整数的五次方和。

瑞士数学家雅各布·伯努利 (Jakob Bernoulli) 于 1705 年去世，他遗作中提出了一个更实用的通用解决方案。伯努利首先推导了计算前 *n* 个正整数的一次方、二次方和三次方和的公式 [^6]。他以多项式形式给出了这些公式，如下所示：

\\\[1 \+ 2 \+ 3 \+ \\cdots \+ n \= \\frac{1}{2}n^2 \+ \\frac{1}{2}n \\\\

1^2 \+ 2^2 \+ 3^2 \+ \\cdots \+ n^2 \= \\frac{1}{3}n^3 \+ \\frac{1}{2}n^2 \+ \\frac{1}{6}n
\\\\

1^3 \+ 2^3 \+ 3^3 \+ \\cdots \+ n^3 \= \\frac{1}{4}n^4 \+ \\frac{1}{2}n^3 \+
\\frac{1}{4}n^2\\]

利用帕斯卡三角形 (Pascal’s Triangle)，伯努利意识到这些多项式遵循一种可预测的模式。本质上，伯努利将每个项的系数分解为两个因子，其中一个因子可以通过帕斯卡三角形确定，另一个因子则可以从多项式中所有系数之和似乎总是等于一的有趣性质中推导出来。确定每个项应附加的指数 (exponent) 并非难题，因为它也遵循可预测的模式。每个系数中必须使用“和为一”规则计算的因子形成了一个序列，这个序列后来被称为伯努利数。

伯努利的发现并不意味着现在计算前 *n* 个正整数的任意给定幂次和变得微不足道。为了计算前 *n* 个正整数的 *k* 次方和，你需要知道直到第 *k* 个伯努利数的所有伯努利数。每个伯努利数只有在已知前一个伯努利数的情况下才能计算。但是，计算一系列长伯努利数比依次推导每个幂次和公式要容易得多，因此伯努利的发现是数学上的一大进步。

## 巴贝奇

查尔斯·巴贝奇 (Charles Babbage) 出生于 1791 年，比伯努利去世晚了近一个世纪。我一直模糊地知道巴贝奇设计但没有建造一台机械计算机。但我从未完全理解那台计算机是如何工作的。事实证明，基本思想并不难理解，这是个好消息。洛夫莱斯的程序就是为巴贝奇的机器之一设计的，所以我们这里需要再快速绕道，谈谈这些机器是如何工作的。

巴贝奇设计了两台独立的机械计算机器。他的第一台机器被称为差分机 (Difference Engine)。在袖珍计算器发明之前，人们依靠对数表来计算大数的乘积。（有一个很好的 Numberphile 视频 https://youtu.be/VRzH4xB0GdM 解释了这是如何做到的。）大型对数表在概念上不难创建，但创建它们所需的计算量巨大，这意味着在巴贝奇时代，它们经常包含错误。巴贝奇对此感到沮丧，于是他试图创造一台能够机械地、因此无误地制表对数的机器 [^7]。

差分机不是一台计算机，因为它只进行加减法运算。它利用了法国数学家加斯帕尔·德·普罗尼 (Gaspard de Prony) 设计的一种方法，该方法将制表对数的过程分解为小步骤 [^8]。这些小步骤只涉及加减法，这意味着可以雇佣一支没有特殊数学天赋或训练的人员队伍来制作表格。德·普罗尼的方法，被称为差分法 (method of divided differences)，可以用来制表任何多项式 (polynomial)。而多项式又可以用来近似对数和三角函数。

为了了解这个过程是如何工作的，考虑以下简单的多项式函数：

\\\[y \= x^2 \+ 1\\]

差分法涉及找到 *y* 对于不同 *x* 值的每个连续值之间的差。然后找到这些差之间的差，并可能找到这些下一级差之间的差，直到出现一个常数差。然后，这些差就可以通过简单的加法来获得多项式的下一个值。

因为上述多项式只是一个二次多项式，我们只需两列差值就能找到常数差：

| x | y | Diff 1 | Diff 2 |
| --- | --- | --- | --- |
| 1 | 2 |  |  |
| 2 | 5 | 3 |  |
| 3 | 10 | 5 | 2 |
| 4 | 17 | 7 | 2 |
| 5 | ? | ? | 2 |
| … | … | … | … |

表 1: 差分表

现在，既然我们知道常数差是 2，我们就可以只通过加法来找到当 *x* 为 5 时 *y* 的值。如果我们将 2 加到“Diff 1”列的最后一个条目 7 上，我们得到 9。如果我们将 9 加到 *y* 列的最后一个条目 17 上，我们得到 26，这就是我们的答案。

巴贝奇的差分机，对于上面表格中的每一列差值，都有一列物理齿轮。每个齿轮代表一个十进制数字，一整列则代表一个十进制数。差分机有八列齿轮，因此它可以制表高达七次的多项式。这些齿轮列最初被设置为与差分表早期行相匹配的值，这些值是预先计算好的。然后，操作员会转动一个曲柄轴，使常数差在机器中传播，因为存储在每列上的值都会加到下一列上。

巴贝奇建造了差分机的一小部分，并用它在聚会上演示他的想法 [^9]。但即使花费了相当于两艘大型战舰造价的公款，他也没有建造出完整的机器 [^10]。巴贝奇在 19 世纪初找不到任何人能以足够的精度制造他所需的齿轮数量。一台能正常工作的差分机直到 20 世纪 90 年代，在精密机械加工出现后才被建造出来。YouTube 上有一个很棒的视频 https://www.youtube.com/watch?v=BlbQsKpq3Ak 演示了一台借给山景城计算机历史博物馆 (Computer History Museum) 的差分机，即使只是为了听机器运行时发出的奇妙声音，也值得一看。

巴贝奇最终对差分机失去了兴趣，因为他意识到可以建造一台更强大、更灵活的机器。他的分析机 (Analytical Engine) 就是我们今天所知的巴贝奇的机械计算机。分析机基于差分机中使用的相同齿轮柱，但差分机只有八列，而分析机则应该有数百列。分析机可以使用穿孔卡片 (punched cards) 进行编程，就像提花织机 (Jacquard Loom) 一样，并且除了加减法外，还能进行乘除法。为了执行这些操作之一，机器的一个部分，称为“运算器” (mill)，会重新配置成适当的形态，从用于数据存储 (data storage) 的其他列中读取操作数 (operands)，然后将结果写回另一列。

巴贝奇称他的新机器为分析机，因为它强大到足以进行类似于数学分析 (mathematical analysis) 的工作。差分机可以制表多项式，但分析机将能够计算，例如，另一个表达式的多项式展开的系数。这是一台令人惊叹的机器，但英国政府明智地拒绝资助其建造。于是巴贝奇出国去了意大利，试图为他的想法争取支持。

## 译者笔记

在都灵，巴贝奇遇到了意大利工程师兼未来的首相路易吉·梅纳布雷亚 (Luigi Menabrea)。他说服梅纳布雷亚写一份关于分析机能完成什么工作的概述。1842 年，梅纳布雷亚用法文发表了一篇关于这个主题的论文。次年，洛夫莱斯将梅纳布雷亚的论文翻译成英文并发表。

洛夫莱斯，当时被称为埃达·拜伦 (Ada Byron)，于 1833 年在一个聚会上首次见到巴贝奇，当时她 17 岁，他 41 岁 [^11]。洛夫莱斯对巴贝奇的差分机着迷不已。她也能理解它的工作原理，因为她从小就接受了广泛的数学辅导。她的母亲安娜贝拉·米尔班克 (Annabella Milbanke) 决定，扎实的数学基础可以抵御洛夫莱斯父亲——著名诗人拜伦勋爵 (Lord Byron) 所拥有的那种狂野浪漫的情感。在 1833 年相遇后，洛夫莱斯和巴贝奇一直属于同一个社交圈，并经常通信。

埃达·拜伦于 1835 年嫁给了威廉·金 (William King)。金后来成为洛夫莱斯伯爵 (Earl of Lovelace)，埃达也因此成为洛夫莱斯伯爵夫人 (Countess of Lovelace)。即使在生了三个孩子之后，她仍然继续她的数学教育，并聘请了德·摩根定律 (De Morgan’s laws) 的发现者奥古斯都·德·摩根 (Augustus de Morgan) 作为她的导师 [^12]。洛夫莱斯立即看到了巴贝奇分析机的潜力，并渴望与他合作推广这个想法。一位朋友建议她为英语读者翻译梅纳布雷亚的论文 [^13]。

梅纳布雷亚的论文简要概述了差分机的工作原理，然后展示了分析机将是一台远超其上的机器。分析机将如此强大，以至于它可以在“*三分钟* 内计算出两个各含二十位数字的乘积” [^14] (原文强调)。梅纳布雷亚进一步举例说明了机器的能力，展示了它如何解决一个简单的线性方程组并展开两个二项式表达式的乘积。在这两种情况下，梅纳布雷亚都提供了洛夫莱斯称之为“发展图” (diagrams of development) 的东西，其中列出了为计算正确答案所需执行的操作序列 [^15]。这些在洛夫莱斯自己的程序意义上也是程序，并且它们最初是在前一年发表的。但正如我们将看到的，梅纳布雷亚的程序只是可能实现的简单示例。它们都微不足道，因为它们不需要任何形式的分支 (branching) 或循环。

洛夫莱斯在她的梅纳布雷亚论文译文后附上了一系列注释，这些注释的总长度远超原文。正是在这里，她对计算领域做出了重大贡献。在注释 A (Note A) 中，洛夫莱斯详细且常以抒情语言解释了这台能够执行任意数学运算的机器的潜力。她预见到像分析机这样的机器不仅限于数字，实际上可以作用于任何对象，“只要这些对象相互间的基本关系能够通过抽象的运算科学来表达，并且能够适应机器的运算符号和机制的作用。” [^16] 她补充说，这台机器有朝一日甚至可以创作音乐。这一见解尤为非凡，因为梅纳布雷亚主要将分析机视为自动化“漫长而枯燥的计算”的工具，这将解放杰出科学家的智力，使其能够进行更高级的思考 [^17]。洛夫莱斯在注释 A 中展现的惊人远见是她今天受到颂扬的一个主要原因。

另一个著名的注释是注释 G (Note G)。洛夫莱斯在注释 G 的开头论证说，尽管分析机拥有令人印象深刻的能力，但它并不能真正被称为“思考”。注释 G 的这一部分后来被艾伦·图灵 (Alan Turing) 称为“洛夫莱斯夫人异议” (Lady Lovelace’s Objection)。然而，洛夫莱斯继续写道，这台机器可以做非凡的事情。为了阐明其处理更复杂问题的能力，洛夫莱斯提供了她计算伯努利数的程序。

完整的程序，以洛夫莱斯在注释 D (Note D) 中解释的扩展“发展图”格式呈现，可以在这里看到：https://upload.wikimedia.org/wikipedia/commons/c/cf/Diagram_for_the_computation_of_Bernoulli_numbers.jpg。该程序本质上是一个操作列表，使用常见的数学符号指定。巴贝奇或洛夫莱斯似乎没有进一步开发出类似分析机操作码 (op code) 的东西。

尽管洛夫莱斯描述的是一种计算直到某个限制的整个伯努利数序列的方法，但她提供的程序只说明了该过程中的一步。她的程序计算了一个她称之为 B7 的数字，现代数学家称之为第八个伯努利数。因此，她的程序旨在解决以下方程：

\\\[B\_7 \= \-1(A\_0 \+ B\_1A\_1 \+ B\_3A\_3 \+ B\_5A\_5\)\\]

在上述公式中，每个项代表特定幂次整数和多项式公式中的一个系数。这里幂次是八，因为第八个伯努利数首次出现在正整数八次方和的公式中。B 和 A 数字代表伯努利发现的两种因子。B1 到 B7 都是不同的伯努利数，根据洛夫莱斯的索引方式进行索引。A0 到 A5 代表伯努利可以使用帕斯卡三角形计算的系数因子。A0、A1、A3 和 A5 的值如下所示。这里 *n* 代表从第一个奇数伯努利数开始的序列中伯努利数的索引。洛夫莱斯的程序使用了 *n* = 4。

\\\[A\_0 \= \-\\frac{1}{2} \\cdot \\frac{2n \- 1}{2n \+ 1} \\\\
A\_1 \= \\frac{2n}{2} \\\\
A\_3 \= \\frac{2n(2n\-1\)(2n\-2\)}{2 \\cdot 3 \\cdot 4} \\\\
A\_5 \= \\frac{2n(2n\-1\)(2n\-2\)(2n\-3\)(2n\-4\)}{2 \\cdot 3 \\cdot 4 \\cdot 5 \\cdot 6}\\]

我创建了一个洛夫莱斯程序到 C 语言的翻译 https://gist.github.com/sinclairtarget/ad18ac65d277e453da5f479d6ccfc20e ，可能更容易理解。洛夫莱斯的程序首先计算 A0 和乘积 B1A1。然后它进入一个循环，重复两次以计算 B3A3 和 B5A5，因为它们是按照相同的模式形成的。在每个乘积计算完成后，它会与所有之前的乘积相加，这样到程序结束时就得到了总和。

显然，C 语言翻译并非洛夫莱斯程序的精确复现。例如，它在栈 (stack) 上声明变量，而洛夫莱斯的变量更像是寄存器 (register)。但它使洛夫莱斯程序中那些有先见之明的部分变得显而易见。C 程序包含两个 `while` 循环，一个嵌套在另一个里面。洛夫莱斯的程序并没有严格意义上的 `while` 循环，但她在注释文本中将操作分组并指定了它们何时应该重复。变量 `v10`，在原始程序和 C 语言翻译中，都作为计数器变量 (counter variable) 运行，每次循环递减，这是任何程序员都会熟悉的结构。事实上，除了大量命名不友好的变量之外，洛夫莱斯程序的 C 语言翻译看起来一点也不陌生。

另一件值得快速提及的事情是，将洛夫莱斯的程序翻译成 C 语言并不难，这要归功于她图表中详尽的细节。与梅纳布雷亚的表格不同，她的表格包含一列名为“任何变量值变化的指示” (Indication of change in the value on any Variable)，这使得追踪程序中状态变化 (mutation of state) 变得容易得多。她在这里为每个变量添加了一个上标索引 (superscript index)，以指示它们所持有的连续值。例如，上标为二意味着这里使用的值是自程序开始以来分配给该变量的第二个值。

## 第一位程序员？

在我将洛夫莱斯的程序翻译成 C 语言后，我能够在自己的电脑上运行它。令我沮丧的是，我一直得到错误的结果。经过一番调试 (debugging) 后，我终于意识到问题不在于我编写的代码。错误在原文中！

在她的“发展图”中，洛夫莱斯将第四个操作写为 `v5 / v4`。但正确的顺序应该是 `v4 / v5`。这很可能是一个排版错误，而不是洛夫莱斯设计的程序中的错误。尽管如此，这一定是计算领域最古老的错误。我惊叹于，在不知情的情况下，我与这个有史以来第一个错误纠结了大约十分钟。

吉姆·兰德尔 (Jim Randall)，另一位将洛夫莱斯程序翻译成 Python https://enigmaticcode.wordpress.com/tag/bernoulli-numbers/ 的博主，也注意到了这个除法错误和另外两个问题。洛夫莱斯发表的程序包含一些小错误，这说明了什么？也许这表明她试图编写的不仅仅是一个演示程序，而是一个真正的程序。毕竟，如果你不编写大量错误，你真的能写出比玩具程序 (toy program) 更复杂的东西吗？

一篇维基百科文章称洛夫莱斯是第一个发表“复杂程序” (complex program) 的人 [^18]。也许这是看待洛夫莱斯成就的正确方式。梅纳布雷亚在洛夫莱斯发表译文的前一年，在他的论文中发表了“发展图”。巴贝奇也编写了二十多个从未发表的程序 [^19]。所以，说洛夫莱斯编写或发表了第一个程序并不完全准确，尽管总有空间争论“程序”到底是什么。即便如此，洛夫莱斯的程序也遥遥领先于之前发表的任何作品。梅纳布雷亚展示的最长程序有 11 个操作，不包含循环或分支；洛夫莱斯的程序包含 25 个操作和一个嵌套循环 (nested loop) (因此也包含分支)。梅纳布雷亚在他的论文末尾写道：

> 一旦机器建成，困难将在于制作卡片；但由于这些卡片仅仅是代数公式的翻译，通过一些简单的符号，将它们的执行交给工人将是容易的 [^20]。

无论是巴贝奇还是梅纳布雷亚，他们对将分析机应用于超出最初促使巴贝奇建造计算机器的直接数学挑战之外的问题，都没有特别的兴趣。洛夫莱斯看到了分析机能够做到的远超巴贝奇或梅纳布雷亚想象的事情。洛夫莱斯也明白，“制作卡片”并非仅仅是事后补充，而且可以做得好，也可以做得差。如果不理解她在注释 G 中的程序，并亲眼看到她在设计上所付出的心血，这一点很难体会。但做到了这一点，你可能会同意，洛夫莱斯，即使她不是第一位程序员，也是第一位配得上这个称号的程序员。

*如果您喜欢这篇文章，每四周会有更多类似的文章发布！请在 Twitter 上关注 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 源](https://twobithistory.org/feed.xml)，以确保您能及时了解新文章的发布。*

*TwoBitHistory 往期回顾…*

> This week's post: Parsing Vim's prestigious pedigree!<https://t.co/1YUszI5dIC>
> 
> — TwoBitHistory (@TwoBitHistory) [August 5, 2018](https://twitter.com/TwoBitHistory/status/1026240555062386689?ref_src=twsrc%5Etfw)

[^1]: Walter Isaacson, The Innovators (New York: Simon & Schuster Paperbacks, 2015), 25.
[^2]: Janet Beery, “Sums of Powers of Positive Integers: Archimedes,” Mathematical Association of America, accessed August 18, 2018, [https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-archimedes-287-212-bce-greece-italy](https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-archimedes-287-212-bce-greece-italy).
[^3]: Janet Beery, “Sums of Powers of Positive Integers: Abu Ali Al-Hasan Ibn Al-Hasan Ibn Al-Haytham,” Mathematical Association of America, accessed August 18, 2018, [https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-abu-ali-al-hasan-ibn-al-hasan-ibn-al-haytham-965-1039-egypt](https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-abu-ali-al-hasan-ibn-al-hasan-ibn-al-haytham-965-1039-egypt).
[^4]: Janet Beery, “Sums of Powers of Positive Integers: Conclusion,” Mathematical Association of America, accessed August 18, 2018, [https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-conclusion](https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-conclusion).
[^5]: Janet Beery, “Sums of Powers of Positive Integers: Blaise Pascal,” Mathematical Association of America, accessed August 18, 2018, [https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-blaise-pascal-1623-1662-france](https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-blaise-pascal-1623-1662-france).
[^6]: Janet Beery, “Sums of Powers of Positive Integers: Jakob Bernoulli,” Mathematical Association of America, accessed August 18, 2018, [https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-jakob-bernoulli-1654-1705-switzerland](https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-jakob-bernoulli-1654-1705-switzerland).
[^7]: Isaacson, 19.
[^8]: Isaacson, 20.
[^9]: Robert Scoble, “A Demo of Charles Babbage’s Difference Engine,” YouTube, June 17, 2010, accessed August 18, 2018, [https://www.youtube.com/watch?v=BlbQsKpq3Ak&feature=youtu.be&t=7m37s](https://www.youtube.com/watch?v=BlbQsKpq3Ak&feature=youtu.be&t=7m37s).
[^10]: Isaacson, 22.
[^11]: Isaacson, 8.
[^12]: Isaacson, 17.
[^13]: Isaacson, 25.
[^14]: Luigi Menabrea, “Sketch of the Analytical Engine,” Scientific Memoirs 3 (1843): 686, accessed August 18, 2018, [https://books.google.com/books/about/Scientific_Memoirs_Selected_from_the_Tra.html?id=qsY-AAAAYAAJ](https://books.google.com/books/about/Scientific_Memoirs_Selected_from_the_Tra.html?id=qsY-AAAAYAAJ).
[^15]: Ada Lovelace, “Translator’s Notes to M. Menabrea’s Memoir,” Scientific Memoirs 3 (1843): 712, accessed August 18, 2018, [https://books.google.com/books/about/Scientific_Memoirs_Selected_from_the_Tra.html?id=qsY-AAAAYAAJ](https://books.google.com/books/about/Scientific_Memoirs_Selected_from_the_Tra.html?id=qsY-AAAAYAAJ).
[^16]: Lovelace, 694.
[^17]: Menabrea, 690.
[^18]: “Bernoulli number,” Wikipedia, accessed August 18, 2018, <https://en.wikipedia.org/wiki/Bernoulli_number>.
[^19]: Isaacson, 29.
[^20]: Menabrea, 689.