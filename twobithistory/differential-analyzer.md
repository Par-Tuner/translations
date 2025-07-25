# 如何使用微分分析机 (来杀人)

*2020 年 4 月 6 日*

微分分析机 (Differential Analyzer) 是一种机械式模拟计算机 (Mechanical, Analog Computer)，能够求解微分方程 (Differential Equations)。如今，微分分析机已不再使用，因为即使是一台廉价的笔记本电脑也能更快地求解相同的方程——而且你还能一边在 HBO 上观看《西部世界》新一季，一边让它在后台运行。然而，在数字计算机 (Digital Computers) 发明之前，微分分析机让数学家们能够进行一些否则根本不切实际的计算。

在今天看来，很难想象一台不是由硅基数字电路构成的计算机是如何工作的。机械式计算机听起来就像是蒸汽朋克小说里的东西。但微分分析机确实有效，甚至被证明是许多研究领域不可或缺的工具。最著名的是，美国陆军曾使用微分分析机来计算其火炮的射程表。即使是最大的火炮，如果没有射程表来帮助瞄准，也无法发挥作用，因此可以说，微分分析机在帮助同盟国赢得第二次世界大战中发挥了重要作用。

要理解微分分析机是如何做到这一切的，你需要知道什么是微分方程。忘了它们是什么了吗？没关系，因为我也忘了。

## 微分方程

微分方程是你可能在大学水平的微积分 I 课程的最后几周首次遇到的概念。到学期末，你那薪水不高的兼职教授会教你极限、导数和积分；如果你把这些概念结合起来，再加上一个等号，你就得到了一个微分方程。

微分方程描述的是某个变量 (或多个变量) 的变化率。一个熟悉的代数表达式，比如 \\(y \= 4x \+ 3\\)，表示变量 \\(y\\) 和变量 \\(x\\) 之间的关系，而一个微分方程，可能看起来像 \\(\\frac{dy}{dx} \= x\\)，甚至 \\(\\frac{dy}{dx} \= 2\\)，则表示一个 *变化率* 与其他变量之间的关系。本质上，微分方程只是用精确的数学术语描述变化率。后面两个微分方程中的第一个表示：“变量 \\(y\\) 相对于 \\(x\\) 的变化率由 \\(x\\) 精确定义”，第二个则表示：“无论 \\(x\\) 是什么，变量 \\(y\\) 相对于 \\(x\\) 的变化率都精确地为 2。”

微分方程之所以有用，是因为在现实世界中，描述复杂系统如何从一个瞬间变化到下一个瞬间，通常比想出一个能描述系统在所有可能瞬间状态的方程更容易。因此，微分方程在物理学和工程学中被广泛使用。一个著名的微分方程是热方程，它描述了热量如何随时间在物体中扩散。要仅给定时间 \\(t\\) 就想出一个能完全描述物体内部热量分布的函数会很困难，但思考热量如何从一个时间扩散到下一个时间则不太可能让你的大脑变成一锅粥——靠近大量冷点的热点可能会变冷，靠近大量热点的冷点可能会变热，等等。因此，热方程，尽管它比上一段中的例子复杂得多，但同样只是对变化率的描述。它描述了物体上任何一点的温度如何随时间变化，具体取决于其温度与周围点的差异。

让我们考虑另一个例子，我认为这会使所有这些概念更具体。如果我站在真空中，将一个网球垂直向上抛，它会在我窒息之前落回地面吗？这种问题，以不那么戏剧化的方式提出，是我在高中物理课上被问到的那种问题，当时我只需要一些基本的牛顿运动方程就能解决。但让我们假设我暂时忘记了这些方程，只记得物体以恒定速率 \\(g\\) (大约 \\(10 \\;m/s^2\\)) 向地球加速。微分方程如何帮助我解决这个问题呢？

嗯，我们可以把我记得的关于高中物理的唯一一件事表达成一个微分方程。网球一旦离开我的手，就会以速率 \\(g\\) 向地球加速。这等同于说球的速度会随时间以速率 \\(g\\) (负方向) 变化。我们甚至可以更进一步说，*我的球离地高度的变化率* (这正是它的速度) 会随时间以负 \\(g\\) 的速率变化。我们可以将其写成以下形式，其中 \\(h\\) 代表高度，\\(t\\) 代表时间：

\\\[\\frac{d^2h}{dt^2} \= \-g\\]

这看起来与我们目前看到的微分方程略有不同，因为它是一个二阶微分方程 (Second-Order Differential Equation)。我们讨论的是变化率的变化率，正如你可能从自己的微积分教育中回忆起来的那样，这涉及到二阶导数。这就是为什么左侧表达式的某些部分看起来像是被平方了。但这个方程仍然只是表达了球以恒定加速度 \\(g\\) 向下加速的事实。

从这里开始，我有一个选择是使用微积分工具来求解微分方程。对于微分方程，这并不意味着找到一个满足关系的单一值或一组值，而是找到一个或一组函数。另一种思考方式是，微分方程告诉我们存在某个函数，其二阶导数是常数 \\(\-g\\)；我们想找到那个函数，因为它会告诉我们球在任何给定时间的高度。这个微分方程恰好很容易求解。通过这样做，我们可以重新推导出我忘记的基本运动方程，并轻松计算出球需要多长时间才能落回地面。

但大多数时候，微分方程很难求解。有时甚至无法求解。因此，鉴于我在大学时计算机科学课比微积分课更认真，我还有另一个选择：将我的微分方程作为模拟的基础。如果我知道网球的初始速度和加速度，那么我可以轻松编写一个小的循环 (for-loop)，也许是用 Python 编写的，它会逐秒迭代我的问题，并告诉我球在初始时间后的任何给定秒 \\(t\\) 的速度是多少。一旦完成，我可以调整我的循环，使其在每次迭代中也使用计算出的速度来更新球的高度。现在我可以运行我的 Python 模拟，并计算出球何时会落回地面。我的模拟不会完全精确，但如果我需要更高的精度，我可以减小时间步长。无论如何，我只是想弄清楚球是否会在我活着的时候落回地面。

这就是求解微分方程的数值方法 (Numerical Approach)。在大多数出现微分方程的领域中，实践中就是这样求解微分方程的。计算机在这里是不可或缺的，因为模拟的精度取决于我们能否在问题中进行数百万个微小步骤。手工完成这项工作显然容易出错且耗时。

那么，如果我不是仅仅站在真空中拿着一个网球，而是站在真空中拿着一个网球，比如说，在 1936 年呢？我仍然想自动化我的计算，但 Claude Shannon 甚至还要一年才能完成他的硕士论文 (那篇论文中他随意地使用电子电路实现了布尔代数)。恐怕没有数字计算机，我们只能转向模拟方式了。

## 微分分析机

第一台微分分析机于 1928 年至 1931 年间由 Vannevar Bush 和 Harold Hazen 在麻省理工学院 (MIT) 建造。两人都是工程师。这台机器是为了解决应用数学和物理学中的实际问题而创建的。它旨在解决 Bush 在 1931 年一篇关于该机器的论文中描述的当代数学家所面临的问题，即他们“不断地被所用方程的复杂性而非其深奥性所阻碍”。

微分分析机是一种由杆、齿轮和旋转盘组成的复杂装置，可以求解高达六阶的微分方程。从这个角度看，它就像一台数字计算机，数字计算机也是由简单部件组成的复杂装置，但不知何故能汇聚成一台能做惊人事情的机器。但数字计算机的电路实现的是布尔逻辑，然后用于模拟任意问题，而微分分析机的杆、齿轮和旋转盘则 *直接* 模拟微分方程问题。这就是微分分析机成为模拟计算机的原因——它是真实问题的直接机械模拟。

齿轮和旋转盘到底是如何进行微积分运算的呢？这实际上是这台机器最容易解释的部分。微分分析机中最重要的组件是六个机械积分器 (Mechanical Integrator)，一个用于六阶微分方程中的每个阶。机械积分器是一种相对简单的设备，可以对单个输入函数进行积分；机械积分器可以追溯到 19 世纪。我们想了解它们是如何工作的，但顺便说一句，Bush 的巨大成就不是发明了机械积分器，而是找到了一种将积分器串联起来以求解高阶微分方程的实用方法。

一个机械积分器由一个大的旋转盘和一个小得多的旋转轮组成。圆盘平放在地面上，就像唱片机的转盘一样。它由一个马达驱动，以恒定速度旋转。小轮悬挂在圆盘上方，轻轻地搁在圆盘表面上——压力足以让圆盘带动小轮转动，但又不足以让小轮无法在圆盘表面上自由侧向滑动。因此，当圆盘转动时，小轮也随之转动。

小轮转动的速度将取决于小轮相对于圆盘中心的位置。当然，圆盘的内部部分比外部部分旋转得慢。小轮保持固定位置，但圆盘安装在一个可以沿一个方向来回移动的滑架上，这会重新定位小轮相对于圆盘中心的位置。现在，这就是积分器工作原理的关键：圆盘滑架的位置由积分器的输入函数驱动。积分器的输出由小轮的旋转决定。因此，你的输入函数驱动了你的输出函数的变化率，而你刚刚将某个函数的导数转换成了函数本身——这就是我们所说的积分！

如果这个解释对你没有帮助，那么亲眼看到机械积分器工作会非常有帮助。其原理出奇地简单，你不可能在不理解其工作原理的情况下观看该设备运行。因此，我创建了一个 [运行中的机械积分器的可视化](https://sinclairtarget.com/differential-analyzer/)，我鼓励你去看一看。该可视化展示了函数 \\(f(x)\\) 如何积分成其反导数 \\(F(x)\\)，同时各种部件旋转和移动。这相当令人兴奋。

![](https://twobithistory.org/images/diff-analyzer-viz.png)
*这是我的可视化工具的一个漂亮截图，但你真的应该去看看实物！*

所以我们有了一个可以为我们进行积分的组件，但这本身不足以求解微分方程。为了向你解释整个过程，我将使用 Bush 在他 1931 年的论文中自己提供的一个例子，这个例子恰好与我们之前讨论微分方程时考虑的例子基本相同。(这是一个愉快的巧合！) Bush 引入了以下微分方程来表示落体的运动：

\\\[\\frac{d^2x}{dt^2} \= \-k\\,\\frac{dx}{dt} \- g\\]

这与我们用来模拟网球运动的方程相同，只是 Bush 用 \\(x\\) 代替了 \\(h\\)，并添加了另一个项来解释空气阻力如何使球减速。这个新项以最简单的方式描述了空气阻力对球的影响：空气会以与球速度成比例的速率减慢球的速度 (这里的 \\(k\\) 是一个比例常数，我们不太关心它的值)。因此，当球移动得越快，空气阻力就越强，进一步减慢球的速度。

要配置微分分析机来求解这个微分方程，我们必须从 Bush 所谓的“输入台” (Input Table) 开始。输入台只是一张安装在滑架上的绘图纸。如果我们要尝试求解一个更复杂的方程，机器的操作员会首先在绘图纸上绘制我们的输入函数，然后，一旦机器开始运行，就使用连接到机器其余部分的指针描绘出该函数。然而，在这种情况下，我们的输入只是常数 \\(g\\)，所以我们只需要将指针移动到正确的值，然后将其留在那里。

那么其他变量 \\(x\\) 和 \\(t\\) 呢？变量 \\(x\\) 是我们的输出，因为它代表球的高度。它将被绘制在放置在输出台 (Output Table) 上的绘图纸上，输出台与输入台类似，只是指针是一支笔，由机器驱动。变量 \\(t\\) 应该只是以恒定速率前进。(在我们之前提出的网球问题的 Python 模拟中，我们只是在循环中递增 \\(t\\)。) 因此，变量 \\(t\\) 来自微分分析机的马达，马达通过以恒定速度旋转连接到它的杆来启动整个过程。

Bush 有一个有用的图表记录了所有这些，我稍后会向你展示，但首先我们需要对我们的微分方程进行一次调整，这将使图表更容易理解。我们可以对方程两边进行一次积分，得到以下结果：

\\\[\\frac{dx}{dt} \= \- \\int \\left(k\\,\\frac{dx}{dt} \+ g\\right)\\,dt\\]

这个方程中的项更好地映射到机器运行时各个部件旋转所代表的值。好的，这是那个图表：

![](https://twobithistory.org/images/analyzer-diagram.png)
*配置用于解决一维落体问题的微分分析机。*

输入台在图表的顶部。输出台在右下角。这里的输出台设置为同时绘制 \\(x\\) 和 \\(\\frac{dx}{dt}\\)，即高度和速度。积分器出现在左下角；由于这是一个二阶微分方程，我们需要两个。马达驱动最顶部的标有 \\(t\\) 的杆。(有趣的是，Bush 将这些水平杆称为“总线” (buses)。)

还有两个组件没有解释。标有小 \\(k\\) 的方框是一个乘法器 (Multiplier)，代表我们的比例常数 \\(k\\)。它接收标有 \\(\\frac{dx}{dt}\\) 的杆的旋转，并使用齿轮比将其放大或缩小。标有 \\(\\sum\\) 符号的方框是一个加法器 (Adder)。它使用巧妙的齿轮排列将两根杆的旋转相加，以驱动第三根杆。我们需要它，因为我们的方程涉及两个项的和。微分分析机中提供的这些额外组件确保了机器可以灵活地模拟包含各种项和系数的方程。

我发现以超慢动作思考马达启动后发生的因果级联很有帮助。马达立即开始以恒定速度旋转标有 \\(t\\) 的杆。因此，我们有了时间的概念。这根杆做了三件事，由连接到它的三根垂直杆所示：它驱动两个积分器中圆盘的旋转，并推动输出台的滑架前进，以便输出笔开始绘图。

现在，如果积分器设置成它们的轮子居中，那么杆 \\(t\\) 的旋转将不会导致其他杆旋转。积分器圆盘会旋转，但轮子，由于它们居中，将不会被驱动。输出图表将只显示一条平线。发生这种情况是因为我们没有考虑问题的初始条件。在我们之前的 Python 模拟中，我们需要知道球的初始速度，我们会在那里将其表示为常数变量或 Python 函数的参数。在这里，我们通过在机器开始运行之前将积分器圆盘位移适当的量来考虑初始速度和加速度。

一旦我们完成了这些，杆 \\(t\\) 的旋转就会通过整个系统传播。物理上，许多东西同时开始旋转，但我们可以认为旋转首先传到积分器 II，它将其与基于 \\(g\\) 计算的加速度表达式结合，然后进行积分以获得结果 \\(\\frac{dx}{dt}\\)。这代表了球的速度。速度反过来又作为积分器 I 的输入，积分器 I 的圆盘被位移，使得输出轮以 \\(\\frac{dx}{dt}\\) 的速率旋转。积分器 I 的输出是我们的最终输出 \\(x\\)，它直接路由到输出台。

我忽略了一个令人困惑的地方，那就是机器中存在一个循环：积分器 II 将标有 \\((k\\,\\frac{dx}{dt} \+ g)\\) 的杆的旋转作为输入，但该杆的旋转部分由积分器 II 本身的输出决定。这可能会让你感到不安，但这里没有物理问题——所有东西都在同时旋转。如果说有什么的话，我们不应该对看到这样的循环感到惊讶，因为微分方程通常将函数的变化率描述为函数本身的函数。(在这个例子中，加速度，即速度的变化率，取决于速度。)

一切配置正确后，我们得到的输出是一个漂亮的图表，绘制了球随时间的位置和速度。这个图表是在纸上的。对于我们现代的数字思维来说，这可能显得荒谬。一张纸质图表能做什么呢？虽然微分分析机确实没有那么神奇，无法为我们的问题写出整洁的数学表达式，但值得记住的是，许多微分方程本来就不可能得到整洁的解析解。机器绘制出的纸质图表包含了与我们之前对落体进行的 Python 模拟所能输出的完全相同的信息：球在任何给定时间的位置。它可以用来回答你可能对该问题提出的任何实际问题。

微分分析机是一台极其酷的机器。它很复杂，但其基本原理无非是旋转的杆和齿轮。你不需要是电气工程师，也不需要知道如何制造微芯片，就能理解其中涉及的所有物理过程。然而，这台机器却能进行微积分运算！它能求解你凭自己永远无法求解的微分方程。微分分析机证明了构建一台有用计算机器所需的关键材料不是硅，而是人类智慧。

## 杀人利器

人类的智慧可以服务于善，也可以服务于恶。正如我所提到的，历史上微分分析机最引人注目的用途是为美国陆军计算火炮射程表。就第二次世界大战是“正义之战”而言，这可能是有益的。但我们也不能否认，微分分析机确实帮助大型火炮更有效地杀死了大量人员。而且它们确实杀死了大量人员——如果维基百科可信的话，第二次世界大战期间被火炮杀死士兵的数量比被轻武器杀死的多。

我稍后会回到道德说教的话题，但这里先快速绕道解释一下为什么计算射程表很困难以及微分分析机是如何提供帮助的，因为看到微分分析机如何应用于实际问题是件好事。射程表告诉操作火炮的炮兵如何抬高炮管才能达到一定的射程。生成射程表的一种方法可能是多次以不同仰角发射特定类型的火炮并记录结果。这在马里兰州的阿伯丁试验场 (Aberdeen Proving Ground) 等试验场进行过。但仅仅通过这种经验观察来生成射程表既昂贵又耗时。而且，如果不以组合方式增加必要的射击次数到无法管理的地步，也无法考虑天气或其他因素，或者不同弹丸重量的影响。因此，使用数学理论，基于少量观察到的射击来填充完整的射程表，是一种更好的方法。

我不想深入探讨这些数学理论是如何工作的，因为数学很复杂，我也不太懂。但正如你可能想象的那样，控制炮弹飞行运动的物理学与控制向上抛掷的网球运动的物理学并没有太大不同。对精度的需求意味着所使用的微分方程必须偏离我们一直在使用的理想化形式，并迅速变得复杂。即使是最初尝试制定严谨的弹道学 (Ballistics) 理论，也涉及考虑弹丸的重量、直径和形状、盛行风、海拔、大气密度以及地球自转等因素的方程 [^1]。

所以这些方程很复杂，但它们仍然是微分方程，微分分析机可以像我们已经看到的那样进行数值求解。微分分析机于 1935 年在阿伯丁试验场投入使用，用于求解弹道方程，极大地加快了射程表的计算过程 [^2]。然而，在第二次世界大战期间，对射程表的需求增长如此之快，以至于美国陆军无法足够快地计算它们，以配合所有运往欧洲的武器。这最终导致陆军资助了宾夕法尼亚大学的 ENIAC 项目，该项目根据你的定义，生产了世界上第一台数字计算机。ENIAC 可以通过重新布线运行任何程序，但它主要是为了比微分分析机快许多倍地执行射程表计算而建造的。

鉴于射程表问题甚至在微分分析机之外也推动了早期计算历史的很大一部分，也许单独挑出微分分析机进行道德上的纠结是不公平的。微分分析机并非因其军事应用而独一无二地受到损害——整个计算领域，在第二次世界大战期间以及之后很长一段时间，都因为美国军方投入的无尽资金而得以发展。

无论如何，我认为微分分析机更有趣的遗产在于它教会我们计算的本质。我很惊讶微分分析机能完成如此多的工作；我猜你也是。人们很容易陷入一种误区，认为计算是只能通过非常快的数字电路来实现的领域。事实上，计算是一个更抽象的过程，而电子数字电路只是我们通常用来完成它的工具。Vannevar Bush 在他关于微分分析机的论文中指出，他的发明只是“利用复杂的机械相互关系来替代错综复杂的推理过程”这一深远项目的一小部分贡献。这说得真好。

*如果你喜欢这篇文章，每四周会发布更多类似的文章！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 订阅](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> 你是否担心你的孩子在“BBS-ing”？你是否有邻居总是谈论他的“门禁游戏” (door games)？
>
> 在 VICE News 的这份特别报道中，我们将带你进入公告板系统 (bulletin board systems) 的简陋地下世界：<https://t.co/hBrKGU2rfB>
>
> — TwoBitHistory (@TwoBitHistory) [February 2, 2020](https://twitter.com/TwoBitHistory/status/1224014531778826240?ref_src=twsrc%5Etfw)

[^1]: Alan Gluchoff. “Artillerymen and Mathematicians: Forest Ray Moulton and Changes in American Exterior Ballistics, 1885\-1934\.” Historia Mathematica, vol. 38, no. 4, 2011, pp. 506–547\., <https://www.sciencedirect.com/science/article/pii/S0315086011000279>.
[^2]: Karl Kempf. “Electronic Computers within the Ordnance Corps,” 1961, accessed April 6, 2020, [https://ftp.arl.army.mil/\~mike/comphist/61ordnance/index.html](https://ftp.arl.army.mil/~mike/comphist/61ordnance/index.html).