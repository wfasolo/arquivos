from instapy import InstaPy

session = InstaPy(username="wfasolo", password="Giana0803")
session.login()
session.like_by_tags(["Flamengo", "flamengo"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!"])
session.end()
