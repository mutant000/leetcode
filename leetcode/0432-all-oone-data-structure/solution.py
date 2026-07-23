class _Bucket:
    def __init__(self, count: int = 0):
        self.count = count
        self.keys = set()
        self.previous = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = _Bucket()
        self.tail = _Bucket()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.key_to_bucket = {}

    def _insert_after(self, bucket: _Bucket, new_bucket: _Bucket) -> None:
        next_bucket = bucket.next
        bucket.next = new_bucket
        new_bucket.previous = bucket
        new_bucket.next = next_bucket
        next_bucket.previous = new_bucket

    def _remove_bucket(self, bucket: _Bucket) -> None:
        bucket.previous.next = bucket.next
        bucket.next.previous = bucket.previous

    def inc(self, key: str) -> None:
        # 新键进入计数为 1 的桶。
        if key not in self.key_to_bucket:
            target = self.head.next

            if target is self.tail or target.count != 1:
                target = _Bucket(1)
                self._insert_after(self.head, target)

            target.keys.add(key)
            self.key_to_bucket[key] = target
            return

        # 已有键移动到右侧计数加 1 的桶。
        current = self.key_to_bucket[key]
        target = current.next

        if target is self.tail or target.count != current.count + 1:
            target = _Bucket(current.count + 1)
            self._insert_after(current, target)

        target.keys.add(key)
        self.key_to_bucket[key] = target
        current.keys.remove(key)

        if not current.keys:
            self._remove_bucket(current)

    def dec(self, key: str) -> None:
        current = self.key_to_bucket[key]

        if current.count == 1:
            del self.key_to_bucket[key]
            current.keys.remove(key)
        else:
            target = current.previous

            if target is self.head or target.count != current.count - 1:
                target = _Bucket(current.count - 1)
                self._insert_after(current.previous, target)

            target.keys.add(key)
            self.key_to_bucket[key] = target
            current.keys.remove(key)

        if not current.keys:
            self._remove_bucket(current)

    def getMaxKey(self) -> str:
        if self.tail.previous is self.head:
            return ""

        return next(iter(self.tail.previous.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""

        return next(iter(self.head.next.keys))
