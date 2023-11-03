class DropConstant:
    def __init__(self):
        print("initialize drop constant")

    def print_hi(self, name: str) -> None:
        """
        :type name: str
        """
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    def print_items1(self, n) -> None:
        for i in range(n):
            print(i)
        for j in range(n):
            print(j)

    def print_items2(self, n) -> None:
        for i in range(n):
            for j in range(n):
                print(i, j)
