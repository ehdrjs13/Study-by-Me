class TimeTools:
    def __init__(self) -> None:
        pass

    '''시분초를 초로 변환'''
    def time2sec(self,time) -> int:

        sec = int(time[0])*3600 + int(time[1])*60 + int(time[2])

        return sec

    '''시간 top3를 반환'''
    def get_top3(self,list) -> list:
            
        top = sorted(list, key=lambda x: self.time2sec(x['time']), reverse=True)[:3]
    
        return top


