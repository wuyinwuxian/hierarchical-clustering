# hierarchical-clustering
层次聚类的测试示例，用Scipy 库实现</br>

## 距离度量方法有如下

- Single-link </br>
定义两个 cluster 之间的距离为两个 cluster 之间距离最近的两个对象间的距离，但这样在聚类的过程中就可能出现链式效应，即有可能聚出长条形状的 cluster；</br>

- Complete-link </br>
定义两个 cluster 之间的距离为两个 cluster 之间距离最远的两个对象间的距离，这样虽然避免了链式效应，但其对异常样本点（不符合数据集的整体分布的噪声点）却非常敏感，容易产生不合理的聚类；</br>

- UPGMA </br>
正好是 Single-link 和 Complete-link 的一个折中，其定义两个 cluster 之间的距离为两个 cluster 之间任意两个对象间的距离的平均值，所有的距离求和再平均</br>

- WPGMA </br>
计算的是两个 cluster 之间两个对象之间的距离的加权平均值，加权的目的是为了使两个 cluster 对距离的计算的影响在同一层次上，而不受 cluster 大小的影响（其计算方法这里没有给出，因为在运行层次聚类算法时，我们并不会直接通过样本点之间的距离之间计算两个 cluster 之间的距离，而是通过已有的 cluster 之间的距离来计算合并后的新的 cluster 和剩余 cluster 之间的距离，这种计算方法将由下一部分中的 Lance-Williams 方法给出）。</br>


- Centroid/UPGMC </br>
给每一个 cluster 计算一个质心（也叫簇的中心），两个 cluster 之间的距离即为对应的两个质心之间的距离，质心可以理解在各个维度上求平均组成的一个点， </br>

- Median/WPGMC  </br>
为每个 cluster 计算质心时，引入了权重。相当于，簇里面每个样本贡献程度不一样 </br>

- Ward </br>
每一个 cluster 定义了一个 ESS （Error Sum of Squares）量作为衡量信息损失的准则，其实就是样本的方差，每个样本减均值的平方和，Ward 方法则是希望找到一种合并方式，使得合并后产生的新的一系列的 cluster 的 ESS 之和相对于合并前的 cluster 的 ESS 之和的增长最小。 </br>

