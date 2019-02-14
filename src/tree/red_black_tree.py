# -*- coding: utf-8 -*-

# 一种含有红黑结点并能够自平衡的二叉树，满足以下性质：
# 性质一：每个节点要么是黑色要么是红色
# 性质二：根节点是黑色
# 性质三：每个叶子节点是黑色（叶子节点是 null 节点，不包含数据只是充当树在此结束的指示）
# 性质四：每个红色节点的两个子节点一定是黑色节点
# 性质五：任意节点到每个叶子节点的路径都包含相同数量的黑节点

# ----  父节点为黑色或空树时  ----
# 父节点是根节点或者树为空树 直接插
# 父节点是黑色 插入节点置为红色即可（原先一定是红黑树，满足性质五，置为红色后任然满足性质五）


# ----  父节点为红色  ----
# ----  父节点为红色，那么如果有叔叔节点，那么也必是红色（初始插入时）  ----
# 步骤-：插入节点维持红色不变，将父节点及叔叔节点置为黑色，祖父节点置为红色，

# ---- 若祖父节点的父节点为黑色，插入结束

# ---- 若祖父节点的父节点为红色，以祖父节点为当前节点

# ---- 若无叔叔节点或叔叔节点也为红色时，重复步骤一

# ---- 若叔叔节点为黑色，当前节点为右子节点
# 步骤二：以当前节点为支点左旋，然后以祖父节点为当前节点
# ---- 当前节点为左子节点且祖父节点为红色，叔叔节点为黑色
# 步骤三：以当前节点为支点右旋，然后以祖父节点为当前节点
# 。。。

# ----  若叔叔节点为黑色，当前节点为左子节点
# 上述右子节点的步骤二、三调换顺序

# 步骤四：判断根节点是否是黑色，非黑色则置黑，插入结束


# 删除最终都转换成了，末尾（叶子节点的前一节点）删除

# 红 黑 红 直接删
# 黑 红 黑 旋转
# 