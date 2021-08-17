from time import time
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from sklearn.datasets import make_blobs
from sklearn.metrics.cluster import adjusted_mutual_info_score
import matplotlib.pyplot as plt

"""
函数描述 : 可视化聚类结果
参数：
    ax     - 要绘制图像的区域，或者说是在画布的哪个区域绘图
    X      - 样本特征矩阵
    labels - 每个样本对应的标签矩阵
    title  - 图的标题
返回值：
    无
"""
def plot_clustering(ax, X, labels, title=None):
    ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='prism')
    if title is not None:
        plt.title(title, size=17)
    plt.axis('off')               # 关闭横纵轴。有横纵轴不太好看，当然也可能是我审美原因
    plt.tight_layout()            # 自动调整子图参数，避免出现显示不全，Matplotlib v1.1 引入的

"""
函数描述 : 绘制层次聚类的树形图
参数：
    Z   - 链接矩阵
返回值：
    无
"""
def plot_tree(Z,title):
    plt.figure(figsize=(10, 6))
    dendrogram(Z, truncate_mode='lastp', p=20, show_leaf_counts=False, leaf_rotation=90, leaf_font_size=15,
               show_contracted=True)  # 参数见 https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram
    plt.title(title + 'Dendrogram for the Agglomerative Clustering')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    plt.tight_layout()
    '''以下两句话是解决TrueType font 问题'''
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'Calibri'           # 也可以设置新罗马字体 plt.rcParams['font.family'] = 'Times New Roman'
    plt.savefig(title + '.pdf', bbox_inches='tight')  # 保存成pdf
    plt.close()                                       # 关闭图窗，不显示


"""生成样本点"""
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels = make_blobs(n_samples = 900, centers = centers,cluster_std = [0.2,0.4,0.5], random_state = 0)  # https://wuyinzhiming.blog.csdn.net/article/details/119752691

"""绘制原始数据"""
plt.figure(num=1,figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c='b')
plt.title('The original dataset')

"""进行 Agglomerative 层次聚类"""
linkage_method_list = ['single', 'complete', 'average', 'ward']   # 度量距离的方法
ncols, nrows = 2, int(np.ceil(len(linkage_method_list) / 2))
plt.subplots(nrows=nrows, ncols=ncols, figsize=(8, 6))
fig2 = plt.figure(num=2,figsize=(8, 6))

for i, linkage_method in enumerate(linkage_method_list):
    print('method %s:' % linkage_method)

    start_time = time()
    Z = linkage(X, method=linkage_method)                      # 一行代码 实现层次聚类
    labels_pred = fcluster(Z, t=3, criterion='maxclust')       # 每个样本的预测结果，采用指定类别数的方式获得
    print('Adjust mutual information: %.3f' %adjusted_mutual_info_score(labels, labels_pred))   # 评价AMI 该量越接近于 1 则说明聚类算法产生的类越接近于真实情况。其他的一些评价指标 https://www.jianshu.com/p/1049db259d38
    print('time used: %.3f seconds' % (time() - start_time))

    plot_tree(Z, title=linkage_method)                                  # 绘制树形图，会较慢

    ax = fig2.add_subplot(nrows, ncols, i + 1)                          # 选定要绘制的子图
    plot_clustering(ax, X, labels_pred, '%s linkage' % linkage_method)  # 可视化聚类结果

plt.show()     # 显示图像

"""
在得到了层次聚类的过程信息 Z 后，我们可以使用 fcluster 函数来获取聚类结果。可以从两个维度来得到距离的结果，一个是指定临界距离 d，
得到在该距离以下的未合并的所有 cluster 作为聚类结果；另一个是指定 cluster 的数量 k，函数会返回最后的 k 个 cluster 作为聚类结果。
使用哪个维度由参数 criterion （maxclust或者distance）决定，对应的临界距离或聚类的数量则由参数 t 所记录。fcluster 函数的结果为一个一维数组，
记录每个样本的类别信息。
"""