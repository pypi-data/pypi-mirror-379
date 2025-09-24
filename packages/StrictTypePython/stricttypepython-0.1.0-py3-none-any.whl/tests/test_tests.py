from StrictTypePython import Types

Types.DEBUG_TYPE_CHECK = False
@Types.remain_forceTypeCheck
@Types.forceUnion((int,list))
def test(TList) :
    TList[0] = 10
    return TList
LIST = [1,2]
test(LIST)