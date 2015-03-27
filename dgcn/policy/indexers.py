from plone.indexer.decorator import indexer
from dgcn.content.photo import IPhoto
from DateTime import DateTime


@indexer(IPhoto)
def photographer(obj):
    return obj.photographer

@indexer(IPhoto)
def year(obj):
    return obj.year

@indexer(IPhoto)
def start(obj):
    if obj.startDate is None:
        return None
    return DateTime(obj.startDate.isoformat())

@indexer(IPhoto)
def end(obj):
    if obj.endDate is None:
        return None
    return DateTime(obj.endDate.isoformat())

