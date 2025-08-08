# Mutable Trees
## Tree Class
Use class to define tree data structure, and compare what's different from using data abstraction.

```python
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = list(branches)
```
We use tree instances similarly to using data abstraction.

## Tree Mutation
**Example: Pruning a Tree**
Removing subtrees from a tree is called pruning the tree.
```python
def prune(t, n):
    """prune all subtrees of t with label n
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
```


