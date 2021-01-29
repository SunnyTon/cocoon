import datetime
def getCenterWarehouseData(cid):
    """添加发布会 body模板"""
    #startTime=(datetime.datetime.now()+datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:00")  #获得当前时间，并往后30天为发布会时间
    startTime=(datetime.datetime.now()).strftime("%Y-%m-%d")  #获得当前时间
    print('现在时间：'+startTime)

    data={
          'centerWarehouseId':cid, #中心仓Id,默认不传
          'token':0,    #默认值
          'date': startTime #%格式   Y-%m-%d
         }
    return data