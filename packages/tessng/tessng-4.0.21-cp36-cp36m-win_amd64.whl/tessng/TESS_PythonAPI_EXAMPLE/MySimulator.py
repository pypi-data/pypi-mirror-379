import random
from datetime import datetime
from PySide2.QtCore import QObject, Signal
from tessng import PyCustomerSimulator, tessngIFace, Online, m2p, p2m


# 用户插件子类，代表用户自定义与仿真相关的实现逻辑，继承自PyCustomerSimulator
class MySimulator(PyCustomerSimulator, QObject):
    # 在自定义面板的信息窗上显示信息的信号
    showRunInfo = Signal(str)

    def __init__(self):
        PyCustomerSimulator.__init__(self)
        QObject.__init__(self)
        # 代表TESS NG的接口
        self.iface = tessngIFace()
        # 代表TESS NG 的路网子接口
        self.netiface = self.iface.netInterface()
        # 代表TESS NG 的仿真子接口
        self.simuiface = self.iface.simuInterface()
        # 代表TESS NG 的界面子接口
        self.guiiface = self.iface.guiInterface()

        # 车辆方阵的车辆数
        self.square_vehi_count: int = 28
        # 飞机速度，飞机后面的车辆速度会被设定为此数据
        self.plane_speed: float = 0
        # 当前正在仿真计算的路网名称
        self.current_net_name: str = ""
        # 相同路网连续仿真次数
        self.simu_count: int = 0

    # 重写父类方法：TESS NG 在仿真开启前调用此方法
    def beforeStart(self, ref_keep_on: bool) -> None:
        # 获取当前路网名称
        tmp_net_name: str = self.netiface.netFilePath()
        if tmp_net_name != self.current_net_name:
            self.current_net_name = tmp_net_name
            self.simu_count = 1
        else:
            self.simu_count += 1

    # 重写父类方法：TESS NG 在仿真开启后调用此方法
    def afterStart(self) -> None:
        print("仿真开始")

    # 重写父类方法：TESS NG 在仿真结束后调用此方法
    def afterStop(self) -> None:
        if self.simu_count <= 3:
            # 重新开启仿真
            self.simuiface.startSimu()

    # 重写父类方法：TESS NG 在每个计算周期结束后调用此方法，核心逻辑实现
    def afterOneStep(self) -> None:
        # 获取仿真精度
        simu_accuracy: int = self.simuiface.simuAccuracy()
        # 获取仿真倍速
        simu_multiples: int = self.simuiface.acceMultiples()
        # 获取当前仿真计算批次
        batch_number = self.simuiface.batchNumber()
        # 获取当前已仿真时间，单位：毫秒
        simu_time = self.simuiface.simuTimeIntervalWithAcceMutiples()
        # 获取开始仿真的现实时间，单位：毫秒
        start_real_time = self.simuiface.startMSecsSinceEpoch()

        # 仿真时间超过600秒则停止仿真
        if simu_time >= 600 * 1000:
            self.simuiface.stopSimu()

        # 获取当前正在运行的车辆列表
        all_vehicles = self.simuiface.allVehiStarted()
        # 获取当前在ID为1的路段上运行的车辆列表
        vehicles = self.simuiface.vehisInLink(1)

        # 在信息窗显示信息
        if batch_number % simu_accuracy == 0:
            # 路段数量
            link_count: int = self.netiface.linkCount()
            # 车辆数
            vehicle_count: int = len(all_vehicles)
            run_info: str = f"路段数：{link_count}\n运行车辆数：{vehicle_count}\n仿真时间：{simu_time}(毫秒)"
            self.showRunInfo.emit(run_info)

        # 动态发车，不通过发车点发送，直接在路段和连接段中间某位置创建并发送
        if batch_number % 50 == 1:
            # 生成随机颜色
            r = hex(256 + random.randint(0,256))[3:].upper()
            g = hex(256 + random.randint(0,256))[3:].upper()
            b = hex(256 + random.randint(0,256))[3:].upper()
            color = f"#{r}{g}{b}"

            # 路段上发车
            dvp = Online.DynaVehiParam()
            dvp.vehiTypeCode = random.randint(0, 4) + 1
            dvp.roadId = 6
            dvp.laneNumber = random.randint(0, 3)
            dvp.dist = 50
            dvp.speed = 20
            dvp.color = color
            vehicle1 = self.simuiface.createGVehicle(dvp)
            if vehicle1 is not None:
                print(f"在路段上创建了车辆：{vehicle1.id()}")

            # 连接段上发车
            dvp2 = Online.DynaVehiParam()
            dvp2.vehiTypeCode = random.randint(0, 4) + 1
            dvp2.roadId = 3
            dvp2.laneNumber = random.randint(0, 3)
            dvp2.toLaneNumber = dvp2.laneNumber  # 默认为-1，如果大于等于0, 在连接段上发车
            dvp2.dist = 50
            dvp2.speed = 20
            dvp2.color = color
            vehicle2 = self.simuiface.createGVehicle(dvp2)
            if vehicle2 is not None:
                print(f"在连接段上创建了车辆：{vehicle2.id()}")

        # 获取当前仿真时间完成穿越采集器的所有车辆信息
        lVehiInfo = self.simuiface.getVehisInfoCollected()
        #if len(lVehiInfo) > 0:
        #    print("车辆信息采集器采集信息：", [(vinfo.collectorId, vinfo.vehiId) for vinfo in lVehiInfo])
        # 获取最近集计时间段内采集器采集的所有车辆集计信息
        lVehiInfoAgg = self.simuiface.getVehisInfoAggregated()
        #if len(lVehisInfoAggr) > 0:
        #    print("车辆信息采集集计数据：", [(vinfo.collectorId, vinfo.vehiCount) for vinfo in lVehisInfoAggr])
        # 获取当前仿真时间排队计数器计数的车辆排队信息
        lVehiQueue = self.simuiface.getVehisQueueCounted()
        #if len(lVehiQueue) > 0:
        #    print("车辆排队计数器计数：", [(vq.counterId, vq.queueLength) for vq in lVehiQueue])
        # 获取最近集计时间段内排队计数器集计数据
        lVehiQueueAgg = self.simuiface.getVehisQueueAggregated()
        #if len(lVehiQueueAggr) > 0:
        #    print("车辆排队集计数据：", [(vqAggr.counterId, vqAggr.avgQueueLength) for vqAggr in lVehiQueueAggr])
        # 获取当前仿真时间行程时间检测器完成的行程时间检测信息
        lVehiTravel = self.simuiface.getVehisTravelDetected()
        #if len(lVehiTravel) > 0:
        #    print("车辆行程时间检测信息：", [(vtrav.detectedId, vtrav.travelDistance) for vtrav in lVehiTravel])
        # 获取最近集计时间段内行程时间检测器集计数据
        lVehiTravAgg = self.simuiface.getVehisTravelAggregated()
        #if len(lVehiTravAggr) > 0:
        #    print("车辆行程时间集计数据：", [(vTravAggr.detectedId, vTravAggr.vehiCount, vTravAggr.avgTravelDistance) for vTravAggr in lVehiTravAggr])

    # 重写父类方法：在车辆启动上路时被TESS NG调用一次
    def initVehicle(self, vehicle) -> None:
        # 设置当前车辆及其驾驶行为过载方法被TESSNG调用频次，即多少个计算周调用一次指定方法。如果对运行效率有极高要求，可以精确控制具体车辆或车辆类型及具体场景相关参数
        self.set_steps_per_call(vehicle)

        # 车辆所在路段名或连接段名
        road_name = vehicle.roadName()
        # 车辆所在路段ID或连接段ID
        road_id = vehicle.roadId()

        # 曹安公路上的车辆特殊处理
        if road_name == '曹安公路':
            # 不含首位数的车辆ID，首位数与车辆来源有关，如发车点、公交线路
            tmp_vehicle_id = vehicle.id() % 100000

            # 飞机
            if tmp_vehicle_id == 1:
                vehicle.setVehiType(12)
                vehicle.initLane(3, m2p(105), 0)
            # 工程车
            elif tmp_vehicle_id >= 2 and tmp_vehicle_id <= 8:
                vehicle.setVehiType(8)
                vehicle.initLane((tmp_vehicle_id - 2) % 7, m2p(80), 0)
            # 消防车
            elif tmp_vehicle_id >= 9 and tmp_vehicle_id <= 15:
                vehicle.setVehiType(9)
                vehicle.initLane((tmp_vehicle_id - 2) % 7, m2p(65), 0)
            # 消防车
            elif tmp_vehicle_id >= 16 and tmp_vehicle_id <= 22:
                vehicle.setVehiType(10)
                vehicle.initLane((tmp_vehicle_id - 2) % 7, m2p(50), 0)
            # 最后两队列小车
            elif tmp_vehicle_id == 23:
                vehicle.setVehiType(1)
                vehicle.initLane(1, m2p(35), 0)
            elif tmp_vehicle_id == 24:
                vehicle.setVehiType(1)
                vehicle.initLane(5, m2p(35), 0)
            elif tmp_vehicle_id == 25:
                vehicle.setVehiType(1)
                vehicle.initLane(1, m2p(20), 0)
            elif tmp_vehicle_id == 26:
                vehicle.setVehiType(1)
                vehicle.initLane(5, m2p(20), 0)
            elif tmp_vehicle_id == 27:
                vehicle.setVehiType(1)
                vehicle.initLane(1, m2p(5), 0)
            elif tmp_vehicle_id == 28:
                vehicle.setVehiType(1)
                vehicle.initLane(5, m2p(5), 0)

            # 设置最后两列小车的长度
            if tmp_vehicle_id >= 23 and tmp_vehicle_id <= 28:
                vehicle.setLength(m2p(4.5), True)

    # 自定义方法：设置本类实现的重写方法的调用频次
    def set_steps_per_call(self, vehicle) -> None:
        net_file_name = self.netiface.netFilePath()

        if "Temp" in net_file_name:
            vehicle.setIsPermitForVehicleDraw(True)
            vehicle.setSteps_calcLimitedLaneNumber(10)
            vehicle.setSteps_calcChangeLaneSafeDist(10)
            vehicle.setSteps_reCalcdesirSpeed(1)
            vehicle.setSteps_reSetSpeed(1)
        else:
            # 仿真精度，即每秒计算次数
            steps = self.simuface.simuAccuracy()

            # 车辆相关方法调用频次
            vehicle.setIsPermitForVehicleDraw(False)
            vehicle.setSteps_beforeNextPoint(steps * 300)
            vehicle.setSteps_nextPoint(steps * 300)
            vehicle.setSteps_afterStep(steps * 300)
            vehicle.setSteps_isStopDriving(steps * 300)

            # 驾驶行为相关方法调用频次
            vehicle.setSteps_reCalcdesirSpeed(steps * 300)
            vehicle.setSteps_calcMaxLimitedSpeed(steps * 300)
            vehicle.setSteps_calcLimitedLaneNumber(steps)
            vehicle.setSteps_calcSpeedLimitByLane(steps)
            vehicle.setSteps_calcChangeLaneSafeDist(steps)
            vehicle.setSteps_reCalcToLeftLane(steps)
            vehicle.setSteps_reCalcToRightLane(steps)
            vehicle.setSteps_reCalcToLeftFreely(steps)
            vehicle.setSteps_reCalcToRightFreely(steps)
            vehicle.setSteps_afterCalcTracingType(steps * 300)
            vehicle.setSteps_beforeMergingToLane(steps * 300)
            vehicle.setSteps_reSetFollowingType(steps * 300)
            vehicle.setSteps_calcAcce(steps * 300)
            vehicle.setSteps_reSetAcce(steps * 300)
            vehicle.setSteps_reSetSpeed(steps * 300)
            vehicle.setSteps_reCalcAngle(steps * 300)
            vehicle.setSteps_recentTimeOfSpeedAndPos(steps * 300)
            vehicle.setSteps_travelOnChangingTrace(steps * 300)
            vehicle.setSteps_leaveOffChangingTrace(steps * 300)
            vehicle.setSteps_beforeNextRoad(steps * 300)

    # 重写父类方法：判断是否移除车辆
    def isStopDriving(self, vehicle) -> bool:
        # 车辆进入ID等于2的路段或连接段，且路离终点小于100米，从路网中移除
        if vehicle.roadId() == 2:
            # 车头到当前路段或连接段终点距离
            dist = vehicle.vehicleDriving().distToEndpoint(True)
            # 如果距终点距离小于100米，车辆停止运行退出路网
            if dist < m2p(100):
                return True
        return False

    # 重写父类方法：在车辆被移除时被TESS NG调用一次
    def afterStopVehicle(self, vehicle) -> None:
        pass

    # 重写父类方法：重新计算车辆的加速度，只对当前帧生效
    def ref_reSetAcce(self, vehicle, inOutAcce) -> bool:
        """
        :param vehicle: 车辆对象
        :param inOutAcce: 车辆加速度，inOutAcce.value是TESS NG已计算的车辆加速度，此方法可以改变它
        :return: True：接受此次修改，False：忽略此次修改
        """
        roadName = vehicle.roadName()
        if roadName == "连接段1":
            if vehicle.currSpeed() > m2p(20 / 3.6):
                inOutAcce.value = m2p(-5)
                return True
            elif vehicle.currSpeed() > m2p(20 / 3.6):
                inOutAcce.value = m2p(-1)
                return True
        return False

    # 重写父类方法：重新计算车辆的期望速度，只对当前帧生效
    def ref_reCalcdesirSpeed(self, vehicle, ref_desirSpeed) -> bool:
        """
        :param vehicle: 车辆对象
        :param ref_desirSpeed: 期望速度，ref_desirSpeed.value，是已计算好的车辆期望速度，此方法可以改变它
        :return: True：接受此次修改，False：忽略此次修改
        """
        tmp_vehicle_id = vehicle.id() % 100000
        road_name = vehicle.roadName()
        if road_name == '曹安公路':
            if tmp_vehicle_id <= self.square_vehi_count:
                simu_time = self.simuiface.simuTimeIntervalWithAcceMutiples()
                if simu_time < 5 * 1000:
                    ref_desirSpeed.value = 0
                elif simu_time < 10 * 1000:
                    ref_desirSpeed.value = m2p(20 / 3.6)
                else:
                    ref_desirSpeed.value = m2p(40 / 3.6)
                return True
        return False

    # 重写父类方法：重新计算车辆的当前速度，只对当前帧生效
    def ref_reSetSpeed(self, vehicle, ref_inOutSpeed) -> bool:
        """
        :param vehicle: 车辆对象
        :param ref_inOutSpeed: 速度，ref_inOutSpeed.value，是已计算好的车辆速度，此方法可以改变它
        :return: True：接受此次修改，False：忽略此次修改
        """
        tmp_vehicle_id = vehicle.id() % 100000
        road_name = vehicle.roadName()
        if road_name == "曹安公路":
            if tmp_vehicle_id == 1:
                self.plane_speed = vehicle.currSpeed()
            elif 2 <= tmp_vehicle_id <= self.square_vehi_count:
                ref_inOutSpeed.value = self.plane_speed
                return True
        return False

    # 重写父类方法：重新计算车辆跟驰参数，安全时距及停车距离，只对当前帧生效
    def ref_reSetFollowingParam(self, vehicle, ref_inOutSi, ref_inOutSd) -> bool:
        """
        :param vehicle: 车辆对象
        :param ref_inOutSi: 安全时距，ref_inOutSi.value是TESS NG已计算好的值，此方法可以改变它
        :param ref_inOutSd: 停车距离，ref_inOutSd.value是TESS NG已计算好的值，此方法可以改变它
        :return: True：接受此次修改，False：忽略此次修改
        """
        road_name = vehicle.roadName()
        if road_name == "连接段2":
            ref_inOutSd.value = m2p(30)
            return True
        return False

    # 重写父类方法：计算车辆是否要左自由变道
    def reCalcToLeftFreely(self, vehicle) -> bool:
        """
        :param vehicle: 车辆对象
        :return: True：车辆向左自由变道，False：TESS NG 自行判断是否要向左自由变道
        """
        # 距离路段终点小于20米不变道
        if vehicle.vehicleDriving().distToEndpoint() - vehicle.length() / 2 < m2p(20):
            return False
        tmp_vehicle_id = vehicle.id() % 100000
        road_name = vehicle.roadName()
        if road_name == "曹安公路":
            if 23 <= tmp_vehicle_id <= 28:
                lane_number = vehicle.vehicleDriving().laneNumber()
                if lane_number in [1, 4]:
                    return True
        return False

    # 重写父类方法：计算车辆是否要右自由变道
    def reCalcToRightFreely(self, vehicle) -> bool:
        """
        :param vehicle: 车辆对象
        :return: True：车辆向右自由变道，False：TESS NG 自行判断是否要向右自由变道
        """
        # 距离路段终点小于20米不变道
        if vehicle.vehicleDriving().distToEndpoint() - vehicle.length() / 2 < m2p(20):
            return False
        tmp_vehicle_id = vehicle.id() % 100000
        road_name = vehicle.roadName()
        if road_name == "曹安公路":
            if 23 <= tmp_vehicle_id <= 28:
                lane_number = vehicle.vehicleDriving().laneNumber()
                if lane_number in [2, 5]:
                    return True
        return False

    # 重写父类方法：计算车辆当前禁行车道序号列表，只对当前帧生效
    def calcLimitedLaneNumber(self, vehicle) -> list:
        """
        :param vehicle: 车辆对象
        :return: 禁行车道的序号的列表
        """
        # 路段ID等于2时，小车走内侧，大车走外侧
        if vehicle.roadIsLink():
            link = vehicle.lane().link()
            if link is not None and link.id() == 2:
                lane_count = link.laneCount()
                # 小车走内侧，大车走外侧，设长度小于8米为小车
                if vehicle.length() < m2p(8):
                    return [num for num in range(lane_count // 2 - 1)]
                else:
                    return [num for num in range(lane_count // 2 - 1, lane_count)]
        return []

    # 重写父类方法：设置信号灯的灯色，只对当前帧生效
    def calcLampColor(self, signal_lamp) -> bool:
        """
        :param signal_lamp: 信号灯头对象
        :return: True：接受此次修改，False：忽略此次修改
        """
        if signal_lamp.id() == 5:
            signal_lamp.setLampColor("红")
            return True
        return False

    # 重写父类方法：计算车道限速，只对当前帧生效
    def ref_calcSpeedLimitByLane(self, link, lane_number: int, ref_outSpeed) -> bool:
        """
        :param link: 路段对象
        :param lane_number: 车道序号，从0开始，从右向左
        :param ref_outSpeed: 可以改变ref_outSpeed.value为设定的限速值，单位：km/h
        :return: True：接受此次修改，False：忽略此次修改
        """
        # ID为2的路段，车道0和1限速30km/h
        if link.id() == 2 and lane_number <= 1:
            ref_outSpeed.value = m2p(30)
            return True
        return False

    # 重写父类方法：动态修改发车参数
    def calcDynaDispatchParameters(self) -> list:
        # 以飞机打头的方阵全部驰出路段后为这条路段的发车点增加发车间隔
        # 当前仿真时间
        simu_time = self.simuiface.simuTimeIntervalWithAcceMutiples()
        # ID等于1的路段上的车辆
        vehicles = self.simuiface.vehisInLink(1)
        if simu_time < 1000 * 10 or len(vehicles) > 0:
            return []
        # 当前时间秒
        now = datetime.now()
        current_second = now.hour * 3600 + now.minute * 60 + now.second
        # 仿真10秒后且ID等于1的路段上车辆数为0，则为ID等于1的发车点增加发车间隔
        di = Online.DispatchInterval()
        di.dispatchId = 1
        di.fromTime = current_second
        di.toTime = di.fromTime + 300 - 1
        di.vehiCount = 300
        di.mlVehicleConsDetail = [
            Online.VehiComposition(1, 60),
            Online.VehiComposition(2, 40)
        ]
        return [di]

    # 重写父类方法：动态修改决策点不同路径流量比
    def calcDynaFlowRatioParameters(self) -> list:
        # 当前仿真计算批次
        batch_number = self.simuiface.batchNumber()
        # 在计算第20批次时修改某决策点各路径流量比
        if batch_number == 20:
            # 一个决策点某个时段各路径车辆分配比
            dfi = Online.DecipointFlowRatioByInterval()
            # 决策点编号
            dfi.deciPointID = 5
            # 起始时间 单位：秒
            dfi.startDateTime = 1
            # 结束时间 单位：秒
            dfi.endDateTime = 999999
            # 路径流量比
            rfr1 = Online.RoutingFlowRatio(1, 3)
            rfr2 = Online.RoutingFlowRatio(2, 4)
            rfr3 = Online.RoutingFlowRatio(3, 3)
            dfi.mlRoutingFlowRatio = [rfr1, rfr2, rfr3]
            return [dfi]
        return []
