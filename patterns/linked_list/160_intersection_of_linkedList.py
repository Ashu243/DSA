

def intersection(headA, headB):
    pa = headA
    pb = headB

    while pa!=pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa

