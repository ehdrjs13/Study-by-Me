class UsrData:
    def __init__(self) -> None:
        from core.analysis_wnn import Analysis

        self.analyze = Analysis()

        self.datas = [{'name':'Tim', 'time':[0, 0, 1],'memo':'demo','subject':'정보'},{'name':'Tim', 'time':[0, 0, 1],'memo':'DEMO','subject':'정보'},{'name':'Tim', 'time':[0, 0, 1],'memo':'DEMO','subject':'정보'}]

        pass

    '''Upload User Nickname and time record. '''
    def upload(self, receivedData: dict) -> None:
        name = receivedData["name"]
        time = receivedData["time"]
        memo = receivedData["memo"]
        subject = self.analyze.classify(receivedData["memo"])

        self.datas.append({'name':name, 'time': time, 'memo': memo, 'subject': subject})

        print(self.datas)
        
        
        return
    
    