# note of Online CRP
## about relaxing function
first cutomer -> first table
btw, waiters trace all dishes and try to allocate customers to proper tables based on
the history of which dishes were served to which table (*prior distribution*).
If a customer dislike the table, moved other table by himself.
If this process occures continuously, the restaurant get mess.
So, waiters try to decrease the probability of miss-sevings.

i番目の客へのテーブル割り当て
- ウェイターに従う割り当て$z_i$
- 最終的に座ったテーブル$y_i$

テーブル$j$と客$i$について、$f_j, e_j$は過去の$i-1$人の客の割り当てミスを追跡する。
``` tex
f_j = \sum_{a=1}^{i-1} \mathcal{1}[y_a = j ^ z_a \ne j]
e_j = \sum_{a=1}^{i-1} \mathcal{1}[z_a = j ^ y_a \ne j]
```
また、relaxing function gは、
$
g(\gamma_1, \gamma_2, e_j, f_j) = (1+\gamma_1)^{f_j}(1-\gamma_2)^{e_j}
$

事後分布推定
```tex
P(z_i=j | z_{-i}, x_i, y_i, \theta, G_0, \alpha)
 = \begin{cases}
 g(\gamma_1, \gamma_2, e_j, f_j) \dfrac{m_j}{i-1+\alpha} H(x_i, \theta_j) & if j \le k \\
 \dfrac{\alpha}{i-1+\alpha} \int H(x_i, \theta_j) dG_0(\theta_j) & if j = k+1
\end{cases}
```


