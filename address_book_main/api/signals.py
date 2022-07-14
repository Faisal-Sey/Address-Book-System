from django import dispatch


upload_complete = dispatch.Signal(providing_args=["bool"])