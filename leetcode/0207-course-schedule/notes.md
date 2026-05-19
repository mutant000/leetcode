# 207. Course Schedule

## 思路

把课程依赖看成有向图：`prerequisite -> course`。

用入度记录每门课还剩多少前置课程。先把入度为 `0` 的课程放入队列，每完成一门课，就把它指向的后续课程入度减一；如果某门后续课程入度变为 `0`，也加入队列。

最后如果完成课程数等于 `numCourses`，说明不存在环，可以修完所有课程。

## 复杂度

- Time: `O(n + p)`，`p` 是依赖数量。
- Space: `O(n + p)`。

## 边界

- 没有依赖时所有课程都能完成。
- 两门课互相依赖会形成环。
- 图中可以有多个互不相连的课程组件。

## 提交记录

- Accepted: https://leetcode.com/problems/course-schedule/submissions/2006803140/
- Testcases: `54 / 54`
- Runtime: `7 ms`
- Memory: `20.41 MB`
