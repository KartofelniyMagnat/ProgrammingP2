def order(item, qty=1, *, takeaway=False):
    return {"item": item, "qty": qty, "takeaway": takeaway}

print(order("coffee"))
print(order("pizza", 2, takeaway=True))