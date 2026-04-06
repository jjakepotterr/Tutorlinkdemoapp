def star_bar(rating, max_stars=5):
    if rating is None:
        return '<span style="color:#aaa;">No ratings yet</span>'
    full = int(rating)
    empty = max_stars - full
    html = "&#9733;" * full + '<span style="color:#ddd;">' + ("&#9733;" * empty) + "</span>"
    return f'<span style="color:#f4c150; font-size:1.1rem;">{html}</span>'
