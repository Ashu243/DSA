# def insertAtBottom(self, st: list[int], x: int) -> list[int]:
#     ans = [0] * (len(st) + 1)
#     ans[0] = x
#     for i in range(1, len(ans)):
#         ans[i] = st[i - 1]
#     return ans


# recursive 
def insertAtBottom(self, st, x):
    if not st:
        st.append(x)
        return st

    top = st.pop()
    self.insertAtBottom(st, x)
    st.append(top)

    return st