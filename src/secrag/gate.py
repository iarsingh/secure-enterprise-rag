class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    q = str(body.get("question", "")).lower(); hits = [w for w in ("password", "api_key", "bearer") if w in q]; failed.extend(hits); failed.append("empty") if not q.strip() else None
    return {"passed": not failed, "failed": failed, "applied": False}
