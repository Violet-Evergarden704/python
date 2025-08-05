# Lec11: Midterm Review
## What Would Python Print?
```python
def delay(arg):
    print('delayed!')
    def g():
        print(arg)
    return g
```
If we call delay(delay)()(6)(), what will python print?
Let's break it down:
1. delay(delay)
2. delay(delay)()
3. delay(delay)()(6)
4. delay(delay)()(6)()

For the first one, delay(delay) will print 'delayed!' and a func that takes in any arg and return delay function.
Then, step 2 means the function is called with no argument, and function delay is returned.
Then in step 3 that means delay(6) is called, and it will print 'delayed!' and return a function that takes in any arg and return 6.
Then in step 4, the function is called with no argument, and it will print 6.

So the output will be:
```
delayed!
delayed!
6
```

```python
def pirate(arg):
    print('Arr!')
    def plunder(arg):
        return arg
    return plunder
```
In this case, if we call add(pirate(3)(square)(4), 1), what will python print?
In fact, though arg seems to be the same name, it's bound to the current frame, which means in this case is 4.
So pirate function always return an identical function, no matter what argument it takes in.
