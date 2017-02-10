# Chinese Restaurant Process
a distribution on the space of partitions of the positive intergers, $\mathcal{N}$.
This would induce a distribution on the partitions of the first $n$ intergers, for every $n \in \mathcal{N}$.
Imagine a restaurant with countably infinitely many tables, labelled $1, 2, \dots$.
Customers walk in and sit down at some table. The tables are chosen according to the following random process.

1. The first customer always chooses the first table.
1. The $n$th customer chooses the first unoccupied table with probability $\dfrac{\alpha}{n-1+ \alpha}$, 
and an occupied table with probability $\dfrac{c}{n-1 + \alpha}$,where $c$ is the number of people sitting at the table.

In the above, $\alpha$ is a scalar parameter of the process.
Let us denote by $k_n$ the number of different tables occupied after $n$ customers have walked in.
Then $1 \le k_n \le n$ and it follows from the above description tha precisely tables $1, \dots, k_n$ occupied.

So, we can make the following observations:
1. The probability of a seating is invariant under permutations, known as *exchangeablity*
1. Any seating arrangement creates a partition. Thus we could define a distribution on the space of all partitions of the integer $n$,
where $n$ is the total number of customers. The number of partitions is given by the partition function $p(n)$, which has no simple closed form.
Asymptotically, $p(n) = \exp(O(\sqrt(n)))$.
1. The expected number of occupied tables for $n$ customers grows logarithmically. In particular $\mathcal{E}[k_n|\alpha] = O(\alpha \log n)$

