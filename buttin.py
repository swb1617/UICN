from selenium.webdriver.common.by import By


class Menu:

    def GetMenuTitle(self):  # 首页标题
        MenuTitle = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout[ "
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.TextView[1]")
        return MenuTitle

    def GetMenuMessageInto(self):  # 首页消息按钮
        MessageInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout[ "
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout[ "
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout[ "
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.view.ViewGroup[1]")
        return MessageInto

    def GetMenuFriendInto(self):  # 首页好友按钮
        FriendInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.view.ViewGroup[2]")
        return FriendInto

    def GetMenuFriendBack(self):
        MenuFriendBack = self.driver.find_element(by=By.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]")
        return MenuFriendBack

    def GetMenuTrainingGoalsInto(self):  # 首页修改训练按钮
        TrainingGoalsInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.view.ViewGroup["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout[1]")
        return TrainingGoalsInto

    def GetMenuMonthGoals(self):  # 首页月骑行目标数据（float）
        MonthGoals = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.TextView[4]")
        return MonthGoals

    def GetMenuFirstData(self):  # 首页第一天数据
        FirstData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "2]/android.widget.FrameLayout["
                                                                "1]/androidx.recyclerview.widget.RecyclerView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return FirstData

    def GetMenuSecondData(self):  # 首页第二条数据
        SecondData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "2]/android.widget.FrameLayout["
                                                                 "1]/androidx.recyclerview.widget.RecyclerView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "2]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.LinearLayout[1]")
        return SecondData

    def GetMenuThirData(self):  # 首页第三条数据
        ThirdData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "2]/android.widget.FrameLayout["
                                                                "1]/androidx.recyclerview.widget.RecyclerView["
                                                                "1]/android.widget.LinearLayout["
                                                                "3]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return ThirdData

    def GetMenuFirstTraining(self):  # 首页第一条训练
        FirstTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.view.ViewGroup["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "2]/android.widget.FrameLayout["
                                                                    "1]/androidx.recyclerview.widget.RecyclerView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.LinearLayout[1]")
        return FirstTraining

    def GetMenuSecondTraining(self):  # 首页第二条训练
        SecondTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.FrameLayout["
                                                                     "1]/androidx.recyclerview.widget.RecyclerView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.LinearLayout[1]")
        return SecondTraining

    def GetMenuThirdTraining(self):  # 首页第三条训练
        ThirdTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.view.ViewGroup["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "2]/android.widget.FrameLayout["
                                                                    "1]/androidx.recyclerview.widget.RecyclerView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "3]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.LinearLayout[1]")
        return ThirdTraining


class Message:
    def GetMeaagaeBack(self):  # 消息页返回按钮
        MessageBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.LinearLayout[1]")
        return MessageBack

    def GetMessageRead(self):  # 信息已读按钮
        MessageRead = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.RelativeLayout[1]")
        return MessageRead


class Data:
    def GetDataBack(self):  # 详情页返回按钮
        DataBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout[1]")
        return DataBack

    def GetDataShare(self):  # 详情也分享按钮
        DataShare = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.ImageView[2]")
        return DataShare

    def GetDataShareBack(self):  # 详情页分享返回按钮
        DataShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.ImageView[1]")
        return DataShareBack

    def GetDataMenuToSendFriendAddFriend(self):
        DataMenuToSendFriendAddFriend = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button")
        return DataMenuToSendFriendAddFriend

    def GetDataShareWatermarkPhoto(self):  # 详情页分享水印照片按钮
        DataShareWatermarkPhoto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout[3]")
        return DataShareWatermarkPhoto

    def GetDataWatermarkPhotoChangePhoto(self):
        DataWatermarkPhotoChangePhoto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".ScrollView/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".TextView[2]")
        return DataWatermarkPhotoChangePhoto

    def GetDataWatermarkPhotoChoosePhoto(self):
        DataWatermarkPhotoChoosePhoto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".RelativeLayout/androidx"
                                                                                    ".recyclerview.widget"
                                                                                    ".RecyclerView/android.widget"
                                                                                    ".RelativeLayout["
                                                                                    "2]/android.widget.TextView")
        return DataWatermarkPhotoChoosePhoto

    def GetDataWatermarkRestoreDefault(self):
        DataWatermarkRestoreDefault = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".FrameLayout/android.widget"
                                                                                  ".ScrollView/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".LinearLayout/android.widget"
                                                                                  ".TextView[1]")
        return DataWatermarkRestoreDefault

    def GetDataWatermarkPhotoSave(self):
        DataWatermarkPhotoSave = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout"
                                                                             "/android.widget.LinearLayout/android"
                                                                             ".widget.FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".FrameLayout/android.widget"
                                                                             ".LinearLayout/android.widget"
                                                                             ".LinearLayout[1]")
        return DataWatermarkPhotoSave

    def GetDataWatermarkPhotoSeePhoto(self):
        GetDataWatermarkPhotoSeePhoto = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".LinearLayout/android.widget"
                                                                                    ".FrameLayout/android.widget"
                                                                                    ".RelativeLayout/android.widget"
                                                                                    ".RelativeLayout["
                                                                                    "2]/android.widget.TextView[3]")
        return GetDataWatermarkPhotoSeePhoto

    def GetDataWatermarkPhotoBack(self):  # 水印照片返回按钮
        DataWatermarkPhotoBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return DataWatermarkPhotoBack

    def GetDataWatermarkPhotoData(self):  # 水印照片第一tap
        DataWatermarkPhotoData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.HorizontalScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return DataWatermarkPhotoData

    def GetDataWatermarkPhotoAlt(self):  # 水印照片第二tap
        DataWatermarkPhotoAlt = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.ScrollView["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.HorizontalScrollView["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout[2]")
        return DataWatermarkPhotoAlt

    def GetDataWatermarkPhotoTrack(self):  # 水印照片第三tap
        DataWatermarkPhotoTrack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.ScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.HorizontalScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout[3]")
        return DataWatermarkPhotoTrack

    def GetDataMenuInfo(self):  # 详情页菜单按钮
        DataMenuInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.ImageView[3]")
        return DataMenuInfo

    def GetDataName(self):  # 详情页数据名称
        DataName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "2]/android.widget.LinearLayout["
                                                               "2]/android.widget.TextView[2]")
        return DataName

    def GetDataDistance(self):  # 详情页里程
        DataDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.ScrollView["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "2]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/androidx.recyclerview.widget.RecyclerView["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.TextView[1]")
        return DataDistance

    def GetDataMapStyleInto(self):  # 详情页切换地图样式按钮
        DataMapStyleInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.ImageView[1]")
        return DataMapStyleInto

    def GetDataMapStyleMode(self):  # 地图样式Dark
        DataMapStyleMode = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "4]/android.widget.ImageView[1]")
        return DataMapStyleMode

    def GetDataMapStyleSave(self):  # 保存地图样式
        DataMapStyleSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.Button[1]")
        return DataMapStyleSave

    def GetDataMapStyleGoals(self):  # 公里点打开关闭按钮
        DataMapStyleGoals = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]/android.widget.Switch["
                                                                        "1]")
        return DataMapStyleGoals

    def GetDataMenuToEditActivity(self):  # 修改活动名称
        DataEditActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataEditActivity

    def GetDataSwitchChart(self):
        DataSwitchChart = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "2]/android.view.ViewGroup["
                                                                      "1]/android.widget.FrameLayout[2]")
        return DataSwitchChart

    def GetDataSwitchingDetails(self):
        DataSwitchingDetails = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "2]/android.view.ViewGroup["
                                                                           "1]/android.widget.FrameLayout[3]")
        return DataSwitchingDetails

    def GetDataMenuToSaveMyLine(self):  # 保存到我的线路
        DataMenuToSaveMyLine = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[2]")
        return DataMenuToSaveMyLine

    def GetDataMenuToSendFriend(self):  # 发送给好友
        DataMenuToSendFriend = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[3]")
        return DataMenuToSendFriend

    def GetDataMenuToExportFile(self):  # 保存数据到文件
        DataMenuToExportFile = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[4]")
        return DataMenuToExportFile

    def GetDataMenuToDeleteData(self):  # 删除数据按钮
        DataMenuToDeleteData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[5]")
        return DataMenuToDeleteData

    def GetDataLineNumber(self):
        DataLineNumber = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.TextView[2]")
        return DataLineNumber

    def GetDataLineDistance(self):
        DataLineDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "2]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataLineDistance

    def GetDataRidingTime(self):
        DataRidingTime = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "2]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/androidx.recyclerview.widget.RecyclerView["
                                                                     "1]/android.widget.RelativeLayout["
                                                                     "2]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.TextView[1]")
        return DataRidingTime

    def GetDataAverageVelocity(self):
        DataAverageVelocity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.ScrollView["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "2]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/androidx.recyclerview.widget"
                                                                          ".RecyclerView["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "3]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.TextView[1]")
        return DataAverageVelocity

    def GetDataMaximumSpeed(self):
        DataMaximumSpeed = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "2]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "4]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataMaximumSpeed

    def GetDataAverageHeartRate(self):
        DataAverageHeartRate = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "2]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/androidx.recyclerview.widget"
                                                                           ".RecyclerView["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "5]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[1]")
        return DataAverageHeartRate

    def GetDataAverageStepFrequency(self):
        DataAverageStepFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.RelativeLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.ScrollView["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "2]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/androidx.recyclerview.widget"
                                                                               ".RecyclerView["
                                                                               "1]/android.widget.RelativeLayout["
                                                                               "6]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.TextView[1]")
        return DataAverageStepFrequency

    def GetDataCalorie(self):
        DataCalorie = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.ScrollView["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "2]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/androidx.recyclerview.widget.RecyclerView["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "14]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.TextView[1]")
        return DataCalorie

    def GetDataChartSpeedChart(self):
        DataChartSpeedChart = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.ScrollView["
                                                                          "1]/androidx.recyclerview.widget"
                                                                          ".RecyclerView["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "2]/android.view.ViewGroup[1]")
        return DataChartSpeedChart

    def GetDataEquipmentModel(self):
        DataEquipmentModel = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.ScrollView["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.LinearLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "2]/android.widget.TextView[1]")
        return DataEquipmentModel

    def GetDataDeviceVersion(self):
        DataDeviceVersion = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "2]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "2]/android.widget.TextView[2]")
        return DataDeviceVersion

    def GetDataEditText(self):  # 数据修改名字文本框
        DataEditActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.RelativeLayout[2]")
        return DataEditActivity

    def GetDataEditSave(self):  # 数据修改名字保存
        DataEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.view.ViewGroup["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.TextView[3]")
        return DataEditSave

    def GetDataSendToFriendText(self):  # 好友id输入框
        DataSendToFriendText = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout[1]")
        return DataSendToFriendText

    def GetDataSendToFriend(self):  # 发送给好友按钮
        DataSendToFriend = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.TextView[2]")
        return DataSendToFriend

    def GetDataSendMessageBack(self):  # 消息界面返回
        DataSendMessageBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.view.ViewGroup["
                                                                          "1]/androidx.recyclerview.widget"
                                                                          ".RecyclerView["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "2]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.LinearLayout[1]")
        return DataSendMessageBack

    def GetDataSendMessageFriendName(self):  # 消息界面好友的名字
        DataSendMessageFriendName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout[1]")
        return DataSendMessageFriendName

    def GetDataSendFriendName(self):  # 发送给好友的名字
        DataSendFriendName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/androidx.recyclerview.widget"
                                                                         ".RecyclerView["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.TextView[1]")
        return DataSendFriendName

    def GetDataExportDataBack(self):  # 数据导出返回
        DataExportDataBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return DataExportDataBack

    def GetDataExportDataFit(self):  # fit文件格式
        DataExportDataFit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return DataExportDataFit

    def GetDataExportDataGpx(self):  # gpx格式
        DataExportDataGpx = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "2]/android.widget.LinearLayout[1]")
        return DataExportDataGpx

    def GetDataExportDataTcx(self):  # 数据导出界面tcx文件格式
        DataExportDataTcx = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "3]/android.widget.LinearLayout[1]")
        return DataExportDataTcx

    def GetDataExportDataDowload(self):  # 数据导出下载按钮
        DataExportDataDowload = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.Button[2]")

        return DataExportDataDowload

    def GetDataExportDataSave(self):  # 数据导出保存
        DataExportDataSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.view.ViewGroup["
                                                                         "1]/android.support.v4.widget.DrawerLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.TextView[1]")
        return DataExportDataSave

    def GetDataDeleteDataOk(self):
        DataDeleteDataOk = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "2]/android.widget.Button[2]")
        return DataDeleteDataOk


class Activity:
    def GetActivityTotalFrequency(self):
        ActivityTotalFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "2]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[1]")
        return ActivityTotalFrequency

    def GetActivityTotalDuration(self):
        ActivityTotalDuration = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "2]/android.widget.LinearLayout["
                                                                            "2]/android.widget.LinearLayout["
                                                                            "1]/android.widget.TextView[1]")
        return ActivityTotalDuration

    def GetActivityTotalAverageVelocity(self):
        ActivityTotalAverageVelocity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "2]/android.widget.LinearLayout["
                                                                                   "3]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.TextView[1]")
        return ActivityTotalAverageVelocity

    def GetActivityMonthFrequency(self):
        ActivityMonthFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "2]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[3]")
        return ActivityMonthFrequency

    def GetActivityTotalDistance(self):  # 活动界面总计里程
        ActivityTotalDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.TextView[1]")
        return ActivityTotalDistance

    def GetActivityCalendarInfo(self):  # 活动界面日历入口
        ActivityCalendarInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return ActivityCalendarInfo

    def GetActivityShareInfo(self):  # 活动界面分享入口
        ActivityShareInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[2]")
        return ActivityShareInfo

    def GetActivityDataStatisticInfo(self):  # 活动界面数据管理入口
        ActivityDataStatisticInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "3]/android.widget.LinearLayout[1]")
        return ActivityDataStatisticInfo

    def GetActivityDataStatisticBack(self):  # 活动界面数据管理入口
        ActivityDataStatisticBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.RelativeLayout["
                                                                               "1]/android.widget.LinearLayout[1]")
        return ActivityDataStatisticBack

    def GetActivityDataStatisticWeek(self):
        ActivityDataStatisticWeek = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.ScrollView["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.Button[1]")
        return ActivityDataStatisticWeek

    def GetActivityDataStatisticMonth(self):
        ActivityDataStatisticMonth = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.ScrollView["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "2]/android.widget.Button[1]")
        return ActivityDataStatisticMonth

    def GetActivityDataStatisticYear(self):
        ActivityDataStatisticYear = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.ScrollView["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "3]/android.widget.Button[1]")
        return ActivityDataStatisticYear

    def GetActivityDataStatisticAll(self):
        ActivityDataStatisticAll = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.ScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "4]/android.widget.Button[1]")
        return ActivityDataStatisticAll

    def GetActivityDataStatisticAllDistances(self):
        ActivityDataStatisticAllDistances = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.ScrollView["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "3]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.TextView[1]")
        return ActivityDataStatisticAllDistances

    def GetActivityDataStatisticAllFrequency(self):
        ActivityDataStatisticAllFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.ScrollView["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "3]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "2]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.TextView[2]")
        return ActivityDataStatisticAllFrequency

    def GetActivityDataStatisticAllDuration(self):
        ActivityDataStatisticAllDuration = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                      "1]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "1]/android.widget.FrameLayout["
                                                                                      "1]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "1]/android.widget.FrameLayout["
                                                                                      "1]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "1]/android.widget.ScrollView["
                                                                                      "1]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "1]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "3]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "2]/android.widget"
                                                                                      ".LinearLayout["
                                                                                      "2]/android.widget.TextView[2]")
        return ActivityDataStatisticAllDuration

    def GetActivityDataStatisticAllAverageVelocity(self):
        ActivityDataStatisticAllAverageVelocity = self.driver.find_element(by=By.XPATH, value="//android.widget"
                                                                                             ".FrameLayout["
                                                                                             "1]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "1]/android.widget"
                                                                                             ".FrameLayout["
                                                                                             "1]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "1]/android.widget"
                                                                                             ".FrameLayout["
                                                                                             "1]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "1]/android.widget"
                                                                                             ".ScrollView["
                                                                                             "1]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "1]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "3]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "2]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "3]/android.widget"
                                                                                             ".LinearLayout["
                                                                                             "1]/android.widget"
                                                                                             ".TextView[1]")
        return ActivityDataStatisticAllAverageVelocity

    def GetActivityDataStatisticMonthFrequency(self):
        ActivityDataStatisticMonthFrequency = self.driver.find_element(by=By.XPATH, value="//android.widget"
                                                                                         ".FrameLayout["
                                                                                         "1]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "1]/android.widget"
                                                                                         ".FrameLayout["
                                                                                         "1]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "1]/android.widget"
                                                                                         ".FrameLayout["
                                                                                         "1]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "1]/android.widget"
                                                                                         ".ScrollView["
                                                                                         "1]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "1]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "3]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "2]/android.widget"
                                                                                         ".LinearLayout["
                                                                                         "1]/android.widget.TextView["
                                                                                         "2]")
        return ActivityDataStatisticMonthFrequency

    def GetActivityPersonalRecordsInfo(self):  # 活动界面个人记录入口
        ActivityPersonalRecordsInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "3]/android.widget.LinearLayout[2]")
        return ActivityPersonalRecordsInfo

    def GetActivityCalendarBack(self):  # 日历界面返回
        ActivityCalendarBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return ActivityCalendarBack

    def GetActivityCalendarGoalsEdit(self):  # 编辑月骑行目标按钮
        ActivityCalendarGoalsEdit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.RelativeLayout[1]")
        return ActivityCalendarGoalsEdit

    def GetActivityCalendarGoalsEditText(self):  # 骑行目标输入框
        ActivityCalendarGoalsEditText = self.driver.find_element(by=By.ID,
                                                                 value="com.igpsport.igpsportandroid:id/et_goal")
        return ActivityCalendarGoalsEditText

    def GetActivityCalendarGoalsEditSave(self):  # 骑行目标保存
        ActivityCalendarGoalsEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.RelativeLayout["
                                                                                    "1]/android.widget.Button[1]")
        return ActivityCalendarGoalsEditSave

    def GetActivityShareBack(self):  # 活动界面分享返回
        ActivityShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareBack

    def GetActivityShareSave(self):  # 活动界面分享保存
        ActivityShareSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareSave

    def GetActivityPersonalRecordsBack(self):  # 个人纪录返回
        ActivityPersonalRecordsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.RelativeLayout["
                                                                                  "1]/android.widget.LinearLayout[1]")
        return ActivityPersonalRecordsBack

    def GetActivityPersonalRecordsShare(self):  # 个人记录分享
        ActivityPersonalRecordsShare = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.RelativeLayout["
                                                                                   "1]/android.widget.RelativeLayout["
                                                                                   "1]")
        return ActivityPersonalRecordsShare

    def GetActivityPersonalRecordsShareBack(self):  # 个人记录分享返回
        ActivityPersonalRecordsShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".RelativeLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout[1]")
        return ActivityPersonalRecordsShareBack


class Tap:
    def GetToHome(self):
        ToHome = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout[2]/android.view.ViewGroup["
                                                             "1]/android.widget.FrameLayout[1]")
        return ToHome

    def GetToActivity(self):
        ToActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "2]/android.view.ViewGroup["
                                                                 "1]/android.widget.FrameLayout[2]")
        return ToActivity

    def GetToDevice(self):
        ToDevice = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "2]/android.view.ViewGroup["
                                                               "1]/android.widget.FrameLayout[3]")
        return ToDevice

    def GetToMe(self):
        ToMe = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout[2]/android.view.ViewGroup["
                                                           "1]/android.widget.FrameLayout[4]")
        return ToMe


class Me:
    def GetMeUserName(self):
        MeUserName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.TextView[1]")
        return MeUserName

    def GetMeUserId(self):
        MeUserId = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout[1]/android.view.ViewGroup["
                                                               "1]/android.widget.ScrollView["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.TextView[2]")
        return MeUserId

    def GetFollowNumber(self):
        FollowNumber = self.driver.find_element(by=By.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
        return FollowNumber

    def GetMeFeedBackTitle(self):
        MeFeedBackTitle = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
        return MeFeedBackTitle

    def GetMEUserDetailsInfo(self):
        MeUserDetailsInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.view.ViewGroup["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return MeUserDetailsInfo

    def GetMeUserSex(self):
        MeUserSex = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "3]/android.widget.LinearLayout["
                                                                "1]/android.widget.TextView[1]")
        return MeUserSex

    def GetMeUserSexInfo(self):
        MeUserSexInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout[3]")
        return MeUserSexInfo

    def GetMeUserSexSave(self):
        MeUserSexSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.Button[2]")
        return MeUserSexSave

    def GetMeSettingHRInfo(self):
        MeSettingHRInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout[8]")
        return MeSettingHRInfo

    def GetMeSettingHR(self):
        MeSettingHR = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "2]/android.widget.RelativeLayout["
                                                                  "2]/android.widget.Button[1]")
        return MeSettingHR

    def GetMeSettingHRBack(self):
        MeSettingHRBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.LinearLayout[1]")
        return MeSettingHRBack

    def GetMeSettingPowerInfo(self):
        MeSettingPowerInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.ScrollView["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout[9]")
        return MeSettingPowerInfo

    def GetMeSettingPower(self):
        MeSettingPower = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.RelativeLayout["
                                                                     "2]/android.widget.Button[1]")
        return MeSettingPower

    def GetMeSettingPowerBack(self):
        MeSettingPowerBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return MeSettingPowerBack

    def GetMeAccountSettingInfo(self):
        MeAccountSettingInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.view.ViewGroup["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "3]/android.widget.RelativeLayout[2]")
        return MeAccountSettingInfo

    def GetMeLanguageMessage(self):
        MeLanguageMessage = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.TextView[2]")
        return MeLanguageMessage

    def GetMeRidingRankInfo(self):
        MeRidingRankInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "3]/android.widget.RelativeLayout[3]")
        return MeRidingRankInfo

    def GetMeRidingRankBack(self):
        MeRidingRankBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout[1]")
        return MeRidingRankBack

    def GetMeAfterSaleServiceInfo(self):
        MeAfterSaleServiceInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.view.ViewGroup["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "3]/android.widget.RelativeLayout[4]")
        return MeAfterSaleServiceInfo

    def GetMeNotification(self):
        MeNotification = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "3]/android.widget.RelativeLayout[5]")
        return MeNotification

    def GetMeAboutUs(self):
        MeAboutUs = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "3]/android.widget.RelativeLayout[7]")
        return MeAboutUs

    def GetMeUserDetailsBack(self):
        MeUserDetailsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return MeUserDetailsBack

    def GetMeUserGoalsEdit(self):
        MeUserGoalsEdit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout[10]")
        return MeUserGoalsEdit

    def GetMeUserGoalsText(self):
        MeUserGoalsText = self.driver.find_element(by=By.ID, value="com.igpsport.igpsportandroid:id/et_goal")
        return MeUserGoalsText

    def GetMeUserGoalsSave(self):
        MeUserGoalsSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.Button[1]")
        return MeUserGoalsSave

    def GetMeAboutUsBack(self):
        MeAboutUsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.ImageView[1]")
        return MeAboutUsBack

    def GetMeNotificationBack(self):
        MeNotificationBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return MeNotificationBack

    def GetMeAfterSaleServiceBack(self):
        MeAfterSaleServiceBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return MeAfterSaleServiceBack

    def GetMeAfterSaleServiceFeedBack(self):
        MeAfterSaleServiceFeedBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.RelativeLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.RelativeLayout[5]")
        return MeAfterSaleServiceFeedBack

    def GetMeFeedBackQuestionType(self):
        MeFeedBackQuestionType = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[2]")
        return MeFeedBackQuestionType

    def GetMeFeedBackQuestionList1(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[1]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList2(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[2]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList3(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[3]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList4(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[4]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList5(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[5]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList6(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[6]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList7(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[7]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList8(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[8]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionList9(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[9]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionLista(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[10]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionListb(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[11]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionText(self):
        MeFeedBackQuestionText = self.driver.find_element(by=By.ID, value="com.igpsport.igpsportandroid:id/etProblem")
        return MeFeedBackQuestionText

    def GetMeFeedBackPictureAdd(self):
        MeFeddbackPictureAdd = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/androidx.recyclerview.widget"
                                                                           ".RecyclerView["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.ImageView[1]")
        return MeFeddbackPictureAdd

    def GetMeFeedBackPictureChoose(self):
        MeFeedBackPictureChoose = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.RelativeLayout["
                                                                              "1]/androidx.recyclerview.widget"
                                                                              ".RecyclerView["
                                                                              "1]/android.widget.RelativeLayout["
                                                                              "2]/android.widget.TextView[1]")
        return MeFeedBackPictureChoose

    def GetMeFeedBackPictureSave(self):
        MeFeedBackPictureSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "2]/android.widget.TextView[3]")
        return MeFeedBackPictureSave

    def GetMeFeedBackTLEText(self):
        MeFeedBackTLEText = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.EditText[2]")
        return MeFeedBackTLEText

    def GetMeFeedBackSubmit(self):
        MeFeedBackSubmit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.Button[1]")
        return MeFeedBackSubmit

    def GetMeAccountSettingBack(self):
        MeAccountSettingBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return MeAccountSettingBack

    def GetMeAccountSettingSave(self):
        MeAccountSettingSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout[1]")
        return MeAccountSettingSave

    def GetMeLanguageSetting(self):
        MeLanguageSetting = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout[1]")
        return MeLanguageSetting

    def GetMeLanguageSettingSave(self):
        MeLanguageSettingSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "1]/android.widget.Button[2]")
        return MeLanguageSettingSave

    def GetMeResetPasswordInfo(self):
        MeResetPasswordInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.RelativeLayout[2]")
        return MeResetPasswordInfo

    def GetMeOldPasswordText(self):
        MeOldPasswordText = self.driver.find_element(by=By.ID, value="com.igpsport.igpsportandroid:id"
                                                                     "/edt_pwd_old_update_password")
        return MeOldPasswordText

    def GetMeNemPasswordText(self):
        MeNemPasswordText = self.driver.find_element(by=By.ID, value="com.igpsport.igpsportandroid:id"
                                                                     "/edt_pwd_new_update_password")
        return MeNemPasswordText

    def GetMeAgainNemPasswordText(self):
        MeAgainNemPasswordText = self.driver.find_element(by=By.ID, value="com.igpsport.igpsportandroid:id"
                                                                          "/edt_pwd_new2_update_password")
        return MeAgainNemPasswordText

    def GetMeConfirmPassword(self):
        MeConfirmPassword = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.Button[1]")
        return MeConfirmPassword

    def GetMeResetPasswordBack(self):
        MeResetPasswordBAck = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout"
                                                                          "/android.widget.LinearLayout/android"
                                                                          ".widget.FrameLayout/android.widget"
                                                                          ".LinearLayout/android.widget.FrameLayout"
                                                                          "/android.widget.LinearLayout/android"
                                                                          ".widget.RelativeLayout/android.widget"
                                                                          ".ImageView")
        return MeResetPasswordBAck


class ComposeTest:
    def GetDeviceRoutesAdd(self):
        DeviceRoutesAdd = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/androidx.recyclerview.widget.RecyclerView["
                                                                      "1]/android.widget.LinearLayout[4]")
        return DeviceRoutesAdd

    def GetDeviceCreateRoutes(self):
        DeviceCreateRoutes = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/androidx.compose.ui.platform.ComposeView["
                                                                         "1]/android.view.View[1]/android.view.View["
                                                                         "2]/android.view.View[1]")
        return DeviceCreateRoutes

    def GetDeviceFirstRoutes(self):
        DeviceFirstRoutes = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/androidx.compose.ui.platform.ComposeView["
                                                                        "1]/android.view.View[1]/android.view.View["
                                                                        "4]/android.view.View[1]/android.view.View["
                                                                        "1]/android.view.View[1]")
        return DeviceFirstRoutes


class ErrorHappen:
    def GetDataNetError(self):
        DataNetError = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout[ "
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout[1]")
        return DataNetError

    def GetDataNetErrorOk(self):
        DataNetErrorOk = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout[ "
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout[ "
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.Button[1]")
        return DataNetErrorOk

    def GetDataError(self):
        DataError = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout[ "
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout[ "
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.ScrollView["
                                                                "2]/android.widget.LinearLayout[ "
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return DataError

    def GetDataErrorLayout(self):
        DataErrorLayout = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout[ "
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout[1]")
        return DataErrorLayout

    def GetDataErrorFeedBack(self):
        DataErrorFeedback = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.TextView[1]")
        return DataErrorFeedback

    def GetDataErrorOk(self):
        DataErrorOk = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.TextView[2]")
        return DataErrorOk

class Friend:
    def GetFriendFirstPeopleName(self):
        FriendFirstPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]")
        return FriendFirstPeopleName

    def GetFriendFirstPeopleDistance(self):
        FriendFirstPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[4]")
        return FriendFirstPeopleDistance

    def GetFriendFirstPeopleFollow(self):
        FriendFirstPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[6]/android.widget.Button")
        return FriendFirstPeopleFollow

    def GetFriendSecondPeopleName(self):
        FriendSecondPeopleName = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]")
        return FriendSecondPeopleName

    def GetFriendSecondPeopleDistance(self):
        FriendSecondPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[4]")
        return FriendSecondPeopleDistance

    def GetFriendSecondPeopleFollow(self):
        FriendSecondPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[6]/android.widget.Button")
        return FriendSecondPeopleFollow

    def GetFriendThirdPeopleName(self):
        FriendThirdPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]")
        return FriendThirdPeopleName

    def GetFriendThirdPeopleDistance(self):
        FriendThirdPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[4]")
        return FriendThirdPeopleDistance

    def GetFriendThirdPeopleFollow(self):
        FriendThirdPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[6]/android.widget.Button")
        return FriendThirdPeopleFollow

    def GetFriendFourthPeopleName(self):
        FriendFourthPeopleName = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[2]")
        return FriendFourthPeopleName

    def GetFriendFourthPeopleDistance(self):
        FriendFourthPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[4]")
        return FriendFourthPeopleDistance

    def GetFriendFourthPeopleFollow(self):
        FriendFourthPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[6]/android.widget.Button")
        return FriendFourthPeopleFollow

    def GetFriendFifthPeopleName(self):
        FriendFifthPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]")
        return FriendFifthPeopleName

    def GetFriendFifthPeopleDistance(self):
        FriendFifthPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[4]")
        return FriendFifthPeopleDistance

    def GetFriendFifthPeopleFollow(self):
        FriendFifthPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[6]/android.widget.Button")
        return FriendFifthPeopleFollow

    def GetFriendSixthPeopleName(self):
        FriendSixthPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[2]")
        return FriendSixthPeopleName

    def GetFriendSixthPeopleDistance(self):
        FriendSixthPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[4]")
        return FriendSixthPeopleDistance

    def GetFriendSixthPeopleFollow(self):
        FriendSixthPeopleFollow = self.driver.find_element(by=By.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[5]/android.view.View[3]/android.view.View[6]/android.widget.Button")
        return FriendSixthPeopleFollow

    def GetFriendSeekFriendId(self):
        FriendSeekFriendId = self.driver.find_element(by=By.XPATH,
                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[3]")
        return FriendSeekFriendId

    def GetFriendSeekText(self):
        FriendSeektext = self.driver.find_element(by=By.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
        return FriendSeektext

    def GetFriendSeekFriendFollow(self):
        FriendSeekFriendFollow = self.driver.find_element(by=By.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[6]/android.widget.Button")
        return FriendSeekFriendFollow

    def GetFriendUnderFirstPeopleName(self):
        FriendUnderFirstPeopleName = self.driver.find_element(by=By.XPATH,
                                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[2]")
        return FriendUnderFirstPeopleName

    def GetFriendUnderFirstPeopleDistance(self):
        FriendUnderFristPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[4]")
        return FriendUnderFristPeopleDistance

    def GetFriendUnderFirstPeopleFollowed(self):
        FriendUnderFirstPeopleFollowed = self.driver.find_element(by=By.XPATH,
                                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[6]/android.widget.Button")
        return FriendUnderFirstPeopleFollowed

    def GetFriendUnderSecondPeopleName(self):
        FriendUnderSecondPeopleName = self.driver.find_element(by=By.XPATH,
                                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[8]")
        return FriendUnderSecondPeopleName

    def GetFriendUnderSecondPeopleDistance(self):
        FriendUnderSecondPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[10]")
        return FriendUnderSecondPeopleDistance

    def GetFriendUnderSecondPeopleFollowed(self):
        FriendUnderSecondPeopleFollowed = self.driver.find_element(by=By.XPATH,
                                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[8]/android.view.View[12]/android.widget.Button")
        return FriendUnderSecondPeopleFollowed

    def GetFriendUnderPeopleChanged(self):
        FriendUnderPeopleChanged = self.driver.find_element(by=By.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[7]/android.widget.Button")
        return FriendUnderPeopleChanged


class Follow:

    def GetFollowInfo(self):
        FollowInfo = self.driver.find_element(by=By.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        return FollowInfo

    def GetFollowBack(self):
        FollowBack = self.driver.find_element(by=By.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[1]")
        return FollowBack

    def GetFollowFirstPeopleName(self):
        FollowFirstPeopleName = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        return FollowFirstPeopleName

    def GetFollowFirstPeopleId(self):
        FollowFirstPeopleId = self.driver.find_element(by=By.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
        return FollowFirstPeopleId

    def GetFollowFirstPeopleDistance(self):
        FollowFirstPeopleDistance = self.driver.find_element(by=By.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]")
        return FollowFirstPeopleDistance

    def GetFollowFirstPeopleInfo(self):
        FollowFirstPeopleInfo = self.driver.find_element(by=By.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout")
        return FollowFirstPeopleInfo


class People:
    def GetPeopleName(self):
        PeopleName = self.driver.find_element(by=By.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        return PeopleName

    def GetPeopleId(self):  # 问题 无法打开关注粉丝列表
        PeopleId = self.driver.find_element(by=By.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]")
        return PeopleId

    def GetPeopleDistance(self):
        PeopleDistance = self.driver.find_element(by=By.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]")
        return PeopleDistance

    def GetPeopleFollowed(self):
        PeopleFollowed = self.driver.find_element(by=By.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        return PeopleFollowed

    def GetPeopleBack(self):
        PeopleBack = self.driver.find_element(by=By.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
        return PeopleBack
