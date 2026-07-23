count = 0

"""
TC: =2^(n+1) - 1 we can use recurrence proof for same

Let T(n) be the number of function calls.
For every call with n > 0:
* current call contributes 1
* first recursive call contributes T(n-1)
* second recursive call contributes T(n-1)

So
T(n)=2T(n-1)+1
T(0)=1 equals,
2^(n+1) - 1

SC: O(n):
  due to the sequential nature of depth-first recursion, the right-side recursive calls only begin after the left-side ones finish, 
  meaning the stack does not simultaneously hold all these calls. This is why the space complexity is O(n)
  
"""
def zig_zag(n):
    global count
    count += 1
    if n == 0:
        return
    print(f"Pre: {n}")
    zig_zag(n - 1)
    print(f"In: {n}")
    zig_zag(n - 1)
    print(f"Post: {n}")


if __name__ == "__main__":
    zig_zag(4)
    print(count)
