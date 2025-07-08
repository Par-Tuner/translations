# Codecademy 对阵 BBC Micro

*2019 年 3 月 31 日*

在 20 世纪 70 年代末，计算机——几十年来一直是一种神秘庞大、只听命于企业巨头的机器——突然变成了普通人可以购买并带回家的东西。一小部分热情的先行者看到了这有多么伟大，并争相购买自己的计算机。然而，对更多人来说，微型计算机 (microcomputer) 的到来引发了对未来的无助焦虑。当时一本杂志上的一则广告承诺，家用计算机将“让你的孩子在学校里获得不公平的优势”。广告中，一个穿着考究西装和领带的男孩正兴致勃勃地举手回答问题，而他身后那些笨头笨脑的同学则在一旁闷闷不乐地看着。这则广告以及其他类似的广告暗示，世界正在迅速变化，如果你不立即学会使用这些令人生畏的新设备，你和你的家人就会落后于时代。

在英国，这种焦虑在政府最高层演变成了对国家竞争力的担忧。总的来说，20 世纪 70 年代对大不列颠而言是令人失望的十年。通货膨胀和失业率居高不下。与此同时，一系列罢工导致伦敦屡次停电。1979 年的一份政府报告担心，未能跟上计算机技术的发展趋势将“进一步加剧我们糟糕的工业表现” [^1]。这个国家在计算机领域似乎已经落后了——所有伟大的计算机公司都是美国公司，而集成电路 (integrated circuits) 则在日本和中国台湾组装。

英国广播公司 (BBC) 是一家由政府资助的公共服务广播机构，它采取了一个大胆的举动，决定通过帮助英国各地的人们克服他们对计算机的厌恶来解决英国的国家竞争力问题。它启动了“计算机素养项目” (Computer Literacy Project)，这是一项多管齐下的教育项目，包括多个电视系列节目、几本书、一个支持小组网络，以及一台专门制造的微型计算机，名为 BBC Micro。该项目非常成功，以至于到 1983 年，《BYTE 杂志》的一位编辑写道：“与美国相比，英国对微型计算机感兴趣的人口比例更高” [^2]。这位编辑惊叹，在英国第五届个人计算机世界展上的人数，比当年西海岸计算机博览会 (West Coast Computer Faire) 的人数还要多。超过六分之一的英国人观看了“计算机素养项目”制作的第一个系列节目中的一集，最终售出了 150 万台 BBC Micro [^3]。

去年，一个包含“计算机素养项目”制作的所有电视系列节目和出版的所有材料的 [档案库](https://computer-literacy-project.pilots.bbcconnectedstudio.co.uk/) 被放到了网上。我观看这些电视节目，并试图想象在 20 世纪 80 年代初期学习计算机是怎样一番体验，这给我带来了乐趣无穷。但更有趣的是计算机是如何被*教授*的。今天，我们仍然担心技术会让人掉队。富有的科技企业家和政府投入大量资金，试图教孩子们“编程”。我们有像 Codecademy 这样的网站，它们利用新技术以交互方式教授编程。人们可能会认为这种方法比傻乎乎的 80 年代电视节目更有效。但事实真是如此吗？

## 计算机素养项目

微型计算机革命始于 1975 年 Altair 8800 的发布 [https://twobithistory.org/2018/07/22/dawn-of-the-microcomputer.html]。仅仅两年后，Apple II、TRS-80 和 Commodore PET 都已发布。新计算机的销量猛增。1978 年，BBC 在一部名为《芯片危机》(Now the Chips Are Down) 的纪录片中探讨了这些新机器必然会带来的巨大社会变革。

这部纪录片令人警醒。在开场五分钟内，旁白就解释说，微电子技术 (microelectronics) 将“彻底改变我们的生活方式”。随着诡异的合成器音乐响起，屏幕上，绿色的电流脉冲在一个放大的微处理器 (microprocessor) 周围跳动，旁白指出，这些新芯片是“日本放弃造船业，以及我们的孩子长大后会找不到工作”的原因。纪录片接着探讨了机器人如何被用于自动化汽车组装，以及欧洲钟表业如何输给了美国的数字手表制造商。它严厉批评英国政府未能为国家的大规模失业未来做好更多准备。

这部纪录片据称曾向英国内阁 (British Cabinet) 展示 [^4]。包括工业部 (Department of Industry) 和人力服务委员会 (Manpower Services Commission) 在内的几个政府机构开始对提高英国公众对计算机的认识感兴趣。人力服务委员会资助了 BBC 教育部门的一个团队前往日本、美国和其他国家进行考察之旅 (fact-finding trip)。这个研究团队制作了一份报告，详细列举了微电子技术将如何确实给工业制造 (industrial manufacturing)、劳资关系 (labor relations) 和办公室工作 (office work) 带来重大变革。1979 年末，BBC 决定制作一个十集电视系列节目，帮助普通英国人“学习如何使用和控制计算机，而不是被它们所支配” [^5]。该项目最终成为一个多媒体项目 (multimedia endeavor)，类似于 BBC 早期的“成人扫盲项目” (Adult Literacy Project)，后者也包括一个电视系列节目和补充课程 (supplemental courses)，帮助两百万人提高了阅读能力。

“计算机素养项目”的制片人热衷于让电视节目包含“实践操作”示例 (hands-on examples)，如果观众家里有微型计算机，他们可以自己尝试。这些示例必须使用 BASIC 语言 (BASIC)，因为那是几乎所有微型计算机上使用的语言（实际上是整个外壳 (shell)）。但制片人面临一个棘手的问题：微型计算机制造商都有自己的 BASIC 语言方言 (dialects of BASIC)，所以无论他们选择哪种方言，都不可避免地会疏远相当一部分观众。唯一的真正解决方案是创建一个新的 BASIC 语言——BBC BASIC，并配套一台微型计算机。英国公众将能够购买这台新的微型计算机，并无需担心软件或硬件差异，即可跟着学习。

BBC 的电视制片人和主持人无法独立制造微型计算机。因此，他们为心目中的计算机制定了一份规格说明，并邀请英国微型计算机公司提出符合要求的新机器方案。这份规格说明要求一台相对强大的计算机，因为 BBC 制片人认为这台机器应该能够运行真实、有用的应用程序。 “计算机素养项目”的技术顾问 (Technical consultants) 也建议，如果向全国教授一种 BASIC 语言方言，那它最好是优秀的。（他们可能没有完全那样措辞，但我敢打赌他们是那样想的。）BBC BASIC 将通过允许递归 (recursion) 和局部变量 (local variables) 来弥补 BASIC 语言的一些常见缺点 [^6]。

BBC 最终决定由一家名为 Acorn Computers 的剑桥公司制造 BBC Micro。在选择 Acorn 时，BBC 放弃了 Clive Sinclair 旗下 Sinclair Research 公司的提案。Sinclair Research 在 1980 年通过 Sinclair ZX80 将大众市场微型计算机 (mass-market microcomputing) 带到了英国。Sinclair 的新计算机 ZX81 价格便宜，但不够强大，无法满足 BBC 的要求。Acorn 的新原型计算机，内部代号为 Proton，将更昂贵但更强大且可扩展。BBC 对此印象深刻。Proton 从未以 Proton 的名义进行市场推广或销售，因为它于 1981 年 12 月以 BBC Micro 的名义发布，也被亲切地称为“小蜜蜂” (The Beeb)。你可以花 235 英镑购买 16k 版本，花 335 英镑购买 32k 版本。

1980 年，Acorn 在英国计算机行业中处于劣势。但 BBC Micro 帮助奠定了公司的传承。如今，世界上最流行的微处理器指令集 (microprocessor instruction set) 是 ARM 架构 (ARM architecture)。“ARM”现在代表“高级精简指令集计算机” (Advanced RISC Machine)，但最初它代表“Acorn 精简指令集计算机” (Acorn RISC Machine)。ARM Holdings 这家公司是该架构的幕后推手，于 1990 年从 Acorn 分拆出来。

![BBC Micro 的图片。](https://twobithistory.org/images/beeb.jpg)
*一张糟糕的 BBC Micro 照片，由我在加利福尼亚州山景城的计算机历史博物馆拍摄。*

## 计算机节目

“计算机素养项目”最终制作了十几个不同的电视系列节目，其中第一个是名为《计算机节目》(The Computer Programme) 的十集系列节目。该系列节目于 1982 年初连续十周播出。每周有 100 万人观看工作日晚间的节目；25 万人观看周日和周一下午的重播。

该节目由两位主持人 Chris Serle 和 Ian McNaught-Davis 主持。Serle 扮演新手 (neophyte)，而拥有大型机 (mainframe computers) 编程专业经验的 McNaught-Davis 则扮演专家 (expert)。这是一个巧妙的设置。它导致了 [尴尬的过渡](https://twitter.com/TwoBitHistory/status/1112372000742404098)——Serle 经常直接从与 McNaught-Davis 的对话转变为对着镜头进行边走边说 (walk-and-talk) 的旁白，你禁不住会想 McNaught-Davis 是不是还在镜头外站着。但这确实意味着 Serle 可以说出观众肯定会有的疑虑。他可以面对满屏的 BASIC 语言代码显得不知所措，也可以问出“这些美元符号都代表什么？”这样的问题。在节目中的几个环节，Serle 和 McNaught-Davis 坐在计算机前，基本上是结对编程 (pair program)，McNaught-Davis 不时提供一些提示，而 Serle 则努力弄明白。如果节目由一个单一的、无所不知的旁白者来呈现，那么亲和力会大打折扣。

该节目还努力展示计算机在普通人生活中的诸多实际应用 (practical applications)。到 20 世纪 80 年代初，家用计算机已经开始与小男孩和视频游戏联系在一起。《计算机节目》的制片人试图避免采访“能力超群的年轻人”，因为那很可能会“增加年长观众的焦虑”，而这正是该节目试图吸引到计算机领域的人群 [^7]。在该系列节目的第一集中，节目的“外景记者” Gill Nevill 采访了一位购买了 Commodore PET 来帮助经营糖果店的女士。这位女士（她叫 Phyllis）看起来六十多岁，但她毫不费力地使用计算机进行会计工作，甚至开始使用她的 PET 计算机为其他企业提供计算机服务，这听起来像是一个有前途的自由职业生涯的开端。Phyllis 说，如果计算机工作发展到取代她的糖果店生意，她也不会介意，因为她更喜欢计算机工作。这次采访本可以是对一个青少年关于他如何修改《打砖块》(Breakout) 游戏使其更快、更具挑战性的采访。但这几乎不会激励任何人。另一方面，如果连 Phyllis 这样的人都能使用计算机，那么你肯定也能。

虽然节目中有很多 BASIC 语言编程的内容，但它真正想教给观众的是计算机的普遍工作原理。节目通过类比 (analogies) 解释这些普遍原理。在第二集中，对提花织机 (Jacquard loom) 进行了深入讨论，这实现了两个目的。首先，它说明计算机并非仅仅基于昨天才发明的神奇技术——计算的一些基本原理可以追溯到两百年前，并且就像在卡片上打孔来控制织布机一样简单。其次，经线和纬线 (warp and weft threads) 的交织被用来展示当一个二进制选择 (binary choice)（纬线是穿过经线上方还是下方？）反复重复时，如何足以产生巨大的变化。当然，这自然引出了关于如何使用二进制数字 (binary digits) 存储信息的讨论。

节目后面有一个关于蒸汽风琴 (steam organ) 的部分，它演奏着编码在长长的分段穿孔卡片 (punched card) 卷上的音乐。这次的类比被用来解释 BASIC 语言中的子程序 (subroutines)。Serle 和 McNaught-Davis 在演播室的地板上铺开整卷穿孔卡片，然后指出那些看起来像副歌重复出现的片段。McNaught-Davis 解释说，子程序就是如果你剪掉那些重复的卡片片段，然后以某种方式添加一条指令，让程序回到第一次播放副歌的原始片段，你就会得到的东西。这是一个绝妙的解释，很可能长期留在人们的脑海中。

我只挑选了几个例子，但我认为总的来说，该节目通过解释计算机赖以运行的原理，出色地揭开了计算机的神秘面纱 (demystifying computers)。该节目本可以专注于教授 BASIC 语言，但它没有。事实证明，这是一个非常有意识的选择。在 1983 年撰写的一篇回顾性文章中，“计算机素养项目”的执行制片人 (executive producer) John Radcliffe 写道：

> 如果计算机像我们相信的那样重要，那么对这门新学科的真正理解对每个人都很重要，也许就像读写能力一样重要。早期的想法，无论是在这里还是在美国，都将编程视为实现计算机素养 (computer literacy) 的主要途径。然而，随着我们思维的不断深入，尽管我们认识到在个人微型计算机上进行“实践操作”的价值，但我们开始减少对编程的强调，更多地关注更广泛的理解，将微型计算机与大型机器联系起来，鼓励人们获得使用各种应用程序和高级语言的经验，并将这些与工业和商业的现实世界经验联系起来……我们相信，一旦人们掌握了这些最简单的原理，他们就能在这门学科上走得更远。

后来，Radcliffe 以类似的口吻写道：

> 关于该系列节目的主要解释方向曾有过很多争论。一种观点认为，节目特别重要的是要提供学习使用微型计算机的实用细节建议。但我们得出的结论是，如果该系列节目要具有任何持续的教育价值，它就必须通过对计算原理的解释，成为进入真实计算机世界的方式。这需要通过结合在微型计算机上的演播室演示、通过类比解释原理，以及通过影片展示实际应用的真实案例来实现。不仅会展示微型计算机，还会展示小型计算机 (mini computers) 和大型机 (mainframes)。

我喜欢这一点，特别是关于小型计算机和大型机的那部分。《计算机节目》的制片人旨在帮助英国人了解情况：计算技术过去是怎样的，未来又将走向何方？计算机现在能做什么，未来又可能做什么？学习一些 BASIC 语言是回答这些问题的一部分，但单独掌握 BASIC 语言不足以使人具备计算机素养。

## 今天的计算机素养

如果你在谷歌上搜索“学习编程”，第一个结果就是 Codecademy 的网站链接。如果说现代有什么与“计算机素养项目”具有相同的覆盖范围和类似目标，那它就是 Codecademy。

“学习编程”是 Codecademy 的标语。我想我不是第一个指出这一点的人——事实上，我可能是在某个地方读到过，现在只是在“剽窃”它——但使用“代码”而非“程序”这个词，揭示了一些东西。它暗示你正在学习的重要事情是如何解码代码，是如何看到满屏的 Python 代码时不会两眼发直。我能理解为什么对普通人来说，这似乎是成为专业程序员的主要障碍。专业程序员整天盯着满是乱码 (gobbledygook) 的计算机显示器，所以，如果我想成为专业程序员，我最好确保我能解读这些乱码。但处理语法并非程序员最具挑战性的部分，面对更大的障碍时，它很快就变得几乎无关紧要。此外，仅仅掌握编程语言的语法知识，你或许能*读懂*代码，但你无法*编写*代码来解决一个新问题。

我最近学习了 Codecademy 的“代码基础” (Code Foundations) 课程，如果你对编程感兴趣（而不是网页开发 (web development) 或数据科学 (data science)），并且从未有过编程经验，该网站会推荐你学习这门课程。课程中确实有一些关于计算机科学历史的课程，但它们敷衍了事且研究不足。（感谢 [这位高尚的互联网义警](https://twitter.com/TwoBitHistory/status/1111305774939234304)，他指出了一个特别严重的错误。）课程的主要重点是教授编程语言的常见结构元素 (structural elements of programming languages)：变量 (variables)、函数 (functions)、控制流 (control flow) 和循环 (loops)。换句话说，课程的重点是让你了解在乱码中发现模式所需知道的一切。

公平地说，Codecademy 也提供其他看起来更充实的课程。但即使是像他们的“计算机科学路径” (Computer Science Path) 课程，也几乎完全专注于编程以及可以在程序中表示的概念。有人可能会争辩说，这正是其核心目的——Codecademy 的主要特点是提供带有自动反馈的交互式编程小课程。而且也没有足够的空间涵盖更多内容，因为在一个简短的自动化课程中，能塞进别人大脑的信息量是有限的。但 BBC 负责启动“计算机素养项目”的制片人也面临这个问题；他们认识到自己受限于媒介，“电视节目本身带来的学习量将是有限的” [^8]。在传递信息量方面有类似限制的情况下，他们选择强调普遍原理而非学习 BASIC 语言。Codecademy 难道不能用提花织机交织经线和纬线的交互式可视化演示 (interactive visualization) 来取代一两节课吗？

我现在正在大声疾呼“普遍原理”的重要性，所以让我解释一下我认为它们是什么以及为什么它们很重要。J. Clark Scott 有一本关于计算机的书，名为《它怎么知道的？》(But How Do It Know?)。书名来源于书中开篇的轶事。一位推销员向一群人解释说，保温瓶能让热食保持热，冷食保持冷。一位观众对这项新发明感到震惊，问道：“但它怎么知道的？”当然，这个笑话在于保温瓶并非感知食物温度然后做出决定——保温瓶的构造就是如此，冷食必然保持冷，热食必然保持热。人们以同样的方式将计算机拟人化 (anthropomorphize)，认为计算机是某种程度上“选择”根据输入代码执行某项操作的数字大脑 (digital brains)。但即使是初步了解计算机的工作原理，也能将机器中的“小人” (homunculus) 移除。这就是为什么提花织机是一个很好的首选示例。它乍一看可能像一个不可思议的设备。它读取穿孔卡片，然后“知道”如何织出正确的图案！现实是平淡无奇的：每排孔对应一根线，该排有孔的地方，对应的线就会被提起。理解这一点可能不会帮助你用计算机做任何新事情，但它会让你相信你所处理的并非某种魔法。我们应该尽快将这种自信传授给初学者。

唉，真正的问题可能在于没有人想了解提花织机。从 Codecademy 强调其所教授内容的专业应用来看，许多人可能开始使用 Codecademy 是因为他们相信它能帮助他们“提升”职业生涯。他们并非不合理地认为，主要挑战将是理解那些乱码，所以他们想“学习编程”。而且他们想尽可能快地学习，利用他们每晚晚饭后到倒头睡觉前的一两个小时。Codecademy 毕竟是一家商业公司，它提供了这些人所寻找的东西——而不是某种涉及 18 世纪发明的机器的迂回解释。

另一方面，“计算机素养项目”是 BBC 的一群制片人和公务员认为教育全国人民了解计算机的最佳方式。我承认，建议我们应该赞扬这群人教导大众他们自己无法探寻到的知识，这听起来有点精英主义。但我忍不住认为他们做对了。许多人最初通过 BBC Micro 学习计算机，其中许多人后来成为了成功的软件开发者 (software developers) 或游戏设计师 (game designers)。 [正如我之前所写](https://twobithistory.org/2018/09/02/learning-basic.html)，我怀疑在计算机相对简单的时代学习计算机是一个巨大的优势。但也许这些人拥有的另一个优势是像《计算机节目》这样的节目，它不仅努力教授编程，还教授计算机如何以及为何能够运行程序。观看《计算机节目》后，你可能无法理解计算机屏幕上的所有乱码，但你并不真的需要理解，因为你知道，无论“代码”看起来如何，计算机总是在做同样的基本事情。而在 Codecademy 上完成一两门课程后，你理解了某些类型的乱码，但对你来说，计算机只是一台神奇的机器，它能以某种方式将乱码变成运行的软件。那不是计算机素养。

*如果你喜欢这篇文章，每四周会有更多类似的文章发布！关注 Twitter 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS feed](https://twobithistory.org/feed.xml)，确保你不会错过新文章。*

*TwoBitHistory 往期回顾…*

> FINALLY some new damn content, amirite?
>
> Wanted to write an article about how Simula bought us object-oriented programming. It did that, but early Simula also flirted with a different vision for how OOP would work. Wrote about that instead!<https://t.co/AYIWRRceI6>
>
> — TwoBitHistory (@TwoBitHistory) [February 1, 2019](https://twitter.com/TwoBitHistory/status/1091148050221944832?ref_src=twsrc%5Etfw)

[^1]: Robert Albury and David Allen, Microelectronics, report (1979).
[^2]: Gregg Williams, “Microcomputing, British Style”, Byte Magazine, 40, January 1983, accessed on March 31, 2019, [https://archive.org/stream/byte-magazine-1983-01/1983_01_BYTE_08-01_Looking_Ahead#page/n41/mode/2up](https://archive.org/stream/byte-magazine-1983-01/1983_01_BYTE_08-01_Looking_Ahead#page/n41/mode/2up).
[^3]: John Radcliffe, “Toward Computer Literacy,” Computer Literacy Project Achive, 42, accessed March 31, 2019, [https://computer-literacy-project.pilots.bbcconnectedstudio.co.uk/media/Towards Computer Literacy.pdf](https://computer-literacy-project.pilots.bbcconnectedstudio.co.uk/media/Towards%20Computer%20Literacy.pdf).
[^4]: David Allen, “About the Computer Literacy Project,” Computer Literacy Project Archive, accessed March 31, 2019, [https://computer-literacy-project.pilots.bbcconnectedstudio.co.uk/history](https://computer-literacy-project.pilots.bbcconnectedstudio.co.uk/history).
[^5]: ibid.
[^6]: Williams, 51.
[^7]: Radcliffe, 11.
[^8]: Radcliffe, 5.