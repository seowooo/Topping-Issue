from flask import Flask

app = Flask(__name__)

import ToppingIssue.views.index_views
import ToppingIssue.views.news_views