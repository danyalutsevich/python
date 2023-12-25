from utils.body_parser import body_parser


def register():
    print("register")
    pass


def login():
    print("login")
    pass


def routing(environ):
    body = body_parser(environ)
    print("Body:", body)
