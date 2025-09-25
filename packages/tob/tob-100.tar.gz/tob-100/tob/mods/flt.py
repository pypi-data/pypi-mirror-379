# This file is placed in the Public Domain.


from ..client import Fleet
from ..method import fmt
from ..thread import name


def flt(event):
    if event.args:
        clts = Fleet.all()
        index = int(event.args[0])
        if index < len(clts):
            event.reply(fmt(Fleet.all()[index]))
        else:
            event.reply(f"only {len(clts)} clients in fleet.")
        return
    event.reply(' | '.join([name(o) for o in Fleet.all()]))