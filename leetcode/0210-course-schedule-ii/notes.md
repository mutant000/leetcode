# 210. Course Schedule II

## 思路

课程和先修关系可以看成有向图：`prerequisite -> course`。

先统计每门课的入度，也就是还剩多少先修课没完成。所有入度为 `0` 的课可以先学，放入队列。

每学完一门课，就把它指向的后续课程入度减一。如果某门后续课程入度变成 `0`，说明它也可以学习了。最后如果学到的课程数量等于 `numCourses`，返回顺序；否则图里有环，返回空列表。

## 复杂度

- 时间复杂度：`O(numCourses + prerequisites.length)`
- 空间复杂度：`O(numCourses + prerequisites.length)`
