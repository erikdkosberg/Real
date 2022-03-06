import time
import asyncio

class Server():
    """
    Handle connections with clients via asyncio;
    """
    
class Generator():
    """
    Quick generators for process manipulation;
    """
    def iter_test():
        for x in range(10):
            yield x

class AsyncProc():
    """
    Define the async processes to be awaited on;
    """
    async def a1():
        test = await iter_test
    async def a2():
        print(time.time())

def main():
    print('hi')

if __name__ == '__main__':
    main()

