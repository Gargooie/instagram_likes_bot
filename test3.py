#instapy works with firefox only due to instagram's chrome ban
import test2
from instapy import InstaPy

sess = InstaPy(username=test2.my_login, password=test2.my_pass)
sess.login()
sess.like_by_tags(["mercedes"], amount=5)
