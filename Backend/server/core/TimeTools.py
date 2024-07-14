class TimeTools:
    def __init__(self) -> None:
        pass

    '''Convert HH:MM:DD into seconds'''
    @staticmethod
    def time2sec(time) -> int:

        sec = int(time[0])*3600 + int(time[1])*60 + int(time[2])

        return sec

    '''Get top3 users' datas'''
    def get_top3(self,list) -> list:
        
        print(list)
        if len(list) > 0:

            top = sorted(list, key=lambda x: TimeTools.time2sec(x['time']), reverse=True)[:3]
        else:
            top = [[],[],[]]

    
        return top


