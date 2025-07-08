# 模拟 Altair

*2017 年 12 月 2 日*

[Altair 8800](https://en.wikipedia.org/wiki/Altair_8800) 是一款于 1975 年发布的自己动手组装的家用电脑套件。Altair 基本上算是第一台个人电脑，尽管它比“个人电脑”这个词的出现早了好几年。它是所有戴尔 (Dell)、惠普 (HP) 或 MacBook 的“亚当”或“夏娃”。

有人觉得为 Z80（一款与 Altair 的英特尔 (Intel) 8080 处理器 (processor) 密切相关的处理器）编写一个模拟器 (emulator) 会很棒，然后又觉得还需要在上面模拟 Altair 的控制面板 (control panel)。所以，如果你曾好奇在 1975 年使用电脑是什么感觉，现在你可以在你的 MacBook 上运行 Altair 了：

![Altair 8800](https://www.autometer.de/unix4fun/z80pack/altair.png)

### 安装它

你可以从[这里](http://www.autometer.de/unix4fun/z80pack/ftp/)提供的 FTP 服务器 (FTP server) 下载 Z80 pack。你需要寻找最新版的 Z80 pack，文件名类似 `z80pack-1.26.tgz`。

首先解压文件：

```
$ tar -xvf z80pack-1.26.tgz
```

进入解压后的目录：

```
$ cd z80pack-1.26
```

控制面板的模拟是基于一个名为 `frontpanel` 的库 (library)。你必须先编译这个库。如果你进入 `frontpanel` 目录，你会找到一个 `README` 文件，其中列出了该库自身的依赖项 (dependencies)。你的经历几乎肯定会与我不同，但也许我的经验能给你一些启发。我通过 [Homebrew](http://brew.sh/) 安装了这些依赖项。为了让库能够编译，我只需要确保将 `/usr/local/include` 添加到 `Makefile.osx` 中 Clang 的包含路径 (include path) 里。

如果你已经满足了依赖项，你应该就能编译这个库了（我们现在在 `z80pack-1.26/frontpanel` 目录下）：

```
$ make -f Makefile.osx ...
$ make -f Makefile.osx clean
```

你应该会得到 `libfrontpanel.so` 文件。我把它复制到了 `/usr/local/lib`。

Altair 模拟器 (simulator) 位于 `z80pack-1.26/altairsim` 目录下。现在你需要编译模拟器本身。进入 `z80pack-1.26/altairsim/srcsim` 目录，再次运行 `make`：

```
$ make -f Makefile.osx ...
$ make -f Makefile.osx clean
```

这个过程会在 `z80pack-1.26/altairsim` 目录下生成一个名为 `altairsim` 的可执行文件 (executable)。运行这个可执行文件，你就能看到那个标志性的 Altair 控制面板了！

如果你真的想深入钻研一下，可以阅读原始的 [Altair 手册](http://www.classiccmp.org/dunfield/altair/d/88opman.pdf)。

*如果你喜欢这篇文章，类似的更新每四周发布一次！关注推特 (Twitter) 上的 [@TwoBitHistory](https://twitter.com/TwoBitHistory) 或订阅 [RSS 订阅源](https://twobithistory.org/feed.xml)，确保你不会错过任何新文章。*