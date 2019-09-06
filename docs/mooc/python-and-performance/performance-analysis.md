<!-- Title: Where program spends time? -->

<!-- Short description:

Before a program can be optimized, one needs to find out the bottlenecks.
In this article we discuss some general principles when analysing performance.

-->

## Where program spends time?

Analyze before you optimize.

Some performance aspects can be considered already in early phases of
software development, but generally one should first focus on making the
program correct. In addition to correctness, readability and maintainability
of the program are very important, and one should try to make the program as
easy to understand as possible. Low-level optimization should be done only
after correctness and readability are taken care of, especially as low-level
optimization normally detracts readability. As stated by famous computer
scientist Donald Knuth already in the 70's:

> Programmers waste enormous amounts of time thinking about, or worrying about,
> the speed of noncritical parts of their programs, and these attempts at
> efficiency actually have a strong negative impact when debugging and
> maintenance are considered: premature optimization is the root of all evil.

However, once a program is working correctly, but performance limits its
usability (i.e. numerical simulation takes several days), one should try to
optimize the program. It is very typical that a program spents most of the
time only in a small part of the program as exemplified by the common
**90/10** rule: **90% of time is spent in 10% of the source code**. To
illustrate this rule, speeding up the 10% part by a factor of 1000 results
only in a 10% speed-up for the program, while speeding up the 90% part by a
factor of 10 gives a 500% speed-up. The actual ratios differ case by case, but
the general pattern is common.

Thus, it is clear that when optimizing one should focus only in the
time-critical parts of the program. How to find these hotspots is the task of
performance analysis. The two main ways to analyze performance are via
**applications own timers**, which measure the time spent in specific region
of a program, or by utilizing special **performance analysis software**.
Performance analysis software can often include information about hardware
counters such as floating pointer operations per second, memory access, cache
hits and misses etc. In the end of this activity we look at some Python
specific tools.
