class UsrData:
    def __init__(self) -> None:
        self.datas = [{'name':'Tim', 'time':[0, 0, 1],'memo':'demo'},{'name':'Tim', 'time':[0, 0, 1],'memo':'DEMO'},{'name':'Tim', 'time':[0, 0, 1],'memo':'DEMO'}]

        pass

    '''Upload User Nickname and time record. '''
    def upload(self, receivedData: dict) -> None:
        name = receivedData["name"]
        time = receivedData["time"]
        memo = receivedData["memo"]

        self.datas.append({'name':name, 'time': time, 'memo': memo})

        print(self.datas)
        
        
        return
    
    