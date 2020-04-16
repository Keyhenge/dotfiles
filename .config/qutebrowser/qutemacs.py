# qutemacs - a simple, preconfigured Emacs binding set for qutebrowser
#
# The aim of this binding set is not to provide bindings for absolutely
# everything, but to provide a stable launching point for people to make their
# own bindings.
#
# Installation:
#
# 1. Copy this file or add this repo as a submodule to your dotfiles.
# 2. Add this line to your config.py, and point the path to this file:
# config.source('qutemacs/qutemacs.py')

config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

c.tabs.background = True
# disable insert mode completely
c.input.insert_mode.auto_enter = False
c.input.insert_mode.auto_leave = False
c.input.insert_mode.plugins = False

# Forward unbound keys
c.input.forward_unbound_keys = "all"

ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

import string

c.bindings.default['normal'] = {}
c.bindings.default['insert'] = {}

c.bindings.commands['insert'] = {
    '<ctrl-space>': 'leave-mode',
    '<ctrl-g>': 'leave-mode;;fake-key <Left>;;fake-key <Right>',
    '<ctrl-f>': 'fake-key <Shift-Right>', 
    '<ctrl-b>': 'fake-key <Shift-Left>',
    '<ctrl-e>': 'fake-key <Shift-End>',
    '<ctrl-a>': 'fake-key <Shift-Home>',
    '<ctrl-p>': 'fake-key <Shift-Up>',
    '<ctrl-n>': 'fake-key <Shift-Down>',
    '<Return>': 'leave-mode',
    '<ctrl-w>': 'fake-key <Ctrl-x>;;message-info "cut to clipboard";;leave-mode',
    '<alt-w>': 'fake-key <Ctrl-c>;;message-info "copy to clipboard";;leave-mode',
    '<backspace>': 'fake-key <backspace>;;leave-mode',
    '<alt-x>': 'leave-mode;;set-cmd-text :',
    '<alt-o>': 'leave-mode;;tab-focus last',
    '<Tab>': 'fake-key <f1>'
}

for char in list(string.ascii_lowercase):
    c.bindings.commands['insert'].update({char: 'fake-key ' + char + ';;leave-mode'})

for CHAR in list(string.ascii_uppercase):
    c.bindings.commands['insert'].update({CHAR: 'fake-key ' + char + ';;leave-mode'})

for num in list(map(lambda x : str(x), range(0, 10))):
    c.bindings.commands['insert'].update({num: 'fake-key ' + num + ';;leave-mode'})
    
for symb in [',', '.', '/', '\'', ';', '[', ']', '\\',
             '!', '@','#','$','%','^','&','*','(',')','-','_', '=', '+', '`', '~',
             ':', '\"', '<', '>', '?','{', '}', '|']:
    c.bindings.commands['insert'].update({symb: 'insert-text ' + symb + ' ;;leave-mode'})

# Bindings
c.bindings.commands['normal'] = {
    # Qutebrowser management
    '<ctrl-x><ctrl-q>': 'quit',
    '<ctrl-x><ctrl-r>': 'config-source',
    '<ctrl-h>': 'set-cmd-text -s :help',
    
    # Navigation
    '<ctrl-space>': 'enter-mode insert',
    '<alt-[>': 'back',
    '<alt-]>': 'forward',
    '<ctrl-v>': 'scroll-page 0 0.7',
    '<alt-v>': 'scroll-page 0 -0.7',
    '<ctrl-r>': 'reload',
    '<alt-x>': 'set-cmd-text :',
    '<ctrl-x>r': 'config-cycle statusbar.hide',
    '<ctrl-x>e': 'edit-url',

    # Information
    '<ctrl-c>i': 'message-info {title}',
    '<ctrl-c>u': 'yank url',
    '<ctrl-c>p': 'yank pretty-url',
    '<ctrl-c>t': 'yank title',
    '<ctrl-c>d': 'yank domain',

    # Searching
    '<ctrl-s>': 'set-cmd-text /',
    '<ctrl-alt-s>': 'search-prev',

    # Hinting
    '<alt-s>': 'hint all',
    '<alt-t>': 'hint links run :open -t {hint-url}',
    '<alt-h>': 'hint links run :open -p {hint-url}',
    '<alt-m>': 'hint links spawn --detach umpv --force-window yes {hint-url}',

    # Tabs/Window management
    '<ctrl-tab>': 'tab-next',
    '<ctrl-shift-tab>': 'tab-prev',
    '<ctrl-x><ctrl-b>': 'set-cmd-text -s :buffer;;fake-key <Down><Down><Down>',
    '<ctrl-x>1': 'tab-only;;message-info "cleared all other tabs"',
    '<ctrl-x>2': 'open -w {url};;tab-close;;message-info "Sent to new window"',
    '<ctrl-x>3': 'open -p {url};;tab-close;;message-info "Sent to new private window"',
    '<ctrl-x>k': 'tab-close',
    '<ctrl-x>0': 'close',
    '<ctrl-x>o': 'tab-focus last',

    # Open
    '<ctrl-l>': 'set-cmd-text -s :open',
    '<ctrl-x><ctrl-f>': 'set-cmd-text -s :open -t',
    '<ctrl-x><ctrl-h>': 'set-cmd-text -s :open -p',
    '<ctrl-x><ctrl-l>': 'set-cmd-text -s :open {url}',

    # Editing
    '<ctrl-shift-e>': 'fake-key <Ctrl-Shift-Right>',
    '<ctrl-shift-a>': 'fake-key <Ctrl-Shift-Left>',
    '<ctrl-/>': 'fake-key <Ctrl-z>',
    '<ctrl-shift-?>': 'fake-key <Ctrl-Shift-z>',
    '<ctrl-k>': 'fake-key <Shift-End>;;fake-key <Backspace>',
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-x>h': 'fake-key <Ctrl-a>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    '<ctrl-w>': 'fake-key <Ctrl-x>;;message-info "cut to clipboard"',
    '<alt-w>': 'fake-key <Ctrl-c>;;message-info "copy to clipboard"',
    '<ctrl-y>': 'insert-text {primary}',

    # Zoom
    '<ctrl-=>': 'zoom-in', #so you don't have to press shift all the time
    '<ctrl-+>': 'zoom-in',
    '<ctrl-->': 'zoom-out',

    '1': 'fake-key 1',
    '2': 'fake-key 2',
    '3': 'fake-key 3',
    '4': 'fake-key 4',
    '5': 'fake-key 5',
    '6': 'fake-key 6',
    '7': 'fake-key 7',
    '8': 'fake-key 8',
    '9': 'fake-key 9',
    '0': 'fake-key 0',

    # escape hatch
    '<ctrl-g>': ESC_BIND,
}

c.bindings.commands['command'] = {
    '<ctrl-s>': 'search-next',
    '<ctrl-r>': 'search-prev',

    '<ctrl-p>': 'completion-item-focus prev',
    '<ctrl-n>': 'completion-item-focus next',

    '<alt-p>': 'command-history-prev',
    '<alt-n>': 'command-history-next',

    # escape hatch
    '<ctrl-g>': 'leave-mode',
}

c.bindings.commands['hint'] = {
    # escape hatch
    '<ctrl-g>': 'leave-mode',
}


c.bindings.commands['caret'] = {
    # escape hatch
    '<ctrl-g>': 'leave-mode',
    '<ctrl-space>': 'toggle-selection'
}

#config.bind('<Tab>', 'fake-key <f1>')
config.bind('<f11>', 'fullscreen')

c.tabs.show = 'switching'
c.statusbar.hide = False
c.url.searchengines["ddg"] = "https://duckduckgo.com/?q={}"
c.url.searchengines["sp"] = "https://duckduckgo.com/?q=!sp+{}"
c.url.searchengines["sx"] = "https://searx.ninja/?q={}&categories=general&language=en-US"

c.url.searchengines["ama"] = "https://www.amazon.com/s?k={}"
c.url.searchengines["ji"] = "https://jisho.org/search/{}"
c.url.searchengines["y"] = "https://www.youtube.com/results?search_query={}"
c.url.searchengines["nixo"] = "https://nixos.org/nixos/options.html#{}"
c.url.searchengines["nixp"] = "https://nixos.org/nixos/packages.html?channel=nixos-unstable&query={}"

c.url.searchengines["DEFAULT"] = "https://searx.ninja/?q={}&categories=general&language=en-US"

c.url.start_pages = ["https://searx.ninja/"]
