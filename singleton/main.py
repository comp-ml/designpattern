import singleton

## generate  instance
print(singleton.Singleton.get_instance())
print(singleton.Singleton.get_instance())
print(singleton.Singleton.get_instance())
print(singleton.Singleton.get_instance())

## Raise: NotImplementedError

try:
    # NotImplementederror
    singleton.Singleton()
    # 1/0 other error
except(NotImplementedError) as e:
    print(e)
except:
    print('other Error')