import time
def onUnlock():
	myo.rotSetCenter()
	myo.unlock("hold")
	
def onPoseEdge(pose, edge):
    print("onPoseEdge: "+pose+", "+edge)

def onPeriodic():
    if(myo.isUnlocked()):
        print myo.get_active_window_title()
        time.sleep(0.5)

