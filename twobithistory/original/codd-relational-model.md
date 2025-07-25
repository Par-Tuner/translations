# Important Papers: Codd and the Relational Model

*29 Dec 2017*


It’s hard to believe today, but the relational database was once the cool new
kid on the block. In 2017, the relational model competes with all sorts of
cutting\-edge NoSQL technologies that make relational database systems seem
old\-fashioned and boring. Yet, 50 years ago, none of the dominant database
systems were relational. Nobody had thought to structure their data that way.
When the relational model did come along, it was a radical new idea that
revolutionized the database world and spawned a multi\-billion dollar industry.



The relational model was introduced in 1970\. Edgar F. Codd, a researcher at
IBM, published a
[paper](https://cs.uwaterloo.ca/~david/cs848s14/codd-relational.pdf) called “A
Relational Model of Data for Large Shared Data Banks.” The paper was a rewrite
of a paper he had circulated internally at IBM a year earlier. The paper is
unassuming; Codd does not announce in his abstract that he has discovered a
brilliant new approach to storing data. He only claims to have employed a novel
tool (the mathematical notion of a “relation”) to address some of the
inadequacies of the prevailing database models.


In 1970, there were two schools of thought about how to structure a database:
the hierarchical model and the network model. The hierarchical model was used
by IBM’s Information Management System (IMS), the dominant database system at
the time. The network model had been specified by a standards committee called
CODASYL (which also—random tidbit—specified COBOL) and implemented by several
other database system vendors. The two models were not really that different;
both could be called “navigational” models. They persisted tree or graph data
structures to disk using pointers to preserve the links between the data.
Retrieving a record stored toward the bottom of the tree would involve first
navigating through all of its ancestor records. These databases were fast (IMS
is still used by many financial institutions partly for this reason, see [this
excellent blog post](https://twobithistory.org/2017/10/07/the-most-important-database.html))
but inflexible. Woe unto those database administrators who suddenly found
themselves needing to query records from the bottom of the tree without having
an obvious place to start at the top.


Codd saw this inflexibility as a symptom of a larger problem. Programs using a
hierarchical or network database had to know about how the stored data was
structured. Programs had to know this because they were responsible for
navigating down this structure to find the information they needed. This was so
true that when Charles Bachman, a major pioneer of the network model, received
a Turing Award for his work in 1973, he gave a speech titled “[The Programmer
as
Navigator](https://pdfs.semanticscholar.org/f371/d196bf0e7b43df6dcbbc44de461925a21709.pdf).”
Of course, if programs were saddled with this responsibility, then they would
immediately break if the structure of the database ever changed. In the
introduction to his 1970 paper, Codd motivates the search for a better model by
arguing that we need “data independence,” which he defines as “the independence
of application programs and terminal activities from growth in data types and
changes in data representation.” The relational model, he argues, “appears to
be superior in several respects to the graph or network model presently in
vogue,” partly because, among other benefits, the relational model “provides a
means of describing data with its natural structure only.” By this he meant
that programs could safely ignore any artificial structures (like trees)
imposed upon the data for storage and retrieval purposes only.


To further illustrate the problem with the navigational models, Codd devotes
the first section of his paper to an example data set involving machine parts
and assembly projects. This dataset, he says, could be represented in existing
systems in at least five different ways. Any program \\(P\\) that is developed
assuming one of five structures will fail when run against at least three of
the other structures. The program \\(P\\) could instead try to figure out ahead of
time which of the structures it might be dealing with, but it would be
difficult to do so in this specific case and practically impossible in the
general case. So, as long as the program needs to know about how the data is
structured, we cannot switch to an alternative structure without breaking the
program. This is a real bummer because (and this is from the abstract) “changes
in data representation will often be needed as a result of changes in query,
update, and report traffic and natural growth in the types of stored
information.”


Codd then introduces his relational model. This model would be refined and
expanded in subsequent papers: In 1971, Codd wrote about ALPHA, a SQL\-like
query language he created; in another 1971 paper, he introduced the first three
normal forms we know and love today; and in 1972, he further developed
relational algebra and relational calculus, the mathematically rigorous
underpinnings of the relational model. But Codd’s 1970 paper contains the
kernel of the relational idea:



> The term *relation* is used here in its accepted mathematical sense. Given
> sets \\(S\_1, S\_i, ..., S\_n\\) (not necessarily distinct), \\(R\\) is a relation
> on these \\(n\\) sets if it is a set of \\(n\\)\-tuples each of which has its
> first element from \\(S\_1\\), its second element from \\(S\_2\\), and so on. We
> shall refer to \\(S\_j\\) as the \\(j\\)th *domain* of \\(R\\). As defined above,
> \\(R\\) is said to have *degree* \\(n\\). Relations of degree 1 are often called
> *unary*, degree 2 *binary*, degree 3 *ternary*, and degree \\(n\\) *n\-ary*.


Today, we call a *relation* a *table*, and a *domain* an *attribute* or a
*column*. The word “table” actually appears nowhere in the paper, though Codd’s
visual representations of relations (which he calls “arrays”) do resemble
tables. Codd defines several more terms, some of which we continue to use and
others we have replaced. He explains primary and foreign keys, as well as what
he calls the “active domain,” which is the set of all distinct values that
actually appear in a given domain or column. He then spends some time
distinguishing between a “simple” and a “nonsimple” domain. A simple domain
contains “atomic” or “nondecomposable” values, like integers. A nonsimple
domain has relations as elements. The example Codd gives here is that of an
employee with a salary history. The salary history is not one salary but a
collection of salaries each associated with a date. So a salary history cannot
be represented by a single number or string.


It’s not obvious how one could store a nonsimple domain in a multi\-dimensional
array, AKA a table. The temptation might be to denote the nonsimple
relationship using some kind of pointer, but then we would be repeating the
mistakes of the navigational models. Instead. Codd introduces normalization,
which at least in the 1970 paper involves nothing more than turning nonsimple
domains into simple ones. This is done by expanding the child relation so that
it includes the primary key of the parent. Each tuple of the child relation
references its parent using simple domains, eliminating the need for a
nonsimple domain in the parent. Normalization means no pointers, sidestepping
all the problems they cause in the navigational models.


At this point, anyone reading Codd’s paper would have several questions, such
as “Okay, how would I actually query such a system?” Codd mentions the
possibility of creating a universal sublanguage for querying relational
databases from other programs, but declines to define such a language in this
particular paper. He does explain, in mathematical terms, many of the
fundamental operations such a language would have to support, like joins,
“projection” (`SELECT` in SQL), and “restriction” (`WHERE`). The amazing thing
about Codd’s 1970 paper is that, really, all the ideas are there—we’ve been
writing `SELECT` statements and joins for almost half a century now.


Codd wraps up the paper by discussing ways in which a normalized relational
database, on top of its other benefits, can reduce redundancy and improve
consistency in data storage. Altogether, the paper is only 11 pages long and
not that difficult of a read. I encourage you to look through it yourself. It
would be another ten years before Codd’s ideas were properly implemented in a
functioning system, but, when they finally were, those systems were so obviously
better than previous systems that they took the world by storm.


*If you enjoyed this post, more like it come out every four weeks! Follow
[@TwoBitHistory](https://twitter.com/TwoBitHistory) on Twitter or subscribe to the
[RSS feed](https://twobithistory.org/feed.xml)
to make sure you know when a new post is out.*