def build_profile(*args, **kwargs):
    return {"args": args, "kwargs": kwargs}

print(build_profile("student", "gamer", name="Ilya", age=18))