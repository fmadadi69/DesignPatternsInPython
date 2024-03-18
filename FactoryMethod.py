class Interviewer:
    def makeInterview(self):
        pass


class Developer(Interviewer):
    def makeInterview(self):
        print(f"Interview is done by a developer")


class CommunityExecutive(Interviewer):
    def makeInterview(self):
        print(f"Interview is done by a community executive")


class HiringManager:
    def chooseInterviewer(self):
        pass

    def takeInterview(self):

        interviewer = self.chooseInterviewer()
        interviewer.makeInterview()


class DevelopmentManager(HiringManager):
    def chooseInterviewer(self):
        return Developer()


class MarketingManager(HiringManager):
    def chooseInterviewer(self):
        return CommunityExecutive()


devManager = DevelopmentManager()
devManager.takeInterview()

marketingManager = MarketingManager()
marketingManager.takeInterview()





