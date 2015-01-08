from plone.indexer.decorator import indexer
from dgcn.content.photo import IPhoto


@indexer(IPhoto)
def photographer(obj):
    return obj.photographer

