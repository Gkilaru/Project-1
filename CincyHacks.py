import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'componententity'
insta_password = 'omalleys'


# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				  delimit_by_numbers=True,
				   max_followers=20001,
				    max_following=25000,
				     min_followers=1,
				      min_following=10)
    session.set_user_interact(amount=1, randomize=False, percentage=100, media='Photo')
    session.set_do_follow(enabled=False, percentage=70)
    session.set_do_like(enabled=True, percentage=100)
    session.set_comments(["This is awesome!", "Follow us to win a $5 Graeters gift card with more prizes all summer!", "We're bringing Virtual Reality to the Web, follow us to see and win prizes!"])
    session.set_do_comment(enabled=True, percentage=100)

    # actions
    session.interact_user_followers(['margeson.jack'], amount=5, randomize=True)

    


except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()