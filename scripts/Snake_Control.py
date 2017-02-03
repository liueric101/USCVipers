import time
def onUnlock():
    myo.rotSetCenter()
    myo.unlock("hold")
	
def onPoseEdge(pose, edge):
    if (pose == 'fist') and (edge == "on"): 
        if myo.get_active_window_title()=="\"Vipers\"":
            print "tru realigion"
        print myo.get_active_window_title()
    if (pose == 'fingersSpread') and (edge == "on"):
        myo.mouse("right","click","")


def onPeriodic():
    if (myo.isUnlocked()): #and (myo.get_active_window_title()=="\"Vipers\""):
        print myo.getBox()
#        if myo.getVBox() == 1:
#            myo.keyboard("w","press","") 
#        elif myo.getVBox() == -1:
#            myo.keyboard("s","press","") 
#        elif myo.getHBox() == 1:
#            myo.keyboard("d","press","") 
#        elif myo.getHBox() == -1:
#            myo.keyboard("a","press","") 

