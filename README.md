<h1>Difference Between Else and Finally in a Try catch block</h1>


The main difference between **else** and **finally** in a try catch block is that the else block will execute only if there's no exception in the try block; i.e if there's any exception raised while executing the try block. it will skip over to the except block and fianlly the **finally** block. The below code shows an example of how the blocks work. No matter what happens while executing the code, the **finally** block will still execute it.

```Python
    try:
        print("I may raise an exception!")
    except:
        print("I will be called only if exception occur!")
    else:
        print("I will be called only if exception didn't occur!")
    finally:
        print("I will be called always!")
```

One other fascinating thing about **finally** block is that even if there's a return statement in the try block, the code inside the finally block **will still get executed**.

```Python
    def doing_something():
        try:
            print("This will obviously get executed")
            return True
        except:
            print("I will get executed if there's any exceptions")
        else:
            print("I will not get executed because there's a reutrn statement in the try block")
        finally:
            print("I will get even if there's a return statement in the try block")
```

