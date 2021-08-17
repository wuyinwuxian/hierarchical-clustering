# hierarchical-clustering
层次聚类的测试示例，用Scipy 库实现</br>

## 距离度量方法有如下

- Single-link </br>
定义两个 cluster 之间的距离为两个 cluster 之间距离最近的两个对象间的距离，但这样在聚类的过程中就可能出现链式效应，即有可能聚出长条形状的 cluster；</br>
![image](https://user-images.githubusercontent.com/72603715/129674914-3734b3de-21fc-4650-ad12-438dd6ce9b7a.png)


- Complete-link </br>
定义两个 cluster 之间的距离为两个 cluster 之间距离最远的两个对象间的距离，这样虽然避免了链式效应，但其对异常样本点（不符合数据集的整体分布的噪声点）却非常敏感，容易产生不合理的聚类；</br>
![image](https://user-images.githubusercontent.com/72603715/129674953-04506cfa-5624-4f59-a9a0-f390d5b03ce1.png)

- UPGMA </br>
正好是 Single-link 和 Complete-link 的一个折中，其定义两个 cluster 之间的距离为两个 cluster 之间任意两个对象间的距离的平均值，所有的距离求和再平均</br>
![image](https://user-images.githubusercontent.com/72603715/129675545-1dd7f9b9-9f1f-4b2f-bc6d-8c7d8a39f3a8.png)


- WPGMA </br>
计算的是两个 cluster 之间两个对象之间的距离的加权平均值，加权的目的是为了使两个 cluster 对距离的计算的影响在同一层次上，而不受 cluster 大小的影响</br>


- Centroid/UPGMC </br>
给每一个 cluster 计算一个质心（也叫簇的中心），两个 cluster 之间的距离即为对应的两个质心之间的距离，质心可以理解在各个维度上求平均组成的一个点， </br>
![image](https://user-images.githubusercontent.com/72603715/129675083-c3efa49c-ef15-4802-adc1-d2165bcb42f2.png)

- Median/WPGMC  </br>
为每个 cluster 计算质心时，引入了权重。相当于，簇里面每个样本贡献程度不一样 </br>

- Ward </br>
每一个 cluster 定义了一个 ESS （Error Sum of Squares）量作为衡量信息损失的准则，其实就是样本的方差，每个样本减均值的平方和，Ward 方法则是希望找到一种合并方式，使得合并后产生的新的一系列的 cluster 的 ESS 之和相对于合并前的 cluster 的 ESS 之和的增长最小。 </br>
![image](https://user-images.githubusercontent.com/72603715/129675147-d20e8205-cd9c-404b-b3de-302539e3d5f0.png)


在运行层次聚类算法时，我们并不会直接通过样本点之间的距离之间计算两个 cluster 之间的距离，而是通过已有的 cluster 之间的距离来计算合并后的新的 cluster 和剩余 cluster 之间的距离，这种计算方法叫 Lance-Williams。

在 Agglomerative 层次聚类算法中，一个迭代过程通常包含将两个 cluster 合并为一个新的 cluster，然后再计算这个新的 cluster 与其他当前未被合并的 cluster 之间的距离，而 Lance-Williams 方法提供了一个通项公式，使得其对不同的 cluster 距离衡量方法都适用。具体地，对于三个 cluster Ck，Ci 和 Cj， Lance-Williams 给出的 Ck 与 Ci 和 Cj 合并后的新 cluster 之间的距离的计算方法如下式所示：
![image](https://user-images.githubusercontent.com/72603715/129675262-142da706-5e46-43ca-9aa4-4141d49a3a0b.png)

![image](https://user-images.githubusercontent.com/72603715/129675416-6f8aea68-500e-4eb7-bbbc-c5ad9f941433.png)

# 实验结果
![image](https://github.com/wuyinwuxian/hierarchical-clustering/blob/main/hierarchical-clustering/clusteringResult.png)
