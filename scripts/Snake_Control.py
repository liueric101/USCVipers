def onUnlock():
    myo.rotSetCenter()
    myo.unlock("hold")
	
def onPoseEdge(pose, edge):
    if (pose == 'fist') and (edge == "on"): 
        print myo.get_active_window_title()
    if (pose == 'fingersSpread') and (edge == "on"):
        myo.mouse("right","click","")

def onBoxChange(box, edge):
    if (myo.isUnlocked()) and (myo.get_active_window_title()=="\"Vipers\""):
        direction = myo.getBox()
        print direction
        if direction == 1:
            myo.keyboard("w","press","") 
        if direction == 3:
            myo.keyboard("d","press","") 
        if direction == 5:
            myo.keyboard("s","press","") 
        if direction == 7:
            myo.keyboard("a","press","") 
