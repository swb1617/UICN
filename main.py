"""
user:石文斌
time：2021/12/06

"""
import time
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from buttin import ComposeTest, Me, Menu, Message, Activity, Tap, Data


class test_UI(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.driver.implicitly_wait(15)  # 稳定元素
        time.sleep(3)
        # print("...........开始.............")

    def tearDown(self) -> None:  # 执行方法后工作
        time.sleep(3)
        self.driver.close_app()
        time.sleep(1)
        self.driver.start_activity('com.igpsport.igpsportandroid', 'com.igpsport.globalapp.activity.v3.SplashActivity')
        time.sleep(1)
        # print("...........结束..............")

    @classmethod
    def setUpClass(cls) -> None:  # 执行测试类前准备工作
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'swb',
            'appPackage': 'com.igpsport.igpsportandroid',
            'appActivity': 'com.igpsport.globalapp.activity.v3.SplashActivity',
            'noReset': True,
            'newCommandTimeout': 6000,
            # 更换底层驱动
            'automationName': 'UiAutomator2',
            'unicodeKeyboard': True,  # 修改手机的输入法
            'resetKeyboard': True
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def SwipeDown(self):  # 定义下滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.5
        y1, y2 = height * 0.35, height * 0.7
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def SwipeLittleUp(self):  # 定义上滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.7
        y1, y2 = height * 0.89, height * 0.86
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def SwipeLittleDown(self):  # 定义上滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.7
        y1, y2 = height * 0.9, height * 0.95
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def GetToast(self, toast_message):
        message = '//*[@text=\'{}\']'.format(toast_message)
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(by=By.XPATH, value=message))
        print(f'toast：', toast_element.text)
        assert toast_element.text == toast_message

    def test_MenuMessage(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuMessageInto(self).click()
            Message.GetMessageRead(self).click()
            Message.GetMeaagaeBack(self).click()
        except:
            self.driver.save_screenshot('MenuMessageError.png')
            raise

    def test_MenuGoals(self):
        MonthGoals = 777
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuTrainingGoalsInto(self).click()
            Me.GetMeUserGoalsText(self).click()
            Me.GetMeUserGoalsText(self).clear()
            Me.GetMeUserGoalsText(self).send_keys(MonthGoals)
            Me.GetMeUserGoalsSave(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MenuGoalsError.png')
            raise

    def test_ChangeMapStyle(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMapStyleInto(self).click()
            Data.GetDataMapStyleMode(self).click()
            Data.GetDataMapStyleSave(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ChangeMapStyleError.png')
            raise

    def test_OpenMapGoals(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMapStyleInto(self).click()
            Data.GetDataMapStyleGoals(self).click()
            Data.GetDataMapStyleSave(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('OpenMapGoalsError.png')
            raise

    def test_SaveMyLine(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(4)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToSaveMyLine(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(3)
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('SaveMyLineError.png')
            raise

    @unittest.skip
    def test_ExportDataFit(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataFit(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataFitError.png')
            raise

    @unittest.skip
    def test_ExportDataGpx(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataGpx(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataGpxError.png')
            raise

    @unittest.skip
    def test_ExportDataTcx(self):  # 导出数据
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToExportFile(self).click()
            Data.GetDataExportDataTcx(self).click()
            Data.GetDataExportDataDowload(self).click()
            Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
            time.sleep(3)
            Data.GetDataExportDataBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ExportDataTcxError.png')
            raise

    @unittest.skip("删除数据")
    def test_DeleteData(self):
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(3)
            Data.GetDataMenuInfo(self).click()
            Data.GetDataMenuToDeleteData(self).click()
            Data.GetDataDeleteDataOk(self).click()
            time.sleep(3)
        except:
            self.driver.save_screenshot('DeleteDataError.png')
            raise

    def test_ShareWatermarkData(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            # Data.GetDataWatermarkPhotoChangePhoto(self).click()
            # Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            # Data.GetDataWatermarkPhotoSeePhoto(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkDataError.png')
            raise

    def test_ShareWatermarkDataDefault(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkDataDefaultError.png')
            raise

    def test_ShareWatermarkDataChoose(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkDataChooseError.png')
            raise

    def test_ShareWatermarkTrack(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            # Data.GetDataWatermarkPhotoChangePhoto(self).click()
            # Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            # Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkTrackError.png')
            raise

    def test_ShareWatermarkTrackDefault(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkTrackDefaultError.png')
            raise

    def test_ShareWatermarkTrackChoose(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(2)
            Data.GetDataShareWatermarkPhoto(self).click()
            Data.GetDataWatermarkPhotoTrack(self).click()
            # Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            time.sleep(1)
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # time.sleep(1)
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkTrackChooseError.png')
            raise

    def test_ShareWatermarkAlt(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(3)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            # Data.GetDataWatermarkPhotoChangePhoto(self).click()
            # Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            # Data.GetDataWatermarkPhotoSeePhoto(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            # self.GetToast("保存成功！")  #获取toast
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            # self.GetToast("保存成功！")  #获取toast
            # time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkAltError.png')
            raise

    def test_ShareWatermarkAltDefault(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(3)
            Data.GetDataShareWatermarkPhoto(self).click()
            # Data.GetDataWatermarkPhotoTrack(self).click()
            Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(1)
            Data.GetDataWatermarkRestoreDefault(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkAltDefaultError.png')
            raise

    def test_ShareWatermarkAltChoose(self):  # 分享水印照片
        try:
            Tap.GetToHome(self).click()
            Menu.GetMenuFirstData(self).click()
            time.sleep(8)
            Data.GetDataShare(self).click()
            time.sleep(3)
            Data.GetDataShareWatermarkPhoto(self).click()  # 国际·国内有区别
            # Data.GetDataWatermarkPhotoTrack(self).click()
            Data.GetDataWatermarkPhotoAlt(self).click()
            # Data.GetDataWatermarkPhotoData(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            Data.GetDataWatermarkPhotoChangePhoto(self).click()
            Data.GetDataWatermarkPhotoChoosePhoto(self).click()
            Data.GetDataWatermarkPhotoSeePhoto(self).click()
            Data.GetDataWatermarkPhotoSave(self).click()
            self.GetToast("保存成功！")  # 获取toast
            # time.sleep(1)
            # Data.GetDataWatermarkRestoreDefault(self).click()
            # Data.GetDataWatermarkPhotoSave(self).click()
            time.sleep(2)
            Data.GetDataWatermarkPhotoBack(self).click()
            Data.GetDataShareBack(self).click()
            Data.GetDataBack(self).click()
        except:
            self.driver.save_screenshot('ShareWatermarkAltChooseError.png')
            raise

    def test_ActivityShare(self):
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityShareInfo(self).click()
            time.sleep(1)
            Activity.GetActivityShareSave(self).click()
            self.GetToast("保存成功！")
            Activity.GetActivityShareBack(self).click()
        except:
            self.driver.save_screenshot('ActivityShareError.png')
            raise

    def test_StatisticData(self):
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityDataStatisticInfo(self).click()
            time.sleep(1)
            Activity.GetActivityDataStatisticBack(self).click()
        except:
            self.driver.save_screenshot('StatisicDataError.png')
            raise

    def test_PersonalRecords(self):
        try:
            Tap.GetToActivity(self).click()
            Activity.GetActivityPersonalRecordsInfo(self).click()
            Activity.GetActivityPersonalRecordsShare(self).click()
            Activity.GetActivityPersonalRecordsShareBack(self).click()
            Activity.GetActivityPersonalRecordsBack(self).click()
        except:
            self.driver.save_screenshot('PersonalRecordsError.png')
            raise

    def test_MeSettingHR(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            Me.GetMeSettingHRInfo(self).click()
            Me.GetMeSettingHR(self).click()
            Me.GetMeSettingHRBack(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('SMeSettingHRError.png')
            raise

    def test_MeSettingPower(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            Me.GetMeSettingPowerInfo(self).click()
            Me.GetMeSettingPower(self).click()
            Me.GetMeSettingPowerBack(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MeSettingPowerError.png')
            raise

    def test_AboutUs(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeAboutUs(self).click()
            time.sleep(3)
            Me.GetMeAboutUsBack(self).click()
        except:
            self.driver.save_screenshot('AboutUsError.png')
            raise

    def test_FeedBack1(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList1(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack1Error.png')
            raise

    def test_FeedBack2(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList2(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack2Error.png')
            raise

    def test_FeedBack3(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList3(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack3Error.png')
            raise

    def test_FeedBack4(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList4(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack4Error.png')
            raise

    def test_FeedBack5(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList5(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack5Error.png')
            raise

    def test_FeedBack6(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList6(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack6Error.png')
            raise

    def test_FeedBack7(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList7(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack7Error.png')
            raise

    def test_FeedBack8(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList8(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack8Error.png')
            raise

    def test_FeedBack9(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionList9(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBack9Error.png')
            raise

    def test_FeedBackA(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionLista(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBackAError.png')
            raise

    def test_FeedBackB(self):  # 反馈界面
        try:
            QuestionName = 'test'
            Tap.GetToMe(self).click()
            Me.GetMeAfterSaleServiceInfo(self).click()
            time.sleep(2)
            Me.GetMeAfterSaleServiceFeedBack(self).click()
            time.sleep(1)
            Me.GetMeFeedBackQuestionType(self).click()
            Me.GetMeFeedBackQuestionListb(self).click()
            Me.GetMeFeedBackQuestionText(self).click()
            Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
            time.sleep(1)
            Me.GetMeFeedBackTLEText(self).send_keys(123456)
            time.sleep(1)
            Me.GetMeFeedBackPictureAdd(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureChoose(self).click()
            time.sleep(1)
            Me.GetMeFeedBackPictureSave(self).click()
            time.sleep(1)
            Me.GetMeFeedBackSubmit(self).click()
            time.sleep(10)
            Me.GetMeAfterSaleServiceBack(self).click()
        except:
            self.driver.save_screenshot('FeedBackBError.png')
            raise

    def test_ActivityChangeGoals(self):
        try:
            MonthlyGoals = 520
            Tap.GetToActivity(self).click()
            Activity.GetActivityCalendarInfo(self).click()
            Activity.GetActivityCalendarGoalsEdit(self).click()
            Activity.GetActivityCalendarGoalsEditText(self).click()
            Activity.GetActivityCalendarGoalsEditText(self).clear()
            Activity.GetActivityCalendarGoalsEditText(self).send_keys(MonthlyGoals)
            Activity.GetActivityCalendarGoalsEditSave(self).click()
            self.GetToast("保存成功！")
            Activity.GetActivityCalendarBack(self).click()
        except:
            self.driver.save_screenshot('ActivityChangeGoalsError.png')
            raise

    @unittest.skip("compose测试")
    def test_ComposeTest(self):
        Tap.GetToDevice(self).click()
        ComposeTest.GetDeviceRoutesAdd(self).click()
        time.sleep(3)
        # Compose.GetDeviceCreateRoutes(self).click()
        ComposeTest.GetDeviceFirstRoutes(self).click()
        self.driver.save_screenshot('ShareWatermarkError.png')

    def test_MenuChangeGoals(self):
        try:
            MonthlyGoals = 888
            Tap.GetToHome(self).click()
            Menu.GetMenuTrainingGoalsInto(self).click()
            Me.GetMeUserGoalsText(self).click()
            Me.GetMeUserGoalsText(self).clear()
            Me.GetMeUserGoalsText(self).send_keys(MonthlyGoals)  # id定位
            Me.GetMeUserGoalsSave(self).click()
            Me.GetMeUserDetailsBack(self).click()
            # NewGoals = Menu.GetMenuMonthGoals(self).text
            # RealGoals = round(float(MonthlyGoals)) - round(float(NewGoals))
            # self.assertEqual(0, RealGoals)
        except:
            self.driver.save_screenshot('MenuChangeGoalsError.png')
            raise

    def test_MeChangeGoals(self):
        try:
            MonthlyGoals = 666
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            Me.GetMeUserGoalsEdit(self).click()
            Me.GetMeUserGoalsText(self).click()
            Me.GetMeUserGoalsText(self).clear()
            Me.GetMeUserGoalsText(self).send_keys(MonthlyGoals)  # id定位
            Me.GetMeUserGoalsSave(self).click()
            Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('MeChangeGoalsError.png')
            raise

    def test_SexChange(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMEUserDetailsInfo(self).click()
            UserSex = Me.GetMeUserSex(self).text
            if UserSex == '男':
                Me.GetMeUserSexInfo(self).click()
                time.sleep(1)
                self.SwipeLittleUp()
                Me.GetMeUserSexSave(self).click()
                Me.GetMeUserDetailsBack(self).click()
                Tap.GetToMe(self).click()
                Me.GetMEUserDetailsInfo(self).click()
                Sex = Me.GetMeUserSex(self).text
                self.assertNotEqual(Sex, UserSex)
                Me.GetMeUserDetailsBack(self).click()
            else:
                Me.GetMeUserSexInfo(self).click()
                self.SwipeLittleDown()
                Me.GetMeUserSexSave(self).click()
                Me.GetMeUserDetailsBack(self).click()
                Tap.GetToMe(self).click()
                Me.GetMEUserDetailsInfo(self).click()
                Sex = Me.GetMeUserSex(self).text
                self.assertNotEqual(Sex, UserSex)
                Me.GetMeUserDetailsBack(self).click()
        except:
            self.driver.save_screenshot('SexChangeError.png')
            raise

    @unittest.skip
    def test_LanguageChange(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            time.sleep(1)
            Me.GetMeLanguageSetting(self).click()
            self.SwipeLittleUp()
            time.sleep(1)
            Me.GetMeLanguageSettingSave(self).click()
            OldLanguage = Me.GetMeLanguageMessage(self).text
            Me.GetMeAccountSettingSave(self).click()
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            NewLanguage = Me.GetMeLanguageMessage(self).text
            Me.GetMeAccountSettingBack(self).click()
            self.assertEqual(OldLanguage, NewLanguage)
        except:
            self.driver.save_screenshot('LanguageChangeError.png')
            raise

    def test_MeNotification(self):
        try:
            Tap.GetToMe(self).click()
            Me.GetMeNotification(self).click()
            time.sleep(3)
            Me.GetMeNotificationBack(self).click()
        except:
            self.driver.save_screenshot('MeNotificationError.png')
            raise

    def test_AccumulatedMileageConsistency(self):
        try:
            Tap.GetToActivity(self).click()
            ActivityDistance = Activity.GetActivityTotalDistance(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            Activity.GetActivityDataStatisticAll(self).click()
            ActivityDistances = Activity.GetActivityDataStatisticAllDistances(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertEqual(ActivityDistance, ActivityDistances)
        except:
            self.driver.save_screenshot('AccumulatedMileageConsistencyError.png')
            raise

    def test_CumulativeTimesConsistency(self):
        try:
            Tap.GetToActivity(self).click()
            ActivityFrequency = Activity.GetActivityTotalFrequency(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            Activity.GetActivityDataStatisticAll(self).click()
            ActivityFrequencys = Activity.GetActivityDataStatisticAllFrequency(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertEqual(ActivityFrequencys, ActivityFrequency)
        except:
            self.driver.save_screenshot('CumulativeTimesConsistencyError.png')
            raise

    def test_AverageVelocityConsistency(self):
        try:
            Tap.GetToActivity(self).click()
            ActivityAverageVelocity = Activity.GetActivityTotalAverageVelocity(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            Activity.GetActivityDataStatisticAll(self).click()
            ActivityAverageVelocitys = Activity.GetActivityDataStatisticAllAverageVelocity(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertIn(ActivityAverageVelocity, ActivityAverageVelocitys)
        except:
            self.driver.save_screenshot('AverageVelocityConsistencyError.png')
            raise

    @unittest.skip("需含有当月骑行记录")
    def test_MonthlyCyclingTimes(self):
        try:
            Tap.GetToActivity(self).click()
            ActivityMonthFrequency = Activity.GetActivityMonthFrequency(self).text
            Activity.GetActivityDataStatisticInfo(self).click()
            time.sleep(1)
            Activity.GetActivityDataStatisticMonth(self).click()
            time.sleep(2)
            ActivityDataStatisicMonthFrequency = Activity.GetActivityDataStatisticMonthFrequency(self).text
            Activity.GetActivityDataStatisticBack(self).click()
            self.assertEqual(ActivityDataStatisicMonthFrequency, ActivityMonthFrequency)
        except:
            self.driver.save_screenshot('MonthlyCyclingTimesError.png')
            raise

    def test_ResetPassword(self):
        try:
            OldPassword = 123456
            NewPassword = 123456
            Tap.GetToMe(self).click()
            Me.GetMeAccountSettingInfo(self).click()
            Me.GetMeResetPasswordInfo(self).click()
            Me.GetMeOldPasswordText(self).click()
            Me.GetMeOldPasswordText(self).send_keys(OldPassword)
            Me.GetMeNemPasswordText(self).click()
            Me.GetMeNemPasswordText(self).send_keys(NewPassword)
            Me.GetMeAgainNemPasswordText(self).click()
            Me.GetMeAgainNemPasswordText(self).send_keys(NewPassword)
            Me.GetMeConfirmPassword(self).click()
            self.GetToast("密码重置完成")
            Me.GetMeAccountSettingBack(self).click()
        except:
            self.driver.save_screenshot('ResetPasswordError.png')
            raise

    def test_NoNewPasswordError(self):
        OldPassword = 123456
        Tap.GetToMe(self).click()
        Me.GetMeAccountSettingInfo(self).click()
        Me.GetMeResetPasswordInfo(self).click()
        Me.GetMeOldPasswordText(self).click()
        Me.GetMeOldPasswordText(self).send_keys(OldPassword)
        Me.GetMeConfirmPassword(self).click()
        try:
            self.GetToast("请输入新密码：")
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
        except:
            self.driver.save_screenshot('NoNewPasswordError.png')
            raise

    def test_NoNewAgainPasswordError(self):
        OldPassword = 123456
        NewPassword = 123456
        Tap.GetToMe(self).click()
        Me.GetMeAccountSettingInfo(self).click()
        Me.GetMeResetPasswordInfo(self).click()
        Me.GetMeOldPasswordText(self).click()
        Me.GetMeOldPasswordText(self).send_keys(OldPassword)
        Me.GetMeNemPasswordText(self).click()
        Me.GetMeNemPasswordText(self).send_keys(NewPassword)
        Me.GetMeConfirmPassword(self).click()
        try:
            self.GetToast("请再次输入新密码：")
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
        except:
            self.driver.save_screenshot('NoNewAgainPasswordError.png')
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
            raise

    def test_NoOldPasswordError(self):
        # OldPassword = 123456
        NewPassword = 123456
        Tap.GetToMe(self).click()
        Me.GetMeAccountSettingInfo(self).click()
        Me.GetMeResetPasswordInfo(self).click()
        Me.GetMeOldPasswordText(self).click()
        # Me.GetMeOldPasswordText(self).send_keys(OldPassword)
        Me.GetMeNemPasswordText(self).click()
        Me.GetMeNemPasswordText(self).send_keys(NewPassword)
        Me.GetMeAgainNemPasswordText(self).click()
        Me.GetMeAgainNemPasswordText(self).send_keys(NewPassword)
        Me.GetMeConfirmPassword(self).click()
        try:
            self.GetToast("请输入旧密码")
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
        except:
            self.driver.save_screenshot('NoOldPasswordError.png')
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
            raise

    def test_NoPasswordError(self):
        # OldPassword = 123456
        # NewPassword = 123456
        Tap.GetToMe(self).click()
        Me.GetMeAccountSettingInfo(self).click()
        Me.GetMeResetPasswordInfo(self).click()
        Me.GetMeOldPasswordText(self).click()
        # Me.GetMeOldPasswordText(self).send_keys(OldPassword)
        # Me.GetMeNemPasswordText(self).click()
        # Me.GetMeNemPasswordText(self).send_keys(NewPassword)
        # Me.GetMeAgainNemPasswordText(self).click()
        # Me.GetMeAgainNemPasswordText(self).send_keys(NewPassword)
        Me.GetMeConfirmPassword(self).click()
        try:
            self.GetToast("请输入旧密码")
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
        except:
            self.driver.save_screenshot('NoPasswordError.png')
            Me.GetMeResetPasswordBack(self).click()
            Me.GetMeAccountSettingBack(self).click()
            raise


if __name__ == '__main__':
    unittest.main()
