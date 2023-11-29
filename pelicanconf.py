# pelicanconf.py

AUTHOR = "Paul"
SITENAME = "World of Paul's Craft"
SITESUBTITLE = (
    "The blog of one random software engineer and his random interests."
)

PATH = "content"

TIMEZONE = "America/Los_Angeles"
DEFAULT_LANG = "en"
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%a %d %B %Y"

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
# )

# Social widget
# SOCIAL = (
#    ("GitHub", "https://github.com/worldofpaulcraft"),
# Add other social links if needed
# )

DEFAULT_PAGINATION = 0

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/clean-blog"  # You need to specify the path to your theme here
HEADER_COVER = "images/blog_header.jpg"

MAIN_MENU = True
MENUITEMS = (
    ("About", "/about.html"),
    ("Archives", "/archives.html"),
#    ("Categories", "/categories"),
    )

STATIC_PATHS = [
    'images',
    'extras',
]
ARTICLE_PATHS = [
    'articles',
]
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_PATHS = [
     'pages',
]
PAGE_URL = "/"
PAGE_SAVE_AS =  "{slug}.html"

CATEGORIES_SAVE_AS = None
AUTHORS_SAVE_AS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.def_list": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.abbr": {},
        "markdown.extensions.md_in_html": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.footnotes": {
            "BACKLINK_TEXT": "&crarr;",
        },
        "markdown.extensions.meta": {},
        "smarty": {"smart_angled_quotes": "true"},
        "markdown.extensions.toc": {
            "permalink": "true",
        },
    }
}

# Plugins

TYPOGRIFY = True
TYPOGRIFY_DASHES = "oldschool"

KATEX_PREAMBLE = ""

TOC = {
    "TOC_HEADERS": "^h[1-6]",  # What headers should be included in
    # the generated toc
    # Expected format is a regular expression
    "TOC_RUN": "true",  # Default value for toc generation,
    # if it does not evaluate
    # to 'true' no toc will be generated
    "TOC_INCLUDE_TITLE": "true",  # If 'true' include title in toc
}

PLUGIN_PATHS = [
    "./plugins/",
]
PLUGINS = [
    "graphviz",
    "pelican_katex",
    "post_stats",
]
