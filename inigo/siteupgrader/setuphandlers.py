from collective.grok import gs
from inigo.siteupgrader import MessageFactory as _

@gs.importstep(
    name=u'inigo.siteupgrader', 
    title=_('inigo.siteupgrader import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('inigo.siteupgrader.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
