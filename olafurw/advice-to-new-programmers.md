# 给新手程序员们的建议
原文：[Advice to new Programmers](http://olafurw.com/2019-01-27-programmer-advice/)

并不是每天都有学生向 709 个软件开发者寻求建议的机会的。

## 综述

在瑞典马尔摩有一所学校叫做 [The Game Assembly](https://www.thegameassembly.com/)。这所学校专注于游戏制作教学。编程、艺术及设计，无所不包。有一个最后一年在游戏工作室度过的三年项目。

因为我为一家[游戏公司](https://www.massive.se/)工作，我们被邀请向这些学生举办讲座。在过去几年间我曾数次做讲座，且非常荣幸得到此机会。

今年我开始向新来的学生们讲演。原计划为[面向对象编程的基础](https://speakerdeck.com/olafurw/the-basics-of-object-oriented-programming)，但我还有另一个想法。

为什么不联系 Twitter 并问他们对“易受影响的年轻人”有什么建议呢？

> 推特上的程序员你们好！
> 几天后我将会向一些易受影响的年轻人演讲
> 他们尚且处于学习的早期阶段，20 来岁的样子。
> 你最想给出什么建议呢？语言是未知的。
> 感谢转推
> （我会在幻灯片中引用你们，所以务必友善：）
> — Ólafur Waage (@olafurw) [January 21, 2019](https://twitter.com/olafurw/status/1087438169585434624?ref_src=twsrc%5Etfw)

我确实没料到能获得 700 余条回复。因为在这条推特与演讲之间只有两天，我并不能总结所有的智慧。但是我也在试着寻找获赞最多的与在游戏产业中工作的人。

但有着太多的数据被掩盖。我需要分析这些回复。

## 获得数据

刚开始我试着仅仅浏览 Twitter 上的时间线并复制文本。但显然，当一个讨论贴达到了一定规模时，Twitter 限制了你能看到的推文数。所以从数据集中我仅能得到 285 个回复。

接下来是使用 Twitter 开发者 API，虽然被限制严重，但允许更多的搜索粒度。

通过 Python 和 Tweepy 及请求间的 5 分钟睡眠，我能够从请求中得到 763 条直接回复于我的推文。这花了 **362 分钟**，或言 **6 个小时**。更短的睡眠时间可能也行，但我睡后留下它自己跑，所以也没多大关系。

```python
for page in tweepy.Cursor(api.search, q="to:olafurw", since_id='1087438169585434624', tweet_mode='extended').pages():
  repliesFile = open("replies.txt", "a")

  for tweet in page:
    repliesFile.write(tweet.in_reply_to_status_id_str + "\n")
    repliesFile.write(tweet.user.screen_name + "\n")
    repliesFile.write(tweet.id_str + "\n")
    repliesFile.write(tweet.full_text.encode("utf-8") + "\n")

    repliesFile.write("\n--==--\n")

  repliesFile.flush()
  repliesFile.close()

  time.sleep(300)
```

## 基本的分析

分析一个文本语料库是在教育领域之中的，且我对此了解不多，也没有时间来深入了解。但我想要强调一些尤为突出的事情。

### 编程是一个人类的领域

763 条推文中有 131 条在谈到其他人。**17.1%**

他们谈论了人类，团队，同事，朋友，同行。

这里是一些例子：

> [@tomjadams](https://twitter.com/tomjadams/status/1088336413827915776)
> 软件是一个团体运动

> [@mrdowden](https://twitter.com/mrdowden/status/1087882550964641792)
> 生活中最重要的事——及你总是在控制的——是你如何对待他人

> [@originalJonLowe](https://twitter.com/originalJonLowe/status/1087594133357760513)
> 在求知之旅中总是宽容、鼓励他人
> 抬举其他开发者，因为在最后的日子里，你是队伍的一部分
> 在成为一个“明星”之上，成为一个团队合作者，因为知识应被共享

> [@ccmccomb](https://twitter.com/ccmccomb/status/1087845662937546756)
> 在计算中永远不要忘了为怜悯之心寻求空间

### 编程是关于持续学习的

13 个回复字面上都是“永远不要停止学习”

763 条推文中的 82 个在某种意义上谈论了学习或实践。**10.7%**

下面是例子：

> [@iam_js_](https://twitter.com/iam_js_/status/1088153200371355650)
> 没有捷径，实践、实践及更多的实践

> [@curtisko](https://twitter.com/curtisko/status/1087725805982093312)
> 你有责任持续地学习与职业发展

> [@hedgeb](https://twitter.com/hedgeb/status/1087525264140234752)
> 即使你只比手册快了一页，你也能指导一些人并在他们的学习编程之路中提供帮助

> [@howbazaar](https://twitter.com/howbazaar/status/1087773774374522881)
> 你将会持续学习
> 你永不止步
> 变得更好需要练习
> 读书，读博客
> 别指望在六个月内变得伟大

### 编程有时会很吓人

许多回复也表达了这个。有许多东西需要你去学习，有许多东西你并不懂。看着领域内的专家也会使人畏缩。

27 条回复谈及错误或失败，29 条关于害怕

> [@jitterted](https://twitter.com/jitterted/status/1087575050318835712)
> 别与其他人相比较，而是与过去的 _你_ 相比较

> [@greberger](https://twitter.com/greberger/status/1087842355481325574)
> 不要害怕说你不懂什么东西
> 别对寻求帮助感到害怕
> 我们都曾（或正在）经历妄自菲薄

> [@ben_deane](https://twitter.com/ben_deane/status/1087805790423904256)
> 我们都会出错
> 试着对自己的错误负责而不惭愧，在他人出现错误时也不要责怪他们

> [@FiddlersCode](https://twitter.com/FiddlersCode/status/1087619274032721926)
> 技术是短暂的，但关系长存
> 感情上试着了解你的同事与你自己
> 有勇气接受你的努力会易受伤害
> 寻求帮助，即使你害怕出丑

### 编程不仅仅是最新的技术

对，闪亮的新库/语言/框架非常酷。但正如许多回复所言，基础原理更要紧。

34 条回复直接地谈论技术，算法及关注于更大的图景。

> [@bjorn_fahller](https://twitter.com/bjorn_fahller/status/1087439484709490689)
> 语言与工具来来去去。
> 学会去看重复的模式，更准确地说，不同语言与库甚至范例中的规律。
> 学习不同技术的优劣，如此你能为你的特定问题精确地选择。

> [@aras_p](https://twitter.com/aras_p/status/1087443639750529025)
> 找到编程领域中使你感兴趣的，并在此工作。
> 小的递增任务——“嘿我把屏幕变成红色的了！现在我又更进一步！”，“我使页面上的按键移动了！”等
> 语言、框架、库、“技术栈”并不重要（别理睬说这些重要的人）。

> [@rickschott](https://twitter.com/rickschott/status/1087492136331812867)
> 世界需要问题解决者，而非被记住的算法。

### 编程对你要求严苛

个人健康是一个普遍的讨论点。睡眠与合理饮食是有关健康行为中排在第一位的。

33 条回复谈论了睡眠，饮食，个人健康与工作时间。

> [@sehurlburt](https://twitter.com/sehurlburt/status/1087448744113684481)
> 睡觉，健康饮食，关心你自己的身体——即使你感觉良好
> 更多的工作时间并不意味着更好的工作，甚至并不意味着更多的工作被做完
> 你不必弄懂你的事业
> 你不需要生活的里程碑来仅仅变得健康与快乐

> [@caffodian](https://twitter.com/caffodian/status/1087449579589591044)
> 照顾好你的身体
> 对，实际编程技巧非常有用，但这能使你使用鼠标而不伤害自己，或久坐而不背疼，看着屏幕而不头疼，等等。

> [@ArvidGerstmann](https://twitter.com/ArvidGerstmann/status/1087462222551490560)
> 不要勉强自己。在你还能时，享受你该死的生活。来自一位 24 岁却感觉像是已经 44 岁的人。

> [@ma_lindstedt](https://twitter.com/ma_lindstedt/status/1087683256835809281)
> 每周工作 100 小时并不意味着你非常投入
> 照顾好你的身体，坦率地与管理者交谈
> 享受你的空闲时间，如此你能得到最棒的工作效率
> 兴趣爱好+朋友与良好的职业道德并不排斥

### 编程，其他有趣的回复

上述分类是寻常的主题，但也有无法归类但值得提及的回复。

30 条回复提及测试

> [@brianokken](https://twitter.com/brianokken/status/1088177245431115776)
> 学着去问这些问题：
> 
> * 我是如何知道它能跑起来的？
> * 我该如何使之自动化？
>   尽快学会依靠自动化测试会节省大量的时间

18 条回复谈论了某种版本控制

> [@UndefinedBehav](https://twitter.com/UndefinedBehav/status/1087441412747128832)
> 使用一个版本控制工具
> 如果某人曾在之前告诉我，我会喜欢它的

14 条提及调试

> [@AliBeeGfx](https://twitter.com/AliBeeGfx/status/1087826867363741696)
> 写代码经常像是测不准原理的对立
> 唯一去了解什么确定的东西 _真的_ 发生的方法是通过调试来近距离观察！

## 感谢

像这样的帖子难得一见。如此之多的人花费时间回复很不可思议

**感谢每一个回复、转推与点赞的人。**

我希望这个帖子能够鼓舞你，我也希望这篇博文能够有所帮助。

> [@ericniebler](https://twitter.com/ericniebler/status/1087447876286869504)
> 保持谦虚，保持好奇。