from collective.grok import gs
from samahan.theme import MessageFactory as _

@gs.importstep(
    name=u'samahan.theme', 
    title=_('samahan.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('samahan.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
