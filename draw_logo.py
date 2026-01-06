import curses

def draw_logo(window, size_x):

    logo = [r'  ____ _   _ ____ _____ _   _ ____  _____',
            r' / ___| | | |  _ \_   _| | | | __ )| ____|',
            r'| |   | | | | |_) || | | | | |  _ \|  _|',
            r'| |___| |_| |  _ < | | | |_| | |_) | |___',
            r' \____|\___/|_| \_\|_|  \___/|____/|_____|',
            'A small TUI app to download Youtube videos.',
            '',
            'Move with arrows. Enter to choose option.'
    ]

    indent = 2

    for index, item in enumerate(logo):
        window.addstr(index + indent, size_x // 2 - len(logo[5]) // 2 - 2, item)

    return len(logo) + indent + 1

