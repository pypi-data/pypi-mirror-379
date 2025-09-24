__all__ = ["stamp_pdf", "verify_pdf"]

def __getattr__(name):
    if name == "stamp_pdf":
        from .stamp_pdf import stamp_pdf
        return stamp_pdf
    if name == "verify_pdf":
        from .verify import verify_pdf
        return verify_pdf
    raise AttributeError(name)