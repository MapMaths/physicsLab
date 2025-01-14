# 所有元件 elements

所有元件共有的attribute:  
.is_bigElement # 是否是大体积元件  
.is_elementXYZ # 是否是元件坐标系  

  
> Note: 如果表格没有***类独有的method***，说明该表格中的所有元件都没有类独有的method

## 逻辑电路

<table border="1">
<thead>
    <tr>
        <td colspan=5>
            逻电元件共有的method:<br>
            set_HighLevelValue # 设置高电平的值<br>
            get_HighLevelValue # 获取高电平的值<br>
            set_LowLevelValue # 设置低电平的值<br>
            get_LowLevelValue # 获取高电平的值<br>
        </td>
    </tr>
    <tr>
        <th>物实元件的中文名</th>
        <th>元件在physicsLab中对应的的类名</th>
        <th>元件在物实存档中对应的名称（即ModelID）</th>
        <th>引脚</th>
        <th>类独有的method</th>
    </tr>
</thead> <tbody>
    <tr>
        <td>逻辑输入</td>
        <td>Logic_Input</td>
        <td>Logic Input</td>
        <td>o</td>
        <td>set_highLevel # 将逻辑输入的状态设置为1</td>
    </tr>
    <tr>
        <td>逻辑输出</td>
        <td>Logic_Output</td>
        <td>Logic Output</td>
        <td>i</td>
        <td>None</td>
    </tr>
    <tr>
        <td>是门</td>
        <td>Yes_Gate</td>
        <td>Yes Gate</td>
        <td>i, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>非门</td>
        <td>No_Gate</td>
        <td>No Gate</td>
        <td>i, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>或门</td>
        <td>Or_Gate</td>
        <td>Or Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>与门</td>
        <td>And_Gate</td>
        <td>And Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>或非门</td>
        <td>Nor_Gate</td>
        <td>Nor Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>与非门</td>
        <td>Nand_Gate</td>
        <td>Nand Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>异或门</td>
        <td>Xor_Gate</td>
        <td>Xor Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>同或门</td>
        <td>Xnor_Gate</td>
        <td>Xnor Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>蕴含门</td>
        <td>Imp_Gate</td>
        <td>Imp Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>蕴含非门</td>
        <td>Nimp_Gate</td>
        <td>Nimp Gate</td>
        <td>i_up, i_low, o</td>
        <td>None</td>
    </tr>
    <tr>
        <td>半加器</td>
        <td>Half_Adder</td>
        <td>Half Adder</td>
        <td>i_up, i_low, o_up, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>全加器</td>
        <td>Full_Adder</td>
        <td>Full Adder</td>
        <td>i_up, i_mid, i_low, o_up, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>二位乘法器</td>
        <td>Multiplier</td>
        <td>Multiplier</td>
        <td>i_up, i_upmid, i_lowmid, i_low, o_up, o_upmid, o_lowmid, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>D触发器</td>
        <td>D_Flipflop</td>
        <td>D Flipflop</td>
        <td>i_up, i_low, o_up, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>T'触发器</td>
        <td>T_Flipflop</td>
        <td>T Flipflop</td>
        <td>i_up, i_low, o_up, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>T触发器</td>
        <td>Real_T_Flipflop</td>
        <td>Real-T Flipflop</td>
        <td>i_up, i_low, o_up, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>JK触发器</td>
        <td>JK_Flipflop</td>
        <td>JK Flipflop</td>
        <td>i_up, i_mid, i_low, o_up, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>计数器</td>
        <td>Counter</td>
        <td>Counter</td>
        <td>i_up, i_low, o_up, o_upmid, o_lowmid, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>随机数发生器</td>
        <td>Random_Generator</td>
        <td>Random Generator</td>
        <td>i_up, i_low, o_up, o_upmid, o_lowmid, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>8位输入器</td>
        <td>eight_bit_Input</td>
        <td>8bit Input</td>
        <td>i_up, i_upmid, i_lowmid, i_low, o_up, o_upmid, o_lowmid, o_low</td>
        <td>set_num # 设置8位输入器的数字</td>
    </tr>
    <tr>
        <td>8位显示器</td>
        <td>eight_bit_Display</td>
        <td>8bit Display</td>
        <td>i_up, i_upmid, i_lowmid, i_low, o_up, o_upmid, o_lowmid, o_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>施密特触发器</td>
        <td>Schmitt_Trigger</td>
        <td>Schmitt Trigger</td>
        <td>i, o</td>
        <td>None</td>
    </tr>
</tbody>
</table>

## 模拟电路
<table border="1">
    <tr>
        <th>物实元件的中文名</th>
        <th>元件在physicsLab中对应的的类名</th>
        <th>元件在物实存档中对应的名称（即ModelID）</th>
        <th>引脚</th>
    </tr>
    <tr>
        <td>555定时器</td>
        <td>NE555</td>
        <td>555 Timer</td>
        <td>VCC, Dis, Thr, Ctrl, Trig, Out, Reset, Ground</td>
    </tr>
    <tr>
        <td>电容</td>
        <td>Basic_Capacitor</td>
        <td>Basic Capacitor</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>电感</td>
        <td>Basic_Inductor</td>
        <td>Basic Inductor</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>二极管</td>
        <td>Basic_Diode</td>
        <td>Basic_Diode</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>发光二极管</td>
        <td>Light_Emitting_Diode</td>
        <td>Light-Emitting Diode</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>接地</td>
        <td>Ground_Component</td>
        <td>Ground Component</td>
        <td>i</td>
    </tr>
    <tr>
        <td>理想变压器</td>
        <td>Transformer</td>
        <td>Transformer</td>
        <td>l_up, l_low, r_up, r_low</td>
    </tr>
    <tr>
        <td>中心抽头变压器</td>
        <td>Tapped_Transformer</td>
        <td>Tapped Transformer</td>
        <td>l_up, l_low, r_up, r_low, mid</td>
    </tr>
    <tr>
        <td>理想互感</td>
        <td>Mutual_Inductor</td>
        <td>Mutual Inductor</td>
        <td>l_up, l_low, r_up, r_low</td>
    </tr>
    <tr>
        <td>全波整流器</td>
        <td>Rectifier</td>
        <td>Rectifier</td>
        <td>l_up, l_low, r_up, r_low</td>
    </tr>
    <tr>
        <td>三极管</td>
        <td>Transistor</td>
        <td>Transistor</td>
        <td>B, C, E</td>
    </tr>
    <tr>
        <td>比较器</td>
        <td>Comparator</td>
        <td>Comparator</td>
        <td>i_up, i_low, o</td>
    </tr>
    <tr>
        <td>运算放大器</td>
        <td>Operational_Amplifier</td>
        <td>Operational Amplifier</td>
        <td>i_up, i_low, o</td>
    </tr>
    <tr>
        <td>继电器</td>
        <td>Relay_Component</td>
        <td>Relay Component</td>
        <td>i_up, i_low, o</td>
    </tr>
    <tr>
        <td>N-MOSFET</td>
        <td>N_MOSFET</td>
        <td>N-MOSFET</td>
        <td>D, S, G</td>
    </tr>
    <tr>
        <td>P-MOSFET</td>
        <td>P_MOSFET</td>
        <td>P-MOSFET</td>
        <td>D, S, G</td>
    </tr>
    <tr>
        <td>正弦波发生器</td>
        <td>Sinewave_Source</td>
        <td>Sinewave Source</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>方波发生器</td>
        <td>Square_Source</td>
        <td>Square Source</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>三角波发生器</td>
        <td>Triangle_Source</td>
        <td>Triangle Source</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>锯齿波发生器</td>
        <td>Sawtooth_Source</td>
        <td>Sawtooth Source</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>尖峰波发生器</td>
        <td>Pulse_Source</td>
        <td>Pulse Source</td>
        <td>red, black</td>
    </tr>
</table>

## 基础电路
<table border="1">
    <tr>
        <th>物实元件的中文名</th>
        <th>元件在physicsLab中对应的的类名</th>
        <th>元件在物实存档中对应的名称（即ModelID）</th>
        <th>引脚</th>
        <th>类独有的method</th>
    </tr>
    <tr>
        <td>简单开关</td>
        <td>Simple_Switch</td>
        <td>Simple Switch</td>
        <td>red, black</td>
        <td>turn_off_switch # 断开开关; turn_on_switch # 闭合开关</td>
    </tr>
    <tr>
        <td>单刀双掷开关</td>
        <td>SPDT_Switch</td>
        <td>SPDT Switch</td>
        <td>l, mid, r</td>
        <td>turn_off_switch # 断开开关; left_turn_on_switch # 向左闭合开关; right_turn_on_switch # 向右闭合开关</td>
    </tr>
    <tr>
        <td>双刀双掷开关</td>
        <td>DPDT_Switch</td>
        <td>DPDT Switch</td>
        <td>l_up, l_low, mid_up, mid_low, r_up, r_low</td>
        <td>turn_off_switch # 断开开关; left_turn_on_switch # 向左闭合开关; right_turn_on_switch # 向右闭合开关</td>
    </tr>
    <tr>
        <td>按钮开关</td>
        <td>Push_Switch</td>
        <td>Push Switch</td>
        <td>red, black</td>
        <td>None</td>
    </tr>
    <tr>
        <td>空气开关</td>
        <td>Air_Switch</td>
        <td>Air Switch</td>
        <td>red, black</td>
        <td>turn_off_switch # 断开开关; turn_on_switch # 闭合开关</td>
    </tr>
    <tr>
        <td>白炽灯泡</td>
        <td>Incandescent_Lamp</td>
        <td>Incandescent Lamp</td>
        <td>red, black</td>
        <td>None</td>
    </tr>
    <tr>
        <td>一节电池</td>
        <td>Battery_Source</td>
        <td>Battery Source</td>
        <td>red, black</td>
        <td>None</td>
    </tr>
    <tr>
        <td>学生电源</td>
        <td>Student_Source</td>
        <td>Student Source</td>
        <td>l, l_mid, r_mid, r</td>
        <td>None</td>
    </tr>
    <tr>
        <td>电阻</td>
        <td>Resistor</td>
        <td>Resistor</td>
        <td>red, black</td>
        <td>None</td>
    </tr>
    <tr>
        <td>保险丝</td>
        <td>Fuse_Component</td>
        <td>Fuse Component</td>
        <td>red, black</td>
        <td>None</td>
    </tr>
    <tr>
        <td>滑动变阻器</td>
        <td>Slide_Rheostat</td>
        <td>Slide Rheostat</td>
        <td>l_up, l_low, r_up, r_low</td>
        <td>None</td>
    </tr>
    <tr>
        <td>灵敏电流计</td>
        <td>Galvanometer</td>
        <td>Galvanometer</td>
        <td>l, mid, r</td>
        <td>None</td>
    </tr>
    <tr>
        <td>微安表</td>
        <td>Microammeter</td>
        <td>Microammeter</td>
        <td>l, mid, r</td>
        <td>None</td>
    </tr>
    <tr>
        <td>电能表</td>
        <td>Electricity_Meter</td>
        <td>Electricity Meter</td>
        <td>l, l_mid, r_mid, r</td>
        <td>None</td>
    </tr>
    <tr>
        <td>电阻箱</td>
        <td>Resistance_Box</td>
        <td>Resistance Box</td>
        <td>l, r</td>
        <td>None</td>
    </tr>
    <tr>
        <td>直流安培表</td>
        <td>Simple_Ammeter</td>
        <td>Simple Ammeter</td>
        <td>l, mid, r</td>
        <td>None</td>
    </tr>
    <tr>
        <td>直流电压表</td>
        <td>Simple_Voltmeter</td>
        <td>Simple Voltmeter</td>
        <td>l, mid, r</td>
        <td>None</td>
    </tr>
</table>

## 其他电路
<table border="1">
    <tr>
        <th>物实元件的中文名</th>
        <th>元件在physicsLab中对应的的类名</th>
        <th>元件在物实存档中对应的名称（即ModelID）</th>
        <th>引脚</th>
    </tr>
    <tr>
        <td>火花隙</td>
        <td>Spark_Gap</td>
        <td>Spark Gap</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>特斯拉线圈</td>
        <td>Tesla_Coil</td>
        <td>Tesla Coil</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>彩色发光二级管</td>
        <td>Color_Light_Emitting_Diode</td>
        <td>Color Light-Emitting Diode</td>
        <td>l_up, l_low, l_mid, r</td>
    </tr>
    <tr>
        <td>演示发光二级管</td>
        <td>Dual_Light_Emitting_Diode</td>
        <td>Dual Light-Emitting Diode</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>电铃</td>
        <td>Electric_Bell</td>
        <td>Electric Bell</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>八音盒</td>
        <td>Musical_Box</td>
        <td>Musical Box</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>小风扇</td>
        <td>Electric_Fan</td>
        <td>Electric Fan</td>
        <td>red, black</td>
    </tr>
    <tr>
        <td>电阻定律实验</td>
        <td>Resistance_Law</td>
        <td>Resistance Law</td>
        <td>l_up, l_upmid, l_lowmid, l_low, r_up, r_upmid, r_lowmid, r_low</td>
    </tr>
    <tr>
        <td>通电螺线管</td>
        <td>Solenoid</td>
        <td>Solenoid</td>
        <td>red, black, subred, subblack</td>
    </tr>
    <tr>
        <td>简单乐器</td>
        <td>Simple_Instrument</td>
        <td>Simple Instrument</td>
        <td>i, o, red, black</td>
    </tr>
    <tr>
        <td>蜂鸣器</td>
        <td>Buzzer</td>
        <td>Buzzer</td>
        <td>red, black</td>
    </tr>
</table>