<!-- Title: Parallel programming concepts -->

<!-- Short description:

In this article we briefly introduce some key concepts related to parallel
programming.

-->

Before starting to program for parallel computers, we need to start with few
basic concepts.

# Computing in parallel

The underlying idea in parallel computing is that the computational problem
can be split into smaller subtasks. Multiple subtasks can then be executed
*simultaneously* by multiple processing units. In modern CPUs, the single
execution unit is typically a CPU core.

![Computing in parallel](https://ugc.futurelearn.com/uploads/assets/5b/11/5b114310-9bb5-4d8f-9907-d6cc15ddc8b9.png)

How the splitting into subtasks is done depends fully on the problem. There
are also various paradigms and programming approaches into the parallelization,
but in this course we focus on message passing approach using Python.

## Types of parallel problems

Parallel programs can be divided in two limiting classes: tighly coupled and 
embarrassingly parallel. In tighly coupled problems there is lots of interaction
between subtasks, and low latency high speed interconnect between the CPUs 
is essential for good performance. Weather simulation is a typical example of
tighly coupled problem.

In embarrassingly parallel cases is very little (or no) interaction between 
subtasks. Programming these types of problems is typically easier, and there are
no high demands for the connection between CPUs. In best cases computers all 
over internet can be used for computing in parallel such as in [Folding@home](https://foldingathome.org/) project where protein folding is studied using 
personal computers all over world.

Many real-world problems fall naturaly somewhere between the two extreme cases.

## Exposing parallelism

One common way to expose parallelism is by distributing the data, for example an
array to individual processing units.

![Data parallelism](https://ugc.futurelearn.com/uploads/assets/41/b3/41b32268-407a-47d6-8f9a-2abbc0f78003.png)

Each processing unit (e.g. CPU core) obtains part of the data, and perform
typically identical or at least very similar operations on the data. Processing
units may need to interact with each other for example exchange information 
about data on domain boundaries.

Other common parallelisation model is the task farm (or master / worker) 
approach, where a master sends tasks to workers and receives then results 
from them.

![Task farm](https://ugc.futurelearn.com/uploads/assets/2c/55/2c55da08-e795-4f1b-93f8-61726bfd299e.png)

The tasks can be computationally similar, but in some cases they can be also 
completely different. There are often more tasks than workers, and tasks are 
then dynamically assigned to workers.

Task farm and data parallel approaches can be also combined, for example, 
each worker could consist of multiple execution units, and the data related
to task distributed to them.

## Parallel scaling

When the size of input data is kept constant, but one increases the number of
processing units, we typically speak about *strong parallel scaling*. The
purpose of parallel programming in this case is to decrease the time to
solve the problem, in ideal case the decrease should be directly proportional
to the number of processing units. That is, doubling the number of processing 
units should halve the execution time. In real-world problems this is rarely 
the case, and typically when increasing the processing units enough the 
execution time can even start to increase, resulting in relative speed-up 

$$
S=\frac{T_p}{T_{p+1}},
$$

where $$T_p$$ is the execution time with $$p$$ processing units which is 
smaller than one.


![Parallel scaling](https://ugc.futurelearn.com/uploads/assets/36/99/36999aa0-67fa-4265-8814-40ff61f18eff.png)

There are several factors which can limit the parallel scaling. Typically, 
parallel program needs to perform some additional operations which are not 
present in serial program. There can be some redundant computations, data needs
to be communicated, and the processing units need to be synchronized. If there
is imbalance in the distribution of the workload, execution time is limited
by the slowest execution unit, and others need to wait its completion. There 
can be also serial parts in the program i.e. parts that cannot be parallelized.
If we designate with $$p_f$$ the fraction of the problem that can be 
parallelized, then the maximum possible speed-up (so called Amdahl's law) is

$$
S_{max} = \frac{1}{1 - p}
$$

As an example, if only 90 % of the problem can be parallelized, maximum 
speed-up is 10 even if one was using 1000 CPU cores.

Parallel programming is not used only for speeding up problems, but also to
enable studies of larger or more accurate problems. In these situations, 
both the size of input data and number of processing units are increased at the
same time, and one speaks about *weak parallel scaling*. In ideal weak scaling
case the execution time remains constant when amount of data and number of 
processing units are increased in same proportion. Good weak scaling is easier
to achieve than good parallel scaling.
